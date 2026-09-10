---
name: api部署
description: 部署RPA/API采集代码到生产服务器并重启计划任务。当用户需要部署采集项目、上传代码到生产环境、重启Windows计划任务、查看计划任务状态时调用。
---

# API 部署技能

将 RPA / 数据采集项目代码部署到生产服务器（Windows），并控制对应的 Windows 计划任务。

## 生产服务器信息（Windows）

| 项目    | 值                                             |
| ----- | --------------------------------------------- |
| 连接方式  | SSH                                           |
| 地址    | `ssh://hiccwin1@34.70.38.156:22`              |
| 用户名   | `hiccwin1`                                    |
| 密码    | `hicc@1234`                                   |
| 目标文件夹 | `C:\hicc`（项目部署到 `C:\hicc\<项目名>`，具体以本次部署的项目为准） |

## 部署流程

### 1. 上传项目到目标文件夹

通过 SSH/SFTP 将本地项目上传到生产服务器 `C:\hicc`。

- **默认只上传本次修改的文件，不要整目录上传**（用户明确要求，避免覆盖服务器上已有的独立配置）。
- 先通过 `git log` / `git show --stat <commit>` 精确确定本次改动涉及的文件清单，再按目录逐一 scp 上传。
- 若本地项目已通过 Git 管理且需整体同步，可在服务器上 `git pull` 拉取最新代码（推荐）。

上传命令示例（Git Bash + sshpass + scp，`<项目名>`、`<相对路径>/<文件名>` 换成本次部署项目及本次改动的文件，文件路径以实际为准，不一定有 router 目录）：

```bash
export SSHPASS="hicc@1234"
cd /d/PycharmProjects/datacollect/<项目名>
sshpass -e scp -o StrictHostKeyChecking=no \
  <相对路径>/<文件名> \
  hiccwin1@34.70.38.156:"C:/hicc/<项目名>/<相对路径>/<文件名>"
```

（远程路径用 `C:/xxx` 正斜杠写法。）

注意事项：

- 上传前确认目标文件夹磁盘空间充足。
- 上传后核对关键文件（`main.py`、`config`、`db`、`data_collect`、`router` 等）是否完整。
- 敏感配置（`.env`、密钥、`token_store/token.json`）若服务器上已存在，**不要覆盖**服务器端配置。

### 2. 确定计划任务名称

根据本次部署的采集/调度模块，确定对应的 Windows 计划任务名称（每次部署的项目不同，任务名也不同）。

- 从服务器上确认本次项目实际使用的任务名：`schtasks /query /tn "任务名"` 或按关键字查询。
- 命名规则一般为项目或模块名称，例如本项目（`hicc_lingxing_api`）对应 `lingxing_amazon_data_collect`。
- 可用下方 `remote_exec.py` 脚本查询服务器任务列表定位真实任务名。

### 3. 停止计划任务

在开始替换代码前，先停止正在运行的计划任务，避免运行中的旧代码与新文件冲突。

```bat
schtasks /end /tn "<计划任务名称>"
```

### 4. 完成代码替换

在任务停止期间，完成代码上传 / Git 拉取 / 替换操作。

### 5. 启动计划任务

代码替换完成后，重新启动计划任务。

```bat
schtasks /run /tn "<计划任务名称>"
```

### 6. 验证计划任务状态

查询计划任务详细状态，确认已正常启动、上次运行结果正常。

```bat
schtasks /query /tn "<计划任务名称>" /v /fo LIST
```

重点检查字段：

- `Status`（状态）：应显示 `Running` / `Ready`
- `Last Run Time`（上次运行时间）
- `Last Result`（上次结果）：`0` 表示成功
- `Next Run Time`（下次运行时间）

> ⚠️ **Last Result = 267009 是正常现象**：十六进制 `0x41303` 表示"任务实例已在运行"（正在运行中），并非失败，不要误判。判定是否正常以 `Status` 和实际接口可用性为准。

## 远程执行 schtasks 的坑与正确姿势（重要）

在 Windows 本地通过 Git Bash + sshpass 执行远端 `schtasks` 命令时，直接拼命令行**极易失败**，已踩坑记录如下：

- ❌ **不要用** `ssh user@host "schtasks /query /tn ..."` 直接拼命令：Git Bash 的 MSYS 会把 `/tn`、`/v`、`/fo` 等 `/` 开头的参数当作路径做转换，导致远端只执行了 `schtasks /query`（输出被系统任务淹没）或参数丢失。
- ❌ **不要用** `cmd /c`（本环境已禁用 cmd）。远程执行请用 PowerShell。

**✅ 推荐方案：用 Python subprocess 封装 sshpass + ssh，把远端命令作为单个字符串参数整体传入**（经本地 Python 测试可靠）：

```python
# remote_exec.py（放在 test 目录，用完即删）
import subprocess, sys

HOST, USER, PASSWD = "34.70.38.156", "hiccwin1", "hicc@1234"
BASH = r"C:\Program Files\Git\usr\bin\bash.exe"

def remote_exec(remote_cmd: str) -> None:
    bash_code = (
        'export SSHPASS="%s"; '
        "sshpass -e ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "
        "%s@%s '%s'" % (PASSWD, USER, HOST, remote_cmd)
    )
    proc = subprocess.run([BASH, "-lc", bash_code], capture_output=True, text=True)
    print(proc.stdout)
    if proc.stderr:
        print("[stderr]", proc.stderr)
    print("[exit]", proc.returncode)
    sys.exit(proc.returncode)

if __name__ == "__main__":
    remote_exec(sys.argv[1])
```

用法（`<计划任务名称>` 换成本次项目的真实任务名）：

```bash
python test\_remote_exec.py "schtasks /query /tn <计划任务名称> /v /fo list"
python test\_remote_exec.py "schtasks /end /tn <计划任务名称>"
python test\_remote_exec.py "schtasks /run /tn <计划任务名称>"
```

其他备选：先把命令写成 `.bat` 上传到服务器，再远端执行该脚本，可规避全部引号/路径问题。

## 安全与注意事项

- SSH 密码为明文敏感信息，仅在授权部署时使用，不要写入代码或公开文档。
- 执行 `schtasks /end` 前确认任务名称正确，避免误停其他任务。
- 生产环境操作需谨慎，先查询再操作，操作前后记录任务状态。
- 若部署失败或任务未正常启动，需回滚到上一版本并排查原因。

