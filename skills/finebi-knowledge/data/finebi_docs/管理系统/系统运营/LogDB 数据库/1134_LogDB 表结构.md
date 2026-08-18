---
title: LogDB 表结构
doc_id: 1134
url: https://help.fanruan.com/finebi6.X/doc-view-1134.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:21
---

> 1. 概述本文将简单介绍 Logdb 数据库中各个数据表和表字段的含义。表名称fine_record_executeBI 执行表fine_record_login登录表fine_record_logou

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# LogDB 表结构
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[67](<edition-list-1134.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文将简单介绍 Logdb 数据库中各个数据表和表字段的含义。
**表**| **名称**  
---|---  
fine_record_execute| BI 执行表  
fine_record_login| 登录表  
fine_record_logout| 登出表6.0.8 及之后版本，该表已弃用  
fine_record_email| 邮件表  
fine_record_write| 填报表  
fine_record_error| 执行出错日志表  
fine_record_param| 常用参数组合表  
fine_record_sms| 短信发送表  
fine_record_operate| 管理日志表  
fine_record_sql| SQL 执行表  
fine_record_gc| GC 记录表  
fine_record_conf| 部分配置信息表  
fine_record_lock| 用户锁定日志表  
fine_tpl_info| 模板属性表  
fine_container_entity| 容器信息表  
fine_function_process| 功能点信息表  
fine_operation_process_log| 云端运维操作日志表  
fine_operation_shutdown_record| 信号量信息表  
fine_plugin_usage| 插件信息表  
fine_schedule_record| 定时任务执行日志表  
fine_config_operation| 删除行为监控表  
fine_relationship| 血缘关系分析表  
fine_intelli_honeypot| 即时埋点表  
fine_intelli_log_honeypot| 日志埋点表  
fine_update_task| 更新任务表  
fine_update_task_detail| 更新任务明细表  
performAnalysis| 数据结构  
fine_intelli_focus_point| 功能埋点表  
fine_real_time_usage| 应用实时情况表  
fine_intelli_consume_point| 性能信息表  
fine_template_error| 执行出错日志  
fine_engine_performance| 计算任务基础信息记录  
fine_sentinel_execution_record| 预警运行监控埋点表  
fine_pretreat_job_result| 日访问统计数据缓存表  
## 2\. fine_record_execute BI 执行表
**BI 执行表** ：报表访问/导出/打印日志，即如果报表访问/导出/打印的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录。
其各个字段对应的含义如下表所示：
**字段名**| **含义**| **备注**|  数据格式  
---|---|---|---  
uuid| 唯一标识字段| -| VARCHAR  
id| 主键| -| VARCHAR  
tname| 仪表板存放路径| -| VARCHAR  
displayName| 挂载到平台的目录名称| 记录目录全路径如果直接访问链接则为空| VARCHAR  
type| 报表访问方式| 具体列举在下面的表格中| INTEGER  
param| 记录被分享节点名称| 2020-08-04 及之后的 JAR 该字段有值如果被分享节点为多层级部门，则记录形式为：1层节点/2层节点/节点每次分享记录一行数据，仅记录，但不导出| VARCHAR  
ip| 操作者 IP | 仅记录，但不导出| VARCHAR  
username| 执行报表的用户| -| VARCHAR  
userrole| 执行报表的用户角色| -| VARCHAR  
consume| 执行耗时| 包括 SQL 执行时间和报表计算时间单位为ms| BIGINT  
time| 日志开始时间| -| BIGINT  
sql| SQL 语句| FR 有效字段，BI 仪表板为空，BI 未使用该字段记录操作的 FineReport 报表中的 sql 语句，不记录FineBI相关 sql 数据表的 sql 语句| VARCHAR  
sqlTime| SQL 执行的总时间| FR 有效字段，BI 仪表板为 0，BI 未使用该字段| BIGINT  
browser| 客户端访问报表所用的浏览器版本| 5.1.11 及之后版本，可通过该字段中的terminal判断访问终端browser：浏览器类型和版本OSInfo：操作系统，分为Windows、Mac、Unixterminal：客户端标识，分为PC、App、H5
  * PC：访问终端为PC 端 
  * App：访问终端为帆软App/HTML5端访问公共链接
  * H5：HTML5端访问非公共链接模板

| VARCHAR  
memory| 报表占用内存，单位 B| FR 有效字段，BI 仪表板为 0，BI 未使用该字段| BIGINT  
reportId| 模板编号| -| VARCHAR  
userId| 用户 ID| -| VARCHAR  
complete| 是否计算完成| FR 有效字段，BI 仪表板为 0，BI 未使用该字段| INTEGER  
source| 访问方式| FR 有效字段，BI 仪表板为 0，BI 未使用该字段integration：通过url访问single：平台访问| VARCHAR  
sessionID| 会话 ID| 用于与性能埋点表中（fine_intelli_consume_point）的前端渲染耗时相关埋点进行关联| VARCHAR  
node| 加载模板的节点名| 需导出treasure包，详情请参见：[云端运维使用步骤](<https://help.fanruan.com/finebi6.0/doc-view-880.html>)| VARCHAR  
error| 模板执行过程中第一个报错信息| 需导出treasure包，详情请参见：[云端运维使用步骤](<https://help.fanruan.com/finebi6.0/doc-view-880.html>)| VARCHAR  
webInfo| 模板执行信息| webResolution：当前模板执行在前端访问时的分辨率，记录格式为x*yfullScreen：当前模板执行在前端访问时是否是全屏模式，记录格式为1/0| VARCHAR  
lastMod| 模板上次改动时间| -| BIGINT  
detail| 详细信息| 用于记录被分享的仪表板明细信息| VARCHAR  
fineMarkId| 预览模板使用的设备 ID| -| VARCHAR  
estimate| 估算内存(非格子计算)，单位KB| -| BIGINT  
注： node、error、webInfo 字段需要更新到 2021-03-17 及之后版本的 JAR 包。
字段 type 具体含义：
**编码 **| **类型**| **参数**  
---|---|---  
0| 分页预览| page  
1| 在线分析| view  
2| 填报预览 | write  
3| 决策报表预览| form  
4| 行式引擎| layer  
5| 在线编辑（历史使用，目前已废弃）| edit  
6| 新填报（历史使用，目前已废弃）| write_plus  
7| 新引擎预览| page_plus  
8| 大屏FVS预览|   
  
9| 开发者调试预览|   
  
10| Excel 分页导出| excel  
11| Excel 原样导出| excelO  
12| Excel整页导出，对应场景包括：1）大数据集导出插件导出Excel2）Excel分页导出、原样导出启用了行式引擎的报表| excelL  
13| Excel 分页分 sheet 导出| excelS  
14| PDF 导出| pdf  
15| Word 导出| word  
16| SVG 导出| svg  
17| CSV 导出| csv  
18| 文本导出| text  
19| JPG 图片导出 | jpg  
20| PNG 图片导出| png  
21| GIF 图片导出| gif  
22| BMP 图片导出| bmp  
23| WBMP 图片导出 | wbmp  
24| 内置数据集导出模板| cpt  
25| HTML 导出| html  
26| 填报 HTML 导出| write_html  
27| BI 导出 Excel|   
  
30| Flash 打印| print_flash  
31| PDF 打印| print_pdf  
32 | Applet 打印| print_applet   
33| 零客户端打印| print_noclient  
34| 本地软件打印| print_native  
101| 查看BI模板| bi_view  
102| 编辑BI模板1）记录逻辑：点开一张仪表板进入编辑状态，等待页面全部加载完毕，无论做多少操作或不做操作，记录一次；下次再点模板进去编辑或者刷新网页记录第二次2）同一张仪表板，每次编辑都会有记录| bi_edit  
103| 分享BI模板| bi_share  
104| 创建BI公共链接| bi_create_publink  
105| 查看BI公共链接| bi_view_share  
106| BI 模板全局导出 PDF| bi_template_export_pdf  
107| BI 模板全局导出 Excel| bi_template_export_excel  
108| BI 组件导出 Excel| bi_component_export_excel  
109| BI模板另存为|   
  
201| 关闭浏览器或者 Tab 页（BI）|   
  
202| 编辑自助数据集|   
  
205| 关闭分享BI模板|   
  
206| 关闭BI公共链接|   
  
301| 预览组件|   
  
302| BI编辑组件|   
  
401| 预览Excel插件模板|   
  
402| 编辑Excel插件模板（预留）|   
  
403| 分享Excel插件模板|   
  
404| 创建Excel插件公共链接|   
  
405| 通过公共链接访问Excel插件模板|   
  
408| Excel组件导出Excel|   
  
409| Excel仪表板另存为|   
  
501| 查看主题|   
  
502| 编辑主题|   
  
503| 分组协作|   
  
504| 主题协作|   
  
602| 编辑基础表|   
  
701| 查看分析文档|   
  
702| 编辑分析文档|   
  
703| 创建分析文档的公共链接|   
  
704| 通过公共链接访问分析文档|   
  
## 3\. fine_record_login 登录表
**登录表** ：用户登录日志，用于记录用户的登录信息。
其各个字段对应的含义如下表所示：
** 字段名**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 登录时间| BIGINT  
ip| 登录 IP 地址| VARCHAR  
username | 登录的用户| VARCHAR  
userrole| 登录的用户角色| VARCHAR  
actionMethod| 登录方式-1：无法获取的登录方式0：默认登录1：跨域登录2：远程设计3：第三方4：移动端| INTEGER  
actionType| 操作类型0：登录1：注销2：超时登出3：保持登录| INTEGER  
authMethod| 认证方式-1：无法获取的认证方式0：密码1：验证码2：集成| INTEGER  
actionResult| 操作结果0：成功1：失败| INTEGER  
  
## 4\. fine_record_logout 登出表
注：6.0.8 及之后版本，该表已弃用。
**登出表** ：用户登出日志，用于记录用户的登出信息。
其各个字段对应的含义如下表所示：
** 字段**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 用户退出平台时间| BIGINT  
ip| 登出 IP 地址| VARCHAR  
username | 登出平台的用户名| VARCHAR  
userrole| 登出平台的用户角色| VARCHAR  
## 5\. fine_record_email 邮件表
**邮件表** ：邮件发送日志（只包含工具栏中的“邮件”），即如果报表发送邮件的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录。
其各个字段对应的含义如下表所示：
** 字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
sender| 发件人用户名| VARCHAR  
receiver| 收件人用户名| VARCHAR  
mail| 收件人邮箱| VARCHAR  
ip| 发送邮件的IP地址| VARCHAR  
username| 发送邮件的用户| VARCHAR  
tname| 此字段在BI暂无用途，为空| VARCHAR  
displayName| 此字段在BI暂无用途，为空| VARCHAR  
content| 此字段在BI暂无用途，为空| VARCHAR  
time| 发送时间| BIGINT  
result| 是否发送成功| BIT  
detail| 详情 | VARCHAR  
## 6\. fine_record_write 填报表
**填报表** ：记录填报日志信息，即如果报表进行填报的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录。
其各个字段对应的含义如下表所示：
**字段 **| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
username| 填报报表的用户| VARCHAR  
tname | 仪表板存放路径| VARCHAR  
time| 填报时间| BIGINT  
sql| SQL 语句| VARCHAR  
sqlTime| SQL 执行的总时间| BIGINT  
result| 是否填报成功| BIT  
ip| 填报报表的IP地址| VARCHAR  
displayName| 仪表板的实际名称，非「目录管理」中仪表板的名称如果直接访问链接则为空| VARCHAR  
detail| 详情| VARCHAR  
browser| 客户端访问报表所用的浏览器版本| VARCHAR  
consume| 执行耗时，包括 SQL 执行时间，报表计算时间| BIGINT  
body| 用 json 数据结构记录以下信息：1）key：请求的固定标志2）value：(times, max,min,avg)
  * times:该类请求出现次数，单位：次
  * max:该类请求最大响应时长，单位：ms
  * min:该类请求最小响应时长，单位：ms
  * avg:该类请求平均响应时长，单位：ms

| VARCHAR  
## 7\. fine_record_error 执行出错日志表
**执行出错日志表** ：即如果报表执行的过程中报错的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录，记录全部 error 和 fatal 级别的报错信息。
其各个字段对应的含义如下表所示：
注：FineBI5.1.19 及之后版本，fine_record_error不再使用，报错信息记录到fine_template_error 表中。
** 字段**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
displayName| 仪表板的实际名称，非「目录管理」中仪表板的名称如果直接访问链接则为空| VARCHAR  
ip| 执行报表的 IP 地址| VARCHAR  
msg| 错误信息| VARCHAR  
time| 出错记录时间| DATE  
tname| 出错的仪表板存放路径如果不是模板出错，则 tname 记录为“非模板触发错误”。| VARCHAR  
trace| 错误路径| VARCHAR  
username| 执行报表的用户| VARCHAR  
userrole| 执行报表的用户角色| VARCHAR  
errorcode| 错误码无错误码时记为空| VARCHAR  
platformDisplay| 是否在平台中显示1-是0-否有记录到此表的错误日志，此字段记为1，反之此字段记为0平台日志的错误日志中过滤展示，只展示 platformDisplay=1 的记录。| INTEGER  
## 8\. fine_record_param 常用参数组合表
**常用参数组合表** ：记录常用参数组合日志信息。
注：fine_record_param 表是FR的常用参数表
其各个字段对应的含义如下表所示：
** 字段**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
templateid| 仪表板 ID| VARCHAR  
username | 用户| VARCHAR  
pgroup| 参数，值以数组形式展示：{参数 1：参数值，参数 2：参数值}2020-02-28 及之后的 JAR ，pgroup 字段值加密显示| VARCHAR  
time| 记录时间| BIGINT  
## 9\. fine_record_sms 短信发送表
**短信发送表** ：记录短信发送日志信息，即如果发送短信的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录.。
其各个字段对应的含义如下表所示：
** 字段**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
receiver| 收件人用户名| VARCHAR  
mobile| 接收人手机号| VARCHAR  
content| 邮件内容| VARCHAR  
time| 发送时间| BIGINT  
result| 是否发送成功| BIT  
detail| 详情| VARCHAR  
sender| 发件人用户名| VARCHAR  
## 10\. fine_record_operate 管理日志表
**管理日志表** ：即用户对模块进行操作的时候，将会在该表中添加一条记录，并在相应字段中填写其对应的信息记录。
其各个字段对应的含义如下表所示：
** 字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
type| 模块（存国际化的 key）| VARCHAR  
item| 设置项| VARCHAR  
resource| 被访问资源| VARCHAR  
operate| 操作| VARCHAR  
username | 用户名| VARCHAR  
ip| 用户 IP 地址| VARCHAR  
time| 用户操作时间| BIGINT  
detail| 详情| VARCHAR  
requestParam| 请求参数| VARCHAR  
platformDisplay| 平台展示级别| INTEGER  
status| 本次操作的成败| INTEGER  
具体需要记录的场景如下表所示：
**TYPE- 模块**| **ITEM- 设置项**| **RESOURCE- 被访问资源**| **OPERATION- 操作**| **DETAIL- 详情**  
---|---|---|---|---  
目录管理| 节点| “节点全路径”| 增/删/改|   
  
目录管理| 模板| “节点全路径”| 增/删/改|   
  
目录管理| 链接| “节点全路径”| 增/删/改|   
  
目录管理| 上报标签| “节点全路径”| 增/删/改|   
  
用户管理| 全局设置|   
| 改|   
  
用户管理| 用户| “姓名（用户名）”| 增/删/改|   
  
用户管理| 部门| “部门全路径”| 增/删/改|   
  
用户管理| 部门下职位| “职位全路径”| 增/删|   
  
用户管理| 职位| "职位名称"| 增/删|   
  
用户管理| 职位下人员| “职位名称”-“姓名（用户名）”| 增/删|   
  
用户管理| 角色| “角色名称”| 增/删/改|   
  
用户管理| 角色下人员| “角色名称”-“姓名（用户名）”| 增/删|   
  
用户管理| 平台使用用户| “姓名（用户名）”| 增/删|   
  
用户管理| BI仅查看用户| “姓名（用户名）”| 增/删|   
  
用户管理| BI编辑用户| “姓名（用户名）”| 增/删|   
  
用户管理| 移动平台用户| “姓名（用户名）”| 增/删|   
  
权限管理| 全局设置|   
| 改|   
  
权限管理| 权限设置| “部门/角色/姓名（用户名）”| 增/删| 权限项：“目录/数据连接/业务包/可管理部门角色”  
类型：查看/授权/编辑  
权限管理| 权限复用| “生效对象【部门/角色/姓名（用户名）】”| 复用| 来源：“部门/角色/姓名（用户名）”  
类型：“权限项”  
系统管理| 登录| 单一登录| 开/关|   
  
系统管理| 登录| 单一登录设置| 改|   
  
系统管理| 登录| 上次登录信息提示| 开/关|   
  
系统管理| 登录| 忘记密码| 开/关|   
  
系统管理| 登录| 短信验证| 开/关|   
  
系统管理| 常规| 常规参数| 改|   
  
系统管理| 常规| BI参数| 改|   
  
系统管理| 打印| 打印设置| 改|   
  
系统管理| 短信| 短信平台| 开/关|   
  
系统管理| 短信| 账号绑定| 改|   
  
系统管理| 邮箱| 发件人账户| 改|   
  
备份还原| 全局配置|   
| 改|   
  
备份还原| 平台配置| 自动备份| 开/关|   
  
备份还原| 平台配置| 备份文件| 增/删/还原|   
  
备份还原| 报表模板| 自动备份| 开/关|   
  
备份还原| 报表模板| 备份文件| 增/删/还原|   
  
备份还原| BI模板| 自动备份| 开/关|   
  
备份还原| BI模板| 备份文件| 增/删/还原|   
  
备份还原| jar包| 自动备份| 开/关|   
  
备份还原| jar包| 备份文件| 增/删/还原|   
  
备份还原| 插件| 自动备份| 开/关|   
  
备份还原| 插件| 备份文件| 增/删/还原|   
  
备份还原| 更新升级| jar包更新| 更新|   
  
备份还原| 更新升级| jar包还原| 还原|   
  
备份还原| 更新升级| 备份jar包| 删|   
  
平台日志| 日志设置|   
| 改|   
  
平台日志| 访问明细|   
| 导出|   
  
平台日志| 用户行为|   
| 导出|   
  
平台日志| 模板热度|   
| 导出|   
  
平台日志| 性能监控|   
| 导出|   
  
内存管理| 智能预警|   
| 改|   
  
内存管理| 内存会话| “姓名（用户名）”-“模板路径”| 结束|   
  
内存管理| 智能释放|   
| 改|   
  
内存管理| 模板限制|   
| 改|   
  
内存管理| 生命周期|   
| 改|   
  
数据连接| 数据连接| “数据连接名”| 增/删/改|   
  
注册信息| 公有云认证/私有云认证/上传lic文件|   
| 改|   
  
安全管理| sql防注入| 禁用特殊关键字| 开/关|   
  
安全管理| sql防注入| 已禁用的特殊关键字| 改|   
  
安全管理| sql防注入| 转义字符| 开/关|   
  
安全管理| sql防注入| 已转义的字符| 改|   
  
定时调度| 定时任务| “任务名称”| 增/删/改|   
  
定时调度| 全局设置|   
| 改|   
  
多级上报| 上报流程| “流程名”| 增/删/改|   
  
多级上报| 上报任务| “任务名”| 增/删/改|   
  
移动平台| 移动平台|   
| 开/关|   
  
移动平台| 授权设备|   
| 改|   
  
移动平台| 二维码配置|   
| 改|   
  
模板认证| 全局设置|   
| 改|   
  
模板认证| 权限设置| “部门/角色/姓名（用户名）”| 增/删| 权限项：“模板路径”  
类型：查看/填报  
远程设计权限| 权限设置| “姓名（用户名）”| 改| 改后权限项：“模板路径”  
插件管理| 插件管理| “插件名”| 安装/删除/启用/禁用/更新|   
  
## 11\. fine_record_sql SQL 执行表
**SQL 执行表** ：记录 SQL 的执行情况。
注：fine_record_sql 表不会存BI模板的sql记录，只会存储FineReport模板的sql计算过程。
其各个字段对应的含义如下表所示：
** 字段**| ** 含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
columns| 数据集规模记录列数| BIGINT  
dsname| 数据集的名称| VARCHAR  
executeid| 执行批次 ID每次预览/查询时，执行的一批 SQL 共用一个批次 ID| VARCHAR  
rows| 数据集规模记录行数| BIGINT  
sqltime| SQL 执行时间单位：毫秒| BIGINT  
connection| 数据连接名| VARCHAR  
connectionID| 数据连接标识ID与功能埋点表（fine_intelli_focus_point）中的数据源连接相关埋点进行关联| VARCHAR  
time| 记录时间| BIGINT  
## 12\. fine_record_gc GC 记录表
**GC 记录表** ：记录系统的 GC 信息。
其各个字段对应的含义如下表所示：
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
heapBeforeUsed| GC 前堆使用内存| BIGINT  
heapAfterUsed| GC 后堆使用内存| BIGINT  
heapBeforeCommitted| GC 前堆申请内存| BIGINT  
heapAfterCommitted| GC 后堆申请内存| BIGINT  
gcStartTime| GC 开始时间| BIGINT  
duration| GC 持续时间| BIGINT  
gcCause| GC 的原因常见原因有：System.gc() Allocation FailurehumongousMetadata GC ThresholdErgonomicsGCLocker Initiated GC| VARCHAR  
gcType| GC 类型分为GC和Full GC| VARCHAR  
metaspaceBeforeUsed| metaspace GC 前使用内存| BIGINT  
metaspaceBeforeCommitted| metaspace GC 前申请内存| BIGINT  
metaspaceAfterUsed| metaspace GC 后使用内存| BIGINT  
metaspaceAfterCommitted| metaspace GC 后申请内存| BIGINT  
balancePromoterScore| 中止分值| INTEGER  
youngBeforeUsed| 年轻代 GC 前使用内存| BIGINT  
youngBeforeCommitted| 年轻代 GC 前申请内存| BIGINT  
youngAfterUsed| 年轻代 GC 后使用内存| BIGINT  
youngAfterCommitted| 年轻代 GC 后申请内存| BIGINT  
loadScore| 整体负载分值| INTEGER  
node| 用户命名的节点名单机下为空| VARCHAR  
oldBeforeUsed| 老年代 GC 前使用内存| BIGINT  
oldBeforeCommitted| 老年代 GC 前申请内存| BIGINT  
oldAfterUsed| 老年代 GC 后使用内存| BIGINT  
oldAfterCommitted| 老年代 GC 后申请内存| BIGINT  
pid| 进程 pid| VARCHAR  
releasePromoterScore| 释放分值| INTEGER  
time| 记录时间| BIGINT  
## 13\. fine_record_conf 部分配置信息表
记录fine_conf_entity中的部分配置信息。
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 记录时间| BIGINT  
id| 配置项| VARCHAR  
value| 配置项值| VARCHAR  
## 14\. fine_record_lock 用户锁定日志表
记录用户锁定的日志
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
lockItem| 锁定对象| VARCHAR  
lockTime| 锁定时间| VARCHAR  
autoUnlockTime| 自动解锁时间| VARCHAR  
## 15\. fine_tpl_info 模板属性表
记录模板属性
注：该表已无实际用途，仅作为备用。因此不会在表中记录任何数据。
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
id| 序号| VARCHAR  
tid| 模板id| VARCHAR  
tname| 物理模板名称记录 reportlet 下的完整路径| VARCHAR  
cnums| 条件属性个数| BIGINT  
formnums| 公式个数| BIGINT  
sheetnums| sheet个数| BIGINT  
dsnums| 数据集个数| BIGINT  
compformnums| 复杂公式的个数包括层次坐标、sql、value公式| BIGINT  
submitnums| 内置提交的个数| BIGINT  
isfrozen| 是否使用了冻结| BIT  
isfoldtree| 是否使用了折叠树| BIT  
widgetnums| 控件个数| BIGINT  
tsize| 模板总大小| BIGINT  
imgsize| 模板里图片的大小| BIGINT  
execute0| 引擎情况汇总0| BIGINT  
execute1| 引擎情况汇总1| BIGINT  
execute2| 引擎情况汇总2| BIGINT  
execute3| 引擎情况汇总3| BIGINT  
execute4| 引擎情况汇总4| BIGINT  
mem0| 内存情况汇总0| BIGINT  
mem1| 内存情况汇总1| BIGINT  
mem2| 内存情况汇总2| BIGINT  
mem3| 内存情况汇总3| BIGINT  
mem4| 内存情况汇总4| BIGINT  
sql0| sql情况汇总0| BIGINT  
sql1| sql情况汇总1| BIGINT  
sql2| sql情况汇总2| BIGINT  
sql3| sql情况汇总3| BIGINT  
sql4| sql情况汇总4| BIGINT  
filternums| 过滤个数| BIGINT  
injectnums| 参数注入个数| BIGINT  
formula| 模板内公式使用情况| VARCHAR  
jsapi| 模板内JS API使用情况| VARCHAR  
recordtime| 模板检测时间| VARCHAR  
## 16\. fine_container_entity 容器信息表
记录容器信息
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
node| 节点名| VARCHAR  
item| 配置项| VARCHAR  
value| 配置项值| VARCHAR  
## 17\. fine_function_process 功能点信息表
记录功能点信息
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
function| 功能点| VARCHAR  
## 18\. fine_operation_process_log 云端运维操作日志表
记录云端运维操作日志
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 记录时间| BIGINT  
node| 节点名称| VARCHAR  
process| 日志内容| VARCHAR  
## 19\. fine_operation_shutdown_record 信号量信息表
记录信号量信息
注：fine_operation_shutdown_record和fine_plugin_usage整合到了fine_intelli_focus_point 表
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
pid| 进程ID| VARCHAR  
startTime| 开始时间| BIGINT  
upTime| 截止时间| BIGINT  
node| 节点| VARCHAR  
signalName| 信号名| VARCHAR  
## 20\. fine_plugin_usage 插件信息表
记录插件信息
注：fine_operation_shutdown_record和fine_plugin_usage整合到了fine_intelli_focus_point 表
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 入库时间| BIGINT  
plugin| 插件名| VARCHAR  
version| 插件版本| VARCHAR  
API| 插件中接口使用情况| VARCHAR  
operation| 插件运行情况| VARCHAR  
register| 插件注册情况| VARCHAR  
enable| 插件是否启用| BIT  
## 21\. fine_schedule_record 定时任务执行日志表
记录定时任务执行信息
**字段**| **含义**| **字段类型**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
id| 主键UUID| VARCHAR  
creator| 创建者| VARCHAR  
detailMessage| 详细信息| VARCHAR  
filePath| 生成附件路径预留字段，未使用| VARCHAR  
logMessage| 日志信息| VARCHAR  
logTime| 任务执行时间日志打印时间| BIGINT  
logType| 日志类型0-失败1-成功2-跳过| INTEGER  
nextFireTime| 下一次记录时间预留字段，未使用| BIGINT  
runType| 附件处理类型0-快照生成1-邮件发送2-FTP上传3-消息推送4-文件打印5-短信发送6-平台挂载7-自定义类8-定时填报9-客户端通知10-SFTP上传| INTEGER  
taskName| 任务名称| VARCHAR  
taskID| 任务ID| VARCHAR  
time| 入库时间| BIGINT  
## 22\. fine_intelli_focus_point 功能埋点表
**功能埋点表：** 用来保存所有公共的埋点信息。
其各个字段对应的含义如下表所示：
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
id| 埋点 ID 编号| VARCHAR  
text| 记录的主要内容| VARCHAR  
source| 埋点来源-1-没有定义来源（UNDEFINED）1-内置 JAR 包的功能点（EMBED）2-插件功能点（PLUGIN）4- FineReport 的功能点（REPORT）8- FineBI 的功能点（BI）| INTEGER  
time| 时间| DATE  
username| 用户名转码处理，超管用户为 0| VARCHAR  
ip| 触发埋点的 IP| VARCHAR  
title| 标题，埋点是什么| VARCHAR  
body| 一个 JSON 数据结构根据功能点 ID 存放不同功能点的信息次要信息，可能为空| VARCHAR  
字段 id 格式说明：
例如：FR-P1001
FR 前缀，表示是 FR 的埋点。
第一位字母表示功能/性能：F-功能、P-性能。
第二位数字表示分类：1-数据源、2-前台、3-报错、4-智能运维、5-设计器。
表中字段 id 和 body 之间的关系如下表所示：
**id**| **body**| **作用**  
---|---|---  
FR-P1001| id：数据连接标识version：数据源版本driver：连接驱动信息times：使用次数connecttime：创建连接的时间| 用于记录数据连接相关的信息  
FR-F3001| 记录具体的报错堆栈| 记录工程启动失败报错原因  
FR-F4001| 初版插件记录示例：{node:2,memory:16,situation:normal,inform:1,type:auto}node 为推荐节点数（推荐单机时记为1）memory 为推荐单机/单节点内存situation 为推荐的情况：记为"normal"时为正常推荐，"error"时为推荐值异常情况，"inequacy"时为运行数据不足情况，"nonsupport"时为不支持推荐配置。其中"normal"情况下 node 与 memory 有值，其余情况 node 与 memory 记为空inform 为是否进行了通知，记为1代表已通知，记为0代表未通知type 为推荐的类型，记为"auto"为根据一自然日运行数据进行推荐的结果，记为"manual"为用户访问接口链接推荐的结果| 内存配置推荐数值  
FR-F4002| 记录示例：{sessionid: xxxxxx, reason: release, detail: row count, load: high load, cell num: 100000, survival time: 600000}sessionid: 被清除的会话 idreason: 会话被清除的原因大类。包括 life(生命周期)，limit(模板限制)，release(智能释放)三项detail: 会话被清除的详细原因
  * reason 记为 life 时，此项记录为空。
  * reason 记为 limit 时，此项记录为：row count（单数据集行数限制)，cell count（单模板单元格限制），sql time（sql执行时长限制），excel cell count（导入Excel单元格限制），commit row count（提交记录数限制），cartesian（填报笛卡尔积限制）
  * reason 记为 release 时，此项记录为：stop calculating

load: 会话被杀时的系统的负载状况。包括endanger（危险状态），terrible load（超高负载），high load（高负载）,normal load（中低负载）cell num：已计算的单元格个数survival time：存活时间| 记录会话因生命周期、模板限制被清除以及高负载时停止计算的情况  
FR-F4003| 记录示例：{type: high load kill, kill num time: 50, kill num cell: 50, session num: 300, load: terrible load}type: 包括high load kill（小杀），terrible load kill（大杀）,remove all（超杀清除所有会话)kill num time: 因未更新时间过长被杀的会话数，type 为 removeAll 时记为空kill num cell: 因格子数过多被杀的会话数，type 为 removeAll 时记为空kill num sum: 被杀的会话数求和session num: 释放会话之前的会话总数load: 会话被杀时的系统的负载状况。包括 endanger（危险状态），terrible load（超高负载），high load（高负载）,normal load（中低负载）| 记录 GC 回调触发的释放会话情况  
FR-F5001| 记录示例：{disk_beforegc:50, disk_aftergc:50}| 记录模板版本管理 GC 清理情况  
FR-F5002| node：节点名time：进程关闭时间pid：进程 pidstartTime：进程开始时间upTime：进程持续时间signalName：信号量| 系统关闭记录：记录系统关闭前后的进程信息以及关闭类型  
FR-F5003| node：节点名containerMem：容器设置的内存大小cpu：CPU 核数disk：磁盘总空间diskUsed 磁盘已使用空间jdkVersion：JDK 版本containerVersion：Web容器版本machineMem：物理机内存system：服务器操作系统systemNum：服务器操作系统位数arch：处理器架构，如x86_64、x86diskSpeed：磁盘存取速度FRbuildNO：FR的 jar 包版本BIbuildNO：BI 的 jar 包版本（记录 BI 的 jar 包版本，未使用 BI 则记为空）serverType：服务器类型（cloud代表云服务器，local代表本地服务器）gcType：垃圾收集器类型| 容器配置情况：应用所在容器、服务器的配置信息。每日记录一次  
FR-F5004| licType：注册类型expireTime：注册到期时间CTRID：合同 IDcompanyId：公司 IDproductVersion：产品版本platformUserNum：用户人数| 用户基本信息：用户的注册信息等内容。每日记录一次  
FR-F5005| tid：模板 IDtName：物理模板名字（reportlets下的完整路径）cNums：条件属性个数formNums：公式个数sheetNums：多 sheet 个数dsNums：数据集个数compFormNums：复杂公式的个数（包括层次坐标、SQL、Value公式）submitNums：内置提交的个数isFrozen：是否使用了冻结isFoldTree：是否使用了折叠树widgetNums：控件个数filterNums：过滤个数injectNums：参数注入个数formula：模板内公式使用情况jsAPI：模板内JS API使用情况（限制记录为255字符）tSize：模板总大小imgSize：模板里图片的大小lineEngine ：是否启用行式引擎（1为启用，0为未启用）execute0-execute4：执行时间的5级的分段记录mem0-mem4：内存使用量的5级的分段记录sql0-sql4：SQL 执行时间的5级的分段记录| 模板属性信息：记录模板的各项信息，每张模板每日输出一条记录  
FR-F5006| id：数据在配置中的位置value：数据值| 配置信息：每日将 FineDB 中的 fine_conf_entity 表中的特定信息记录一次  
FR-F5007| plugin：插件名version：插件版本API：插件中所用接口情况opration：插件运行情况register：插件注册情况enable：插件是否启用| 插件使用情况：插件的使用情况，每个插件在每日记录一次  
FR-F5008| function：功能点购买情况| 功能点购买情况：功能点购买情况，每日记录一次  
## 23\. fine_real_time_usage 应用实时情况表
**应用实时情况表** ：记录应用实时情况。
其各个字段对应的含义如下表所示：
** 字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
node| 节点名2019-05-20 及之后 JAR 新增字段| VARCHAR  
cpu| CPU 利用率| DOUBLE  
memory| 当前 JVM 内存情况| BIGINT  
time| 记录时间，每分钟一条| BIGINT  
sessionNum| 存活会话数2019-05-20 及之后 JAR 新增字段| BIGINT  
onlineNum| 系统在线人数2019-05-20 及之后 JAR 新增字段| BIGINT  
pid| 进程 PID2019-05-20 及之后 JAR 新增字段| VARCHAR  
templateRequest| 正在计算的模板请求数| INTEGER  
httpRequest| 总的正在处理的 http 请求数| INTEGER  
sessionRequest| 正在处理的带 sessionid 的请求数| INTEGER  
fineIO| fineIO 占用堆外内存大小单位 KB2020-08-04 及之后 JAR 新增字段| BIGINT  
NIO| NIO 占用堆外内存大小单位 KB2020-08-04 及之后 JAR 新增字段| BIGINT  
bufferMemUse| 堆外使用总内存directMem「nio」和mappedMem单位 KB2020-08-04 及之后 JAR 新增字段| BIGINT  
physicalMemUse| 物理内存已使用空间单位 KB2020-08-04 及之后 JAR 新增字段| BIGINT  
physicalMemFree| 物理内存空闲空间单位 KB2020-08-04 及之后 JAR 新增字段| BIGINT  
## 24\. fine_intelli_consume_point 性能信息表
**性能信息表** ：记录性能相关信息。
其各个字段对应的含义如下表所示：
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| String  
time| 时间开始时间| Long  
id| 埋点 id 编号
  * 仪表板ID：X964
  * 组件ID：X963
  * 自助数据集ID：X961
  * 资源内容ID（模板名字，分析表名字等）：FR-P2004

| String  
text| 资源内容：模板名字，分析表名字等或资源ID：模板 ID，分析表 ID，表 ID等| String  
source| 埋点来源Original 类里面embed：表示当前系统的plugin：表示插件的埋点undefined：表示没有定义来源| Int  
username| 操作者| String  
ip| 操作 IP| String  
title| 6.1版本该字段为空| String  
frFullVersion| FR版本| String  
biFullVersion| BI版本| String  
cloudVersion| 云端运维版本| String  
finish| 结束时间FR 有效字段、BI 为 0，BI 未使用该字段| String  
consume| 耗时 单位 ms| String  
memory| 内存大小 单位 byteFR 有效字段、BI 为 0，BI 未使用该字段| String  
type| 操作类型可以表明是进行了哪种操作。BI 未使用该字段| String  
comment| 资源备注可以是更具体一些的信息，需要直接分析的数据。BI未使用该字段| String  
body| 埋点具体信息一个 JSON 数据结构，根据不同的埋点里面存放不同的信息| String  
## 25\. fine_template_error 执行出错日志
其各个字段对应的含义如下表所示：
注：FineBI5.1.19 及之后版本，fine_record_error不再使用，报错信息记录到fine_template_error 表中。
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 出错记录时间| BIGINT  
displayName| 挂载到平台的目录名称，平台前端处理为国际化noPath：表示非挂载访问| VARCHAR  
tname| 出错的物理模板名字（reportlet下的完整路径）| VARCHAR  
username| 执行模板的用户，平台前端处理为国际化notLogged：未登录访问fromSchedule：定时调度| VARCHAR  
ip| 执行模板的IP地址（定时调度为空）| VARCHAR  
msg| 错误信息，不包含具体错误位置等，基本和错误代码匹配（比如单元格死循环，不显示具体的单元格）| VARCHAR  
trace| 错误堆栈长度1000字符，超过截断| VARCHAR  
code| 错误代码| VARCHAR  
para| 出错时的查询参数| VARCHAR  
result| 是否成功预览1：预览成功0：预览失败| BIGINT  
platformDisplay| 是否在「管理系统>智能运维>平台日志」中显示0：不显示1：显示| BIGINT  
## 26\. fine_config_operation 删除行为监控表
记录分组、业务包、表、关联的删除操作
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 时间| Long  
user| 用户名| VARCHAR  
resource_type| 资源类型，包括：仪表板分组业务包表关联| VARCHAR  
operate_type| 操作类型，目前只记录删除操作| VARCHAR  
info| 配置信息，表名、业务包名、分组名等等| VARCHAR  
thread_name| 线程名| VARCHAR  
## 27\. fine_relationship 血缘关系分析表
记录数据表仪表板的血缘关系数据。
该表已弃用，如需查询可使用：[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 时间| Long  
tableId| 表名| VARCHAR  
tableName| 转义名| VARCHAR  
engine| 使用引擎| VARCHAR  
tableType| 表类型：database：db表sql：sql表server：服务器数据集excel：excel表analysis：自助数据集confAnalysis：编辑过的基础表| VARCHAR  
creatorName| 表创建者| VARCHAR  
childTable| 子表名| VARCHAR  
firstChild| 是否是直接子表0：不是直接子表1：是直接子表| Long  
dashboardName| 仪表板名| VARCHAR  
dashboardId| 仪表板ID| VARCHAR  
## 28\. fine_intelli_honeypot 即时埋点表
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 用户的唯一标识字段| VARCHAR  
id| 埋点ID| VARCHAR  
time| 日志时间| BIGINT  
addr| ip| VARCHAR  
userName| 操作用户名| VARCHAR  
tableId| 操作表ID| VARCHAR  
comment| 操作对象转义名| VARCHAR  
target| 操作对象| VARCHAR  
tableName| 操作表名| VARCHAR  
transferName| 操作备注| VARCHAR  
describe| 参数| VARCHAR  
## 29\. fine_intelli_log_honeypot 日志埋点表
**字段**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
id| ID| VARCHAR  
startTime| 报错日志时间| BIGINT  
errorCode| 报错编码| VARCHAR  
time| 记录时间| BIGINT  
## 30\. fine_update_task 更新任务表
注：5.1.12 之前的 BI 工程，该部分信息可在 LogDB 中查看。
5.1.12 及之后版本的 BI 工程，该部分信息可在 FineDB 中查看。
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 任务的唯一标识字段| string  
planId| 任务实例唯一标识，每一次运行都不同| string  
taskName| 任务名称表名+任务类型（单表/业务包/全局）| string  
startTime| 任务开始时间| Long  
endTime| 任务结束时间| Long  
runningResult| 完成状态ALL：全部成功PART：部分成功| string  
state| 更新状态END：已结束RUNNING：运行| string  
triggerType| 触发方式MANUAL：手动AUTO：定时| string  
roleId| 触发人Id| string  
roleName| 触发人名称| string  
countOverView| 任务中各类型的表的更新情况。JSONexpectBaseTableUpdate：期望的基础表数量actualBaseTableUpdate：实际成功更新的基础表数量expectComplexUpdate：期望的自助数据集数量actualComplexUpdate：实际成功的自助数据集数量expectRelationUpdate：期望的关联更新数量actualRelationUpdate：实际成功的关联数量| string  
extra1| 额外的字段1| string  
extra2| 额外的字段2| string  
extra3| 额外的字段3| string  
time| 数据插入时间，swift表清理需要| Long  
## 31\. fine_update_task_detail 更新任务明细表
注：5.1.6 之前的 BI 工程，更新任务相关的信息，记录在 fine_DSGenerateFinishMap_SwiftTable（数据集更新信息临时表）和 fine_DSGenerate_SwiftTable（数据集更新信息表）中
5.1.6~5.1.11 之间的 BI 工程，该部分信息可在 LogDB 的fine_update_task_detail（更新任务明细表）中查看。
5.1.12 及之后版本的 BI 工程，该部分信息可在 FineDB 的fine_update_task_detail（更新任务明细表）中查看。
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 任务的唯一标识字段| string  
planId| 任务实例唯一标识，每一次运行都不同| string  
loadId| 明细标识，在一个更新任务中唯一| Integer  
loadName| 明细信息的名字表为表名+包名，关联为关联的信息| string  
loadType| 明细类型BASE：基础表FAST、ETL：自助数据集RELATION：关联| string  
updateType| 更新类型FULL：全量INCREASE：增量| string  
state| 更新状态LOADING：更新中SUCCESS：成功PART_SUCCESS：部分成功WAITING：排队等待WRONG：失败| string  
endTime| 数据更新结束时间| Long  
effectTime| 生效时间，真正可用| Long  
startTime| 更新开始时间| Long  
execption| 失败报错信息| string  
failedSonId| 基础表导致的更新失败的表的ID集合| string  
extra1| 额外的字段1| string  
extra2| 额外的字段2| string  
extra3| 额外的字段3| string  
time| 数据插入时间，swift表清理需要| Long  
fatherFailedIds| 更新失败的父表的ID集合| string  
tableId| 额外的字段| string  
updateCount| 变化的行数，可能有增有减5.1.10 版本新增字段| Long  
errorCode| 错误代码5.1.10 版本新增字段| Long  
totalCount| 总行数5.1.10 版本新增字段| Long  
deleteCount| 增量减行数5.1.10 版本新增字段| Long  
writeTime| 写文件时间5.1.10 版本新增字段| Long  
etlFlow| 自助数据集的步骤5.1.10 版本新增字段| string  
appendCount| 增量增行数5.1.10 版本新增字段| Long  
columns| 列5.1.10 版本新增字段| Long  
jdbcTime| 数据获取时间5.1.10 版本新增字段| Long  
openTime| sql执行时间5.1.10 版本新增字段| Long  
infos| 非报错信息（只有国际化的key值和参数）5.1.10 版本新增字段| string  
## 32\. performAnalysis 数据结构
包括仪表板和数据准备两种结构。
注：该表目前已禁用，不会写入任何数据。如需查看数据表相关的SQL语句，请在「[BI工具](<https://help.fanruan.com/finebi6.0/doc-view-1546.html>)」的SQL性能监控中查看。
**字段名**| **含义**| **数据格式**  
---|---|---  
uuid| 唯一标识字段| String  
time|   
| Long  
type| 大类类型0：仪表盘1：数据准备| Int  
user| 用户名称| String  
startTime| 开始时间| Long  
endTime| 结束时间| Long  
category| 仪表盘名称/表名称| String  
subCategory| 组件名称/步骤名称| String  
event|   
| String  
subEvent|   
| String  
exclusiveDuration| 该事件独占时间| Long  
dataSource| 描述数据源信息| String  
query| 执行的SQL| String  
row| 行数| Int  
contentSize| 所占内存大小| Long  
exception| 异常信息如果出现异常信息记录到这里方便排查问题| String  
additionalInfo| 额外信息| String  
**事件列表**
**事件大类**| **事件名称**| **含义**  
---|---|---  
仪表盘type:0| cache| SpiderBaseCriteria| SQL三级缓存  
GroupCacheProcedure  
CrossCacheProcedure| 数二级缓存  
GroupPagingCacheProcedure  
CrossPagingCacheProcedure| 分页一级缓存  
crossPage  
groupPage| 分页处理  
makeTree| 二维表树化  
postGroup| 多指标后重新进行分组汇总  
treeSort| 树排序  
multiTarget(Old)| 多指标计算逻辑（老引擎）可能拆分多个SQL  
multiTarget(New)| 多指标计算逻辑（新引擎）可能拆分多个SQL  
数据准备type:1| previewData| 表数据的预览（非编辑内）  
processResult| 自主数据集编辑内数据预览  
getData| 获取自主数据集编辑内预览数据  
公共事件type: 0 or 1| sqlQuery| SQL数据查询  
excelQuery| Excel数据查询  
getFields| 获取字段信息  
## 33\. fine_engine_performance 计算任务基础信息记录
引擎性能埋点需求，对计算耗时等相关信息进行埋点记录。  

字段名  
| 含义| 数据格式  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 记录时间| BIGINT  
queryId| 查询标识/ID| VARCHAR  
startTime| 开始时间| BIGINT  
endTime| 结束时间| BIGINT  
engineType| 引擎类型1：直连2：抽取| INTEGER  
innerEngineType| 细分内部引擎类型| INTEGER  
baseStartTime| 基础计算开始时间| BIGINT  
baseEndTime| 基础计算结束时间| BIGINT  
dataModelCol| 基础结果列数| INTEGER  
dataModelRow| 基础结果行数| INTEGER  
dataModelMem| 基础结果内存占用大小| INTEGER  
peakMemory| 计算结果中内存峰值| BIGINT  
cacheHitType| 缓存命中情况| INTEGER  
cacheCost| 缓存处理耗时| BIGINT  
matchType| 一些策略的命中情况0：表示未命中1：表示规则命中但是实际未命中2：表示规则命中，实际命中| INTEGER  
parseTime| 解析耗时| BIGINT  
mergeCost| 并发计算后合并操作的耗时| BIGINT  
tableId| 数据集id| VARCHAR  
widgetId| 组件id| VARCHAR  
widgetType| 组件类型| INTEGER  
dashboardId| 模板id| VARCHAR  
baseCriteria| 基础查询信息| VARCHAR  
extra| 拓展字段| VARCHAR  
executeType| 运行状态0：成功1：报错| INTEGER  
username| 操作用户  
| VARCHAR  
frFullVersion| FR版本| VARCHAR  
biFullVersion| BI版本| VARCHAR  
cloudVersion| 云端运维版本| VARCHAR  
## 34\. fine_sentinel_execution_record 预警运行监控埋点表
**预警运行监控埋点表** ：提供清晰可见的运行监控信息，以追溯预警任务执行情况。
请确保安装了最新版数据预警插件，否则可能无法出现该表。
其各个字段对应的含义如下表所示：
字段名  
| 含义| 数据格式| 备注  
---|---|---|---  
uuid| 唯一标识字段| VARCHAR| -  
time| 埋点创建时间戳| BIGINT| -  
taskid| 预警任务id| VARCHAR| -  
taskName| 预警任务名| VARCHAR| -  
creator| 预警创建者| VARCHAR| -  
triggerTime| 预警触发时间戳| BIGINT| -  
triggerType| 预警触发类型| INTEGER| 0 为定时调度执行，1 为手动执行  
notifyStatus| 通知执行状态| INTEGER| -1 为初始化，0 为未触发，1 为跳过（重复通知免打扰），2 为执行通知  
notifierInfo| 预警推送详情| VARCHAR| 预警推送渠道
  * 邮件、短信、平台直接记录名称，例如“短信”
  * 客户端通知拼接记录对应的应用群聊等，例如“钉钉-钉钉应用-钉钉群聊”（应用和群聊是非必须的，可能存在没有应用或没有群聊的情况）
  * 应用接口通知拼接记录对应终端的名称，例如“应用接口-XXX”
  * 多选的情况下拼接记录

  
receivers| 预警接收人| VARCHAR| 具体推送人员用户名的清单，‘，’号拼接  
data| 预警快照数据| VARCHAR| 预警快照数据，含最大值，最小值等  
snapshotPath| 预警附件地址| VARCHAR| 预警附件地址，asssets目录  
jobStatus| 预警任务执行状态| INTEGER| -1 为初始化，0 为执行失败，1 为执行成功  
detailMessage| 任务执行详情| VARCHAR| 预警执行成功则为空，执行失败记录错误堆栈  
## 35 fine_pretreat_job_result 日访问统计数据缓存表
swift每天凌晨会有个定时任务，去查询前一天访问统计中的「日访问量，日活跃模板数，日活跃用户数」，并记录到该表中作为缓存。
字段名| 描述| 数据格式  
---|---|---  
uuid| 唯一标识字段| VARCHAR  
time| 时间| BIGINT  
taskId| 任务ID| VARCHAR  
taskResult| 查询的结果：包括日活跃用户数，日活跃模板数，日访问量| VARCHAR  
taskCondition| 查询的条件：任务类型 + 查询时间范围| VARCHAR  
taskType| 任务类型| VARCHAR  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：平台日志 LogDB 数据库](<index.php?doc-view-706.html>)
[下一篇：平台日志同步到其他数据库插件 ![](/core/style/forward.png) ](<index.php?doc-view-1030.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
