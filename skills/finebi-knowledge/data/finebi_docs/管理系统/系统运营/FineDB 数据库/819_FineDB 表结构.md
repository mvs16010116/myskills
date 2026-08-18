---
title: FineDB 表结构
doc_id: 819
url: https://help.fanruan.com/finebi6.X/doc-view-819.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:15
---

> 1. 概述本文简单介绍 FineDB 数据库中包含的表字段说明。注1：由于外接数据库的类型不同，字段的数据类型不完全一致，本文以工程内置数据库为例，用户需自行匹配。注2：FineDB&nbsp;配置库用

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineDB 表结构
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[75](<edition-list-819.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-11-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文简单介绍 FineDB 数据库中包含的表字段说明。
注1：由于外接数据库的类型不同，字段的数据类型不完全一致，本文以工程内置数据库为例，用户需自行匹配。
注2：FineDB 配置库用于存放工程配置信息，各表之间存在关联关系，随意改动可能导致工程无法启动等严重后果。
**请勿手动增！删！改！FineDB 数据库内的任何数据！有可能造成不可修复的 BUG，需自行承担后果。**
### 1.1 表列表
分类| 子分类| 表名| 简介  
---|---|---|---  
权限控制| 用户-部门职位-角色| FINE_USER| 用户表  
FINE_EXTRA_PROPERTY| 用户额外信息表  
FINE_DEPARTMENT| 部门表  
FINE_POST| 职位表  
FINE_DEP_ROLE| 部门职位的中间表，用户通过该表关联部门与职务  
FINE_CUSTOM_ROLE| 自定义角色表  
FINE_USER_ROLE_MIDDLE| 用户角色的中间表，用户通过该表关联到自定义角色和部门职务角色  
FINE_SOFT_DATA| 同步用户软删除数据表，存储同步用户软删除的数据  
FINE_TENANT| 租户表  
权限-目录| FINE_AUTHORITY| 权限表，只记录当前目录被授予的权限，该目录下的模板和子目录权限不会被记录  
FINE_AUTHORITY_OBJECT| 权限实体表，记录当前目录（不包含该目录下的模板及子目录）权限的对象、目录名称、报表名称  
FINE_AUTH_PREFERENCE| 权限面板用户偏好设置  
FINE_HOMEPAGE_EXPAND| 首页扩展表记录主页类型权限实体的扩展属性  
FINE_FAVORITE_ENTRY| 收藏节点表  
平台操作| 登录| FINE_LAST_LOGIN| 上次登录信息表  
FINE_LOGIN_LOCK| 登录锁定表由于密码错误次数过多导致的锁定详情请参见：[登录锁定](<https://help.fanruan.com/finebi6.0/doc-view-744.html>)  
FINE_BLOCK_IP| 登录锁定IP表由于同一 IP 访问频率过高导致的锁定详情请参见：[访问控制](<https://help.fanruan.com/finereport/doc-view-2455.html>)  
备份还原| FINE_BACKUP_NODE| 备份节点表  
FINE_BACKUP_EXCLUDE_ENTITY| 备份忽略信息表  
定时调度| FINE_SCHEDULE_TASK| 定时任务表  
FINE_SCHEDULE_TASK_PARAM| 定时调度任务参数值  
FINE_SCHEDULE_TASK_EXTEND| 定时调度任务额外属性记录定时调度任务的多选报表模板中的模板参数和模板路径  
FINE_SCHEDULE_TASK_LOG| 定时调度任务树状监控日志  
FINE_SCHEDULE_RECORD| 定时调度任务执行日志  
FINE_SCHEDULE_OUTPUT| 定时任务中的导出  
FINE_BASE_OUTPUT| 任务附件处理主表  
FINE_OUTPUT_CLASS| 自定义类处理  
FINE_OUTPUT_CLIENT_NOTICE| 客户端通知  
FINE_OUTPUT_EMAIL| 推送邮件  
FINE_OUTPUT_FTP| FTP 上传  
FINE_OUTPUT_MOUNT| 定时调度任务挂载目录  
FINE_OUTPUT_PLATFORM_MSG| 平台系统消息  
FINE_OUTPUT_PRINT| 打印处理  
FINE_OUTPUT_SFTP| SFTP 上传  
FINE_OUTPUT_SMS| 发送短信  
FINE_USAGE_DATA| 定时任务触达人数记录表  
消息| FINE_BASE_MESSAGE| 平台消息主表  
FINE_PROCESS_MESSAGE| 上报消息  
FINE_SYSTEM_MESSAGE| 平台系统消息  
上报| FINE_WORKFLOW| 上报流程中的流程  
FINE_WORKFLOW_TASK| 上报流程中的任务  
FINE_WORKFLOW_TASK_IMPL| 上报流程中的任务下发出来的具体任务  
FINE_WORKFLOW_NODE| 上报流程中的节点  
FINE_WORKFLOW_STASH_DATA| 上报流程中的数据暂存  
FINE_WORKFLOW_LOG| 上报流程中的操作日志  
系统管理| 配置| FINE_CONF_CLASSNAME| 配置类的字段是接口类型的情况下，记录其类型  
FINE_CONF_ENTITY| 存储配置类中的数据  
FINE_CONF_XMLENTITY| 有些字段的结构极其复杂，为了将其存储到数据库中，存储成 XML 的方式  
FINE_INTERNATIONAL| 记录多语言数据的表  
FINE_LABEL| 标签表  
FINE_LABEL_INDEX| 标签关系表  
FINE_OPS_EXCEED_TEMPLATES| 超限模板  
SWIFT 模块| FINE_SWIFT_COL_IDX_CONF| 字段索引配置  
FINE_SWIFT_CONFIG_ENTITY| Swift 内部配置表  
FINE_SWIFT_METADATA| 用于存放数据表元数据  
FINE_SWIFT_SEG_LOCATION| Swift Segment 分布信息  
FINE_SWIFT_SEGMENTS| Swift Segment 详细信息  
FINE_SWIFT_SERVICE_INFO| 保存 Swift 服务信息  
FINE_SWIFT_TAB_IDX_CONF| 表索引配置  
FINE_SWIFT_TABLE_PATH| Cube 中间目录配置管理  
FINE_SWIFT_CLUSTER_SIZE| 已弃用  
FINE_SWIFT_DAYS_RECORD| 日访问统计数据缓存表  
FINE_SWIFT_FILEKEY| Swift数据块(seg)的时间索引表  
FINE_SWIFT_RESTORE_RESULT| 日志还原临时记录  
Quartz 模块| QRTZ_BLOB_TRIGGERS| 以 Blob 类型存储的触发器  
QRTZ_CALENDARS| 日历信息存放表  
QRTZ_CRON_TRIGGERS| 存放 Cron 类型的触发器  
QRTZ_FIRED_TRIGGERS| 存放已触发的触发器  
QRTZ_JOB_DETAILS| 存放一个 JobDetail 信息  
QRTZ_LOCKS| 存储程序的悲观锁的信息  
QRTZ_PAUSED_TRIGGER_GRPS| 存储已暂停的 Trigger 组的信息  
QRTZ_SCHEDULER_STATE| 存储集群中 note 实例信息  
QRTZ_SIMPLE_TRIGGERS| 简单触发器的信息  
QRTZ_SIMPROP_TRIGGERS| 存储 CalendarIntervalTrigger 和 DailyTimeIntervalTrigger  
QRTZ_TRIGGERS| 触发器的基本信息  
其他模块| 移动端| FINE_MOBILE_DEVICE| 移动端设备表  
FINE_MOBILE_PUSH_MESSAGE| 移动端消息推送表  
FINE_WEIXIN_USER_RELATION| 手动匹配下的平台和微信用户对应表  
FINE_WEIXIN_OUTPUT| 微信推送的定时调度任务信息  
FINE_WEIXIN_AGENT| 微信管理中的应用信息表  
FINE_WEIXIN_GROUP| 微信管理中的微信群信息表  
FINE_DINGTALK_USER_RELATION| 手动匹配下的平台和钉钉用户对应表  
FINE_DINGTALK_OUTPUT| 钉钉推送的定时调度任务信息  
FINE_DINGTALK_AGENT| 钉钉管理中的应用信息表  
FINE_DINGTALK_GROUP| 钉钉管理中的钉钉群信息表  
FINE_FEISHU_USER_RELATION| 手动匹配下的平台和飞书用户对应表  
FINE_FEISHU_OUTPUT| 飞书推送的定时调度任务信息  
FINE_FEISHU_AGENT| 飞书管理中的应用信息表  
FINE_FEISHU_GROUP| 飞书管理中的飞书群信息表  
报表| FINE_PARAM_TEMPLATE| 模板参数组合  
FINE_PRINT_OFFSET| 打印偏移  
FINE_PRINT_OFFSET_IP_RELATE| 打印偏移 IP 关联表  
FINE_REMOTE_DESIGN_AUTH| 远程设计用户表  
FINE_WRITE_STASH| 填报暂存表  
FINE_PROCESS_EXPAND| 上报流程类型权限实体的扩展属性表  
FINE_REPORT_EXPAND| 报表类型权限实体的扩展属性表  
FINE_EXCEL_SUBMIT_TASK| Excel 批量导入权限实体扩展表  
FINE_VCS| 模板版本管理表  
FINE_COMPONENT_HEALTH| 组件健康记录表  
开放平台相关| FR_OPEN_API| API信息  
FR_OPEN_APP| 客户端信息  
FR_OPEN_AUTH| 权限信息  
FR_OPEN_GROUP| API组名  
FR_OPEN_PRIVILEGE| 开放平台权限表  
FR_OPEN_RELATION| group和api的关联表  
FR_OPEN_API_PERFORMANCE| API查询率  
多产品连接工具相关| FINE_COORDINATOR_ENTRY| 从服务器的模板  
FINE_COORDINATOR_SERVER| 从服务器的信息  
BI| FINE_BI_CONF_ENTITY| BI的配置类数据表  
FINE_BI_CONF_ENTITY_VALUE| BI的配置类数据明细表  
FINE_BI_REPORT_EXPAND| BI报表扩展表  
FINE_DASHBOARD_INDEX| 已弃用  
FINE_REPORT_TABLES_INDEX| 仪表板所用数据集表  
FINE_REPORT_STYLE| 仪表板样式配置  
FINE_REPORT_LINK| 仪表板短链信息表  
FINE_REPORT_WARNING| 仪表板配置预警信息表  
FINE_STATISTIC_OPERATOR| 直连自助数据集统计信息表  
FINE_STATISTIC_TABLE| 直连基础数据集统计信息表  
FINE_STATISTIC_TABLE_INFO| 直连自助数据集步骤信息表  
FINE_UPDATE_TASK| 更新任务表5.1.12 及之后版本新增  
FINE_UPDATE_TASK_DETAIL| 更新任务明细表5.1.12 及之后版本新增  
FINE_UPDATE_DETAIL_INFO| 更新任务明细信息表  
FINE_FAVORITE_REPORT| 分享的仪表板收藏记录表  
FINE_SHARE_INDEX| 已弃用  
FINE_PACK_FILTER| BI业务包行过滤器表  
### 1.2 表间关系
#### 1.2.1 权限
![未命名文件.png](/core/style/lod.png)
#### 1.2.2 上报
![](/core/style/lod.png)
#### 1.2.3 定时调度
![](/core/style/lod.png)
#### 1.2.4 消息
![](/core/style/lod.png)
#### 1.2.5 打印
![](/core/style/lod.png)
注：基于上述表结构，且各表间不直接关联，因此涉及到直接操作数据库的，必须手动删除中间表内的数据。
例如：删除一个部门 = 删除 department + 删除 dep_role + 删除 user_role_middle；
删除一个用户 = 删除 user + 删除 user_role_middle + 删除 extra_property。
## 2\. 用户-部门职位-角色
### 2.1 FINE_USER 用户表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键 关联的表字段fine_extra_property>relatedIdfine_user_role_middle>userIdfine_base_message>userIdfine_auth_preference>userIdfine_favorite_entry>userIdfine_last_login>userIdfine_login_lock>userIdfine_workflow_task>creatorIdfine_authority>roleId| VARCHAR| 255  
BIRTHDAY| 生日| TIMESTAMP| 26  
CREATIONTYPE| 创建类型1：手动创建2：同步创建| INTEGER| 32  
DESCRIPTION| 描述| VARCHAR| 1000  
EMAIL| 邮箱| VARCHAR| 255  
ENABLE| 是否启用1：启用0：不启用| BOOLEAN| 0  
LANGUAGE| 国际化语言| VARCHAR| 255  
LASTOPERATIONTYPE| 最后修改类型1：手动修改2：同步修改| INTEGER| 32  
MALE| 性别true：男false：女| BOOLEAN| 0  
MOBILE| 手机号| VARCHAR| 255  
PASSWORD| 密码该字段值为平台用户密码加密后的密文，不影响平台用户登录数据决策系统| VARCHAR| 255  
REALNAME| 姓名| VARCHAR| 255  
USERNAME| 用户名 关联的表字段fine_base_message>userNamefine_workflow_task>creatorNamefine_schedule_record>creatorfine_schedule_task>creator| VARCHAR| 255  
WORKPHONE| 手机号| VARCHAR| 255  
REALALIAS| realName 排序索引例如姓名是安娜，REALALIAS就是anFR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
USERALIAS| userName 排序索引例如用户名是Alice，USERALIAS就是aliceFR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
SALT| 盐值参数用户密码更新时，盐值随之更新，增加安全度FR：10.0.18 及之后的版本，新增字段BI：5.1.15 及之后的版本，新增字段| VARCHAR| 255  
### 2.2 FINE_EXTRA_PROPERTY 用户额外信息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
NAME| 属性名称user_product_type.platform.bi_datamining：超管user_product_type.platform：PC端使用用户user_product_type.platform.bi_view：BI使用用户-查看用户user_product_type.platform.bi_design：BI使用用户-设计用户user_product_type.mobile：移动端使用用户extra_super_user：用「新增超级管理员」插件新增的超管password_change_time：密码修改时间| VARCHAR| 255  
RELATEDID| 用户id 关联的表字段fine_user>id| VARCHAR| 255  
TYPE| 所关联的数据项类型| INTEGER| 32  
VALUE| 属性值| VARCHAR| 65536  
### 2.3 FINE_DEPARTMENT 部门表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键 关联表字段fine_dep_role>departmentId| VARCHAR| 255  
CREATIONTYPE| 创建类型1：手动创建2：同步创建| INTEGER| 32  
DESCRIPTION| 描述| VARCHAR| 1000  
ENABLE| 是否启用true：启用false：不启用| BOOLEAN| 0  
LASTOPERATIONTYPE| 最后修改类型1：手动修改2：同步修改| INTEGER| 32  
NAME| 部门名| VARCHAR| 255  
PARENTID| 父部门 ID| VARCHAR| 255  
FULLPATH| 部门完整路径祖父部门 ID父部门 ID... FR：2019-05-20 及之后的 JAR，新增字段BI：2019-06-13 及之后的 JAR，新增字段| VARCHAR| 65536  
ALIAS| NAME排序索引例如部门是领导部，ALIAS就是ldb FR：2019-12-05 及之后的 JAR，新增字段BI：2010-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
### 2.4 FINE_POST 职位表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键 关联表字段fine_dep_role>postId| VARCHAR| 255  
CREATIONTYPE| 创建类型1：手动创建2：同步创建| INTEGER| 32  
DESCRIPTION| 描述| VARCHAR| 1000  
ENABLE| 是否启用1：启用0：不启用| BOOLEAN| 0  
LASTOPERATIONTYPE| 最后修改类型1：手动修改2：同步修改| INTEGER| 32  
NAME| 职位名| VARCHAR| 255  
ALIAS| NAME排序索引例如职位是开发工程师，ALIAS就是kfgcs FR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
TENANTID| 租户ID 暂无用途，保留字段| VARCHAR| 255  
### 2.5 FINE_DEP_ROLE 部门职位的中间表
**字段名**| **描述**| **数据类型**| **长度**| **备注**  
---|---|---|---|---  
ID| 主键| VARCHAR| 255| 关联表字段fine_user_role_middle>roleId  
CREATIONTYPE| 创建类型1：手动创建2：同步创建| INTEGER| 32| -  
DEPARTMENTID| 所关联的部门和职务 IDdepartmentId 为空，postId 为空：表示内置+同步部门的所有部门角色(前台不可见)departmentId 为空，postId 不为空：不存在departmentId 不为空，postId 为空：表示不包含职务的部门角色departmentId 不为空，postId 不为空：表示正常部门职务角色| VARCHAR| 255| 关联表字段fine_department>id  
POSTID| VARCHAR| 255| 关联表字段fine_post>id  
LASTOPERATIONTYPE| 最后修改类型1 - 手动修改2 - 同步修改| INTEGER| 32| -  
FULLPATH| 中间数据完整路径| VARCHAR| 3000| FR：2019-05-20 及之后的 JAR，新增字段BI：2019-06-13 及之后的 JAR，新增字段  
TENANTID| 租户ID| VARCHAR| 255| 暂无用途，保留字段  
### 2.6 FINE_CUSTOM_ROLE 自定义角色表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键 关联表字段fine_user_role_middle>roleId| VARCHAR| 255  
CREATIONTYPE| 创建类型1：管理员手动创建 2：同步数据集创建| INTEGER| 32  
DESCRIPTION| 描述信息| VARCHAR| 255  
ENABLE| 是否启用true：启用false：不启用| BOOLEAN| 0  
LASTOPERATIONTYPE| 最后修改类型1：手动修改2：同步修改| INTEGER| 32  
NAME| 角色名| VARCHAR| 255  
ALIAS| NAME排序字段索引例如角色是项目运维，ALIAS就是xmyw FR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
### 2.7 FINE_USER_ROLE_MIDDLE 用户角色的中间表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ROLEID| 所关联的广义角色 IDdepRoleId 或 customRoleId 关联表字段fine_dep_role>idfine_custom_role>idfine_authority>roleId| VARCHAR| 255  
ROLETYPE| 所关联的广义角色类型1：部门职位2：自定义角色| INTEGER| 32  
USERID| 所关联的用户 ID 关联表字段fine_user>id| VARCHAR| 255  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
### 2.8 FINE_SOFT_DATA 同步用户软删除数据表
  * 同步源中删除的数据，从finedb中真实删除，保存不同类型的数据到软删除表中。
  * 同步源中恢复的数据，从软删除表中恢复，相同名称的字段的ID不会发生改变，不影响权限使用。

**字段名**| **描述**| **数据类型**| **长度**| **备注**  
---|---|---|---|---  
ID| 主键| VARCHAR| 255| -  
DELETEDID| 待删除的id| VARCHAR| 255| 1）字段DELETEDID+TYPE组成唯一键即任意两条数据的DELETEDID、TYPE不能完全相同2）字段DELETEDNAME+TYPE组成唯一键即任意两条数据的DELETEDNAME、TYPE不能完全相同  
DELETEDNAME| 待删除的名称用户：userName部门：计算的完整部门名职位：职位名角色：角色名部门职位：部门id+职位id| VARCHAR| 255  
TYPE| 删除的数据类型1：部门2：角色3：用户4：职位5：部门职位中间表6：同步用户与手动自定义角色关系数据7：同步用户与部门职务关系数据| INTEGER| 32  
### 2.9 FINE_TENANT 租户表
暂无用途
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 用户ID| VARCHAR| 255  
NAME| 用户名| VARCHAR| 255  
## 3\. 权限-目录
### 3.1 FINE_AUTHORITY 权限表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AUTHORITY| 权限值1：拒绝2：允许| INTEGER| 32  
AUTHORITYENTITYID| 所关联的权限实体id关联表字段FINE_AUTHORITY_OBJECT>id| VARCHAR| 255  
AUTHORITYENTITYTYPE| 所关联的权限实体类型**平台类型** 0：目录权限，管理系统权限，实体都在 authority_object 表中1：人员管理-部门权限，人员管理-角色权限2：数据连接权限7：定时调度权限8：服务器数据集权限**报表类型** 101：FineReport 模板权限（模板认证）**BI 类型** 201：BI数据权限202：BI数据行过滤器权限（*外界感知不到）203：BI仪表板权限（主要用于分享）204 - BI模板权限（模板认证）205 - BI仪表板分享控制（角色到角色）206 - BI自助数据集分享207 - BI自助数据集分享（角色到角色）| INTEGER| 32  
AUTHORITYTYPE| 权限类型**平台类型** 1：查看权限  
2：授权权限  
3：编辑权限  
4：数据连接管理权限  
7：定时调度管理权限9：人员管理的管理权限10：服务器数据集管理权限**报表类型** 101：FineReport 模板认证权限102：FineReport 模板查看权限103：FineReport 模板填报权限104：FineReport 批量导入任务权限105：FineReport上报流程权限**BI 类型** 201：BI数据使用权限202：BI数据管理权限203：BI报表导出权限204：BI仪表板分享权限205：BI模板认证权限206：BI模板查看权限207：BI模板导出权限208：BI仪表板分享角色控制权限209：BI仪表板分享功能权限210：BI仪表板公共链接功能权限212：BI协作角色权限213：BI协作使用权限214：BI协作编辑权限215：BI组件数据权限| INTEGER| 32  
ROLEID| 所关联的广义角色id 关联表字段fine_dep_role>idfine_custom_role>idfine_user_role_middle>roleidfine_user>id| VARCHAR| 255  
ROLETYPE| 所关联的广义角色类型1：部门，部门下职务2：自定义角色3：用户4：职务| INTEGER| 32  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
### 3.2 FINE_AUTHORITY_OBJECT 权限实体表
包含目录信息、管理系统
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键 关联表字段FINE_AUTHORITY>AUTHORITYENTITYID| VARCHAR| 255  
EXPANDID| 所关联的扩展属性记录id| VARCHAR| 255  
EXPANDTYPE| 所关联的扩展属性类型**平台类型** 1：平台管理系统节点2：首页3：目录5：链接6：文件**报表类型** 101：上报流程102：FineReport 报表**BI 类型** 201：BI 报表| INTEGER| 32  
PARENTID| 所关联的父节点 ID| VARCHAR| 255  
COVERID| 封面 ID系统管理>外观配置>目录样式中的目录封面| VARCHAR| 255  
DESCRIPTION| 描述信息| VARCHAR| 65536  
DEVICETYPE| 显示类型0：未勾选 PC 、平板、手机1：PC2：平板3：PC 、平板4：手机5：勾选 PC 、手机6：勾选平板、手机7：勾选 PC 、平板、手机| INTEGER| 32  
DISPLAYNAME| 显示报表名称和目录名称| VARCHAR| 255  
ICON| 图标 ID系统管理>外观配置>目录样式中的目录图标| VARCHAR| 255  
PATH| 路径，不同 entry 类型表示的意义不同| VARCHAR| 255  
SORTINDEX| 排序顺序| BIGINT| 64  
MOBILEICON| 移动图标 ID| VARCHAR| 255  
FULLPATH| 实体完整路径FR：2019-05-20 及之后的 JAR，新增字段BI：2019-06-13 及之后的 JAR，新增字段| VARCHAR| 65536  
TENANTID| 租户ID暂无用途，保留字段| VARCHAR| 255  
### 3.3 FINE_AUTH_PREFERENCE 权限面板用户偏好设置
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AUTHTYPE| 权限面板类型| INTEGER| 32  
AUTHVISIBLECFG| 权限可见性配置| BIGINT| 64  
USERID| 用户 ID 关联表字段fine_user>id| VARCHAR| 255  
### 3.4 FINE_HOMEPAGE_EXPAND 首页扩展表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ANDROIDPADHOMEPAGE| 用于 Android 平板的主页链接| VARCHAR| 1000  
ANDROIDPHONEHOMEPAGE| 用于 Android 手机的主页链接| VARCHAR| 1000  
IPADHOMEPAGE| 用于 iPad 的主页链接| VARCHAR| 1000  
IPHONEHOMEPAGE| 用于 iPhone 的主页链接| VARCHAR| 1000  
PCHOMEPAGE| 用于 PC 的主页链接| VARCHAR| 1000  
TYPE| 主页类型0：FineReport 模板1：平台目录2：链接3：FineBI 模板| INTEGER| 32  
### 3.5 FINE_FAVORITE_ENTRY 收藏节点表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ENTRYID| 收藏报表 ID| VARCHAR| 255  
TIME| 收藏时间| TIMESTAMP| 26  
USERID| 收藏用户 ID 关联表字段fine_user>id| VARCHAR| 255  
## 4\. 登录
### 4.1 FINE_LAST_LOGIN 上次登录信息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CITY| 登录所在城市| VARCHAR| 255  
IP| 登录所用 IP| VARCHAR| 255  
TIME| 登录时间| TIMESTAMP| 26  
USERID| 登录用户 ID 关联表字段fine_user>id| VARCHAR| 255  
### 4.2 FINE_LOGIN_LOCK 登录锁定表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ERRORTIME| 密码错误次数| INTEGER| 32  
LOCKOBJECT| 锁定 IP 或 username| VARCHAR| 255  
LOCKOBJECTVALUE| IP 或 username 的值| VARCHAR| 255  
LOCKTIME| 何时被锁| TIMESTAMP| 26  
LOCKED| 通常为空| BOOLEAN| 0  
UNLOCKTIME| 何时解锁| TIMESTAMP| 26  
USERID| 用户 ID 关联表字段fine_user>id| VARCHAR| 255  
### 4.3 FINE_BLOCK_IP 登录锁定 IP 表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATETIME| 锁定时间| TIMESTAMP| 26  
IP| 锁定的 IP| VARCHAR| 255  
REJECTEDVISITS| 拒绝次数| INTEGER| 32  
## 5\. 备份还原
### 5.1 FINE_BACKUP_NODE 备份节点表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
BACKUPMODULE| 备份模块jar：JAR包jar-cluster：集群下的jar包（较特殊。集群下，jar包备份会自动转为代理实现，故单独分出这个模块）plugins：插件dashboards：仪表板reportlets：报表模板config：平台配置| VARCHAR| 255  
BACKUPNAME| 备份名| VARCHAR| 255  
BACKUPTIME| 何时备份| TIMESTAMP| 26  
SAVEPATH| 备份地址| VARCHAR| 1000  
BACKUPSIZE| 备份文件大小| DOUBLE| 64  
TYPE| 类型auto：自动备份manual ：手动备份FR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
BACKUPENDTIME| 备份结束时间FR：10.0.11 及之后的版本，新增字段BI：5.1.8 及之后的版本，新增字段| TIMESTAMP| 26  
STATUS| 备份状态  
0：无  
1：成功  
2：失败FR：10.0.11 及之后的版本，新增字段BI：5.1.8 及之后的版本，新增字段| INTEGER| 32  
DETAIL| 详情（出错日志）FR：10.0.11 及之后的版本，新增字段BI：5.1.8 及之后的版本，新增字段| VARCHAR| 65536  
### 5.2 FINE_BACKUP_EXCLUDE_ENTITY 备份忽略信息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 有一些功能配置项是不参与备份还原的，于是有了这张执行备份功能时会被跳过的表。id和value没有具体含义，存储的信息依功能而定。| VARCHAR| 255  
VALUE| VARCHAR| 255  
## 6\. 定时调度
### 6.1 FINE_SCHEDULE_TASK 定时任务表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键关联表字段fine_schedule_task_param>taskIdfine_schedule_record>taskId| VARCHAR| 255  
BACKUPFILEPATH| 备份文件路径预留字段，未使用| VARCHAR| 1000  
CREATOR| 任务创建者关联表字段fine_user>userNamefine_schedule_record>creator| VARCHAR| 255  
EDITABLE| 任务是否可编辑true：可编辑false：不可编辑预留字段，未使用| BOOLEAN| 0  
FILECLEARCOUNT| 附件清理数目-1：不清理0：任务结束即清理1：不清理其他正整数：保留次| INTEGER| 32  
NEXTFIRETIME| 下次执行时间yyyy-MM-dd HH:mm:ss| TIMESTAMP| 26  
OUTPUTSTR| 任务附件处理类型组合字符串，用于条件查询的过滤文件处理方式，逗号隔开：1：邮件通知  
2：FTP上传附件  
3：平台通知  
5：短信通知  
6：挂载平台  
7：自定义附件处理  
8：打印文件  
9：客户端通知  
10：SFTP 上传| VARCHAR| 1000  
PREFIRETIME| 上次执行时间yyyy-MM-dd HH:mm:ss| TIMESTAMP| 26  
REPEATTIME| 重复执行时间间隔| INTEGER| 32  
REPEATTIMES| 重复次数| INTEGER| 32  
SENDBACKUPFILE| 是否发送备份文件true：发送false：不发送预留字段，未使用| BOOLEAN| 0  
SHOWTYPE| 展示类型0：分页预览1：填报预览2：数据分析预览3：PC端预览4：新填报| INTEGER| 32  
TASKCONDITION| 任务状态json格式，包含 type 和 description。**type：** 0：始终执行1：公式判断2：自定义类判断**description：** 具体内容（具体公式或类名）| VARCHAR| 255  
TASKDESCRIPTION| 任务描述预留字段，未使用| VARCHAR| 1000  
TASKNAME| 任务名称| VARCHAR| 255  
TASKPARAMETER| 任务参数json形式，包含 inputStyle 参数输入方式，name 参数名称，type 参数类型，value 参数值**inputStyle 输入方式（非必须）** 0：默认1：数据集**type 参数类型** String：字符串Integer：整型Double：双精度型Date：日期Boolean：布尔值TableColumn：数据集列 **value 参数值** 若参数输入方式为默认，则 value 为字符串若参数输入方式为数据集，则包括 value 数据集名称，colname 数据集字段值| VARCHAR| 65536  
TASKSTATE| 任务状态0：启动1：暂停2：已结束与前台展示的状态不一定对应，展示到前台前需要经过计算| INTEGER| 32  
TASKTYPE| 任务类型0：无调度对象1：报表模板2：BI模板3：多选报表模板| INTEGER| 32  
TEMPLATEPATH| 报表模板/BI模板路径| VARCHAR| 1000  
TRIGGERGROUP| 触发器组json形式，包含多个触发器，包含触发器类型，时间等**triggerType 触发器类型：** 1：只执行一次2：简单重复执行3：明细频率设置4：表达式设置 **startTime 开始时间：** yyyy-MM-dd HH:mm:ss **startType 开始类型：** 1：立即执行2：选择开始时间 **endType 结束类型：** 1：执行完立即结束2：无期限3：选择结束时间4：额外执行多少次 **recurrenceInterval 简单重复执行时间间隔（非必须）****recurrenceIntervalUnit 简单重复执行时间间隔时间单位（非必须）** 1：分钟2：小时3：天4：周**repeatCount 额外执行次数（非必须）：** 整数**hours 明细频率执行小时数（非必须）：** 整数**minutes 明细频率执行分钟数（非必须）：** 整数**dayType 明细频率执行执行日（非必须）：** 1：每日2：每周3：每月**monthDays 明细频率执行执行日为每月时，选择每月的具体天数（非必须）：** 整数数组**weekDays 明细频率执行执行日为每周时，选择每周的具体天数（非必须）：** 整数数组**months 明细频率执行时，哪几个月执行（非必须）：** 整数数组| VARCHAR| 65536  
USERGROUP| 用户组json形式： customRole 角色列表：角色ID数组customRoleStr 角色列表字符串：前台展示用departmentAndPost 部门列表：部门 ID 数组departmentStr 部门列表字符串：前台展示用platformUser 用户列表（非必须）：数组，格式为"姓名(用户名)"platformUserStr 用户列表字符串（非必须）：前台展示用userType 用户类型：1 - 平台用户，2 - 自定义用户columnIndex 自定义用户-数据集列序号（非必须）columnIndexStr 自定义用户-数据集列名（非必须）tableDataName 自定义用户-数据集名称（非必须）| VARCHAR| 65536  
SCHEDULEOUTPUT| 任务推送关联表字段fine_schedule_output>id| VARCHAR| 255  
CONDITIONPARAMETER| 执行条件的自定义类参数json 形式：name 参数名称 value 参数值FR：2020-06-08 及之后的 JAR，新增字段BI：2020-08-04 及之后的 JAR，新增字段| VARCHAR| 1000  
### 6.2 FINE_SCHEDULE_TASK_PARAM 定时调度任务参数值
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
PARAM| 参数列表json 形式：参数名：参数值| VARCHAR| 65536  
TASKNAME| 任务名称| VARCHAR| 255  
TASKID| 任务ID关联表字段fine_schedule_task>id| VARCHAR| 255  
### 6.3 FINE_SCHEDULE_TASK_EXTEND 定时调度任务额外属性
**字段名**|  描述| **数据类型**| **长度**  
---|---|---|---  
ID| 记录ID| VARCHAR| 255  
TASKID| 定时调度任务ID| VARCHAR| 255  
TASKPARAMETERMAP| 定时调度任务多选报表模板的参数| VARCHAR| 65536  
TEMPLATEPATHS| 定时调度任务的多选报表模板| VARCHAR| 4000  
### 6.4 FINE_SCHEDULE_TASK_LOG 定时调度任务树状监控日志
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 记录ID| VARCHAR| 255  
LOGTIME| 日志时间| BIGINT| 64  
LOGTYPE| 日志类型0：失败1：成功2：跳过| INTEGER| 32  
TASKID| 定时调度任务ID| VARCHAR| 255  
TASKLOG| 定时调度任务日志| VARCHAR| 16777216  
TASKNAME| 定时调度任务名称| VARCHAR| 255  
### 6.5 FINE_SCHEDULE_RECORD 定时调度任务执行日志
注：JAR 包在 2019-05-20 之前的工程，使用 fine_schedule_record 表存储定时调度任务执行日志
JAR 包在 2019-05-20 及之后的工程，使用 LogDB 数据库中的 fine_schedule_record 表存储定时调度任务执行日志，请参考：[平台日志 LogDB 数据库](<https://help.fanruan.com/finebi6.0/doc-view-706.html>)
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATOR| 创建者| VARCHAR| 255  
DETAILMESSAGE| 详细信息| VARCHAR| 65536  
FILEPATH| 生成附件路径预留字段，未使用| VARCHAR| 1000  
LOGMESSAGE| 日志信息| VARCHAR| 255  
LOGTIME| 任务执行时间日志打印时间| TIMESTAMP| 26  
LOGTYPE| 日志类型0：失败1：成功2：跳过| INTEGER| 32  
NEXTFIRETIME| 下一次记录时间预留字段，未使用| TIMESTAMP| 26  
RUNTYPE| 附件处理类型0：快照生成1：邮件发送2：FTP 上传3：平台消息推送4：文件打印5：短信发送6：挂载平台7：自定义类处理8：定时填报9：客户端通知10：SFTP 上传-1：附件发送（默认）| INTEGER| 32  
TASKNAME| 任务名称| VARCHAR| 255  
TASKID| 任务ID关联表字段fine_schedule_task>id| VARCHAR| 255  
### 6.6 FINE_SCHEDULE_OUTPUT 定时任务中的导出
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键关联表字段fine_schedule_task>scheduleOutputfine_base_output>outputId| VARCHAR| 255  
BASENAME| 生成附件名称| VARCHAR| 65536  
CREATEATTACHBYUSERNAME| 是否按不同用户生成不同附件1：是0：否| BOOLEAN| 0  
FORMATS| 导出附件类型json 格式：formatNum 文件处理方式：0：输出 CPR1：输出新版 EXCEL2：输出 PDF4：输出 WORD8：输出旧版 EXCEL16：输出 PNG32：输出 FRR| VARCHAR| 255  
BASEMAMEMAP| 定时调度中单张报表模板/BI模板的附件名称| VARCHAR| 65536  
FORMATSMAP| 定时调度单张报表模板/BI模板的附件导出的格式| VARCHAR| 65536  
### 6.7 FINE_BASE_OUTPUT 任务附件处理主表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ACTIONNAME| 附件处理类名| VARCHAR| 255  
EXECUTEBYUSER| 是否按不同用户分别执行1：是0：否| BOOLEAN| 0  
RESULTURL| 结果链接| VARCHAR| 1000  
RUNTYPE| 附件处理类型0：快照生成1：邮件发送2：FTP 上传3：平台消息推送4：文件打印5：短信发送6：挂载平台7：自定义类处理8：定时填报9：客户端通知10：SFTP上传-1：附件发送（默认）| INTEGER| 32  
OUTPUTID| 导出id关联表字段fine_schedule_output>id| VARCHAR| 255  
### 6.8 FINE_OUTPUT_CLASS 自定义类处理
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CLASSNAME| 自定义类名| VARCHAR| 255  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
### 6.9 FINE_OUTPUT_CLIENT_NOTICE 客户端通知表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ADDRESSEE| 接收人| VARCHAR| 65536  
CONTENT| 内容| VARCHAR| 65536  
CUSTOMIZELINK| 自定义链接| VARCHAR| 65536  
LINKOPENTYPE| 链接类型1：定时结果链接2：自定义链接| INTEGER| 32  
MEDIAID| 富文本消息的图片 ID| VARCHAR| 255  
SUBJECT| 主题| VARCHAR| 65536  
TERMINAL| 推送终端目前固定为1，代表app通知| INTEGER| 32  
TYPE| 消息类型1：链接消息2：图文消息3：文件消息| INTEGER| 32  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
### 6.10 FINE_OUTPUT_EMAIL 推送邮件表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ADDLINK| 结果链接| BOOLEAN| 0  
BCCADDRESS| 密送| VARCHAR| 65536  
BODYCONTENT| 内容| VARCHAR| 65536  
CCADDRESS| 抄送| VARCHAR| 65536  
PREVIEWATTACH| 正文预览| BOOLEAN| 0  
SUBJECT| 主题| VARCHAR| 65536  
USEATTACH| 使用附件| BOOLEAN| 0  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
CUSTOMADDRESS| 自定义邮箱的收件人| VARCHAR| 1000  
CUSTOMBCCADDRESS| 自定义邮箱的密送| VARCHAR| 1000  
CUSTOMCCADDRESS| 自定义邮箱的抄送| VARCHAR| 1000  
PREVIEWWIDGET| 是否勾选「正文预览组件内容」FR：10.0.13 及之后的版本，新增字段BI：5.1.10 及之后的版本，新增字段| BOOLEAN| 0  
ADDLINKLIST| 定时调度中单张模板的结果连接| VARCHAR| 65536  
EMAILACCOUNTCONFIGID| 发件人ID| VARCHAR| 255  
REVIEWATTACHLIST| 定时调度中单张模板正文预览的内容| VARCHAR| 65536  
USEATTACHLIST| 定时调度中单张模板生成的附件| VARCHAR| 65536  
### 6.11 FINE_OUTPUT_FTP FTP上传表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
PASSWORD| 密码| VARCHAR| 255  
PORT| 端口号| VARCHAR| 255  
SAVEPATH| 上传路径| VARCHAR| 255  
SERVERADDRESS| 服务器地址| VARCHAR| 255  
USERNAME| 用户名| VARCHAR| 255  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
FTPMODE| FTP 模式passive：被动模式avtive：主动模式| VARCHAR| 255  
### 6.12 FINE_OUTPUT_MOUNT 定时调度任务挂载目录
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
DESCRIPTION| 描述| VARCHAR| 65536  
FOLDERENTRYID| 挂载目录 ID| VARCHAR| 255  
FOLDERENTRYNAME| 挂载目录名称| VARCHAR| 255  
FOLDERENTRYSTR| 挂载目录| VARCHAR| 255  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
### 6.13 FINE_OUTPUT_PLATFORM_MSG 平台系统消息
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CONTENT| 内容| VARCHAR| 65536  
LINKOPENTYPE| 链接类型1：定时结果链接2：自定义链接| INTEGER| 32  
SUBJECT| 主题| VARCHAR| 65536  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
### 6.14 FINE_OUTPUT_PRINT 打印处理
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
PRINTERNAME| 打印机名称| VARCHAR| 255  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
### 6.15 FINE_OUTPUT_SFTP SFTP上传表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
PASSWORD| 密码| VARCHAR| 255  
PORT| 端口号| VARCHAR| 255  
PRIVATEKEY| 私钥| VARCHAR| 255  
SAVEPATH| 上传路径| VARCHAR| 255  
SERVERADDRESS| 服务器地址| VARCHAR| 255  
USERNAME| 用户名| VARCHAR| 255  
### 6.16 FINE_OUTPUT_SMS 短信发送
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
TEMPLATEID| 模板 ID| INTEGER| 32  
ID| 主键关联表字段fine_base_output>id| VARCHAR| 255  
SMSPARAM| 短信参数，json形式，包括：id：参数IDname：参数名称value：参数值type：参数类型**type类型包括：** String：字符串Integer：整型Double：双精度型Date：日期Boolean：布尔值Formula：公式 FR：2019-12-05 及之后的 JAR，新增字段BI：2020-01-15 及之后的 JAR，新增字段| VARCHAR| 255  
### 6.17 FINE_USAGE_DATA 定时任务触达人数记录表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 记录ID| VARCHAR| 255  
DATA| 记录数据| VARCHAR| 1000  
DATATYPE| 记录数据类型| INTEGER| 32  
SUBTYPE| 记录数据子类型| INTEGER| 32  
TAG| 记录数据名称| VARCHAR| 255  
## 7\. 消息
### 7.1 FINE_BASE_MESSAGE 基础消息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATETIME| 消息创建时间| TIMESTAMP| 26  
DATETIME| 消息时间| TIMESTAMP| 26  
MESSAGE| 消息内容| VARCHAR| 65536  
READED| 是否已读1：是0：否| BOOLEAN| 0  
TOASTED| 是否已弹窗提示1：是0：否| BOOLEAN| 0  
TYPE| 消息类型0：系统消息1：上报消息2：模板消息3：移动端消息-1：未知消息| INTEGER| 32  
URL| URL| VARCHAR| 1000  
URLTYPE| URL 类型0：无1：内部链接类型，例如 /report/entry/{id}2：外部链接类型，例如 www.fanruan.com3：平台木块路由，跳转到系统管理某个 Tab 页面4：平台内打开多个模板的 URL| INTEGER| 32  
USERID| 用户 ID关联表字段fine_user>id| VARCHAR| 255  
USERNAME| 用户名关联表字段fine_user>userName| VARCHAR| 255  
### 7.2 FINE_PROCESS_MESSAGE 推送消息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ALLTASKID| 全部任务 ID| VARCHAR| 255  
DEADLINE| 结束时间| TIMESTAMP| 26  
PROCESSED| 是否完成1：完成0：未完成| BOOLEAN| 0  
TASKID| 上报任务 ID| VARCHAR| 255  
ID| 主键关联表字段fine_base_message>id| VARCHAR| 255  
### 7.3 FINE_SYSTEM_MESSAGE 系统消息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
TERMINAL| 推送终端目前固定为1，代表PC端消息通知| BIGINT| 64  
TITLE| 主题| VARCHAR| 255  
ID| 主键关联表字段fine_base_message>id| VARCHAR| 255  
## 8\. 上报
注：2018-12-27 之后的 JAR，新增上报相关表。
### 8.1 FINE_WORKFLOW 上报中的流程表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATETIME| 创建时间| TIMESTAMP| 26  
CREATORID| 创建者 ID关联表字段fine_workflow_task>creatorIdfine_workflow_stash_data>userIdfine_workflow_log>operatorname| VARCHAR| 255  
DESCRIPTION| 描述| VARCHAR| 65536  
NAME| 流程名称| VARCHAR| 255  
NODESID| 节点 ID关联表字段fine_workflow_node>id| VARCHAR| 65536  
### 8.2 FINE_WORKFLOW_TASK 上报中流程任务表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键关联表字段fine_workflow_task_impl>taskId| VARCHAR| 255  
CREATETIME| 创建时间| TIMESTAMP| 26  
CREATORID| 创建者 ID关联表字段fine_user>idfine_workflow>creatorId| VARCHAR| 255  
CREATORNAME| 创建者姓名关联表字段fine_user>username| VARCHAR| 255  
DEADLINEDATE| 截止时间| INTEGER| 32  
DEADLINETYPE| 截止类型| VARCHAR| 255  
ISSUECONTROL| 定时下发| VARCHAR| 65536  
ISSUEOVER| 是否下发结束1：是0：否| BOOLEAN| 0  
LEAPFROGBACK| 越级回退| BOOLEAN| 0  
NAME| 任务名称| VARCHAR| 255  
PARENTID| 父任务 ID关联表字段fine_workflow_task_impl>parentId| VARCHAR| 255  
PROCESSID| 流程 ID关联表字段fine_workflow_task_impl>processId| VARCHAR| 255  
REMINDCONTROL| 提醒方式| VARCHAR| 65536  
TASKNAMECALCULATEONCE| 添加任务时是否勾选「仅在任务发起时计算一次」1：勾选2：不勾选| BOOLEAN| 0  
### 8.3 FINE_WORKFLOW_TASK_IMPL 具体任务表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ALERTED| 是否预警1：是0：否| BOOLEAN| 0  
COMPLETESTATE| 当前任务的操作人及完成状态，1：已完成0：未完成例如：{"demo/authority/产品销售情况查询.cpt":{"sunlin":0}}| VARCHAR| 65536  
CREATETIME| 创建时间（下发的时间）| TIMESTAMP| 26  
CURRENTNODEIDX| 当前的流程节点 ID| INTEGER| 32  
DEADLINE| 截止时间| TIMESTAMP| 26  
FRTASKID| 源 Task 的 ID| VARCHAR| 255  
NAME| 任务名| VARCHAR| 255  
NEEDALLCOMPLETE| 是否需要全部完成1：是0：否| BOOLEAN| 0  
NODEROUTE| 节点走过的路径json| VARCHAR| 65536  
NOTE| 备注| VARCHAR| 16777216  
OPERATORJSON| Node 上的第几个节点是多用户的| VARCHAR| 65536  
OPERATOROFFSET| 多用户节点的第几个用户| VARCHAR| 65536  
OPERATOROFFSETNAME| 多用户节点的第几个用户的名字| VARCHAR| 65536  
PARENTID| 父任务 ID关联表字段fine_workflow_task>parentId| VARCHAR| 255  
PROCESSID| 流程 ID关联表字段fine_workflow_task>processId| VARCHAR| 255  
REPORTOFFSET| 第几个模板| INTEGER| 32  
SENDTIME| 发送时间| TIMESTAMP| 26  
SENDER| 发送人| VARCHAR| 255  
SENDERID| 发送人 ID| VARCHAR| 255  
SONTASKID| 子任务的 ID [{nodeIdx:0, userId:1, taskId:1}]| VARCHAR| 255  
STATE| 任务状态-1：初始0：等待上报1：等待审核2：审核通过3：被退回4：已经关闭5：超时| INTEGER| 32  
TASKID| 源 Task 的 ID关联表字段fine_workflow_task>Id| VARCHAR| 255  
TASKBACKTARGET| 回退的信息| VARCHAR| 255  
### 8.4 FINE_WORKFLOW_NODE 上报流程节点表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键关联表字段fine_workflow>nodesId| VARCHAR| 255  
ALERTCONTROL| 预警详细信息| VARCHAR| 1000  
AUTHORITY| 权限| VARCHAR| 255  
DESCRIPTION| 描述| VARCHAR| 1000  
NAME| 节点名| VARCHAR| 255  
NEEDALLCOMPLETE| 是否需要全部完成后流转1：是0：否| BOOLEAN| 0  
NEEDOFFLINEREPORT| 是否需要离线填报1：是0：否| BOOLEAN| 0  
PROCESSID| 流程 ID| VARCHAR| 255  
REPORTCONTROL| 上报详细信息| VARCHAR| 1000  
### 8.5 FINE_WORKFLOW_STASH_DATA 上报流程数据暂存表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
DATA| 数据| VARCHAR| 16777216  
REPORTPATH| 报表路径| VARCHAR| 65536  
USERID| 用户 ID关联表字段fine_workflow>creatorId| VARCHAR| 255  
TASKID| 任务 ID| VARCHAR| 255  
### 8.6 FINE_WORKFLOW_LOG 上报流程操作日志
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
DATETIME| 时间| TIMESTAMP| 26  
MESSAGE| 消息| VARCHAR| 65536  
OPERATORNAME| 操作者名称关联表字段fine_workflow>creatorId| VARCHAR| 255  
PROCESSNAME| 流程名称| VARCHAR| 255  
TASKNAME| 任务名称| VARCHAR| 255  
## 9\. 系统配置
### 9.1 FINE_CONF_CLASSNAME 接口型配置类型表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 当前字段在配置中的位置| VARCHAR| 255  
CLASSNAME| 在配置中对应的配置值所属的字段类型| VARCHAR| 255  
### 9.2 FINE_CONF_ENTITY 配置类数据表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 数据在配置中的位置| VARCHAR| 255  
VALUE| 数据值| VARCHAR| 65536  
注：存储在数据库的配置内容大多都在这张表，如：id = BackupConfig.backupMemory , value = 1024表示给 BackupConfig 中的 backupMemory 配置一个值 1024，含义是自动备份最多占 1024mb 。
平台常用配置项及前台未提供配置界面，基本都存储在fine_conf_entity表中，详情请参见：[配置信息存储表](<https://help.fanruan.com/finebi6.0/doc-view-907.html>)
### 9.3 FINE_CONF_XMLENTITY xml存储的配置对应表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 数据在配置中的位置| VARCHAR| 255  
VALUE| 该字段的 XML 文本值| BLOB| 67108864  
### 9.4 FINE_INTERNATIONAL 多语言支撑国际化数据表
注：该表出现在 JAR 包在 2020-02-28 及之后的版本中。
**字段名**| **描述**| **数据类型**| **长度**| **备注**  
---|---|---|---|---  
ID| 主键| VARCHAR| 255| -  
DESCRIPTION| 描述| VARCHAR| 1000| -  
I18NKEY| 国际化的 key| VARCHAR| 255| -  
LANGUAGE| 国际化语言zh_CN：简体中文zh_TW：繁体中文en_ US：英语ja_JP：日文ko_KR：韩文| VARCHAR| 255| -  
I18NVALUE| 国际化的值| VARCHAR| 1000| 汉字需要用 [在线转换工具](<https://www.javawind.net/tools/native2ascii.jsp?action=transform>) 进行Unicode编码转化后再写入  
### 9.5 FINE_LABEL 标签表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 记录ID| VARCHAR| 255  
LABELNAME| 标签名称| VARCHAR| 255  
RELATEDTYPE| 标签关联类型| INTEGER| 32  
### 9.6 FINE_LABEL_INDEX 标签关系表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 记录ID| VARCHAR| 255  
LABELID| 标签ID| VARCHAR| 255  
RELATEDID| 标签关联ID| VARCHAR| 255  
### 9.7 FINE_OPS_EXCEED_TEMPLATES 超限模板
注：11.0.5 及之后版本的 FineReport /5.1.23 及之后版本的 FineBI 新增该表。
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| id| VARCHAR| 255  
TEMPLATENAME| 模板名称| VARCHAR| 255  
TEMPLATETYPE| 超限类型| VARCHAR| 255  
## 10\. Swift模块（不允许修改）
### 10.1 FINE_SWIFT_COL_IDX_CONF 字段索引配置表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
COLUMNNAME| 字段名| VARCHAR| 255  
TABLEKEY| 数据表 SourceKey| VARCHAR| 255  
REQUIREGLOBALDICT| 是否生成全局索引1：是0：否| BOOLEAN| 0  
REQUIREINDEX| 是否生成索引1：是0：否| BOOLEAN| 0  
### 10.2 FINE_SWIFT_CONFIG_ENTITY Swift内部配置表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CONFIGKEY| 配置所在的位置| VARCHAR| 255  
CONFIGVALUE| 配置值| VARCHAR| 65536  
### 10.3 FINE_SWIFT_METADATA 数据表元数据存放表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 数据表算出来的 SourceKey| VARCHAR| 255  
FIELDS| 字段信息| VARCHAR| 65536  
REMARK| 转译名| VARCHAR| 255  
SCHEMANAME| 数据库表的 Schema| VARCHAR| 255  
SWIFTSCHEMA| 数据文件存放位置CUBE / LOG| VARCHAR| 255  
TABLENAME| 表名| VARCHAR| 255  
### 10.4 FINE_SWIFT_SEG_LOCATION Swift Segment 分布信息
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CLUSTERID| 集群 ID| VARCHAR| 255  
SEGMENTID| 生成的 Segment ID| VARCHAR| 255  
SOURCEKEY| 数据表 SourceKey，表示 Segment 属于哪个表| VARCHAR| 255  
### 10.5 FINE_SWIFT_SEGMENTS Swift Segment 详细信息
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 生成的 Segment ID| VARCHAR| 255  
SEGMENTORDER| Segment 序号| INTEGER| 32  
SEGMENTOWNER| 数据表 SourceKey，表示 Segment 属于哪个表| VARCHAR| 255  
SEGMENTURI| 数据文件的相对 URL| VARCHAR| 65536  
STORETYPE| 数据保存类型MEMORY：内存存储，只在内存有，关机就丢失NIO：是把内存的内容写入到文件，解决关机丢失的问题FINE_IO：fr自己实现的一个io框架，NIO文件满了就往FINE_IO里写| VARCHAR| 255  
SWIFTSCHEMA| 数据文件存放目录CUBE / LOG| VARCHAR| 255  
### 10.6 FINE_SWIFT_SERVICE_INFO 保存 Swift 服务信息
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| Service ID| VARCHAR| 255  
CLUSTER_ID| 集群 ID| VARCHAR| 255  
IS_SINGLETON| 是否只启动一个1：是0：否| BOOLEAN| 0  
SERVICE| 服务类型cluster_master_service：记录主节点id，供所有节点同步使用  
其它：每个节点启动的服务（如查询、导入、历史、实时等服务）| VARCHAR| 255  
SERVICE_INFO| 服务的其他信息| VARCHAR| 255  
### 10.7 FINE_SWIFT_TAB_IDX_CONF 表索引配置
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
TABLEKEY| 表 SourceKey| VARCHAR| 255  
ALLOTRULE| 分块逻辑| VARCHAR| 255  
### 10.8 FINE_SWIFT_TABLE_PATH Cube 中间目录配置管理
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CLUSTERID| 集群 ID单机为 LOCAL| VARCHAR| 255  
TABLEKEY| 表 SourceKey| VARCHAR| 255  
LASTPATH| 上次使用的临时目录| INTEGER| 32  
TABLEPATH| 当前使用的中间目录| INTEGER| 32  
TMPDIR| 生成 Cube 时使用的中间目录| INTEGER| 32  
### 10.9 FINE_SWIFT_CLUSTER_SIZE 
该表已弃用。
**字段名**| **数据类型**| **长度**  
---|---|---  
ID| VARCHAR| 255  
PRIMARY_CLUSTER_SIZE| INTEGER| 32  
DESCRIPTION| VARCHAR| 255  
### 10.10 FINE_SWIFT_DAYS_RECORD 日访问统计数据缓存表
注：该表于2022年7月弃用，内容转由logdb的fine_pretreat_job_result表存储。
swift每天凌晨会有个定时任务，去查询前一天访问统计中的「日访问量，日活跃模板数，日活跃用户数」，并记录到该表中作为缓存。
这张表字段名中的「TASK」意思就是这个定时任务。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
TASK_ID| 任务ID| VARCHAR| 255  
TASK_RESULT| 查询的结果：包括日活跃用户数，日活跃模板数，日访问量| VARCHAR| 4096  
TASK_CONDITION| 查询的条件：任务类型 + 查询时间范围| VARCHAR| 1024  
TASK_TYPE| 任务类型| VARCHAR| 255  
### 10.11 FINE_SWIFT_FILEKEY swift数据块(seg)的时间索引表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SEGMENTID| swift数据块的id，对应fine_swift_segments的id| VARCHAR| 255  
TIMEKEY| 数据块的文件索引。2021-4-11之后的版本，cubes目录改了，每天都会生成一个文件夹存储这一天的数据，并以日期命名，例如：20210701| VARCHAR| 255  
### 10.12 FINE_SWIFT_RESTORE_RESULT 日志还原临时记录
该表为临时状态表，写入后立即删除，正常情况下该表内容为空。  

字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
UUID| 记录id| VARCHAR| 255  
CLUSTERID| 集群id  
单机为LOCAL| VARCHAR| 255  
ENDTIME| 日志还原区间的右边界| BIGINT| 64  
ERRORCODE| 错误码| INTEGER| 32  
ERRORMSG| 错误信息| VARCHAR| 255  
EXCEPTION| 异常信息| VARCHAR| 65536  
STARTTIME| 日志还原区间的左边界| BIGINT| 64  
SUCCESS| 日志还原过程结果  
true：成功  
false：失败| BOOLEAN| [NULL]  
## 11\. Quartz 模块（不允许修改）
### 11.1 QRTZ_BLOB_TRIGGERS 以 Blob 类型存储的触发器
作为 Blob 类型存储，用于 Quartz 用户使用 JDBC 创建自己定制的 Trigger 类型，JobStore 并不知道如何存储实例的时候。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| qrtz_triggers 表 trigger_group 的外键| VARCHAR| 255  
TRIGGER_NAME| qrtz_triggers 表 trigger_name 的外键| VARCHAR| 255  
BLOB_DATA| 一个 blob 字段，存放持久化 Trigger 对象| VARBINARY| 16777216  
### 11.2 QRTZ_CALENDARS 日历信息存放表
以 Blob 类型存储存放日历信息， quartz可配置一个日历来指定一个时间范围。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
CALENDAR_NAME| 日历名称| VARCHAR| 255  
SCHED_NAME| 调度名称| VARCHAR| 255  
CALENDAR| 一个 blob 字段，存放持久化 calendar 对象| VARBINARY| 4000  
### 11.3 QRTZ_CRON_TRIGGERS 存放 Cron 类型的触发器
存储触发器的 cron 表达式表。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| qrtz_triggers 表 trigger_group 的外键| VARCHAR| 255  
TRIGGER_NAME| qrtz_triggers 表 trigger_name 的外键| VARCHAR| 255  
CRON_EXPRESSION| Cron 表达式| VARCHAR| 255  
TIME_ZONE_ID| 时区| VARCHAR| 255  
### 11.4 QRTZ_FIRED_TRIGGERS 存放已触发的触发器
存储与已触发的 Trigger 相关的状态信息，以及相联 Job 的执行信息。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ENTRY_ID| 调度器实例 id| VARCHAR| 255  
SCHED_NAME| 调度名称| VARCHAR| 255  
FIRED_TIME| 触发的时间| NUMERIC| 19  
INSTANCE_NAME| 调度器实例名| VARCHAR| 255  
IS_NONCONCURRENT| 是否并发1：是0：否| BOOLEAN| 0  
JOB_GROUP| 集群中 job 所属组的名字| VARCHAR| 255  
JOB_NAME| 集群中 job 的名字| VARCHAR| 255  
PRIORITY| 优先级| INTEGER| 32  
REQUESTS_RECOVERY| 是否接受恢复执行，默认为 01：是0：否| BOOLEAN| 0  
SCHED_TIME| 定时器制定的时间| NUMERIC| 19  
STATE| 状态| VARCHAR| 255  
TRIGGER_GROUP| qrtz_triggers 表 trigger_group 的外键| VARCHAR| 255  
TRIGGER_NAME| qrtz_triggers 表 trigger_name 的外键| VARCHAR| 255  
### 11.5 QRTZ_JOB_DETAILS 存放一个 JobDetail 信息
存储每一个已配置的 jobDetail 的详细信息。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
JOB_GROUP| 集群中 job 的所属组的名字| VARCHAR| 255  
JOB_NAME| 集群中 job 的名字| VARCHAR| 255  
SCHED_NAME| 调度名称| VARCHAR| 255  
DESCRIPTION| 集群中个 notejob 实现类的全限定名，quartz 就是根据这个路径到 classpath 找到该 job 类| VARCHAR| 255  
IS_DURABLE| 是否持久化1：是，quartz 会把 job 持久化到数据库中0：否| BOOLEAN| 0  
IS_NONCONCURRENT| 是否并发执行1：是0：否| BOOLEAN| 0  
IS_UPDATE_DATA| 是否更新数据1：是0：否| BOOLEAN| 0  
JOB_CLASS_NAME| 集群中 notejob 实现类的全限定名，quartz 就是根据这个路径到 classpath 找到该 job 类| VARCHAR| 255  
JOB_DATA| 一个 blob 字段，存放持久化 job 对象| VARBINARY| 16777216  
REQUESTS_RECOVERY| 是否接受恢复执行，默认为01：是0：否| BOOLEAN| 0  
CREATOP| -| VARCHAR| 255  
### 11.6 QRTZ_LOCKS 存放悲观锁信息
存储程序的悲观锁的信息（假如使用了悲观锁）。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
LOCK_NAME| 悲观锁名称| VARCHAR| 255  
SCHED_NAME| 调度名称| VARCHAR| 255  
### 11.7 QRTZ_PAUSED_TRIGGER_GRPS
存储已暂停的 Trigger 组的信息。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| qrtz_triggers表trigger_group的外键| VARCHAR| 255  
### 11.8 QRTZ_SCHEDULER_STATE
存储集群中 note 实例信息，quartz 会定时读取该表的信息判断集群中每个实例的当前状态。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
INSTANCE_NAME| 之前配置文件中org.quartz.scheduler.instanceId配置的名字，就会写入该字段| VARCHAR| 255  
SCHED_NAME| 调度名称| VARCHAR| 255  
CHECKIN_INTERVAL| 检查间隔时间| NUMERIC| 19  
LAST_CHECKIN_TIME| 上次检查时间| NUMERIC| 19  
### 11.9 QRTZ_SIMPLE_TRIGGERS 简单触发器的信息
存储简单的 Trigger，包括重复次数，间隔，以及已触发的次数。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| 触发器组| VARCHAR| 255  
TRIGGER_NAME| 触发器名称| VARCHAR| 255  
REPEAT_COUNT| 重复的次数统计| NUMERIC| 19  
REPEAT_INTERVAL| 重复时间间隔| NUMERIC| 19  
TIMES_TRIGGERED| 已触发的次数| NUMERIC| 19  
### 11.10 QRTZ_SIMPROP_TRIGGERS
qrtz_simprop_triggers 存储CalendarIntervalTrigger（类似于SimpleTrigger，指定从某一个时间开始，以一定的时间间隔执行的任务触发器）和 DailyTimeIntervalTrigger（指定每天的某个时间段内，以一定的时间间隔执行的任务触发器）
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| qrtz_triggers表trigger_group的外键| VARCHAR| 255  
TRIGGER_NAME| qrtz_triggers表trigger_ name的外键| VARCHAR| 255  
BOOL_PROP_1| Boolean类型的trigger的第一个参数| BOOLEAN| 0  
BOOL_PROP_2| Boolean类型的trigger的第二个参数| BOOLEAN| 0  
DEC_PROP_1| decimal类型的trigger的第一个参数| NUMERIC| 19  
DEC_PROP_2| decimal类型的trigger的第二个参数| NUMERIC| 19  
INT_PROP_1| int类型的trigger的第一个参数| INTEGER| 32  
INT_PROP_2| int类型的trigger的第二个参数| INTEGER| 32  
LONG_PROP_1| long类型的trigger的第一个参数| NUMERIC| 19  
LONG_PROP_2| long类型的trigger的第二个参数| NUMERIC| 19  
STR_PROP_1| String类型的trigger的第一个参数| VARCHAR| 255  
STR_PROP_2| String类型的trigger的第二个参数| VARCHAR| 255  
STR_PROP_3| String类型的trigger的第三个参数| VARCHAR| 255  
### 11.11 QRTZ_TRIGGERS 触发器的基本信息
保存触发器的基本信息。
注：设置 [用户同步数据集](<https://help.fanruan.com/finebi6.0/doc-view-413.html>) 后，在 qrtz_triggers 表中找到「JOB_NAME」为「syncUser」的数据，可查看更新用户时间。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
SCHED_NAME| 调度名称| VARCHAR| 255  
TRIGGER_GROUP| 触发器组名称| VARCHAR| 255  
TRIGGER_NAME| 触发器名称| VARCHAR| 255  
CALENDAR_NAME| 日程表名称| VARCHAR| 255  
DESCRIPTION| 详细描述信息| VARCHAR| 255  
END_TIME| 结束时间| NUMERIC| 19  
JOB_DATA| 一个 blob 字段，存放持久化 job 对象| VARBINARY| 16777216  
JOB_GROUP| qrtz_job_details 表 job_group 的外键| VARCHAR| 255  
JOB_NAME| qrtz_job_details 表 job_name 的外键| VARCHAR| 255  
MISFIRE_INSTR| 措施或者是补偿执行的策略| INTEGER| 32  
NEXT_FIRE_TIME| 下一次触发时间| NUMERIC| 19  
PREV_FIRE_TIME| 上一次触发时间| NUMERIC| 19  
PRIORITY| 优先级| INTEGER| 32  
START_TIME| 开始时间| NUMERIC| 19  
TRIGGER_STATE| 当前触发器状态WAITING：等待 PAUSED：暂停 ACQUIRED：正常执行 BLOCKED：阻塞 ERROR：错误| VARCHAR| 255  
TRIGGER_TYPE| 触发器的类型SIMPLE：在特定时间间隔后重复执行。如9点开始，每隔1小时，执行一次。CRON：基于日历计划，如每周二凌晨2点执行。| VARCHAR| 255  
APPOINT_ID| 平台集群节点id。表示该trigger需要在哪一个节点运行，为空则都执行。| VARCHAR| 255  
## 12\. 移动端
### 12.1 FINE_MOBILE_DEVICE 移动端设备表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATEDATE| 设备添加日期| TIMESTAMP| 26  
DEVICENAME| 设备名称| VARCHAR| 255  
MACADDRESS| 设备 Mac 地址| VARCHAR| 255  
PASSED| 设备是否通过认证1：是0：否| BOOLEAN| 0  
UPDATEDATE| 设备修改日期| TIMESTAMP| 26  
USERNAME| 关联的用户名| VARCHAR| 255  
### 12.2 FINE_MOBILE_PUSH_MESSAGE 移动端消息推送表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
GROUPID| 消息接收组 ID| VARCHAR| 255  
MEDIAID| 富文本消息的图片 ID| VARCHAR| 255  
MSGTYPE| 消息类型1：普通文本消息2：图文消息3：文件消息| INTEGER| 32  
TERMINAL| 推送终端目前固定为1，代表app通知| INTEGER| 32  
TITLE| 消息标题| VARCHAR| 255  
ID| 主键| VARCHAR| 255  
### 12.3 FINE_WEIXIN_USER_RELATION 手动匹配下的平台和微信用户对应表
注：仅当定时调度任务中勾选了「客户端通知>微信通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
FSUSER| 平台用户名| VARCHAR| 255  
WEIXINUSER| 微信userid| VARCHAR| 255  
### 12.4 FINE_WEIXIN_OUTPUT 微信推送的定时调度任务信息
注：仅当定时调度任务中勾选了「客户端通知>微信通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
AGENTID| 应用ID| VARCHAR| 255  
CONTENT| 客户端通知的内容| VARCHAR| 255  
CUSTOMIZELINK| 自定义链接填的内容| VARCHAR| 255  
LINKOPENTYPE| 客户端通知的链接类型1：定时调度链接2：自定义链接| VARCHAR| 255  
MEDIAID| 调用上传接口得到的文件或者图片的mediaId| VARCHAR| 255  
SUBJECT| 客户端通知的标题| VARCHAR| 255  
TERMINAL| 固定是 2，对应微信通知| INTEGER| 32  
TYPE| 客户端通知的消息类型1：链接消息2：图文消息3：文件消息| INTEGER| 32  
ID| 主键| VARCHAR| 255  
ADDRESSEE| 额外接收消息的客户端，1代表推送群| INTEGER| 32  
CHATGROUPS| 存储推送群id的String数组| VARCHAR| 255  
### 12.5 FINE_WEIXIN_AGENT 微信管理中的应用信息表
注：仅当定时调度任务中勾选了「客户端通知>微信通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
AGENTNAME| 应用名称| VARCHAR| 255  
CORPID| 企业corpId| VARCHAR| 255  
SECRET| 应用秘钥| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
TYPE| 应用类型1：管理组秘钥的应用，属于老旧应用2：正常应用3：未能获取到token的应用| INTEGER| 32  
### 12.6 FINE_WEIXIN_GROUP 微信管理中的微信群信息表
注：仅当定时调度任务中勾选了「客户端通知>微信群通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
GROUPID| 群的chatid，用于推送| VARCHAR| 255  
GROUPNAME| 群名称| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
### 12.7 FINE_DINGTALK_USER_RELATION 手动匹配下的平台和钉钉用户对应表
注：仅当定时调度任务中勾选了「客户端通知>钉钉通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
FSUSER| 平台用户名| VARCHAR| 255  
DINGTALKUSER| 钉钉userid| VARCHAR| 255  
### 12.8 FINE_DINGTALK_OUTPUT 钉钉推送的定时调度任务信息
注：仅当定时调度任务中勾选了「客户端通知>钉钉通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
AGENTID| 应用ID| VARCHAR| 255  
CONTENT| 客户端通知的内容| VARCHAR| 255  
CUSTOMIZELINK| 自定义链接填的内容| VARCHAR| 255  
LINKOPENTYPE| 客户端通知的链接类型1：定时调度链接2：自定义链接| VARCHAR| 255  
MEDIAID| 调用上传接口得到的文件或者图片的mediaId| VARCHAR| 255  
SUBJECT| 客户端通知的标题| VARCHAR| 255  
TERMINAL| 固定是4，对应钉钉通知| INTEGER| 32  
TYPE| 客户端通知的消息类型1：链接消息2：图文消息3：文件消息| INTEGER| 32  
ID| 主键| VARCHAR| 255  
ADDRESSEE| 额外接收消息的客户端，1代表推送群| INTEGER| 32  
CHATGROUPS| 存储推送群id的String数组| VARCHAR| 255  
### 12.9 FINE_DINGTALK_AGENT 钉钉管理中的应用信息表
注：仅当定时调度任务中勾选了「客户端通知>钉钉通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
AGENTNAME| 应用名称| VARCHAR| 255  
APPKEY| 应用appKey|   
|   
  
CORPID| 企业corpId| VARCHAR| 255  
SECRET| 应用秘钥| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
TYPE| 应用类型1：正常应用2：未能获取到token的应用| INTEGER| 32  
### 12.10 FINE_DINGTALK_GROUP 钉钉管理中的钉钉群信息表
注：仅当定时调度任务中勾选了「客户端通知>钉钉群通知」并保存时，该表出现并生成数据。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
GROUPID| 群的chatid，用于推送| VARCHAR| 255  
GROUPNAME| 群名称| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
### 12.11 FINE_FEISHU_USER_RELATION 手动匹配下的平台和飞书用户对应表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
FSUSER| 平台用户名| VARCHAR| 255  
FEISHUUSER| 飞书userid| VARCHAR| 255  
### 12.12 FINE_FEISHU_OUTPUT 飞书推送的定时调度任务信息
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
AGENTID| 应用ID| VARCHAR| 255  
CONTENT| 客户端通知的内容| VARCHAR| 255  
CUSTOMIZELINK| 自定义链接填的内容| VARCHAR| 255  
LINKOPENTYPE| 客户端通知的链接类型1：定时调度链接2：自定义链接| VARCHAR| 255  
MEDIAID| 调用上传接口得到的文件或者图片的mediaId| VARCHAR| 255  
SUBJECT| 客户端通知的标题| VARCHAR| 255  
TERMINAL| 固定是4，对应钉钉通知| INTEGER| 32  
TYPE| 客户端通知的消息类型1：链接消息2：图文消息3：文件消息| INTEGER| 32  
ID| 主键| VARCHAR| 255  
ADDRESSEE| 额外接收消息的客户端，1代表推送群| INTEGER| 32  
CHATGROUPS| 存储推送群id的String数组| VARCHAR| 255  
### 12.13 FINE_FEISHU_AGENT 飞书管理中的应用信息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
AGENTNAME| 应用名称| VARCHAR| 255  
CORPID| 企业corpId| VARCHAR| 255  
ENCRYPTED| 是否加密true：加密false：不加密| BOOLEAN| 0  
SECRET| 应用秘钥| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
TYPE| 应用类型1：管理组秘钥的应用，属于老旧应用2：正常应用3：未能获取到token的应用| INTEGER| 32  
### 12.14 FINE_FEISHU_GROUP 飞书管理中的飞书群信息表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
AGENTID| 应用ID| VARCHAR| 255  
GROUPID| 群的chatid，用于推送| VARCHAR| 255  
GROUPNAME| 群名称| VARCHAR| 255  
TIMESTAMP| 时间戳| VARCHAR| 255  
## 13\. 报表
### 13.1 FINE_PARAM_TEMPLATE 模板参数组合
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
TEMPLATEID| 模板 ID| VARCHAR| 255  
TPGROUP| 参数组合| VARCHAR| 65536  
USERNAME| 用户名| VARCHAR| 255  
### 13.2 FINE_PRINT_OFFSET 打印偏移
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CPTNAME| 模板名称| VARCHAR| 50  
IP| 客户端ip地址| VARCHAR| 20  
OFFSETX| 横向偏移量| VARCHAR| 50  
OFFSETY| 纵向偏移量| VARCHAR| 50  
SIGN| 偏移选项0：不偏移1：全局配置2：单模板配置| VARCHAR| 10  
### 13.3 FINE_PRINT_OFFSET_IP_RELATE 打印偏移 IP 关联表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CHILDIP| 关联客户端 IP关联表字段fine_print_offset>id| VARCHAR| 20  
MOTHERID| 对应打印偏移表的 ID 字段| VARCHAR| 255  
### 13.4 FINE_REMOTE_DESIGN_AUTH 远程设计用户表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
PATH| 有远程设计权限的路径| VARCHAR| 1000  
PATHTYPE| 路径类型0：文件 1：文件夹| BOOLEAN| 0  
USERID| 用户 ID| VARCHAR| 255  
USERNAME| 用户名| VARCHAR| 255  
ROLETYPE| 角色类型0：无角色1：部门职务角色2：自定义角色3：用户角色| INTEGER| 32  
### 13.5 FINE_WRITE_STASH 填报暂存表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
DATA| 暂存数据| VARCHAR| 16777216  
REPORTPATH| 模板路径| VARCHAR| 1000  
USERNAME| 用户名| VARCHAR| 255  
### 13.6 FINE_PROCESS_EXPAND FineReport 上报扩展表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
PROCESSTYPE| 上报流程类型1：上报任务管理2：上报流程管理3：我的上报任务| INTEGER| 32  
### 13.7 FINE_REPORT_EXPAND FineReport 报表扩展表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
SHOWTYPE| 0：填报1：分页2：分析3：表单预览4：新填报| INTEGER| 32  
TRANSMITPARAMETERS| 自定义的一些预览参数| VARCHAR| 65536  
### 13.8 FINE_EXCEL_SUBMIT_TASK Excel批量导入权限实体扩展表
注：JAR 包在 2018-12-27 之后的 FR 工程，新增该表。
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATETIME| 任务创建时间| TIMESTAMP| 26  
DESCRIPTION| 描述| VARCHAR| 1000  
NAME| 任务名称| VARCHAR| 255  
REPORTPATH| 关联模板路径| VARCHAR| 1000  
SUBMITTIME| 提交时间| TIMESTAMP| 26  
### 13.9 FINE_VCS 模板版本管理表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
COMMITCODE| 用来回滚 commit| VARCHAR| 255  
COMMITMSG| git commit Msg| VARCHAR| 255  
FILENAME| 模板名称| VARCHAR| 255  
TIME| 提交时间| TIMESTAMP| 26  
USERNAME| 用户名| VARCHAR| 255  
VERSION| 版本号| INTEGER| 32  
### 13.10 FINE_COMPONENT_HEALTH 组件健康记录表
  

**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CLUSTERNODEID| 节点ID| VARCHAR| 255  
EXTRAINFO| 额外信息暂无用途，保留字段| VARCHAR| 65536  
MODULE| 模块| VARCHAR| 255  
STATUS| 状态类型  
1：可用  
2：未开启  
3：有异常  
4：超时  
5：未知错误| INTEGER| 32  
TIME| 提交时间| TIMESTAMP| 26  
  

## 14\. 开放平台插件
注：由于安装了开放平台插件，才会产生本章所有表。
### 14.1 FR_OPEN_API API信息
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
CREATETIME| 创建日期| TIMESTAMP| 26  
DESCRIPTION| 描述| VARCHAR| 255  
EDITABLE| 可编辑  
1：可编辑  
0：不可编辑| INTEGER| 32  
ENABLE| 可用  
1：可用  
0：不可用| INTEGER| 32  
NAME| 显示名的国际化key| VARCHAR| 255  
CLASS| 类路径| VARCHAR| 255  
CONFIG| 配置项（json）| VARCHAR| 10000  
TDEFAULT| 默认参数（json）| VARCHAR| 255  
INFO| 请求路径| VARCHAR| 255  
ISPUBLIC| 是否公开  
1：公开  
0：不公开| INTEGER| 32  
METHOD| 方法（GET/POST等）| VARCHAR| 255  
### 14.2 FR_OPEN_APP 客户端信息
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
CREATETIME| 创建日期| TIMESTAMP| 26  
DESCRIPTION| 描述| VARCHAR| 255  
EDITABLE| 可编辑  
1：可编辑  
0：不可编辑| INTEGER| 32  
ENABLE| 可用  
1：可用  
0：不可用| INTEGER| 32  
NAME| 显示名的国际化key| VARCHAR| 255  
ICON| 图标| VARCHAR| 255  
SECRET| 密钥（加密后）| VARCHAR| 255  
SPAREAUTH| 认证器ID| VARCHAR| 255  
### 14.3 FR_OPEN_AUTH 权限信息
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
CREATETIME| 创建日期| TIMESTAMP| 26  
DESCRIPTION| 描述| VARCHAR| 255  
EDITABLE| 可编辑  
1：可编辑  
0：不可编辑| INTEGER| 32  
ENABLE| 可用  
1：可用  
0：不可用| INTEGER| 32  
NAME| 显示名的国际化key| VARCHAR| 255  
CLAZZ| 类路径| VARCHAR| 255  
CONFIG| 配置项（json）| VARCHAR| 255  
TDEFAULT| 默认参数（json）| VARCHAR| 255  
### 14.4 FR_OPEN_GROUP API组名
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
CREATETIME| 创建日期| TIMESTAMP| 26  
DESCRIPTION| 描述| VARCHAR| 255  
EDITABLE| 可编辑  
1：可编辑  
0：不可编辑| INTEGER| 32  
ENABLE| 可用  
1：可用  
0：不可用| INTEGER| 32  
NAME| 显示名的国际化key| VARCHAR| 255  
### 14.5 FR_OPEN_PRIVILEGE 开放平台权限表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
APIID| apiId| VARCHAR| 255  
CLIENTID| 客户端id| VARCHAR| 255  
### 14.6 FR_OPEN_RELATION group和api的关联表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| ID| VARCHAR| 255  
GROUPID| 组Id| VARCHAR| 255  
### 14.7 FR_OPEN_API_PERFORMANCE API查询率
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| api接口的id| VARCHAR| 255  
FREQUENCY| 对应api的访问频率限制单位：次/s| INTEGER| 32  
  
## 15\. 多产品连接工具插件
注：由于安装了多产品连接工具插件，才会产生本章所有表。
### 15.1 FINE_COORDINATOR_ENTRY 从服务器的模板
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ORIGINPATH| 从服务器模板原始路径| VARCHAR| 255  
### 15.2 FINE_COORDINATOR_SERVER 从服务器的信息
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
NAME| 从服务器名称| VARCHAR| 255  
URL| 从服务器URL地址| VARCHAR| 1000  
WITHTEMPLATE| 是否是模板服务器0：不是1：是| BOOLEAN| -  
## 16\. BI（BI独有）
### 16.1 FINE_BI_CONF_ENTITY BI的配置类数据表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| 主键uuid| VARCHAR| 255  
IS_SEGMENT| 是否数据分段保存| INTEGER| 32  
KEY_CLASS| 自定义或默认的类名| VARCHAR| 255  
ENTITY_KEY| 4000，key值| VARCHAR| 4000  
NAMESPACE| 命名空间| VARCHAR| 255  
SEGMENT_LENGTH| 数据分段每段长度| INTEGER| 32  
VALUE_CLASS| 自定义或默认的类名| VARCHAR| 255  
ENTITY_VALUE| 4GB，value值，如果分段保存，这里的值为空字符串| VARCHAR| 16777216  
VALUES_INDEX| 数据段索引| VARCHAR| 65536  
VALUES_LENGTH| 数据实际长度| INTEGER| 32  
### 16.2 FINE_BI_CONF_ENTITY_VALUE BI的配置类数据明细表
**字段名**| **描述**| **数据类型**| **长度**  
---|---|---|---  
ID| entity_id + 分段位置| VARCHAR| 255  
ENTITY_ID| 对应fine_bi_conf_entity表的主键| VARCHAR| 255  
ENTITY_VALUE| value转二进制分段| VARCHAR| 16777216  
### 16.3 FINE_BI_REPORT_EXPAND BI 报表扩展表
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
TEMPLATEID| 挂载资源的展示ID注：6.0与6.1版本，该字段记录内容不完全相同| VARCHAR| 255  
### 16.4 FINE_DASHBOARD_INDEX 仪表板节点索引表
该表已弃用，如需查看仪表板相关信息，可参考：[仪表板相关](<https://help.fanruan.com/finebi6.X/doc-view-2072.html#9f3d1bec8ba1b549>)
若用户从5.0升级至6.0版本，FineDB中会保留该表，但不会继续更新该表。
该表保存所有仪表板信息，包含仪表板的编号。
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
APPLYTIME| 申请挂出的时间| BIGINT| 64  
CREATEBY| 创建者用户id| VARCHAR| 255  
FOLDER| 标记是否为文件夹节点true：是文件夹false：不是文件夹| BOOLEAN| 0  
HANGOUT| 标记挂出状态-1：未分组（普通用户的仪表板文件夹的状态）1：申请挂出2：挂出3：其他状态| INTEGER| 32  
INITTIME| 创建时间| BIGINT| 64  
LASTUPDATETIME| 最后更新时间| BIGINT| 64  
MOUNTEDDIRIDS| mountedDirlds有值的就是被挂出的| VARCHAR| 16777216  
NAME| 展示用的名字| VARCHAR| 255  
PID| 父节点id| VARCHAR| 255  
REPORTID| 节点id，和id一致| VARCHAR| 255  
REPORTPUBLICLINK| 公共链接| VARCHAR| 16777216  
SHARED| 字段弃用| BOOLEAN| 0  
WATERMARK| 水印是否开启1 - 是0 - 否| BOOLEAN| 0  
### 16.5 FINE_REPORT_TABLES_INDEX 仪表板所用数据集表
注：FineBI6.0起该表已弃用，请查询FINEBI_REPORT_INDEX_EN表，详情请参见：[FineDB表结构-BI配置](<https://help.fanruan.com/finebi6.X/doc-view-2072.html#9f3d1bec8ba1b549>)
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
REPORTID| 节点 id，和 id 一致关联表字段fine_dashboard_index>reportId| VARCHAR| 255  
TABLES| 仪表板使用到的数据集的信息| VARCHAR| 16777216  
### 16.6 FINE_REPORT_STYLE 仪表板样式配置
注：FineBI6.0起该表已弃用，请查询FINEBI_REPORT_STYLE_EN表，详情请参见：[FineDB表结构-BI配置](<https://help.fanruan.com/finebi6.X/doc-view-2072.html#9f3d1bec8ba1b549>)
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
CREATEBY| 仪表板创建者 ID| VARCHAR| 255  
GLOBAL| 是否是全局样式true：是所有用户可以选择的全局样式flase：是 CREATEBY 用户独有的样式| BOOLEAN| 0  
NAME| 仪表板样式名称| VARCHAR| 255  
STYLE| 仪表板样式明细| VARCHAR| 16777216  
STYLEID| 仪表板样式Id| VARCHAR| 255  
### 16.7 FINE_REPORT_LINK 仪表板公共链接信息表
注：FineBI6.0起该表已弃用，请查询FINEBI_REPORT_LINK_EN表，详情请参见：[FineDB表结构-BI配置](<https://help.fanruan.com/finebi6.X/doc-view-2072.html#9f3d1bec8ba1b549>)
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键ID| VARCHAR| 255  
LINKID| 公共链接ID| VARCHAR| 255  
REPORTID| 仪表板ID| VARCHAR| 255  
### 16.8 FINE_REPORT_WARNING 仪表板配置预警信息表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键ID| VARCHAR| 255  
DESCRIPTION| 预警信息| VARCHAR| 16777216  
REPORTID| 仪表板ID| VARCHAR| 255  
WARNINGID| 预警ID| VARCHAR| 255  
WIDGETID| 组件ID| VARCHAR| 255  
### 16.9 FINE_STATISTIC_OPERATOR 直连自助数据集统计信息表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
OPERATORID| 步骤唯一标识符| VARCHAR| 255  
RECORDTIME| 当前记录的时间| BIGINT| 64  
ROWSIZE| 当前步骤数据行数| INTEGER| 32  
TABLENAME| 步骤所在表的唯一标识符| VARCHAR| 1024  
### 16.10 FINE_STATISTIC_TABLE 直连基础数据集统计信息表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
RECORDTIME| 当前记录的时间| BIGINT| 64  
ROWSIZE| 表的预览行数| INTEGER| 32  
TABLENAME| 表唯一标识符| VARCHAR| 1024  
### 16.11 FINE_STATISTIC_TABLE_INFO 直连自助数据集步骤信息表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
OPERATORIDS| 步骤唯一标识符| VARCHAR| 65536  
RECORDTIME| 当前记录的时间| BIGINT| 64  
TABLENAME| 步骤所在表的唯一标识符| VARCHAR| 1024  
### 16.12 FINE_UPDATE_TASK 更新任务表
注：5.1.12 及之后版本的 BI 工程，新增该表。
5.1.12 之前的 BI 工程，该部分信息可在 LogDB 中查看。
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
COUNTOVERVIEW| 任务中各类型的表的更新情况。JSON  
expectBaseTableUpdate：期望的基础表数量  
actualBaseTableUpdate：实际成功更新的基础表数量  
expectComplexUpdate：期望的自助数据集数量  
actualComplexUpdate：实际成功的自助数据集数量  
expectRelationUpdate：期望的关联更新数量  
actualRelationUpdate：实际成功的关联数量| VARCHAR| 255  
ENDTIME| 任务结束时间| BIGINT| 64  
PLANID| 任务实例唯一标识，每一次运行都不同| VARCHAR| 255  
ROLEID| 触发人Id| VARCHAR| 255  
ROLENAME| 触发人名称| VARCHAR| 255  
RUNNINGRESULT| 完成状态  
ALL：全部成功  
PART：部分成功| VARCHAR| 255  
STARTTIME| 任务开始时间| BIGINT| 64  
STATETYPE| 更新状态  
END：已结束| VARCHAR| 255  
TASKNAME| 任务名称  
表名+任务类型（单表/业务包/全局）| VARCHAR| 255  
TIME| 数据插入时间，swift表清理需要| BIGINT| 64  
TRIGGERID| 触发ID| VARCHAR| 255  
TRIGGERTYPE| 触发方式  
MANUAL：手动触发更新  
AUTO：定时更新任务DEFAULT：默认，自动抽取| VARCHAR| 255  
### 16.13 FINE_UPDATE_TASK_DETAIL 更新任务明细表
注：5.1.12 及之后版本的 BI 工程，新增该表。  

5.1.12 之前的 BI 工程，该部分信息可在 LogDB 中查看。
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
APPENDCOUNT| 增量增行数| BIGINT| 64  
COLUMNCOUNT| 列数| BIGINT| 64  
DELETECOUNT| 增量减行数| BIGINT| 64  
EFFECTTIME| 生效时间，真正可用| BIGINT| 64  
ENDTIME| 数据更新结束时间| BIGINT| 64  
ERRORCODE| 错误代码| INTEGER| 32  
ETLFLOW| 自助数据集的步骤| VARCHAR| 5000  
FAILEDSONID| 基础表导致的更新失败的表的ID集合| VARCHAR| 65536  
FATHERFAILEDIDS| 更新失败的父表的ID集合| VARCHAR| 5000  
INFOMSG| 非报错信息（只有国际化的key值和参数）| VARCHAR| 5000  
JDBCTIME| 数据获取时间| BIGINT| 64  
LOADID| 明细标识，在一个更新任务中唯一| INTEGER| 32  
LOADNAME| 明细信息的名字  
表为表名+包名，关联为关联的信息| VARCHAR| 65536  
LOADTYPE| 明细类型  
BASE：基础表  
FAST、ETL：自助数据集  
RELATION：关联| VARCHAR| 255  
OPENTIME| sql执行时间| BIGINT| 64  
PLANID| 任务实例唯一标识，每一次运行都不同| VARCHAR| 255  
STARTTIME| 更新开始时间| BIGINT| 64  
STATETYPE| 更新状态  
SUCCESS：成功  
WRONG：失败| VARCHAR| 255  
TABLEID| 表ID| VARCHAR| 255  
TABLENAME| 表名称| VARCHAR| 255  
TIME| 数据插入时间，swift表清理需要| BIGINT| 64  
TOTALCOUNT| 总行数| BIGINT| 64  
UPDATECOUNT| 变化的行数，可能有增有减| BIGINT| 64  
UPDATETYPE| 更新类型  
FULL：全量  
INCREASE：增量| VARCHAR| 255  
WRITETIME| 写文件时间| BIGINT| 64  
ERRORCODE对应内容如下表所示：
表类型| ERRORCODE| 异常说明  
---|---|---  
基础表| 100001| Excel源文件缺失，请重新上传后更新  
100002| 我们无法连接到包含该数据集的数据连接，请检查数据连接可用性  
100003| 基础表字段跟数据库返回字段不一致，请修改或删除缺失字段。缺失字段:{xxx}，数据库返回字段:[xxx]  
100004| 该基础表已经进行过行列转换或者自循环列操作，无法进行增量更新，请全量更新该基础表  
100005| 服务器数据集无法执行增量更新，请配置为全量更新，并取消增量更新配置  
100006| 服务器数据集更新异常（[这里报java异常类详细错误]）  
100007| 增量更新相关语句均为空，请检查该数据集的增量更新配置情况  
100008| 因超过最大可更新时间而被智能查杀，该表历史更新耗时为：[xxx]，查杀时更新耗时为：[xxx]，请检查该表数据连接是否正常  
自助数据集| 100000| 对于关联：由于直接或间接引用到的 [xxx(xxx)与xxx(xxx)] 的关联更新失败，这些数据集的衍生数据集均没有更新  
100009| 数据集字段可用性出现问题，问题字段已经标记为红色，建议重新编辑本数据集后再次更新。被依赖的数据集发生更改有可能会引发该错误  
100010| 更新时检测到笛卡尔积，数据严重膨胀，操作中止。请检查左右合并步骤中的合并依据列数据是否有重复值，请确保重复值不应过多。  
关联| 100011| xxx(xxx)的关联字段[xxx]字段名中包含非法字符xxx，无法成功生成关联关系，请去除非法字符并更新  
100012| xxx(xxx)与xxx(xxx)无法成功生成关联关系，关联字段[xxx]类型不一致，请重新配置并更新  
100013| xxx(xxx)的关联字段[xxx]数据重复，无法成功生成关联关系，请去除重复数据并更新  
100014| xxx(xxx)与xxx(xxx)无法成功生成关联关系，xxx(xxx)的关联字段[xxx]不存在，请选择有效的关联字段并更新  
100015| xxx(xxx)与xxx(xxx)无法成功生成关联关系，权限继承所使用的xxx(xxx)的关联字段[xxx]不存在，请检查权限继承设置  
100016| 无法找到关联的数据集，关联可能被删除  
100017| xxx(xxx)与xxx(xxx)关联所依赖的表更新失败，该关联未更新  
100018| 更新任务被中断，不再执行  
100019| 无法找到数据集，可能已经被删除  
  

### 16.14 FINE_UPDATE_DETAIL_INFO 更新任务明细信息表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 唯一标识字段| VARCHAR| 255  
ENDTIME| 该任务的结束时间| BIGINT| 64  
EXCEPTIONMSG| 异常前缀信息| VARBINARY| 67108864  
EXCEPTIONPREFIX| 该明细的一条异常信息| VARCHAR| 255  
LOADID| 明细标识，在一个更新任务中唯一| INTEGER| 32  
LOADTYPE| 明细类型：  
1：基础表  
2：自助数据集  
3：关联| VARCHAR| 255  
PLANID| 任务实例唯一标识，每一次运行都不同，一张表存在多条| VARCHAR| 255  
TIME| 数据插入时间| BIGINT| 64  
### 16.15 FINE_FAVORITE_REPORT 分享的仪表板收藏记录表
字段名  
| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键ID| VARCHAR| 255  
DASHBOARDID| 仪表板ID| VARCHAR| 255  
TIME| 数据插入时间| TIMESTAMP| 26  
USERID| 用户ID| VARCHAR| 255  
### 16.16 FINE_SHARE_INDEX 存储分享的数据权限设置
注：FineBI6.0及以上版本，该表弃用，对应配置存储到FINEBI_REPORT_SHARE_EN中。
详情请参见：[FineDB表结构-BI配置](<https://help.fanruan.com/finebi6.X/doc-view-2072.html>)
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
ENTITYID| 实体ID，即reportID| VARCHAR| 255  
ENTITYPATH| 实体路径fullPath，即仪表板路径| VARCHAR| 255  
ENTITYTYPE| 实体类型0：仪表板1：文件夹| INTEGER| 32  
SHARETYPE| 分享数据权限类型0：使用创建者权限1：使用被分享者权限| INTEGER| 32  
### 16.17 FINE_PACK_FILTER BI业务包行过滤器表
FineBI 数据集中的行权限控制信息保存在这张表中。
字段名| 描述| 数据类型| 长度  
---|---|---|---  
ID| 主键| VARCHAR| 255  
FILTER| 过滤器实际内容| VARCHAR| 16777216  
PACKAGEID| 业务包的ID| VARCHAR| 255  
ROLEID| 拥有的广义角色ID  
关联表字段fine_authority>roleId| VARCHAR| 255  
ROLETYPE| 拥有的广义角色类型1：部门职务角色 2：自定义角色 3：用户角色| INTEGER| 32  
TABLEID| 过滤器关联数据表的ID2020-9 新增| VARCHAR| 255  
ENABLE| 是否启用true：启用false：不启用| BOOLEAN| [NULL]  
### 16.18 FINEBI_PUBLISH_TASK
字段名  
| 描述| 字段类型  
---|---|---  
id| 唯一键| 文本  
creator|   
关联的表字段fine_user>id| 文本  
  
details| 发布信息ID| 文本  
itemId| 发布资源ID| 文本  
itemType| 发布资源类型33：仪表板3：数据集| 数值  
publishTaskId| 发布任务ID| 文本  
status| 发布状态1：申请发布2：申请取消发布3：已发布| 数值  
time| 时间| 数值  
type|   
| 数值  
### 16.19 finebi_publish_detail
发布流程中的中间过程表，在普通用户申请（发布、卸载）阶段临时记录中间信息，当发布操作完成时，并不会在这张表中记录下发布成功状态的数据
字段名  
| 描述| 字段类型  
---|---|---  
id| 唯一键| 文本  
commentValue|   
base64编码记录| 文本  
deviceType|   
| 数值  
locationId|   
| 文本  
locationType|   
| 数值  
showName|   
| 文本  
  

  

  

  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：修改外接数据库账号密码](<index.php?doc-view-1332.html>)
[下一篇：FineDB表结构-BI配置 ![](/core/style/forward.png) ](<index.php?doc-view-2072.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
