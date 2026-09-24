# 主题⑥ 插件开发（BE / BP / UI）

> 覆盖：三类插件的选择与开发流程、**事件与事务语义**、**调试**、**插件启停与客开监控**、高频坑。
> 典型问法："BE 插件怎么写"、"BP 插件怎么做"、"UI 插件"、"插件怎么调试"、"插件不生效"、"插件报错"、"插件怎么停用"。
>
> **不覆盖**（这三块是平台通用能力，已归位到语义更准的主题）：
>
> - **OQL 数据访问、事务与 Session** → 主题③ `references/ubf-uap-dev.md` 第 7–8 章
> - **补丁包制作与部署** → 主题① `references/environment.md` 第 7 章
> - **AI 幻觉 API 对照表**（资料权威性判据）→ 主题⑤ `references/sources.md` 第 6 章
>
> ⚠️ **动手前先读 [第 8 章](#8-高频坑清单)**——公网 U9 客开资料里混有大量 AI 生成的假 API，照着写必然编译不过。

---

## 1. 三类插件与选择

`【官方】` `【社区】`

U9 cloud UAP 引入**基于事件的插件开发体系**。客开实际只涉及三类插件：

| 类型 | 挂载点 | 触发时机 | 典型用途 | 配置文件 |
|---|---|---|---|---|
| **BE 插件** | 业务实体（BE）的**实体事件** | 实体保存/更新/审核等状态变更时 | 校验拦截、自动赋值、写中间表、触发外部系统 | `*.sub.xml` |
| **BP 插件** | 业务操作（BP / SV） | 用户点按钮、**定时任务**、批处理 | 调用 ISV 代理回写、批量处理、轮询外部结果 | 无独立订阅文件 |
| **UI 插件** | 界面（Form） | 页面加载/渲染/点击 | 非侵入式加工具栏按钮、底部按钮、下拉菜单 | `Extension.xml` |

### 1.1 选择决策

```
要做什么？
├─ 在某单据保存/审核时插入逻辑，或拦截非法数据
│   → BE 插件（事件驱动，与业务操作同一事务）
├─ 要跑定时任务 / 批量处理 / 回写单据
│   → BP 插件
├─ 只想在标准页面上加按钮，不改原生页面
│   → UI 插件
└─ 要对外暴露自定义 RESTful 接口
    → 轻量服务项目（SV），不是插件（部署方式见 `references/environment.md` 第 7.7 节）
```

### 1.2 典型组合场景

`【社区】` 采购订单审批外迁 OA（zhanyd 完整实测案例，双源印证）：

| 组件 | 职责 | 实现 |
|---|---|---|
| **BE 插件** | 业务员提交审核时，把采购订单写入中间表，触发 OA 流程 | C# BE 插件 |
| 中间表 | 暂存待审批数据 | SQL Server 自建表 |
| OA 系统 | 走审批流 | 外部 Web API |
| **BP 插件** | 定时轮询中间表，把 OA 审核结果回写 U9 | C# BP 插件（定时任务） |

> **BE 插件相比"数据库触发器 / 定时轮询"的三个优势**：事件驱动（只在状态变更时触发）、**与业务操作同一数据库事务**（数据一致性有保障）、上下文完整（能拿到当前用户、组织）。

---

## 2. BE 插件开发

`【社区】`（zhanyd，腾讯云开发者社区 / ITPUB，2022，含完整可编译代码）

### 2.1 开发步骤

1. 打开 U9 的**插件工具**（UBF Studio / ubfdev）
2. **工具 → 配置**，填好环境路径（配置项见 `references/environment.md`）
3. **文件 → 新建**，新建解决方案
4. 修改项目名称
5. 右键解决方案 → **新建项目**，填名称、命名空间、程序集，**类型选 `BE`**
6. 右键项目 → **添加事件集**
   - 插件模块选目标模块（如"供应链-采购管理"）
   - 搜索目标实体（如"采购"）→ 选实体（如"采购订单"）→ 确定
7. 右键 `PurchaseOrder` → **添加事件**（如 `Updating`）→ 点**生成**，生成项目代码
   - 右下角消息记录里能看到生成的项目路径
8. 打开生成的项目 → 编写代码（见 2.3）

### 2.2 订阅文件 `*.sub.xml`

生成的项目里 `sub.xml` **默认隐藏**——需点 VS 的"**显示所有文件**"才能看到，然后右键 → "包括在项目中"。

```xml
<?xml version="1.0" encoding="utf-16"?>
<pub-sub>
    <subcription event="UFIDA.U9.PM.PO.PurchaseOrder.Updating">
        <subscriber type="UFIDA.U9.Cust.Canaan.PurchaseOrderPlugBE.Updating,UFIDA.U9.Cust.Canaan.PurchaseOrderPlugBE.dll" />
    </subcription>
</pub-sub>
```

> **命名规律**：
> - `subcription event` = **实体全名** + `.` + 事件名
> - `subscriber type` = 自定义命名空间的**类名** + `,` + **程序集 DLL 名**

**还要做**：右键项目 → 引用 → 把必要的 DLL 加进来。

### 2.3 代码

代码写在生成的事件类里（如 `UpdatingExtend.cs`）。

```csharp
namespace UFIDA.U9.Cust.Canaan.PurchaseOrderPlugBE
{
    using UFSoft.UBF.Business;
    using UFSoft.UBF.Util.DataAccess;
    using UFIDA.U9.Base.UserRole;

    public partial class Updating
    {
        private void Do_Notify(object[] args)
        {
            #region 从事件参数中取得当前业务实体
            if (args == null || args.Length == 0 || !(args[0] is UFSoft.UBF.Business.EntityEvent))
                return;

            BusinessEntity.EntityKey key = ((UFSoft.UBF.Business.EntityEvent)args[0]).EntityKey;
            if (key == null)
                return;

            UFIDA.U9.PM.PO.PurchaseOrder purchaseOrderBe =
                key.GetEntity() as UFIDA.U9.PM.PO.PurchaseOrder;
            if (purchaseOrderBe == null)
                return;
            #endregion

            // 业务逻辑：审核状态为"核准中"时，写中间表触发外部流程
            if (purchaseOrderBe.Status.Value == 1)
            {
                String userID = Context.LoginUserID;
                User user = User.Finder.FindByID(userID);
                String userWorkCode = user == null ? "" : user.Code;

                // ... 后续处理
            }
        }
    }
}
```

**关键 API**（**全部为 `UFSoft.UBF.*` / `UFIDA.U9.*` 命名空间——这是判断资料真伪的标尺**）：

| 元素 | 作用 |
|---|---|
| `UFSoft.UBF.Business.EntityEvent` | 实体事件参数类型 |
| `((EntityEvent)args[0]).EntityKey` | 取出实体主键对象 |
| `BusinessEntity.EntityKey.GetEntity()` | 由主键取出实体实例 |
| `Context.LoginUserID` | 当前登录用户 ID |
| `User.Finder.FindByID(userID)` | 通过 Finder 按 ID 查找用户 |
| `DataAccessor.RunSQL(conn, sql, paras, out ds)` | 执行 SQL 返回 DataSet（**遗留写法，优先用 OQL，见 `references/ubf-uap-dev.md` 第 7 章**） |
| `DataParamList` | SQL 参数集合 |

> ⚠️ **`DataAccessor.RunSQL` 是硬编码 SQL 的遗留写法**。示例代码里常见字符串拼接（`"where PRID = " + purchaseOrderBe.ID`）——**有 SQL 注入风险，且绕过了实体层的业务规则**。生产代码应改用 **OQL + `OqlParam`**（`references/ubf-uap-dev.md` 第 7 章）或 **ISV 代理**（第 4 章）。

---

## 3. 事件与事务语义

这是插件开发最容易出错的地方，也是公网资料最缺失的部分。

### 3.1 事件清单怎么拿（**不要猜**）

`【官方】`

**权威获取方式**：UBF Studio → 项目右键 → **添加事件集** → 选实体 → 右键实体 → **添加事件**，向导会列出该实体**全部可订阅事件**。

> **不要凭记忆或网上文章猜事件名**。事件名与实体绑定，不同实体可订阅的事件可能不同；写错事件名会导致插件**静默不触发**（不报错，最难排查）。

**已实测确认的事件**：`Updating`（采购订单 `UFIDA.U9.PM.PO.PurchaseOrder`）

### 3.2 实体生命周期方法与 `OriginalData` 时机

`【官方】` 摘自《U9研发体系（实体操作API参考手册）》

实体生命周期方法（BE 层面）：`OnSetDefaultValue` / `OnInserting` / `OnInserted` / `OnUpdating` / `OnUpdated`

**`OriginalData` 的刷新时机**（**插件里读旧值必须懂这个**）：

| 场景 | `OriginalData` 内容 | 刷新时点 |
|---|---|---|
| **新建** | **id = 0 的空实体对象**，所有属性为默认值 | `OnInserted` 执行完后 |
| **修改** | **旧对象**（修改前的值） | `OnUpdated` 执行完后 |
| **查询** | — | 查询后刷新 |
| **删除** | 无意义 | 取决于删除对象的加载方式 |

> **踩坑点**：在 `OnSetDefaultValue` / `OnInserting` / `OnInserted` 里访问新建对象的 `OriginalData`，拿到的是 **id=0 的空对象**，属性全为默认值。**先看 `OriginalData.ID` 是否为 0 再决定怎么用。**

### 3.3 事务语义

`【社区】`

- **BE 插件运行在业务操作的同一个数据库事务内**——插件里抛异常 → **整个业务操作回滚**（这是 BE 插件能做"校验拦截"的原理）
- 因此：**插件里的耗时操作（HTTP 调用外部系统）会拉长事务、锁住资源**。触发外部流程时，推荐**只写中间表，让 BP 插件去异步调外部接口**
- 需要独立事务时，显式开事务（见 `references/ubf-uap-dev.md` 第 8 章）

---

## 4. BP 插件开发（含定时任务）

`【社区】`（zhanyd，双源印证）

### 4.1 开发步骤

1. 打开 ubfdev → **文件 → 新建解决方案** → **勾选"操作项目"** → 输入解决方案名 → 确定
2. 修改项目名称，**并删除自动生成的 `.ubfbp` 文件**（点"属性"按钮改名称）
3. **新建业务组件**：右键项目 → 新建 → **业务操作组件** → 填组件名 → 确定
4. 选**模型视图**，双击项目打开操作页面
5. 拖动"操作"按钮到窗体 → 点操作实体 → 点"属性" → 修改名称
6. **修改事务类型为 `required`**
7. 右键项目 → **构造** → 消息列表里能看到生成代码的路径
8. 打开生成的项目 → 右键"引用" → **添加引用**
   - ⚠️ **BP 必须引入 `*PMISV.Agent.dll`（ISV 代理）**
9. 编写代码

### 4.2 代码结构（生成 + 手写）

```csharp
public partial class UpdateStatus
{
    internal BaseStrategy Select()
    {
        return new UpdateStatusImpementStrategy();
    }
}

internal partial class UpdateStatusImpementStrategy : BaseStrategy
{
    public override object Do(object obj)
    {
        UpdateStatus bpObj = (UpdateStatus)obj;

        // auto generating code end, underside is user custom code
        // ... 用户代码

        return null;
    }
}
```

> **结构要点**：`Select()` 返回策略对象；真正的逻辑在 `XxxImpementStrategy.Do(object obj)` 里（注意生成的名字是 `Impement`，**少一个 l**，是产品自带的拼写，不要"修正"它）。

### 4.3 调用 ISV 代理回写单据

```csharp
// 生成审核状态 BP 对象
UFIDA.U9.ISV.PO.Proxy.ApprovePOISVProxy approveProxy =
    new UFIDA.U9.ISV.PO.Proxy.ApprovePOISVProxy();

List<IDCodeNameDTOData> dtoDatas = new List<IDCodeNameDTOData>();
IDCodeNameDTOData dtoData = new IDCodeNameDTOData();
dtoData.ID = Convert.ToInt64(dataRow["PRID"]);
dtoDatas.Add(dtoData);

approveProxy.ActionType = 8;   // 审核：8
approveProxy.POList = dtoDatas;
approveProxy.TargetOrgCode = UFIDA.U9.Base.Context.LoginOrg.Code;
approveProxy.Do();
```

> **两个要点**：
> 1. **ISV 代理（`*ISVProxy`）是 BP 插件调用标准业务逻辑的推荐方式**——比拼 SQL 安全，且会走完整的业务规则与事务
> 2. `IDCodeNameDTOData` 携带 `ID` 字段——**印证了 DTO 清单的发现：U9 的维度引用对象同时带 ID + Code + Name**（见 `references/api-dto.md`）

---

## 5. UI 插件开发

`【社区】`（CSDN 文库资料，**该来源标注为 AI 生成，本章内容整体为 `【待核实】`，请以官方 Extension Schema 文档为准**）

**核心机制**：基于 U9 标准化扩展框架，通过**声明式配置 + 代码逻辑**结合，**在不修改原生页面源码的前提下**动态注入自定义 UI 元素。

### 5.1 页面定位：FormID vs URI

| 定位方式 | 示例 | 特点 |
|---|---|---|
| **FormID** | `PO.PurchaseOrder`、`SO.SalesOrder` | U9 为每个标准页面分配的唯一内部标识符，**在元数据层固化，跨版本稳定**。**生产环境推荐** |
| URI | `/U9App/PO/PurchaseOrder.aspx` | 前端路由地址，直观，但**易受 IIS 虚拟目录、多租户路径、版本升级影响** |

**查找 FormID 的三种方法**：

1. 浏览器 F12 查看页面源码中 `<form id="form1">` 上方的注释块
2. U9 后台"**系统管理 → 扩展管理 → UI 插件管理**"反查已注册插件
3. 调用 SDK 的 `U9.Business.UI.PageHelper.GetFormIDByUri()` 动态解析

### 5.2 配置与扩展点

配置文件（`Extension.xml` 或 `Plugin.config`）需声明：插件基本信息（ID/名称/版本/作者）、目标页面（FormID/URI）、扩展点类型、UI 元素定义（按钮 ID/文本/图标/可见性/启用条件）、事件处理器绑定。

| 扩展点 | 节点 | 说明 |
|---|---|---|
| 工具栏按钮 | `<Toolbar>` → `<Button>` | 支持前置/后置插入位置控制 |
| 页面底部按钮区 | `<BottomButton>` | 常用于"批量审核"、"导出 PDF"等辅助操作 |
| 下拉按钮 | `<DropDownMenu>` → `<DropDownItem>` | 先注册主按钮，再嵌套菜单项，支持图标/快捷键/分隔线 |

**动态可见性表达式**：

```
VisibleExpression="CurrentUserInfo.IsInRole('采购主管')"
```

### 5.3 关键辅助类与进阶要点

| 类 | 作用 |
|---|---|
| `CHelper` | 通用辅助类：`GetPageContext()`、`ShowMessage()`、`NavigateTo()`、`ExecuteAction()` |
| `CommonFunction` | 企业开发者自主构建，沉淀业务共性逻辑；实例方法可通过 `[U9.Extension.Framework.ExtensionMethod]` 特性注册为插件可调用函数 |

- **生命周期钩子**：`OnLoad`、`OnBeforeRender`、`OnAfterRender`
- **客户端脚本注入**：`<Script>` 节点引用外部 JS 或内联代码
- **权限控制**：结合 U9 角色权限体系做按钮级开关
- **多语言**：利用 U9 资源文件机制实现 Label 国际化
- **热部署调试**：改 `Extension.xml` 后**无需重启 IIS**，清 U9 临时编译目录即可

**部署闭环**：

```
VS 创建 Class Library 项目
  → 引用 U9.Extension.Framework.dll 与 U9.Business.dll
  → 编码
  → 打包为「带签名的 DLL + 配置文件」组合包
  → U9 后台「扩展管理」上传启用
```

---

## 6. 调试

`【实测】`（三个独立来源一致：腾讯云 zhanyd / 工匠智造文档 / cnblogs）

### 6.1 附加到哪个进程 ⚠️ **关键差异**

| 插件类型 | 附加进程 |
|---|---|
| **BE 插件** | **`w3wp.exe`**（IIS 工作进程） |
| **UI 插件** | **`w3wp.exe`** |
| **BP 插件** | ⚠️ **`ApplicationService.exe`**（**不是 w3wp.exe**） |
| 轻量服务（SV） | `w3wp.exe` |

> **BP 插件调试最常见的失败原因就是附加错了进程**。附加 `w3wp.exe` 打断点永远不会命中。

**操作**：VS → 调试 → **附加到进程** → 按名称筛（`w3` 或 `ApplicationService`）→ 附加 → 命中已下的断点。

### 6.2 日志

U9 日志目录：`U9\Log`

> ⚠️ 公网文章里的 `U9.Common.LogHelper.LogInfo(...)` **属于幻觉 API**（见 `references/sources.md` 第 6 章）。**日志类的正确命名空间需以官方《数据库访问API参考手册》为准**，本知识库未验证。

### 6.3 用 dnSpy 追底层源码

VS 附加进程**只能调试自己写的代码**（`Extend` 文件里的），无法步入官方源码。

要看底层实现 → 用 **dnSpy** 加载目标 DLL → 调试 → 附加到进程。可追踪官方代码，排查"标准逻辑为什么这样走"。

---

## 7. 插件启停与客开监控

`【社区】`

**临时暂停某个客开插件**：

1. U9 菜单进入「**客开监控**」→ 右键新窗口打开
2. 在打开的**网址后加上 `&Admin=true`** → 按钮变为可用
3. 选中客开插件 → **暂停运行**

> ⚠️ **这是临时暂停，IIS 重启后会自动恢复生效**。要**永久停用，需删除对应配置文件**。

**删除客开注册**：

```sql
DELETE FROM dbo.system_InstalledAppModulePack WHERE ...
```

---

## 8. 高频坑清单

> ⚠️ 公网 U9 客开资料混有大量 AI 生成的假 API（`U9.Platform.*` / `BEAS` / `IBusinessPlugin` 等），**对照表已移至** `references/sources.md` 第 6 章。

| # | 坑 | 表现 | 解法 |
|---|---|---|---|
| 1 | **事件名写错** | 插件**静默不触发**，无报错 | 用 UBF Studio「添加事件」向导取事件名，别手写 |
| 2 | **BP 调试附加错进程** | 断点永不命中 | BP 附加 **`ApplicationService.exe`**，不是 `w3wp.exe` |
| 3 | **`sub.xml` 没包括进项目** | 部署后订阅不生效 | VS 点"显示所有文件"→ 右键 `sub.xml` → 包括在项目中 |
| 4 | **BP 没引 `*PMISV.Agent.dll`** | 编译不过 / ISV 代理不可用 | 右键引用 → 加 ISV 代理 DLL |
| 5 | **补丁 `version` 与环境不符** | 导入补丁提示**"版本无效"** | `desktopBuild.xml` 的 version 改成与环境一致 |
| 6 | **建表脚本进了补丁包** | **线上表数据被清空** | 构造生成的建表脚本**不要**放入补丁包 |
| 7 | **`ReportMD` 建了子文件夹** | 报表/打印模型导入异常 | 所有 xml **平铺**在同一层 |
| 8 | **在 `OnInserting` 里读 `OriginalData`** | 拿到 id=0 的空对象，属性全默认 | 先判 `OriginalData.ID == 0` |
| 9 | **插件里调外部 HTTP 接口** | 长事务、锁表、超时 | 只写中间表，外部调用交给 BP 插件异步做 |
| 10 | **`EntityDataQuery` 用 `select *`** | 字段解析依赖**表结构**而非实体结构，结果不可预期 | **显式列出字段名** |
| 11 | **`IDataReader` 没 `Close()`** | 连接泄漏 | `finally` 里关闭 |
| 12 | **对子对象用 `Clear()` 想删数据** | 数据没删 | 删除只能用 **`Remove()`** |
| 13 | **临时暂停插件后重启 IIS** | 插件又活了 | 永久停用要**删配置文件** |
| 14 | **`DataAccessor.RunSQL` 拼字符串** | SQL 注入 + 绕过业务规则 | 改用 **OQL + `OqlParam`** 或 **ISV 代理** |

---

## 9. 三类插件对比小结

| 插件类型 | 配置文件 | 调试附加进程 | 部署方式 |
|---|---|---|---|
| **BE 插件** | `*.sub.xml`（订阅文件，**需手动包括进项目**） | `w3wp.exe` | 编译 DLL，随**补丁包**发布 |
| **BP 插件** | 无独立订阅文件 | **`ApplicationService.exe`** | 编译 DLL（`BpImplement` + `BpAgent`），随补丁包发布 |
| **UI 插件** | `Extension.xml` / `Plugin.config` | `w3wp.exe` | 带签名 DLL + 配置，通过后台"扩展管理"上传 |

---

## 相关主题

- 环境搭建、UBF Studio 配置、**补丁包制作与部署**、许可 → `references/environment.md`
- 实体/服务/界面模型的**设计**（写代码之前做的事）、扩展字段、弹性域、**OQL 数据访问**、**事务与 Session** → `references/ubf-uap-dev.md`
- 字段含义、DTO、物理表名获取 → `references/api-dto.md`
- 报表与打印模板 → `references/report-dev.md`
- 资料来源、官方手册清单、**AI 幻觉 API 对照表** → `references/sources.md`
