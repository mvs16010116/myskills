---
title: fine_conf_entity表内容
doc_id: 907
url: https://help.fanruan.com/finebi6.X/doc-view-907.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:18
---

> 1.&nbsp;问题描述FineBI 中的一些配置、数据连接、权限设置等都保存到 FineDB 相应的配置表中。本文汇总了平台相关设置的存储位置，以及部分平台无法直接设置的修改项。大部分的配置项都存储在

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# fine_conf_entity表内容
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[22](<edition-list-907.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-03-11 
[](<javascript:;>) [](<javascript:>)
## 1\. 问题描述
FineBI 中的一些配置、数据连接、权限设置等都保存到 FineDB 相应的配置表中。
本文汇总了平台相关设置的存储位置，以及部分平台无法直接设置的修改项。
大部分的配置项都存储在 finedb 中的 FINE_CONF_ENTITY 表中。
其他表结构请参见：[FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>)
## 2\. 目录管理
分类| 描述| 存储表  
---|---|---  
平台首页| 默认首页、自定义首页| FINE_HOMEPAGE_EXPAND  
平台目录| 平台目录| FINE_AUTHORITY_OBJECT  
常用设置及常用帮助| 点击管理系统，未进入具体子目录的常用设置及常用帮助| JAR 包  
## 3\. 用户管理
「用户管理」大部分设置请参见 [FineDB 表结构](<https://help.fanruan.com/finereport/doc-view-3151.html>) 中的用户-部门职务-角色小节
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
用户同步数据集| 管理系统-用户管理-同步用户| FINE_CONF_ENTITY| UserDataSetConfig.dataSetName| 用户信息表|  数据集名称  
UserDataSetConfig.departmentColumn| -1| 部门列   
UserDataSetConfig.departmentIdColumn| -1| 部门ID列   
UserDataSetConfig.emailColumn| -1| 邮箱列   
UserDataSetConfig.mobileColumn| -1| 手机列   
UserDataSetConfig.passwordColumn| 2| 密码列   
UserDataSetConfig.postColumn| -1| 职务列   
UserDataSetConfig.postIdColumn| -1| 职务ID列   
UserDataSetConfig.rate| 43200| 同步频率   
UserDataSetConfig.realNameColumn| 1| 姓名列   
UserDataSetConfig.roleColumn| -1|  角色列  
UserDataSetConfig.roleIdColumn| -1|  角色ID列  
UserDataSetConfig.turnOn| TRUE|  是否开启  
UserDataSetConfig.userIdColumn| -1|  用户ID列  
UserDataSetConfig.usernameColumn| 0| 用户名列   
平台内置认证| 管理系统-用户管理-全局配置-认证方式-平台内置认证| /| /| /| 无存储字段，默认内置认证切换其他认证方式后，如需切换内置认证，将其他认证方式对应的字段删除即可  
ldap认证  
  
| 管理系统-用户管理-全局配置-认证方式-ldap认证  
  
| FINE_CONF_ENTITY  
  
| FSConfig.passport.ldapUrl|   
| URL  
FSConfig.passport.ldapSearchBase|   
| 检索位置  
FSConfig.passport.retrieveLocAsBaseDN| ture/fasle| 不将检索位置作为baseDN  
FSConfig.passport.authentication|   
| 认证方式  
FSConfig.passport.contextFactory|   
| 前后关系  
FSConfig.passport.referral|   
| 转诊  
FSConfig.passport.principalSuffix|   
| 用户名后缀  
FSConfig.passport.ldapSystemName|   
| 管理员名称  
FSConfig.passport.ldapSystemPassword|   
| 管理员密码  
http认证| 管理系统-用户管理-全局配置-认证方式-http认证| FINE_CONF_ENTITY| FSConfig.passport.publicKey|   
| 公钥  
FSConfig.passport.url|   
| 认证地址  
添加用户后邮件通知| 管理系统-用户管理-全局配置-添加用户后邮件通知| FINE_CONF_ENTITY| UserRemindConfig.emailRemindAfterAddUser| true/false|   
  
重置密码后邮件通知| 管理系统-用户管理-全局配置-重置密码后邮件通知| FINE_CONF_ENTITY| UserRemindConfig.emailRemindAfterResetPassword| true/false|   
  
## 4\. 权限管理
「权限管理」大部分设置请参见 [FineDB 表结构](<https://help.fanruan.com/finereport/doc-view-3151.html>) 中的 权限-目录 小节
分类| 描述| 存储表| 字段id| 字段值  
---|---|---|---|---  
分级授权| 管理系统-权限管理-全局配置-分级授权| FINE_CONF_ENTITY| FSConfig.authorizeAttr.gradeAuthority| true/false  
目录编辑权限| 管理系统-权限管理-全局配置-目录编辑权限| FINE_CONF_ENTITY| FSConfig.authorizeAttr.editReportAuthority| true/false  
数据链接控制| 管理系统-权限管理-全局配置-数据链接控制| FINE_CONF_ENTITY| FSConfig.authorizeAttr.dataConnectionAuthority| true/false  
## 5\. 外观配置
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
登录方式| 管理系统-外观配置-登录页中的登录方式| FINE_CONF_ENTITY| AppearanceConfig.loginType| 0| 0表示用默认登录页插件1表示设置了登录网页  
AppearanceConfig.loginUrl|   
| 当设置了登录网页后具体的登录地址的保存位置  
登录标题| 管理系统-外观配置-登录页中-登录标题| FINE_CONF_ENTITY| AppearanceConfig.loginTitle|   
|   
  
登录logo| 管理系统-外观配置-登录页中-登录logo| FINE_CONF_ENTITY| AppearanceConfig.loginLogoImgId  
|   
| 图标上传后的缓存id删除此行设置过的登录也logo将恢复默认效果  
AppearanceConfig.loginLogoImgName|   
| 背景图文件名带后缀  
AppearanceConfig.images.MapCachexxxxx|   
| 设置不同的背景图字段id后的缓存时间戳不同  
显示品牌信息| 管理系统-外观配置-登录页中-显示品牌信息| FINE_CONF_ENTITY| AppearanceConfig.copyrightInfoDisplay| true/false| 默认true  
登录主题色| 管理系统-外观配置-登录页中-登录主题色| FINE_CONF_ENTITY| AppearanceConfig.loginColor|   
|   
  
登录风格| 管理系统-外观配置-登录页中-登录风格| FINE_CONF_ENTITY| AppearanceConfig.loginPageId|   
| 安装登录风格插件后也选否则为default  
背景图片  
  
| 管理系统-外观配置-登录页中-背景图片  
  
| FINE_CONF_ENTITY  
  
| AppearanceConfig.loginImg| true/fasle| ture表示用自定义设置的背景false表示用默认背景图  
AppearanceConfig.loginImgId|   
| 图片上传后的缓存id  
AppearanceConfig.images.MapCachexxxxx| login_bg| 设置不同的背景图字段id后的缓存时间戳不同  
平台主题| 管理系统-外观配置-平台主题| FINE_CONF_ENTITY| AppearanceConfig.themeId| modern/classic| modern：扁平化classic：经典  
平台标题| 管理系统-外观配置-平台样式-平台标题| FINE_CONF_ENTITY| AppearanceConfig.platformTitle|   
|   
  
平台logo| 管理系统-外观配置-平台样式-平台logo| FINE_CONF_ENTITY| AppearanceConfig.logoImgId|   
| 图标上传后的缓存id  
AppearanceConfig.logoImgName|   
| 背景图文件名带后缀  
AppearanceConfig.images.MapCachexxxxx|   
| 设置不同的背景图字段id后的缓存时间戳不同  
配色| 管理系统-外观配置-平台样式-配色| FINE_CONF_ENTITY| AppearanceConfig.colorScheme| 0/1/2| 0表示浅色1表示深色2表示自定义  
框架样式-顶部标题行样式| 管理系统-外观配置-平台样式-配色-自定义-顶部标题行样式| FINE_CONF_ENTITY| AppearanceConfig.headerType| 1/2| 1表示分块式背景2表示一体式背景  
框架样式-其余颜色| 管理系统-外观配置-平台样式-配色-自定义-其余颜色| FINE_CONF_ENTITY| AppearanceConfig.customColors|   
| 数组，一共6个值，从上到下的颜色  
自定义目录图标| 管理系统-外观配置-目录样式-目录图标-自定义目录图标| FINE_CONF_ENTITY| AppearanceConfig.customEntryIcons|   
| 数组，自定义上传了几个图标，就是有几个值  
自定义封面图标| 管理系统-外观配置-目录样式-封面图标-自定义封面图标| FINE_CONF_ENTITY| AppearanceConfig.customEntryCovers|   
| 数组，自定义上传了几个图标，就是有几个值  
## 6\. 系统管理
分类  
| 描述| 存储表| 字段ID| 字段值| 备注  
---|---|---|---|---|---  
密码| 重置超管密码| FINE_CONF_ENTITY| SystemConfig.serverInit| success/fail|   
  
登录| 管理系统-系统管理-登录-单一登录设置| FINE_CONF_ENTITY| FSConfig.loginConfig.singleLogin| true/false|   
  
FSConfig.loginConfig.singleLoginMode| 1/2| 1表示后登录踢出先登录2表示已登录禁止再登录  
管理系统-系统管理-登录-上次登录信息提示| FINE_CONF_ENTITY| FSConfig.loginConfig.showLastLoginInfo| true/false|   
  
管理系统-系统管理-登录-登录超时设置| FINE_CONF_ENTITY| FSConfig.loginConfig.loginTimeout|   
| 单位ms  
管理系统-系统管理-登录-密码策略设置-忘记密码| FINE_CONF_ENTITY| PasswordStrategyConfig.forgetPassword| true/false| 初始无此字段，开启后出现  
管理系统-系统管理-登录-密码策略设置-密码定期更新| FINE_CONF_ENTITY| PasswordStrategyConfig.passwordUpdateRegularly| true/false| 初始无此字段，开启后出现  
PasswordStrategyConfig.updateCycle|   
| 更新周期，单位d  
PasswordStrategyConfig.daysOfUpdateEarlyWarning|   
| 提前x天提醒，单位d  
管理系统-系统管理-登录-密码策略设置-密码强度设置| FINE_CONF_ENTITY| PasswordStrategyConfig.passwordStrengthLimit| true/false| 初始无此字段，开启后出现  
PasswordStrategyConfig.passwordLength|   
| 密码长度  
PasswordStrategyConfig.includeNumbers| true/false| 初始无此字段，开启后出现包含数字，默认true  
PasswordStrategyConfig.includeLowercaseLetters| true/false| 初始无此字段，开启后出现包含小写字母，默认true  
PasswordStrategyConfig.includeCapitalLetters| true/false| 初始无此字段，开启后出现包含大写字母，默认false  
PasswordStrategyConfig.includeSymbol| true/false| 初始无此字段，开启后出现包含符号，默认false  
管理系统-系统管理-登录-密码策略设置-修改密码验证方式| FINE_CONF_ENTITY| PasswordStrategyConfig.emailVerificationAfterChangePassword| true/false| 邮件验证  
PasswordStrategyConfig.smsVerificationAfterChangePassword| true/false| 短信验证  
管理系统-系统管理-登录-登陆验证设置| FINE_CONF_ENTITY| LoginVerificationConfig.sliderVerification| true/false| 滑块验证  
LoginVerificationConfig.emailVerification| true/false| 邮件验证（需要先配置好邮箱）  
LoginVerificationConfig.smsVerification| true/false| 短信验证（需要先配置好短信平台）  
管理系统-系统管理-登录-登陆锁定| FINE_CONF_ENTITY| LoginLockConfig.lock| true/false| 默认false  
LoginLockConfig.passwordErrorTimes|   
| 密码错误次数  
LoginLockConfig.lockingTime|   
| 锁定时间  
LoginLockConfig.lockObject| username/ip| 锁定对象  
LoginLockConfig.lockAdmin| true/false| 锁定管理员  
常规| 管理系统-系统管理-常规-连接网址中心| FINE_CONF_ENTITY| CloudCenterConfig.online| true/false|   
  
管理系统-系统管理-常规-Gzip压缩| FINE_CONF_ENTITY| ServerPreferenceConfig.supportGzip| true/false|   
  
管理系统-系统管理-常规-Servletl路径名| FINE_CONF_ENTITY| ServerConfig.servletName|   
| 不允许设置为ReportServer  
管理系统-系统管理-常规-服务器端字符编码| FINE_CONF_ENTITY| ServerConfig.serverCharset|   
| 默认UTF-8  
管理系统-系统管理-常规-网络报表根目录名| /|   
|   
|   
  
管理系统-系统管理-常规-报表资源根目录名| /|   
|   
|   
  
管理系统-系统管理-常规-周开始于| FINE_CONF_ENTITY| ServerPreferenceConfig.firstDayOfWeek| 0/1| 0表示开始于周日  
管理系统-系统管理-常规-资源服务器| FINE_CONF_ENTITY| ServerPreferenceConfig.useResServer| true/false| 是否开启资源服务器  
ServerPreferenceConfig.resServerPath|   
| 资源服务器地址  
管理系统-系统管理-常规-websocket配置| FINE_CONF_ENTITY| WebSocketConfig.usingProxy| true/false| 是否使用代理服务器  
WebSocketConfig.requestPorts|   
| websocket请求端口  
WebSocketConfig.socketContext|   
| websocket请求路径  
管理系统-系统管理-常规-https设置| FINE_CONF_ENTITY| WebSocketConfig.protocol|   
| 服务器协议  
WebSocketConfig.keyStore|   
| SSL密钥路径  
WebSocketConfig.keyStorePassword|   
| SSL密钥密码  
WebSocketConfig.keyStoreFormat|   
| SSL证书类型  
打印| 管理系统-系统管理-打印-零客户端打印| FINE_CONF_ENTITY| PrintConfig.printSettingsAttrData.noClientPrintAttr.setMarginOnPrint| true/false| 打印时可设置打印边距  
  
| 管理系统-系统管理-打印-本地软件打印| FINE_CONF_ENTITY| PrintConfig.printSettingsAttrData.nativePrintAttr.showDialog| true/false| 打印是否需要打印设置窗口  
邮箱| 管理系统-系统管理-邮箱| FINE_CONF_ENTITY| EmailServerConfig.mailHost|   
| 邮件服务器  
EmailServerConfig.encryption|   
| 加密方式  
EmailServerConfig.port|   
| 端口  
EmailServerConfig.fromEmailAddress|   
| 发件人地址  
EmailServerConfig.password|   
| 密码  
EmailServerConfig.user|   
| 显示姓名  
短信| 管理系统-系统管理-短信| FINE_CONF_ENTITY| MarketConfig.smsOpen| true/false| 是否使用短信平台  
缓存| 管理系统-系统管理-数据集共享-个数| FINE_CONF_ENTITY| CacheConfig.dbConfig.maxElementsInMemory|   
| 共享数据集最大个数  
管理系统-系统管理-数据集共享-缓存原则| FINE_CONF_ENTITY| CacheConfig.dbConfig.memoryStoreEvictionPolicy| LRU/LFU/FIFO| LRU：最近使用  
LFU：最不常使用  
FIFO：先进先出  
管理系统-系统管理-数据集共享-最大空闲时间| FINE_CONF_ENTITY| CacheConfig.dbConfig.timeToIdleSeconds|   
| 单位ms  
管理系统-系统管理-数据集共享-最大生存时间| FINE_CONF_ENTITY| CacheConfig.dbConfig.timeToLiveSeconds|   
| 单位ms  
管理系统-系统管理-模板缓存属性设置-总是重新读取模板| FINE_CONF_ENTITY| CacheConfig.alwaysReloadTpl| true/false|   
  
## 7\. 定时调度
「定时调度」大部分配置请参见 [FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>) 中的 定时调度 小节
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
运行失败提醒| 管理系统-用户管理-全局配置-短信提醒| FINE_CONF_ENTITY| ScheduleSettingConfig.smsChecked| true/false|   
  
ScheduleSettingConfig.smsReceiver|   
| 收件人地址  
管理系统-用户管理-全局配置-平台消息| FINE_CONF_ENTITY| ScheduleSettingConfig.platformMessageChecked| true/false|   
  
ScheduleSettingConfig.platformMessageReceiver|   
| 收信用户  
管理系统-用户管理-全局配置-邮件提醒| FINE_CONF_ENTITY| ScheduleSettingConfig.emailChecked| true/false|   
  
ScheduleSettingConfig.emailReceiver|   
| 邮件地址  
## 8\. 移动平台
「移动平台」大部分配置请参见 [FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>) 中的 移动端 小节
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
APP启动画面| 管理系统-移动平台-APP启动画面| FINE_CONF_ENTITY| MobileConfig.phoneLaunchImgId|   
| 手机，设置自定义图片后若想回复默认，删除此行数据即可  
MobileConfig.padLaunchImgId|   
| 平板，设置自定义图片后若想回复默认，删除此行数据即可  
设备绑定| 管理系统-移动平台-设备绑定| FINE_CONF_ENTITY| MobileConfig.mobileDeviceBinding| true/false|   
  
二维码配置| 管理系统-移动平台-二维码配置| FINE_CONF_ENTITY| MobileConfig.qrcodeServerName|   
| 服务器名称  
MobileConfig.qrcodeServerUrl|   
| 服务器地址  
主题| 管理系统-移动平台-主题| FINE_CONF_ENTITY| MobileConfig.activeTheme|   
| 若安装有其他主题插件的话，可以选择  
目录| 管理系统-移动平台-目录-目录结构| FINE_CONF_ENTITY| MobileConfig.entryStyleId|   
| 目录结构，若安装有移动端目录插件，可以选择  
管理系统-移动平台-目录-横幅| FINE_CONF_ENTITY| MobileConfig.banner.enabled| true/false|   
  
管理系统-移动平台-目录-模板| FINE_CONF_ENTITY| MobileConfig.template.enabled| true/false|   
  
MobileConfig.template.name|   
| 模板名  
MobileConfig.template.path|   
| 模板路径  
MobileConfig.template.position| top/bottom| 显示位置  
管理系统-移动平台-目录-目录图标| FINE_CONF_ENTITY| MobileConfig.customIcons|   
| 数组，保存自定义上传的图标  
其他| 管理系统-移动平台-其他-常规设置| FINE_CONF_ENTITY| MobileConfig.refreshable| true/false|   
  
管理系统-移动平台-其他-h5设置| FINE_CONF_ENTITY| Html5Config.isUsedJSBridge| true/false| 是否使用JSBridge  
Html5Config.jsLink|   
| 引入js的地址  
Html5Config.cssLink|   
| 引入css的地址  
## 9\. 注册管理
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
注册| 管理系统-注册管理| FINE_CONF_ENTITY| license.type| 1/2/3/4| 0：本地机器认证1：加密锁认证2：私有云认证3：公有云认证4：本地容器认证  
license.serverAddress|   
| 私有云注册地址  
license.appKey|   
| 公有云账号  
license.appSecretKey|   
| 公有云密码  
## 10\. 智能运维
### 10.1 内存管理
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
内存预警| 系统管理-智能运维-内存管理-智能预警| FINE_CONF_ENTITY| PrewarningConfig.warningOpen| true/false|   
  
PrewarningConfig.messageRemindOpen| true/false| 短信提醒  
PrewarningConfig.phoneNumbers|   
| 手机号  
PrewarningConfig.platformMessageRemindOpen| true/false| 平台消息提醒  
PrewarningConfig.platformMessageReceiver|   
| 收信用户  
PrewarningConfig.mailRemindOpen| true/false| 邮件提醒  
PrewarningConfig.mailReceivers|   
| 邮件地址  
智能释放| 系统管理-智能运维-内存管理-智能释放| FINE_CONF_ENTITY| IntelliReleaseConfig.memoryAlarmOpen| true/false| 报表内存智能释放  
IntelliReleaseConfig.message|   
| 警报提示  
模板限制| 系统管理-智能运维-内存管理-模板限制-通用限制-单数据集行数限制| FINE_CONF_ENTITY| TempRestrictionConfig.openRowControl| true/false|   
  
TempRestrictionConfig.maxDSRowCount|   
| 单数据集最大行数  
TempRestrictionConfig.rowOverMsg|   
| 超出提示  
系统管理-智能运维-内存管理-模板限制-通用限制-单模板单元格点置| FINE_CONF_ENTITY| CustomRestrictionConfig.openCellControl| true/false|   
  
CustomRestrictionConfig.maxDSCellCount|   
| 单模板最大单元格子数  
CustomRestrictionConfig.cellOverMsg|   
| 超出提示  
系统管理-智能运维-内存管理-模板限制-通用限制-sql执行时长限制| FINE_CONF_ENTITY| TempRestrictionConfig.openSQLTimeControl| true/false|   
  
TempRestrictionConfig.maxSQLTime|   
| sql最大执行时长，单位s  
TempRestrictionConfig.sqlTimeOverMsg|   
| 超出提示  
系统管理-智能运维-内存管理-模板限制-通用限制-导入excel单元格限制| FINE_CONF_ENTITY| TempRestrictionConfig.openExcelImportCellCountControl| true/false|   
  
TempRestrictionConfig.maxExcelImportCellCount|   
| 导入excel最大单元格数  
TempRestrictionConfig.excelImportCellCountOverMsg|   
| 超出提示  
系统管理-智能运维-内存管理-模板限制-通用限制-提交记录数限制| FINE_CONF_ENTITY| TempRestrictionConfig.openCommitRowCountControl| true/false|   
  
TempRestrictionConfig.openCartesianControl| true/false| 允许笛卡尔积填报  
TempRestrictionConfig.maxCommitRowCount|   
| 填报最大提交记录数  
TempRestrictionConfig.commitRowCountOverMsg|   
| 超出提示  
系统管理-智能运维-内存管理-模板限制-部分模板单独限制-单独限制的模板| FINE_CONF_ENTITY| RelaxationRestrictionConfig.relaxationTemps|   
| 数组，模板名  
其余部分模板单独限制存储均与通用限制类似，差别在于：通用限制为TempRestrictionConfig，部门模板单独限制为RelaxationRestrictionConfig  
生命周期| 系统管理-智能运维-内存管理-生命周期| FINE_CONF_ENTITY| LifecycleConfig.lifeCycle|   
| 清理超过x分钟无操作的会话  
### 10.2 集群配置
大部分配置请参见：[Web 集群数据库可配置项说明文档](<https://help.fanruan.com/finereport/doc-view-2855.html>)
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
全局配置| 管理系统-智能运维-集群配置-全局配置| FINE_CONF_ENTITY| ClusterExceptionWarningConfig.mailRemindOpen| true/false| 邮件提醒  
ClusterExceptionWarningConfig.mailReceivers|   
| 邮件收件地址  
ClusterExceptionWarningConfig.messageRemindOpen| true/false| 短信提醒  
ClusterExceptionWarningConfig.phoneNumbers|   
| 收件人  
ClusterExceptionWarningConfig.platformMessageRemindOpen| true/false| 平台消息提醒  
ClusterExceptionWarningConfig.platformMessageReceiver|   
| 收件用户  
集群配置| 管理系统-智能运维-集群配置-集群配置| FINE_CONF_ENTITY| FineClusterConfig.params.protocol| TCP/UDP|   
  
参数配置| 管理系统-智能运维-集群配置-参数配置| FINE_CONF_ENTITY| RedisConfig.tableNamePrefix|   
| key前缀  
### 10.3 备份还原
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
全局设置| 管理系统-智能运维-备份还原-全局设置| FINE_CONF_ENTITY| BackupConfig.backupPath|   
| 备份路径  
BackupConfig.frequency|   
| 备份频率  
BackupConfig.backupNumber|   
| 份数上线  
BackupConfig.backupMemory|   
| 备份容量  
管理系统-智能运维-备份还原| FINE_CONF_ENTITY| BackupConfig.moduleBackup|   
| 备份的组件  
平台配置| 管理系统-智能运维-备份还原-平台配置| FINE_CONF_ENTITY| BackupConfig.moduleBackup.config.autoBackup| true/false| 开启自动备份  
BackupConfig.moduleBackup.config.moduleName| config| 模块名  
报表模板| 管理系统-智能运维-备份还原-报表模板| FINE_CONF_ENTITY| BackupConfig.moduleBackup.reportlets.autoBackup| true/false| 开启自动备份  
BackupConfig.moduleBackup.reportlets.moduleName| reportlets| 模块名  
JAR 包| 管理系统-智能运维-备份还原-jar包| FINE_CONF_ENTITY| BackupConfig.moduleBackup.jar.autoBackup| true/false| 开启自动备份  
BackupConfig.moduleBackup.jar.moduleName| jar| 模块名  
BackupConfig.moduleBackup.jar-cluster.autoBackup| true/false| 开启自动备份  
BackupConfig.moduleBackup.jar-cluster.moduleName| jar-cluster| 模块名  
插件| 管理系统-智能运维-备份还原-插件| FINE_CONF_ENTITY| BackupConfig.moduleBackup.plugins.autoBackup| true/false| 开启自动备份  
BackupConfig.moduleBackup.plugins.moduleName| plugins| 模块名  
更新升级| 管理系统-智能运维-备份还原-更新升级| FINE_CONF_ENTITY| UpdatePushConfig.open| true/false| 自动推送更新  
### 10.4 平台日志
「平台日志」大部分配置请参见 [FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>)
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
全局配置| 管理系统-智能运维-平台日志-全局配置| FINE_CONF_ENTITY| Log4jConfig.rootLevel| DEBUG/INFO/WARN/ERROR/FATAL| 日志级别  
LogCleanConfig.open| ture/false| 开启日志清理  
管理系统-智能运维-平台日志-全局配置-自动清理| FINE_CONF_ENTITY| LogCleanConfig.autoCleanTime|   
| 每隔X自动清理，单位d  
LogCleanConfig.autoDataTime|   
| 保留近X的数据  
管理系统-智能运维-平台日志-全局配置-手动清理| FINE_CONF_ENTITY| LogCleanConfig.manualDataTime|   
| 保留近X的数据  
管理系统-智能运维-平台日志-全局配置-清理预警| FINE_CONF_ENTITY| LogCleanConfig.cleanWarnStarted| ture/false| 开启清理预警  
LogCleanConfig.triggerThreshold|   
| 触发条件  
LogCleanConfig.smsChecked| ture/false| 开启短信提醒  
LogCleanConfig.smsReceiver|   
| 收件人  
LogCleanConfig.platformMessageChecked| ture/false| 开启平台消息  
LogCleanConfig.platformMessageReceiver|   
| 数组，平台收件人  
LogCleanConfig.emailChecked| ture/false| 开启邮件提醒  
LogCleanConfig.emailReceiver|   
| 邮件收件地址  
### 10.5 云端运维
分类| 描述| 存储表| 字段id| 备注  
---|---|---|---|---  
云端运维| 管理系统-智能运维-云端运维| FINE_CONF_ENTITY| MarketConfig.cloudOperationMaintenanceAppKey| 应用标识ID  
MarketConfig.cloudOperationMaintenanceAppName| 工程名  
MarketConfig.cloudOperationMaintenanceAppSecret| 应用秘钥  
MarketConfig.cloudOperationMaintenanceAutoUpload| 开启自动上传  
MarketConfig.cloudOperationMaintenanceAvailable| 开通云端运维  
MarketConfig.cloudOperationMaintenanceId| 应用ID  
## 11\. 数据连接
存储在FINE_CONF_ENTITY表中
**1）数据连接**  

字段| 含义| 值  
---|---|---  
ConnectionConfig.connections|  数据连接名称列表| ["FRDemo","finedb"]  
ConnectionConfig.connections.FRDemo.authentication.password| 密码，做了加密（__EMPTY__表示设置为空）| __EMPTY__  
ConnectionConfig.connections.FRDemo.authentication.username| 用户名| __EMPTY__  
ConnectionConfig.connections.FRDemo.catalog| 元数据| __EMPTY__  
ConnectionConfig.connections.FRDemo.creator| 创建者| designer  
ConnectionConfig.connections.FRDemo.database| 数据库| __EMPTY__  
ConnectionConfig.connections.FRDemo.dbcpAttr.initialSize| 初始化连接数| 0  
ConnectionConfig.connections.FRDemo.dbcpAttr.keepAlive| 空闲连接可用性定期检查| true  
ConnectionConfig.connections.FRDemo.dbcpAttr.keepAliveBetweenTimeMillis| 空闲连接可用性定期检查时间阈值| 120000  
ConnectionConfig.connections.FRDemo.dbcpAttr.maxActive| 最大活跃连接数| 50  
ConnectionConfig.connections.FRDemo.dbcpAttr.maxEvictableIdleTimeMillis| 空闲连接强制回收时间阈值| 25200000  
ConnectionConfig.connections.FRDemo.dbcpAttr.maxIdle| 最大空闲连接数| 10  
ConnectionConfig.connections.FRDemo.dbcpAttr.maxWait| 最大等待时间| 10000  
ConnectionConfig.connections.FRDemo.dbcpAttr.minEvictableIdleTimeMillis| 保持空闲最小时间值| 1800000  
ConnectionConfig.connections.FRDemo.dbcpAttr.minIdle| 最小空闲连接数| 0  
ConnectionConfig.connections.FRDemo.dbcpAttr.numTestsPerEvictionRun| 空闲连接回收检查数| 3  
ConnectionConfig.connections.FRDemo.dbcpAttr.testOnBorrow| 获取连接前检验| false  
ConnectionConfig.connections.FRDemo.dbcpAttr.testOnReturn| 归还连接前校验| false  
ConnectionConfig.connections.FRDemo.dbcpAttr.testWhileIdle| 开启空闲回收器校验| false  
ConnectionConfig.connections.FRDemo.dbcpAttr.timeBetweenEvictionRunsMillis| 空闲连接回收器休眠时间| -1  
ConnectionConfig.connections.FRDemo.dbcpAttr.validationQuery| 校验语句| __EMPTY__  
ConnectionConfig.connections.FRDemo.driver| 驱动| org.sqlite.JDBC  
ConnectionConfig.connections.FRDemo.driverSource| 驱动来源| __EMPTY__  
ConnectionConfig.connections.FRDemo.encryptPassword| 是否要对密码加密| true  
ConnectionConfig.connections.FRDemo.fetchSize| 控制从数据库中获取数据的批处理大小的设置| -1  
ConnectionConfig.connections.FRDemo.identity| 连接池对象| 12636be1-b3ea-4a1b-aba0-1fcd12499992  
ConnectionConfig.connections.FRDemo.schema| 模式| __EMPTY__  
ConnectionConfig.connections.FRDemo.url| 数据连接的 URL| jdbc:sqlite://${ENV_HOME}/../help/FRDemo.db  
  
  
**2）服务器数据集**
字段id| 字段值| 备注  
---|---|---  
TableDataConfig.tableDatas|   
| 数组，所有服务器数据集名  
TableDataConfig.tableDatas.YYY.database.name|   
| 数据连接名  
TableDataConfig.tableDatas.YYY.maxMemRowCount| -1| 最大内存行数，默认-1所以都存在内存；如果设置了缓存到磁盘，即为具体设置值  
TableDataConfig.tableDatas.YYY.pageQuerySql|   
| 分页sql  
TableDataConfig.tableDatas.YYY.parameters|   
| 参数  
TableDataConfig.tableDatas.YYY.query|   
| sql  
TableDataConfig.tableDatas.YYY.share| true/false| 是否开启共享数据集  
TableDataConfig.tableDatas.YYY.columnClassList|   
| 数组，列的类型  
TableDataConfig.tableDatas.YYY.columnNameList|   
| 数组，列名  
TableDataConfig.tableDatas.YYY.filePath|   
| 文件数据集路径  
TableDataConfig.tableDatas.YYY.needColumnName| true/false| 第一列是否包含列名  
## 12\. 安全管理
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
安全防护| 管理系统-安全管理-安全防护| FINE_CONF_ENTITY| WebSecurityConfig.cacheControlEnabled| true/false| 浏览器缓存禁用  
WebSecurityConfig.contentSecurityPolicyEnabled| true/false| CSP内容安全策略  
WebSecurityConfig.contentTypeOptionsEnabled| true/false| 内容嗅探攻击防护  
WebSecurityConfig.fileVerificationEnabled| true/false| 文件上传校验  
WebSecurityConfig.frameOptionsEnabled| true/false| 点击劫持攻击防护  
WebSecurityConfig.httpHeadersEnabled| true/false| security Headers  
WebSecurityConfig.remoteEvaluateLimitEnabled| true/false| 脚本调用公式限制  
WebSecurityConfig.securityCookie| true/false| cookie增强，只有开启https才可开启  
WebSecurityConfig.xssProtectionEnabled| true/false| xss攻击防护  
访问控制| 管理系统-安全管理-访问控制| FINE_CONF_ENTITY| WebSecurityConfig.rateLimitEnabled| true/false| 频率限制  
WebSecurityConfig.rateLimitUnitTime|   
| x秒内  
WebSecurityConfig.rateLimitCount|   
| 允许访问次数  
SQL防注入| 管理系统-安全管理-SQL防注入| FINE_CONF_ENTITY| PreventSqlInjConfig.useForbidWord| true/false| 禁用特殊关键字  
PreventSqlInjConfig.useEscapeSpecialChar| true/false| 转义字符  
PreventSqlInjConfig.customSpecialCharList|   
| 自定义添加的字符  
PreventSqlInjConfig.selectedSpecialCharList|   
| 已选择的转义字符  
PreventSqlInjConfig.customForbidWordList|   
| 自定义添加的特殊关键字  
PreventSqlInjConfig.selectedForbidWordList|   
| 已禁用的特殊关键字  
全局水印| 管理系统-安全管理-全局水印| FINE_CONF_ENTITY| WatermarkConfig.valid| true/false| 是否开启全局水印  
WatermarkConfig.watermarkData.textType| formula/username/ip/time| 水印内容类型  
WatermarkConfig.watermarkData.text|   
| 当水印类型为公式时，具体的公式内容  
WatermarkConfig.watermarkData.color|   
| 水印颜色  
WatermarkConfig.watermarkData.fontSize|   
| 水印字号  
WatermarkConfig.watermarkData.horizontalGap|   
| 水印间距-横向  
WatermarkConfig.watermarkData.verticalGap|   
| 水印间距-纵向  
## 13\. 模板认证
分类| 描述| 存储表| 字段id| 字段值| 备注  
---|---|---|---|---|---  
全局配置| 系统管理-模板认证-全局配置| FINE_CONF_ENTITY| TemplateAuthConfig.tempAuthOpen| true/false| 是否开启模板认证  
TemplateAuthConfig.tempAuthType| 0/1/2/3| 模板认证类型0，仅认证用户名密码1，角色权限认证2，数字签名认证  
TemplateAuthConfig.digitalAuthKey|   
| 数字签名秘钥  
TemplateAuthConfig.configuredOnce| true/false| 是否曾经开启过模板认证  
## 14\. 非界面配置项
对于前台未提供配置界面，但记录在 fine_conf_entity 表中的属性如下表所示：
key（id）| value（默认值）| 说明  
---|---|---  
JAR包在 2020-04-26 到 2020-06-20 之间：FSConfig.loginConfig.tokenFromCookieJAR包在 2020-06-20 及之后：ServerConfig.tokenFromCookie| false| 开启后后台校验token时可从Cookie中取，解决HttpOnly下后台单点和跨域单点登录失败的问题  
WebSecurityConfig.xssProtectionHeader| 1; mode=block| XSS攻击防护Header X-XSS-Protection的值  
WebSecurityConfig.frameOptionsHeader| SAMEORIGIN| 点击劫持攻击防护Header X-Frame-Options的值  
WebSecurityConfig.contentTypeOptionsHeader| nosniff| 内容嗅探攻击防护Header X-Content-Type-Options的值  
WebSecurityConfig.contentSecurityPolicyHeader| object-src 'self'| CSP内容安全策略Header Content-Security-Policy的值  
WebSecurityConfig.cacheControlHeader| no-cache| 浏览器缓存禁用Header Cache-Control的值  
WebSecurityConfig.cacheControlExpiresHeader| 0| 浏览器缓存禁用Header Expires的值  
WebSecurityConfig.cacheControlPragmaHeader| no-cache| 浏览器缓存禁用Header Pragma的值  
WebSecurityConfig.hstsHeader| max-age=31536000; includeSubDomains| HSTS Header Strict-Transport-Security的值  
BackupConfig.customValueLength| 65536| 备份conf表，自定义value长度  
BackupConfig.customKeyLength| 1500| 备份conf表，自定义id长度  
FSConfig.loginConfig.forceRedirectAfterLogin| false|  登录后强制跳转，默认关闭  
SystemConfig.serverInit| ""| 平台是否初始化完成 success/fail  
WebSocketConfig.port| [38888, 39888]| 端口  
WebSocketConfig.protocol| plain| 如果是https服务器，则需要设置为ssl  
WebSocketConfig.keyStore| ""| 存放文件的路径(这边最好用绝对路径)，一般用keyStore，trustStore待验证  
WebSocketConfig.keyStorePassword| ""| 申请时候用到的密钥  
WebSocketConfig.keyStoreFormat| JKS| 默认用JKS（如果是pfx证书，改成PKCS12）  
WebSocketConfig.trustStore| ""| 文件路径(这边最好用绝对路径)  
WebSocketConfig.trustStorePassword| ""| 申请时候用秘钥  
WebSocketConfig.trustStoreFormat| JKS| 默认用JKS（如果是pfx证书，改成PKCS12）  
WebSocketConfig.socketContext| /socket.io| 用于修改websocket的路由  
ServerConfig.cookiePath| /| cookie路径注：请在部署工程时配置，尤其是多个工程部署在同一服务器下，且使用了相同域名时，请务必配置。否则会造成浏览器存储多个cookie，需要每个用户手动清除cookie才能登录成功  
ScheduleSettingConfig.taskTimeout| 300000| 定时任务超过时间，默认5分钟  
SecurityConfig.frontSeed| 随机的16位字符串| 用于给前端加密提供秘钥，初始是随机的16位字符串，可自行修改  
WebSecurityConfig.loginValidateStrict| false/true| 用于限制跨域登录接口，以及cas后台登录接口的使用，如果配置true，则不能使用这俩接口  
LoadConfig.minorTerribleThreshold| 0.09| minorGC后，晋升到老年代的对象速率与EDEN区的比值大小超过这个值算是超高负载  
LoadConfig.minorHighThreshold| 0.06| minorGC后，晋升到老年代的对象速率与EDEN区的比值大小超过这个值算是高负载  
LoadConfig.minorMidThreshold| 0.03| minorGC后，晋升到老年代的对象速率与EDEN区的比值大小超过这个值算是中等负载  
LoadConfig.majorExtremeTerribleThreshold| 0.95| majorGC后，残留在老年代对象大小与老年代大小的比值超过这个值算是极限负载  
LoadConfig.majorTerribleThreshold| 0.85| majorGC后，残留在老年代对象大小与老年代大小的比值超过这个值算是超高负载  
LoadConfig.majorHighThreshold| 0.7| majorGC后，残留在老年代对象大小与老年代大小的比值超过这个值算是高负载  
IntelliReleaseConfig.highInterruptRate| 0.8| 第一次小范围杀会话时，会话格子数超过模板限制格子数值的80%时被杀死  
IntelliReleaseConfig.highInterruptAgainRate| 0.6| 第二次小范围杀会话时，会话格子数超过模板限制格子数值的60%时被杀死  
IntelliReleaseConfig.highKillRate| 0.1| 第一次小范围杀会话后，被杀死会话数不足10%时进行第二次小范围杀会话  
IntelliReleaseConfig.terribleInterruptRate| 0.6| 第一次大范围杀会话时，会话格子数超过模板限制格子数值的60%时被杀死  
IntelliReleaseConfig.terribleInterruptAgainRate| 0.4| 第二次大范围杀会话时，会话格子数超过模板限制格子数值的40%时被杀死  
IntelliReleaseConfig.terribleKillRate| 0.2| 第一次大范围杀会话后，被杀死会话数不足20%时进行第二次大范围杀会话  
IntelliReleaseConfig.waitInLineRate| 0.9| 高负载时此模板90%概率排队  
IntelliReleaseConfig.defaultCellCount| 1000000| 大小范围杀会话时，如果模板格子数限制关闭默认格子数1_000_000  
IntelliReleaseConfig.releaseSessionInterval| 20| 在20s内如果此次gc后负载状态低于或等于上次gc状态则不进行大/小范围杀会话  
WebSecurityConfig.fileInspectorType| 1| 开启了安全管理的文件校验后，用此配置文件上传校验类型0-(综合，后缀不在白名单内放行，否则校验头) 1-(白名单，后缀在白名单且头匹配的才放行) 2-(黑名单，后缀不在黑名单内放行)  
QuartzConfig.threadCount| 100| 定时调度模块最大线程数（8月16之后版本支持）  
QuartzConfig.maxConnections| 50| 定时调度模块最大连接数（8月16之后版本支持）  
ScheduleSettingConfig.timeoutRemind| true| 定时调度任务是否开启监控日志超时提醒  
ClusterTimeMonitorConfig.sumCount| 3| 集群单次时间误差检测任务中, 尝试误差分析的总次数  
ClusterTimeMonitorConfig.permitCount| 1| 集群单次时间误差检测任务中, 多次误差分析中最小成功次数  
ClusterTimeMonitorConfig.permitError| 10*1000| 集群单次时间误差检测任务中, 允许时间误差值,单位 ms  
FileServerMonitorConfig.messageInterval| 1| FTP 异常消息通知频率,单位 h  
JarConsistenceConfig.messageInterval| 6| Jar不一致异常消息通知频率,单位 h  
RedisClusterMonitorConfig.messageInterval| 6| Redis 节点异常消息通知频率,单位 h  
RedisConfig.maxConnection| 200| Redis 连接池最大实例总数  
RedisConfig.expireStateRemoveInterval| 5*60*1000| 状态服务器 过期 key 删除间隔时间,单位 ms  
RedisConfig.database| 0| Redis 指定数据库  
RedisClusterConfig.maxConnection| 200| Redis Cluster 连接池最大实例总数  
FineClusterConfig.params.encrypt| false| 集群通信加密开关，默认为false  
## 15\. Spider 引擎截流参数
5.1.11 版本新增三个参数，可对 Spider 引擎的查询进行截流，避免持续高并发导致 http 线程耗尽，阻塞非 Spider 查询。
注：下表所示的参数修改后，需重启生效。
id| value| 说明  
---|---|---  
DistributedOptimizationConfig.spiderConfig.spider_engine_queue_size_limit| 默认值为 -1   
| **含义：** Spider 引擎处理查询和等待查询的队列大小，进入的查询如果超出后会等待一段时间，如果超时还是没有进入队列则拒绝并报错-1 表示无穷大，也就是不会拒绝**建议值：** 200，即 Spider 最多处理或等待处理 200 个查询  
DistributedOptimizationConfig.spiderConfig.spider_engine_queue_try_wait| 默认值为 500  
| **含义：** 当请求无法进入等待队列时，自旋一段时间（单位：毫秒），尝试不断进入该参数意义是平衡短查询 + 高并发的体验，如果 Spider 引擎是因为大量短查询而繁忙的，设定这个时间的重试可以减少被拒绝的概率**建议值：** 500，即一个请求在 500 毫秒内会尝试不断进入队列，超时后仍然被拒绝才会报错  
DistributedOptimizationConfig.spiderConfig.spider_engine_queue_refuse_msg| 默认值为：spider engine overload| **含义：** 当请求最终被拒绝而报错，显示的文案**建议值：**  
用户可自定义  
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：BI系统配置数据集](<index.php?doc-view-2149.html>)
[下一篇：fine_conf_entity可视化配置 ![](/core/style/forward.png) ](<index.php?doc-view-1235.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
