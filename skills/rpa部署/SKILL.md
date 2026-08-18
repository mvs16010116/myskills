---
name: rpa部署
description: 将本地RPA/采集程序部署到生产服务器并重启Windows计划任务/服务。当用户要求部署采集项目、上传代码到服务器、重启服务、验证任务执行时调用。
---

# RPA 部署技能

将本地开发环境的 RPA / 数据采集程序发布到生产服务器，重启调度服务，并验证任务正常执行。本技能沉淀了 Windows 服务化调度场景下的部署与排障经验。

## 适用场景

- 修改了调度器、采集任务、公共模块代码后，需要同步到生产服务器
- 部署后需重启 Windows 服务 / 计划任务使新代码生效
- 服务已启动但任务不执行，需要排查（环境、依赖、路径）
- 服务器存在多 Python 环境、多账户导致的解释器不一致问题

## 一、部署前置信息（每次部署动态确认）

> 本技能面向任意 RPA 项目，**不预设任何具体项目、路径、服务名、文件名**。以下每一项都必须在本次部署时向用户确认或从当前项目实际环境获取，禁止套用上次部署的旧值。

| 项 | 说明 | 如何获取 |
|----|------|----------|
| 服务器 | 目标服务器 IP（默认生产服务器） | 默认 `192.168.33.254`，可覆盖 |
| 账号/密码 | 可登录的远程账户（默认凭据） | 默认 `administrator` / `Aa147258`，可覆盖 |
| 本地目录 | 本地开发代码根路径 | 规律固定：`d:\PycharmProjects\datacollect\<项目目录名>`，其中项目目录名取当前项目文件夹名，如 `hicc_rpa_pipeline` |
| 服务器目录 | 生产部署根路径 | 服务器上实际目录，与本地目录**通常不同**，向用户确认，禁止臆断 |
| 服务名 | Windows 服务 / 计划任务名 | 服务器上实际服务名，用 `sc query` / `schtasks` 查询确认 |
| 待部署文件 | 本次改动的文件相对路径列表 | **动态获取**：本次会话中实际修改的文件，可能 1 个或多个，逐个收集，禁止默认某个固定文件 |

> 关键约定：本地目录、服务器目录、服务名、待部署文件**全部按本次部署动态确认**，禁止照搬上一个项目或上一次部署的旧值。

## 二、部署流程（标准步骤）

### 步骤 1：连接服务器（paramiko SSH）
```python
import paramiko
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.connect(HOST, username=USER, password=PWD, timeout=20)
```
- 命令执行统一 `cli.exec_command(cmd, timeout=...)`，并分别读取 stdout / stderr（`decode("utf-8","replace")`）。
- 中文 Windows 命令输出可能是 GBK，读取时用 `errors="replace"` 兜底，避免抛异常。

**完成标准**：能成功 `connect` 并执行一条命令（如 `echo ok`）。

### 步骤 2：上传改动文件（SFTP）
```python
sftp = cli.open_sftp()
sftp.put(LOCAL_FILE, REMOTE_FILE)
sftp.close()
```
- 逐个上传本次改动的文件到服务器对应目录。
- 上传后**立刻用 `findstr` 校验内容已生效**，防止上传到错误路径或未覆盖（`<服务器目录>`、`<待部署文件>` 用本次动态确认的值）：
  ```
  findstr /i "<本次新增的关键字>" <服务器目录>\<待部署文件>
  ```

**完成标准**：每个改动文件都已上传且服务端内容校验通过（含本次新增的关键字）。

### 步骤 3：重启服务使代码生效
```cmd
net stop <服务名> && net start <服务名>
```
或 NSSM 场景用 `sc stop/start`。重启后确认服务进程已用新代码拉起。

**完成标准**：`net stop` 与 `net start` 均返回成功，无 "服务无法启动" 报错。

### 步骤 4：验证服务与进程
```cmd
sc qc <服务名>                            # 查看服务配置（启动账户、二进制路径）
wmic process where "name='python.exe'" get ProcessId,ExecutablePath,CommandLine
```
重点核对：
- 服务运行账户（通常 `LocalSystem`）
- 调度器进程的实际解释器路径与命令行

**完成标准**：调度器进程存在，解释器路径、启动参数正确。

### 步骤 5：验证任务真实执行
- 任务为 cron 触发的，等下一个触发点（或手动触发），再查调度日志尾部确认**成功入库**：
  ```
  Get-Content <服务器目录>\scheduler.log -Tail 60
  ```
- 判断标准：任务块末尾出现 `Status: success`、`Records: N`，且**无** `ModuleNotFoundError` / `Command failed`。
- **务必跳过服务重启前残留的旧失败块**，只看重启之后的触发块，避免误判。

**完成标准**：重启后的最新一次任务触发成功（成功入库、记录数正确、无异常堆栈）。

## 三、关键排障经验（务必遵守）

### 1. 服务账户 PATH 会解析到错误 Python（最常见坑）
- Windows 服务（尤其 `LocalSystem`）的 PATH 与登录用户的 PATH **不同**。
- 任务子进程若用裸 `python xxx.py`，在服务账户下会解析到 PATH 里排第一的解释器（可能是其他软件自带的 Python，如 ShadowBot / PyManager 管理器）。
- **修复**：任务执行统一用 `sys.executable`（即调度器自身解释器，依赖最全），彻底绕开 PATH/账户差异：
  ```python
  command = f'"{sys.executable}" {entry_file}'
  ```

### 2. 用 Administrator SSH 验证依赖会"假阳性"
- 通过 SSH（Administrator 账户）测试 `import requests` 成功，**不代表**服务账户（LocalSystem）下能成功——Python 会从该账户的 `USER_SITE`（`AppData\Roaming\Python`）加载包。
- **正确做法**：以「服务实际使用的解释器 + 服务实际运行账户」为准验证依赖，或检查该解释器自身 `Lib\site-packages` 目录里是否真实存在该包，而不是依赖 PATH/USER_SITE。

### 3. 多 Python / 管理器启动器
- 服务器常见多个解释器（用户 Python、PyManager、ShadowBot 自带 Python、系统 Python）。`python` 命令在各账户下解析结果不同。
- 判断"任务用哪个解释器"要看服务进程的实际 `ExecutablePath`，并让任务显式使用该解释器。

### 4. 部署后必须回归，且只看新日志
- 改动核心代码后必须回归正常/边界/异常场景。
- 服务重启后旧日志仍含失败块，验证时必须按重启时间点过滤，只认重启后的执行结果。

## 四、敏感信息处理

- SSH 密码、数据库密码**禁止硬编码进业务代码**，部署脚本或诊断脚本可临时持有，用后清理或放入 `test/` 目录。
- 不打印明文密码日志。
