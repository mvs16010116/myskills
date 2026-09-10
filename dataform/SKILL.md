---
name: dataform
description: 拉取、推送和同步 GCP Dataform 仓库代码（通过 Dataform REST API，不依赖 Git/GitHub）。当用户需要把 Dataform 工作区代码拉取到本地、修改后推送回 Dataform、补齐/校验 actions 配置，或创建编译结果验证配置时调用。
---

# GCP Dataform 代码同步技能

通过 GCP Dataform REST API 在工作区与本地之间同步代码。纯 GCP 方式，不涉及 Git/GitHub，适用于任何 Dataform 仓库。

## 前置要求

- 已安装 gcloud 并认证（`gcloud auth login`）
- 网络可达 `dataform.googleapis.com`（v1beta1）

## 常用参数

| 参数 | 说明 |
| --- | --- |
| `--project` | GCP 项目 ID（如 `hiccpet-481303`） |
| `--location` | 区域（如 `asia-southeast1`） |
| `--repo` | Dataform 仓库 ID 或名称 |
| `--workspace` | 工作区名称（如 `default`、`hicc_ods`） |

脚本位置：`scripts/dataform_cli.py`（与 skill 同级目录，直接以 python 运行）。

## 命令

### 1. 拉取（pull）

将整个工作区代码递归拉取到本地目录，自动跳过 `node_modules`、`.git`、`.dataform` 等构建产物目录；空文件也正确落盘。

```bash
python scripts/dataform_cli.py pull \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS> \
  --out <本地输出目录>
```

完成标准：本地目录文件与工作区一致（含空文件）。

### 2. 推送（push）

将本地改动写入工作区并提交。支持两种方式：

- **单文件/指定文件**：`--file "本地路径=远端路径"`，可重复使用多次。
- **整个目录**：`--dir <本地目录>`，远端路径为相对该目录的路径（适合整体同步）。

```bash
# 推送单个文件
python scripts/dataform_cli.py push \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS> \
  --file "d:\xxx\definitions\actions.yaml=definitions/actions.yaml" \
  --message "补充缺失配置"

# 推送整个本地目录
python scripts/dataform_cli.py push \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS> \
  --dir "d:\xxx\dataform_lingxing_amazon" \
  --message "同步全部改动"
```

`--author` 默认取 gcloud 账号邮箱，可用 `--author <邮箱>` 覆盖。

完成标准：writeFile 与 commit 均成功返回，远端 `readFile` 可读到新内容。

### 3. 编译校验（compile）

创建编译结果并校验无错误，用于确认配置（如 actions.yaml）在远端可正常编译。

```bash
python scripts/dataform_cli.py compile \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS>
```

完成标准：输出 `编译通过，0 错误`。

### 4. 提交历史（log）

打印仓库最近的提交历史（提交说明 + 提交人邮箱）。

```bash
python scripts/dataform_cli.py log \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS> \
  --limit 20   # 可选，最多显示条数，默认 20
python scripts/dataform_cli.py log \
  --project <PROJECT> --location <LOC> --repo <REPO> --workspace <WS> \
  --all         # 打印全部提交历史（自动翻页）
```

> 注意：`fetchHistory` 挂在 repository 层级，不受工作区限制，`--workspace` 传任意已存在的工作区即可。

完成标准：输出按时间倒序的提交列表（提交说明 + 提交人 + 提交时间）。

## 注意事项与常见坑

- **writeFile 请求字段是 `contents`（base64），不是 `fileContents`** —— 写错会报 `Unknown name "fileContents"`。
- **空文件**：`readFile` 对空文件不返回 `fileContents` 字段，脚本已处理为空内容。
- **编译结果挂在 repository 层级**，body 的 `workspace` 需传完整路径 `projects/.../workspaces/<WS>`。
- 若需执行工作流（真正跑数据），在编译结果通过后，再创建 workflow invocation。
