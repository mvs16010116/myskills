---
title: FineBI升级前环境检查风险项修复方案
doc_id: 2004
url: https://help.fanruan.com/finebi6.X/doc-view-2004.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:57
---

> 1. 概述使用「FR和BI升级检测」工具，进行 6.0 升级检测时，导出的风险项及修复方案介绍。6.0升级前环境检测步骤详情参见：FineBI升级前环境检查2. 风险项及修复方案检测工具处理：是升级检测

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI升级前环境检查风险项修复方案
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[13](<edition-list-2004.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-11-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
使用「FR和BI升级检测」工具，进行 6.0 升级检测时，导出的风险项及修复方案介绍。
6.0升级前环境检测步骤详情参见：[FineBI升级前环境检查](<https://help.fanruan.com/finebi6.X/doc-view-2001.html>)
## 2\. 风险项及修复方案
检测工具处理：是升级检测插件自动处理
分类| 阻塞等级| 处理方式  
| 检查内容  
| 界面提示内容| Excel提示内容  
---|---|---|---|---|---  
配置| SUGGEST| 检测工具处理| 1）有配置外置库2）WEB-INF/config/db.properties中hibernate.hbm2ddl.auto值是否设置为update| 无需提示| 检测到系统配置hibernate.hbm2ddl.auto不为update，修改该配置参数为update，否则升级过程中无法进行配置兼容升级  
配置| WARN  
| 手动处理| 1）检测MySQL参数max_allowed_packet需配置小于1073741824，则标记为警告项2）检测不到MySQL参数max_allowed_packet，则标记为警告项| WARN:配置外置库为MySQL且参数max_allowed_packet小于1073741824，影响配置兼容执行WARN : 当前外置库连接用户无权限查询MySQL的max_allowed_packet参数，要求参数值>=1073741824,请您自行查询| 检测到外置库为MySQL，且参数max_allowed_packet<1073741824,升级过程需要对配置进行兼容调整，参数过小会导致配置写入数据库失败，为保证升级顺利进行，请您优先调整max_allowed_packet参数，调整方式如下方案一：MySQL 安装目录下的「my.ini」文件中的[mysqld] 字段中的「max_allowed_packet = 1M」修改为 1024M ，重启 MySQL 即可。方案二：1）使用「set global max_allowed_packet = 1073741824;」 语句将「max_allowed_packet」的值设置为 1024M，无需重启。2）使用「show VARIABLES like '%max_allowed_packet%';」 语句查看是否修改成功。  
配置| SUGGEST| 检测工具处理| UpdatePushConfig.open”，检测值是否为false，标记为提示项| 导出文件提示|   
  
配置| BLOCK| 手动处理| 获取spider_local_root_path对应的路径，检查对应路径下是否可以创建文件| 检测到XXXX路径下无文件创建权限，该路径为数据更新路径且必须有文件读写权限| 检测到XXXX路径下无文件创建权限，该路径为数据更新路径且必须有文件读写权限，请使用chmod路径给该路径赋权 ，命令格式如下 chmod -R 777 xxx路径  
配置| BLOCK| 手动处理  
| 检测更新路径是否设置，且为绝对路径| 配置库中更新路径为..\spider，不是绝对路径，请根据全局更新界面更新文件存放的绝对路径配置修改配置库中的更新路径为绝对路径，若不配置，升级后数据将因找不到db文件而预览失败；配置方式：  
INSERT INTO FINE_CONF_ENTITY VALUES('DistributedOptimizationConfig.spiderConfig.spider_local_root_path','全局更新界面更新文件存放的绝对路径')| 配置库中更新路径为..\spider，不是绝对路径，请根据全局更新界面更新文件存放的绝对路径配置修改配置库中的更新路径为绝对路径，若不配置，升级后数据将因找不到db文件而预览失败；配置方式：  
INSERT INTO FINE_CONF_ENTITY VALUES('DistributedOptimizationConfig.spiderConfig.spider_local_root_path','全局更新界面更新文件存放的绝对路径')  
配置| BLOCK/WARN| 手动处理| 1、jdk版本为oracle的1.8.0.102，需先升级JDK，标记为阻塞项2、检测不到JDK版本信息，标记为警告项| BLOCK: JDK版本低于1.8.0.102，升级后会因为JDK漏洞导致启动异常，请您先升级JDK版本在进行BI升级WARN : 当前无法获取JDK版本，请您先确认JDK版本大于1.8.0.102| 检测到jdk 版本低于1.8.0.102 ，旧版本JDK存在漏洞，升级后会存在启动崩溃的现象，需要更换为1.8.0.102以后版本的 jdk 再进行升级。 JDK版本更新后引入加密套件，可能导致数据连接连接不上，需要按照如下文档进行完善：[JDK 升级及注意事项](<https://help.fanruan.com/finebi6.X/doc-view-1617.html>)  
配置| WARN| 手动处理| 检测 FineClusterConfig.params.cluster**为false** 且SystemOptimizationConfig.biClusterMasterNodeHostName 非空hotBackConf.master 非空 SystemOptimizationConfig.ClientMasterId **非空** hotBackConf.slave 非空StateServerConfig.type != standoneStateServerConfig.clusterMode != false| WARN : 检测当前为单机环境但是残留集群相关配置，需删除残留参数| 检测当前为单机环境但是残留集群相关配置，需删除残留参数，以下热备参数需删除，需连接配置库中将fine_conf_entity表中对应参数进行修改非空则提示需删除ID为：SystemOptimizationConfig.biClusterMasterNodeHostName 非空则提示需删除ID为：hotBackConf.master 非空则提示需删除ID为：SystemOptimizationConfig.ClientMasterId 非空则提示需删除ID为：hotBackConf.slave 以下为redis配置参数，请确认redis配置是否仍在使用，如已停止使用登陆超级管理员，在智能运维→ 集群配置中,将状态服务器改为关闭状态  
配置| WARN| 手动处理| 检测是否有当天的备份文件| WARN : 检测到系统近一天内无成功备份，请确认系统配置有备份| 检测到当前系统中近一天内无备份文件，建议您备份后再进行升级：[备份还原](<https://help.fanruan.com/finebi6.0/doc-view-400.html>)  
驱动| WARN| 手动处理| 检测外置库为oracle11g及以上版本且lib目录下无ojdbc8| WARN : 检测到外置库为oracle11g及以上的版本，建议您使用匹配的驱动ojdbc8| 检测到当前系统使用的外置库为oracle11g及之后的版本，建议您将驱动更换为ojdbc8再进行升级，需要将ojdbc14.jar文件更换为ojdbc8.jar和orai18n.jar两个jar文件  
驱动| BLOCK| 手动处理| hive、phoenix、spark、impala、TRANSWARP 、INCEPTOR安装驱动隔离插件| BLOCK：驱动冲突阻塞| 检测到系统使用了hive、phoenix、spark、impala、TRANSWARP 、INCEPTOR等大数据平台，其使用的驱动容易和BI的代码产生冲突，强烈建议您配置驱动隔离以保证系统的稳定运行，详细配置方式：[5.1.2 及之后版本驱动隔离插件](<https://help.fanruan.com/finebi5.1/doc-view-697.html>)  
lib异常文件| BLOCK| 手动处理| commons等jar，检测后提示删除| BLOCK：lib异常文件冲突阻塞| 检测到该文件容易和BI的代码产生冲突，需要您删除之后重启BI，然后进行升级  
lib异常文件| BLOCK| 手动处理| lib下文件夹、zip文件、重名文件，检测后提示删除| BLOCK：lib异常文件冲突阻塞| 检测到lib文件中存在文件夹、zip文件、重名文件，此类型文件极容易导致BI运行不稳定，需要您删除之后重启BI，然后进行升级。  
lib异常文件| WARN| 手动处理| lib下文件夹下非txt和jar文件认为是非法文件，检测后提示删除| WARNING：lib异常文件警告，建议删除| 检测到lib文件中存在非jar和非txt的文件，可能对工程产生影响，请删除后在升级。  
lib异常文件| BLOCK| 手动处理| hive、phoenix、spark、impala、TRANSWARP 、INCEPTOR、hbase、maxcomputer、kylin、驱动包**hive：** geronimo-jaspi、hadoop-common、hive-jdbc、xercesImpl**spark：** hadoop-core、hive-jdbc**maxcomputer** slf4j-log4j、odps-jdbc**TRANSWARP -INCEPTOR** TRANSWARP 、INCEPTOR**hbase、phoenix** phoenix**impala** impala**kylin** kylin| BLOCK：lib异常文件冲突阻塞| 检测到lib文件中存在hive、phoenix、spark、impala、TRANSWARP 、INCEPTOR等大数据平台的驱动，该文件容易和BI的代码产生冲突，需要您删除之后重启BI，然后进行升级  
lib异常文件| BLOCK| 手动处理| 检测是否存在fr-xxxx-8.0、fr-xxxx-9.0、fr-xxxx-4.0、fr-xxxx-4.1、fr-slf4j-frlog4j| BLOCK：lib异常文件冲突阻塞| 检测到lib文件中存在8.0、9.0版本的jar文件，该文件容易和BI的代码产生冲突，需要您删除之后重启BI，然后进行升级  
插件| WARN| 手动处理| 检测插件名存在JSD、SLN等二开插件| WARN：检测到插件管理中存在二开插件，建议您联系技术支持确认新版本插件的是否兼容| 检测到插件管理中存在二开插件，建议您联系技术支持确认新版本插件的是否兼容  
插件| WARN| 手动处理| 插件检测插件名称存在压缩文件名fr-plugin-platform-bridge，压缩文件名com.tptj.plugin.hg.platform.bridge；安装文件名plugin-com.tptj.plugin.hg.platform.bridge明确需升级插件| WARN：检测到插件管理中存在单点插件，建议您联系技术支持获取新版本插件| 检测到插件管理中存在单点登录插件，建议您联系技术支持确认新版本插件的是否兼容  
插件| WARN| 手动处理| 微信插件检测| 检测到当前工程集成了微信，需要升级前将微信管理插件和html5移动端展现插件升级到最新的版本| 检测到当前工程集成了微信，需要升级前将微信管理插件和html5移动端展现插件升级到最新的版本  
插件| SUGGEST| 检测工具处理| 删除插件plugin-com.fr.plugin.decision.data.check，压缩文件plugin-com.fr.plugin.decision.data.check| 导出文件提示| 检测到插件管理中存在无效插件插件，该插件影响升级执行，会在升级过程中自动删除  
插件| SUGGEST| 检测工具处理| 删除插件数据集切换表bi-plugin-table-switcher-1.0.2-513.zip| 导出文件提示| 检测到插件管理中存在无效插件插件，该插件影响升级执行，会在升级过程中自动删除  
插件| SUGGEST| 检测工具处理| 删除插件仪表板默认选择表格fr-plugin-default-widget-type-1.0.0.zip| 导出文件提示| 检测到插件管理中存在仪表板默认选择表格插件，新版本已包含该功能，会在升级过程中自动删除  
插件| SUGGEST| 检测工具处理| 删除com.fr.plugin.platform.safelogin| 导出文件提示| 检测到插件管理中存在9.0版本插件，当前系统为10.0版本，该插件对系统稳定性产生隐患，已自动删除  
插件| WARN| 手动处理| 检测插件名称是否存在name : 多ldap登录id不为： com.fr.plugin.decision.multi.ldap.passport提示升级后需要重新配置| 导出文件提示| 检测到插件管理中存在 “ 多域LDAP认证 ” 插件，该插件新版本功能逻辑发生变更，需手动进行调整，详见帮助文档：[多域LDAP认证](<https://help.fanruan.com/finebi6.0/doc-view-1188.html>)  
插件| SUGGEST| 检测工具处理| 删除插件名称是否存在plugin-com.finebi.memory-1.0.5、plugin-com.finebi.memory-1.0.5删除插件名称是否存在plugin-com.finebi.memory-1.0.6、plugin-com.finebi.memory-1.0.6| 导出文件提示| 检测到插件管理中存在旧版本内存管理插件，当前系统为10.0版本，该插件对系统稳定性产生隐患，已自动删除  
插件| SUGGEST| 检测工具处理| 压缩文件名fr-plugin-bi-inspector id ：com.finebi.plugin.bi.inspector 安装文件名：plugin-com.finebi.plugin.bi.inspector压缩文件名fr-plugin-bi-cleaner id ：com.finebi.plugin.bi.cleaner 安装文件名：plugin-com.finebi.plugin.bi.cleaner| 导出文件提示| 检测到插件管理中存在旧版本工具插件，该插件对系统稳定性产生隐患，已自动删除  
插件| WARN| 手动处理| 检测当前环境是否能连接到插件商城，提示升级后插件需要升级| WARN :如果可以连接提示升级后登录插件管理页面升级对应插件升级项如果不可以连接提示打开插件商城<https://market.fanruan.com/>查看已安装插件是否有新版本更新| （有外网）升级后请登陆系统，打开插件管理页面升级提示需要升级的插件，当前已经安装XXX个插件，如不更新对应的插件将导致部分功能异常。或（无外网）检测到当前环境无法连接到插件商城，请打开[插件商城](<https://market.fanruan.com/>)查看已安装插件是否有新版本更新，并下载对应的插件进行本地更新，当前已经安装XXX个插件，如不更新对应的插件将导致部分功能异常。  
插件| WARN| 手动处理| 插件依赖丢失可能导致的插件异常（如果该项可以实现13、14、22可以无需提示）|   
|   
  
插件| suggest| 检测工具处理| 删除插件文件名：plugin-com.fr.plugin.operationID：com.fr.plugin.operation|   
|   
  
插件  
| WARN  
| 升级工具处理| 检测spider数据集插件plugin-report-spider-dataset| Spider数据集插件6.0版本中仅支持只读效果，新增使用由FDL处理| Spider数据集插件6.0版本中仅支持只读效果，新增使用由FDL处理  
插件| SUGGEST| 升级工具处理| 删除驱动隔离插件plugin-decision-driver-loaderhttps://git.fanruan.com/fanruan/demo-driver-loader/src/master| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本已包含该功能，会在升级过程中自动删除  
插件| SUGGEST| 升级工具处理| 删除前端区分处理分析表插件bi-plugin-classify-table| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本不再区分处理分析表，会在升级过程中自动删除  
插件| SUGGEST| 升级工具处理| 删除BI模板访问socket插件plugin-bi-websocket-visit| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本已包含该功能，会在升级过程中自动删除  
插件| SUGGEST| 升级工具处理| HTTPS_SameSite_跨域com.fr.plugin.decision.cookie.check| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本已包含该功能，会在升级过程中自动删除  
插件| SUGGEST| 升级工具处理| 数据集中SQL可全屏com.fr.solution.plugin.better.sql.editor| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本已包含该功能，会在升级过程中自动删除  
插件| SUGGEST| 升级工具处理| 新手引导com.fr.plugin.user.guide| 导出文件提示| 新版本已内置  
插件| SUGGEST| 升级工具处理| BI字段分组插件com.finebi.plugin.fieldgroup| 导出文件提示| 不再支持此插件  
插件| SUGGEST| 手动处理| 删除BI模板屏幕自适应 plugin-bi-screen-adaptive升级后自动更新为BI模板屏幕自适应plus：plugin-bi-show-adaptive| 导出文件提示| 检测到插件管理中存在 ”XXXX“ 插件，新版本已不支持该插件，会在升级过程中自动删除；如需使用，请于插件商城下载“BI模板屏幕自适应plus”插件  
插件| SUGGEST| 手动处理| 开放平台插件是否安装| 工程安装了开放平台插件| 工程安装了开放平台插件com.tptj.plugin.hg.client.center.v10，主插件是这个；  
[com.finebi.plugin.open.client.bi](<http://com.finebi.plugin.open.client.bi/>)，bi接口 子插件是这个  
数据| WARN| 手动处理| 检测自定义函数class的规范性| WARN：自定义函数xxx无法序列化| 检测到系统中存在自定义函数xxxxx，该函数编写不规范导致无法序列化，请重新修改适配。  
数据| WARN| 手动处理| 检测到用户自助数据集下Excel表使用了自循环列| WARN：用户自助数据集下的Excel表升级后不再支持自循环列步骤| 检测到XX用户自助数据集的xxExcel表存在自循环列步骤，建议移动到公共数据  
数据| WARN| 手动处理| 检测复合过滤组件参数使用了过滤组件| WARN：复合过滤组件不再支持引用控件参数的用法| 检测到复合过滤组件x使用到了过滤组件的参数用法，建议调整不含过滤组件参数的过滤方法  
数据| WARN| 手动处理| 检测到用户自助数据集下Excel表使用了关联| 检测到用户自助数据集的Excel表存在关联，建议删掉| 检测到用户自助数据集的Excel表存在关联，建议删掉  
环境| BLOCK/WARN| 手动处理| 磁盘空间检测<1g，标记为阻塞项检测不到磁盘空间，标记为警告项|   
| 检测到当前磁盘剩余空间不足1G，请确保磁盘空间大于1G再进行升级，您可以先清理磁盘空间然后进行升级”  
环境| WARN| 手动处理| 是否发生升级回退|   
| 检测到您系统曾经发生升级未按照文档回退配置内容，该操作可能产生脏数据，强烈建议您先测试环境进行升级验证  
环境| BLOCK/WARN| 手动处理| 检测外置库DDL权限缺失，标记为阻塞项|   
| 检测到您系统使用外置库且当前用户无外置库表的增删改查（DDL）权限，建议您联系数据库运维人员修改对应权限后再进行升级  
环境| BLOCK/WARN| 手动处理| 检测外置库编码mysql编码不为utf8或utf8mb4，标记阻塞SQL server编码不为为Chinese_PRC_CS_AS，如果是Chinese_PRC_CI_AS标记为warn，其他的为BLOCK|   
| 检测外置库编码不为要求的编码  
环境| WARN| 手动处理| 检测当前环境是否为集群环境，如果是提示更新nginx| WARN :检测到当前环境为集群环境，升级后请更新nginx转发配置| WARN :检测到当前环境为集群环境，升级后请更新nginx转发配置  
环境| WARN| 手动处理| 检测redis状态是否正常| 工程的redis状态可能存在异常，请确认无问题后再升级| 工程的redis状态可能存在异常，请确认无问题后再升级  
环境| WARN| 手动处理| 检测FTP连接状态| 工程的ftp连接状态可能存在异常，请确认无问题后再升级| 工程的ftp连接状态可能存在异常，请确认无问题后再升级  
环境| WARN| 手动处理| 单一登录检测| 单一登录状态为关闭| 单一登录状态为关闭  
环境| WARN| 手动处理| 检测是否正式lic| 工程lic未注册| 工程lic未注册  
环境| WARN| 手动处理| 检测系统是否是arm架构| 系统为arm架构，需使用arm架构的升级工具| 系统为arm架构，需使用arm架构的升级工具  
环境| WARN| 手动处理| windows环境变量检测| 检测到当前工程为windows环境，需要手动添加升级工具\fine-bi-upgrade-windows\environment\windows\jre\bin配置到系统环境变量path中，以避免工具启动找不到内置jre环境变量导致升级失败| 检测到当前工程为windows环境，需要手动添加升级工具\fine-bi-upgrade-windows\environment\windows\jre\bin配置到系统环境变量path中，以避免工具启动找不到内置jre环境变量导致升级失败  
环境| SUGGEST| 手动处理| API接口变更提示|   
| 升级后需清理浏览器缓存  
环境| BLOCK| 手动处理| 检测运行环境是否存在msvcr120.dll|   
| msvcr120.dll运行库不存在，需要安装x64版本的 Visual Studio 2010 (VC++ 10.0) 之后再进行升级, 可参考微软帮助文档：[点击进入](<https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-160%E3%80%82>)  
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineBI升级前环境检查](<index.php?doc-view-2001.html>)
[下一篇：FineBI5升6风险评估表填写说明 ![](/core/style/forward.png) ](<index.php?doc-view-2147.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
