# 主题① 环境搭建与部署

> 覆盖：U9C/UBF 环境要求、系统准备、SQL Server + SSRS + UFRPT 配置、UBF Studio 安装、`IDEConfig.xml` 详解、许可申请、环境问题速查、发布部署链路、**补丁包制作与部署**。
> **这一章是所有开发的前置条件。配不好，后面全部走不通。**

---

## 1. 环境要求（2024+）

`【实测】` docs.ilyl.life，2024 年 6 月

| 组件 | 要求 |
|---|---|
| 操作系统 | Windows 8 以上（示例用 Windows 10 家庭版） |
| 数据库 | Microsoft SQL Server 2022（**开发人员模式**） |
| 报表服务 | Microsoft SQL Server 2022 Reporting Services |
| 管理工具 | SSMS |
| 开发 IDE | **Visual Studio 2026** |
| .NET 框架 | **.NET Framework 4.8** |
| 必备工具 | **Everything**（文件秒搜，解决"缺文件"问题） |

**版本演进**：

| 时期 | .NET | VS |
|---|---|---|
| U9C 最新 | .NET Framework 4.8 | Visual Studio 2026 |
| 此前 | .NET Framework 4.5 | Visual Studio 2019 |
| UBFStudio V2.8 时代（2008） | .NET Framework 3.0 | Visual Studio 2005（**已完全不适用**） |

---

## 2. 系统准备

`【实测】`

### 2.1 开启 IIS

1. 控制面板 → 程序 → 启用或关闭 Windows 功能（快捷方式：运行 `appwiz.cpl`）
2. **全选** `Internet Information Services` 和 `Internet Information Services 可承载的 Web 核心`

### 2.2 开启管理员模式（Windows 10 组策略）

1. 运行 `gpedit.msc`
2. 定位：计算机配置 → Windows 设置 → 安全设置 → 本地策略 → 安全选项
3. **禁用**以下两项策略：
   - 用户账户控制：以管理员批准模式运行所有管理员
   - 用户账户控制：用于内置管理员账户的管理员批准模式

---

## 3. 数据库与报表服务

### 3.1 安装 SQL Server 2022

`【实测】`

- 选择**开发人员模式**安装
- 选择**口令认证模式**（SQL 认证），下一步安装

### 3.2 安装并配置 SSRS ⭐

`【实测】`

**安装位置**：

```
C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer
```

**配置步骤**：

1. 选择**开发人员模式**
2. **配置报表服务器**
3. **服务账户** → 改为"使用其他账户"，填**当前电脑登录账户**（格式：`电脑名\账户名`）
4. **Web 服务 URL** → 点击"应用"，生成报表服务
   - 地址形式：`http://电脑名:80/ReportServer`
5. **数据库** → 点击"更改数据库" → **新建数据库** → 凭证使用 **SQL 凭证**
6. **Web 门户 URL** → 点击"应用"，生成门户 URL
   - 地址形式：`http://电脑名:90/Reports`
7. **加密密钥** → 点击"删除"（删除加密的内容）→ 再点击"更改"

> ⚠️ **不要勾选"执行账户"**。

**设置 ReportServer 目录权限**：

对以下文件夹设置 **Everyone 权限**：

```
C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer
```

### 3.3 添加 UFRPT 插件支持 ⭐⭐

`【实测】` **这是报表开发最关键的一步**

编辑文件：

```
C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer\rsreportserver.config
```

在 `<Data>` 节点下添加 `<Extension>` 项：

```xml
<Data>
    <Extension Name="XML" Type="Microsoft.ReportingServices.DataExtensions.XmlDPConnection,Microsoft.ReportingServices.DataExtensions"/>
    <Extension Name="UFRPT" Type="UFSoft.UBF.Report.ExtendLibrary.ReportConnection,UFSoft.UBF.Report.DataProviderForRS"/>
</Data>
```

> **不添加这一行，报表数据源就选不到 `UFRPT` 提供者类型，整个报表开发无法进行。**

**UFRPT 是什么**：U9 自研的 SSRS Data Extension。U9C 报表不是自研引擎，而是架在 SSRS 之上，靠 UFRPT 扩展才能连 U9 数据源。

---

## 4. 安装 U9C 与 UBF

`【实测】`

- **U9C 和 UBF 都要以管理员方式运行安装**
- 补丁地址：`219.141.185.72:170`
- **申请试用许可**：进入 U9HUB 社区申请，一般**当天通过**

> **主要安装问题**：安装时文件不完整、缺少各种文件配置，会导致 U9C 或 UBF 出现各种错。遇到问题**优先查 U9HUB 社区**。

### 4.1 UBF Studio 安装步骤

`【手册】` UBFStudio 使用手册 V2.8（步骤框架仍适用，**路径需按 U9C 实际安装调整**）

**第一步**：运行 `Setup.exe`，安装 UBF Studio 到指定目录。

**第二步**：解压缩 `PubRef.rar`。
> 建议放在与安装目录**同级**的目录下，**不要**放在 UBF Studio 安装目录里面。

**第三步**：配置系统引用库路径。两种方法：

- **方法 A（IDE 内）**：进入 UBF Studio（开始菜单或直接运行 `devenv.exe`）→ 主菜单 → 工具 → 配置 → 修改"系统引用库路径"为正确的 `PubRef` 文件夹路径
- **方法 B（手工）**：打开安装目录下的 `IDEConfig.xml`，找到 `ModelLibPath` 项：

```xml
<ModelLibPath>..\PubRef</ModelLibPath>
```

> **小技巧**：程序默认的系统引用库路径是与安装目录同级的 `PubRef` 目录。如果解压缩位置与此相同，本步骤可忽略。

**第四步**：编辑安装目录下的 `environment.xml`，修改数据库配置：

```xml
<system>
    <connectionString>
        packet size=4096;
        user id=u9test;
        Connection Timeout=150;
        Max Pool size=1500;
        data source=u9ubfdb;
        persist security info=True;
        initial catalog=u9test;
        password=u9test
    </connectionString>
</system>
```

| 配置项 | 含义 |
|---|---|
| `data source` | 数据库服务器名 |
| `initial catalog` | 数据库名 |
| `user id` | 数据库用户名 |
| `password` | 登录密码 |

> - 数据库配置信息**主要用于发布相关操作**。不使用发布操作时可不予理会
> - V2.8 手册中 `environment.xml` 默认配置为当时的 U9 测试数据库

**第五步**：以**管理员方式**运行安装 U9C 和 UBF。

---

## 5. IDEConfig.xml 配置详解

`【手册】` `【社区】`

配置对话框中的所有配置信息均保存在安装目录下的 `IDEConfig.xml` 中，**直接修改该文件同样有效**。

| 配置项 | 说明 |
|---|---|
| 安装路径 | UBF Studio 的安装路径（只读） |
| 系统引用库路径 | 系统引用库 `PubRef` 的所在路径 |
| 模型代码生成路径 | 模型设计完成后生成代码时使用 |
| 测试用例生成路径 | 供 UBF 开发者自己使用 |
| 界面生成路径 | — |
| 界面库路径 | — |
| 应用组件运行库路径 | 组件发布为运行态时保存的路径。**应用模型层级树的设置文件也保存在该目录下** |
| 发布站点地址 | 站点发布和部署时使用的路径 |
| 数据库脚本生成路径 | 数据库脚本生成的路径 |
| 应用服务器路径 | 应用服务器的路径 |

### 5.1 ⚠️ 设计模式开关（做报表/打印必须切）

`IDEConfig.xml` 中有一个**设计模式开关**：

- `True` → **打印、报表设计模式**
- `False` → **单据设计模式**

`【社区】` **做报表/打印模板开发时必须切到对应模式，否则界面上的相关菜单不出现。**

### 5.2 典型配置值示例

`【社区】` U9 V6 环境（把 `D:\yonyou` 换成你的实际安装路径）：

| 配置项 | 典型值 |
|---|---|
| 系统引用库 | `D:\yonyou\UBFV60\U9.VOB.Product.UBF\UBFStudio\Runtime` |
| 界面路径 | `D:\yonyou\U9V60\Portal\UILib` |
| 应用组件运行库路径 | `D:\yonyou\U9V60\Portal\ApplicationServer\Libs` |
| Portal 路径 | `D:\yonyou\U9V60\Portal` |
| UI 元数据库路径 | `D:\yonyou\UBFV60\U9.VOB.Product.Metadata\UI` |

---

## 6. 环境问题速查

`【实测】`

| 现象 | 原因 | 处理 |
|---|---|---|
| U9C/UBF 各种稀奇古怪问题 | **安装时文件不完整**，缺少各种文件配置 | 以管理员方式重装；**优先查 U9HUB 社区**；用 Everything 定位缺失文件 |
| 打开报表提示"未能加载文件或程序集 `UFSoft.UBF.Report.Base`" | 缺少报表程序集 | 用 **Everything** 搜索 `UFSoft.UBF.Report.base.dll`，**取其中一个**放到 `...\SSRS\ReportServer\Bin` 下 |
| UBF 无法发布报表，"删除用户方案失败" | 程序集版本不一致 | 用 Everything 搜索提示的文件（如 `UFSOFT.UBF.View.Query.dll`），**取最大或最新的一个**，替换 UBF 安装目录下的文件 |
| **报表类型显示"系统定义"而非"用户定义"** | **UBF 安装问题**或文件不全 | 重装/补齐文件 |
| **用户程序集部署显示的不是自己的电脑** | **报表服务器（SSRS）未配置正确** | 回到 [3.2](#32-安装并配置-ssrs-) 重查 SSRS 配置 |
| 站点起不来 | IIS 或 SSRS 配置问题 | 检查 IIS 与 SSRS 配置 |

> **必备工具：Everything**（文件秒搜）——用于解决 U9C 各类"缺文件"问题。

---

## 7. 发布与部署链路

`【手册】` `【官方】`

```
设计（元数据）
   ├── 实体项目
   │     ├── 生成代码 → 编译 → 运行期组件
   │     ├── DSL 文件 → 运行期元数据库
   │     └── 数据库项目 → 建库脚本 → 执行 → 物理表
   ├── 操作/服务项目
   │     ├── 生成代码 → 编写业务逻辑 → 编译 → 运行期组件
   │     └── DSL 文件 → 运行期元数据库（供工作流组件使用）
   └── 界面项目（UIModel + Form）
         └── 界面元数据 → 界面库
                     ↓
            应用的构建构造补丁包
                     ↓
              安装补丁包 → 运行
```

### 7.1 关键要点

| 要点 | 说明 |
|---|---|
| **补丁包** | `【官方】` 完成设计后，通过"应用的构建"构造**补丁包**，安装补丁包后即可运行。能力清单与制作流程见 [7.4](#74-补丁包能做什么) |
| **零代码单据** | `【官方】` **简单单据不用写代码**，前台录完数据即可直接进行持久化保存 |
| **OR 映射** | 数据库项目中的表只是**本地描述文件**，必须生成建库脚本并**针对指定数据库服务器执行**，才生成真正的数据表 |
| **元数据库发布** | DSL 文件发布到运行期元数据库——**这一步决定了设计期的改动能否在运行期生效** |
| **环境配置** | `environment.xml` 的数据库配置**主要用于发布相关操作** |

### 7.2 升级兼容性

| 客开方式 | 升级影响 |
|---|---|
| 弹性域预置字段 | ✅ 无影响 |
| 扩展实体 + 元数据绑定 | ✅ 安全（框架动态绑定） |
| 标准实体元数据扩展 | ⚠️ 需评估补丁冲突 |
| UI 插件（FormID 绑定） | ✅ 跨版本兼容性较好 |
| UI 插件（URI 绑定） | ❌ 易受 URL 结构调整影响 |
| **直接改物理表** | ❌❌ **会被覆盖或报错** |

### 7.3 报表发布（简述）

报表发布走**报表容器右键 → 发布应用**，含菜单发布与程序集部署，详见 `references/report-dev.md`。

### 7.4 补丁包能做什么

`【社区】`（《用友U9二次开发手册-U9补丁制作》 + zhanyd，双源一致）

| 能力 | 说明 |
|---|---|
| 拷贝文件（DLL） | 到 Portal 下指定路径 |
| 执行 `bdxml` 装配文件 | 元数据装配 |
| 导入报表和打印模板 | |
| 执行前置脚本 / 后置脚本 | |
| 执行建实体及数据资源脚本 | |

### 7.5 补丁制作流程

1. **准备补丁数据库**：把"补丁库.bak"还原到 SQL Server（如 `U9Build21_SP1_FIX`）
2. **改 `BuildTool\environment.xml`** 的连接串，指向本机补丁库：
   ```
   packet size=4096;user id=sa;Connection Timeout=150;Max Pool size=1500;
   data source=XXX;persist security info=True;initial catalog=U9Build21_SP1_FIX;password=XXX
   ```
3. **改 `BuildTool\desktopBuild.xml`**：U9 Portal 的**上一级目录**路径、构造完成生成文件夹的路径
4. 运行 **`UFIDA.UBF.Build.Engine.DesktopBuild.exe`**（U9 桌面构造工具）→ 新建方案 → 输入方案名 → 构造（**BOM 提示可以不管**）→ 自动生成补丁文件夹结构
5. 按 [7.6](#76-补丁文件夹结构放什么) 把文件放进对应目录 → **生成安装信息** → **生成补丁**

> ⚠️ **`desktopBuild.xml` 里的 `version` 必须与本机 U9 环境版本对应**（2.8 / 3.0 / 5.0 …）。不对应时导入补丁会提示**"版本无效"**。
>
> 补丁模块名建议**以 `Cust_` 开头**，便于与官方模块区分。

### 7.6 补丁文件夹结构（放什么）⭐

| 目录 | 放什么 |
|---|---|
| `AssemblyInfo` | `Setup.bdxml`（**各模块装配文件的集合**） |
| `Files` | **所有需要拷贝的文件**：BE / BP / UI / SV 的 DLL、UI/BE 插件的配置文件、所有需拷到服务器 Portal 下的文件 |
| `Metadata` | 模型构造生成的文件 + 与原数据脚本一起生成的 bulk 文件 + BE/BP/UI/SV 生成的所有 bulk 文件（默认生成在 UBF 下） |
| `PostSQL` | 所有需要执行的脚本 |
| `PreScript` | **预置脚本集合**——补丁刚开始部署时优先执行的脚本 |
| `ReportMD` | 报表模型与打印模型的所有 xml，**混合放一起，不要建子文件夹** |

> ⚠️ **构造生成的建表脚本不要放进补丁包**——否则会**清除掉数据库表的原有数据**。

**BP 插件补丁还要做**（`【社区】` zhanyd）：

1. 把 ubfdev 解决方案路径下的 **`.bdxml`** 复制到 `AssemblyInfo` 文件夹
2. 复制 BP 相关编译文件到 `Files`：
   - `项目路径\BpImplement\bin\Debug`
   - `项目路径\BpAgent\bin\Debug`
3. 复制 **`.bulk`** 文件（从 `UBFV60\U9.VOB.Product.Other` 之类的默认生成路径）
4. **不确定要拷哪些文件时，参考 `AutoBuild.bat` 里的内容**

### 7.7 轻量服务（SV）的部署差异

`【实测】`（工匠智造文档）

轻量服务项目（`.ubfserproj`）产出 RESTful 接口，部署方式与插件不同：

| 项 | 说明 |
|---|---|
| 产物 | **项目文件 6 个** + **每个接口 1 个文件** |
| 目标目录 | `\xxx\Portal\RestServices` |
| 每个接口要配一个配置文件 | 如 `UFIDA.Cust.GJ.itemMaster.IFindItemMaster.config` |
| 生效 | **重启 IIS** |
| 调用地址 | `xxxx/U9/RestServices/xxx.svc/Do` |
| 拷贝失败时 | **先关闭 ApplicationServer 再拷贝** |

> 部署时项目文件放哪、接口怎么配，**参考历史项目即可**（产品无完整文档）。

---

## 8. 许可与资源入口

| 资源 | 地址 | 说明 |
|---|---|---|
| **U9HUB 官方开发者社区** ⭐ | <https://u9hub.diwork.com/> | 注册后申请**试用许可，一般当天通过**。知识库、问答、产品手册、补丁 |
| 补丁地址 | `219.141.185.72:170` | 补丁服务器 |
| 官方 OpenAPI 文档站 | <https://openapi.yyu9c.com/doc.html> | 615 个接口 |
| U9C 实操文档站 | <https://docs.ilyl.life:8443/tools/yonyou/u9c/> | 环境搭建、报表开发、单点登录 |

---

## 9. 单点登录（SSO）配置

`【实测】` docs.ilyl.life

**前置**：使用 EA 登录 U9C → 打开**第三方应用接口授权** → 创建应用 → 记录**应用 ID** 和**应用密钥**。

**接口**：

```
GET {U9CAddress}/U9C/webapi/OAuth2/SSOLogin
    ?clientid={ClientId}
    &clientsecret={ClientSecret}
    &entCode={EntCode}
    &userCode={UserCode}
    &orgCode={OrgCode}
    &loginType=1
```

**响应**：`{ ResCode, Success, ResMsg, Data }`，`ResCode == 0` 时 `Data` 为 apitoken。

**换取登录 URL**：

```
{U9CAddress}/U9C/api/v1/autologin.aspx?apitoken={Data}
```

**C# 实现**：

```csharp
const string U9CAddress = "http://127.0.0.1";
const string ClientId = "";
const string ClientSecret = "";
const string EntCode = "";
const string UserCode = "";
const string OrgCode = "";

var SSOUrl = $"/U9C/webapi/OAuth2/SSOLogin?clientid={ClientId}&clientsecret={ClientSecret}&entCode={EntCode}&userCode={UserCode}&orgCode={OrgCode}&loginType=1";

using (HttpClient client = new HttpClient())
{
    client.BaseAddress = new Uri(U9CAddress);
    var ssoResult = await client.GetFromJsonAsync<SSO>(SSOUrl);
    if (ssoResult == null || ssoResult.ResCode != 0) return;

    var loginUrl = $"{U9CAddress}/U9C/api/v1/autologin.aspx?apitoken={ssoResult.Data}";
    Process.Start(new ProcessStartInfo { FileName = loginUrl, UseShellExecute = true });
}

class SSO
{
    public int ResCode { get; set; }
    public bool Success { get; set; }
    public string ResMsg { get; set; }
    public string Data { get; set; }
}
```

**Java 实现**：同一 URL，`OkHttp` + `Gson` 解析同样的 `SSOResult` 结构，再用 `Desktop.getDesktop().browse(new URI(loginUrl))` 打开。

---

## 相关主题

- 插件编码与调试（附加进程）→ `references/plugin-dev.md`
- OQL 数据访问、事务与 Session → `references/ubf-uap-dev.md`
- 报表服务器配置的**报表侧**用法 → `references/report-dev.md`
- UBF Studio 的 IDE 与设计器 → `references/ubf-uap-dev.md`
- 资料来源与可信度 → `references/sources.md`
