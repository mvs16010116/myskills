---
title: FineReport 集成到 FineBI
doc_id: 67
url: https://help.fanruan.com/finebi6.X/doc-view-67.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:20
---

> 1. 概述1.1&nbsp;应用场景在实际使用过程中存在需要将 FineReport 工程集成到 FineBI 数据决策系统上使用的情况。将 FineReport 集成到 FineBI ，可以将这两个软

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineReport 集成到 FineBI
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[57](<edition-list-67.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-02 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
在实际使用过程中存在需要将 FineReport 工程集成到 FineBI 数据决策系统上使用的情况。
  * 将 FineReport 集成到 FineBI ，可以将这两个软件合并成一个整体的系统，应用服务只需维护一套。
  * FineReport 集成到 FineBI 后，统一 FineBI 和 FineReport 的用户、权限体系、门户以及管理系统，用户登录时只需要登录一个平台。


### 1.2 方案选择
请根据你的实际情况，选择适合的集成方案。
情况  
| 方案说明  
---|---  
完全未部署希望部署一个包含FineBI和FineReport功能的工程| 1）部署一个FineBI工程，其中会自带FineReport相关JAR2）注册license时，选购FineReport相关功能点3）制作FineReport模板时，使用设计器远程连接该FineBI工程即可可参考：[FineReport 设计器远程连接 FineBI 工程 ](<https://help.fanruan.com/finebi6.X/doc-view-931.html>)  
已有一个FineBI工程（已有仪表板或平台配置）希望增加FineReport相关功能| 1）无需重新部署工程，FineBI工程本身就自带FineReport相关JAR2）license增购FineReport相关功能点3）制作FineReport模板时，使用设计器远程连接该FineBI工程即可可参考：[FineReport 设计器远程连接 FineBI 工程](<https://help.fanruan.com/finebi6.X/doc-view-931.html>)  
已有一个FineReport工程（已有模板，无平台配置）希望增加FineBI相关功能| 1）部署一个FineBI工程，其中会自带FineReport相关JAR2）按照本文执行  
已有一个FineReport工程和一个FineBI工程（已有仪表板、模板和配置）希望将这两个工程整合到一个工程| 完全按照本文执行  
已有一个FineReport工程和一个FineBI工程（已有仪表板、模板和平台配置）保留两个工程，无需集成但希望能统一门户访问模板/仪表板| 通过「多产品连接工具」插件，即可实现跨工程挂载模板可参考：[多产品连接工具插件](<https://help.fanruan.com/finebi6.X/doc-view-1179.html>)  
## 2\. 准备步骤
### 2.1 确认服务器配置
请根据工程访问量和数据量，对FineBI工程的内存、CPU、磁盘等配置进行增加，确保集成后的工程可正常运行。
详情请参见：[确认FineBI项目服务器配置 ](<https://help.fanruan.com/fineops/doc-view-134.html>)
### 2.2 确认工程版本一致
请确保FineBI与FineReport版本完全一致，且版本兼容。
**1）确认FineBI各模块版本兼容**
  * 管理员登录FineBI系统，点击「管理系统>注册管理>版本信息」。
  * 查看报表模块和BI模块版本，对照 [FineBI 与 FineReport 版本适配说明](<https://help.fanruan.com/finebi6.0/doc-view-1061.html>) ，确认版本是否兼容  



**2）确认FineBI与FineReport版本一致**
  * 管理员登录FineReport系统，点击「管理系统>注册管理>版本信息」。
  * 查看FineReport的报表模块版本，与上一步FineBI的报表模块版本对比，确认完全一致，请精确到JAR包。


如版本不一致，请对其中一个工程进行升级/回退处理，务必确保一致，否则无法集成。
小版本升级指南请参考：[FineReport工程小版本升级指南](<https://help.fanruan.com/finereport/doc-view-1163.html>) 、[非容器化FineBI6.0.x小版本升级指南](<https://help.fanruan.com/finebi6.X/doc-view-2126.html>)
![](/core/style/lod.png)
### 2.3 资源导出
配置库，即finedb，本文方案仅能保留FineBI工程的配置库。
对于FineReport工程的配置，如果仍然非常希望保留  

可通过 [资源迁移](<https://help.fanruan.com/finereport/doc-view-2604.html>) 先导出相关数据连接、服务器数据集、目录等内容，在集成后再资源导入。
注：该步骤不能完全保证一定保留FineReport工程配置，只能尽可能的降低集成后的工程配置难度
## 3\. 工程集成
### 3.1 关闭工程
请参考「[关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>)」文档，关闭FineReport和FineBI工程
### 3.2 拷贝文件
请将FineReport工程中相关文件，拷贝到FineBI工程中同位置。  

如有相同文件，一般建议保留FineBI文件不覆盖。
工程文件| 说明  
  
---|---  
/webroot/WEB-INF/lib| 作用：工程原有/外部引入的JAR包，提供工程所有基础功能，是工程的关键文件是否必须拷贝：必须拷贝如有相同文件，请务必保留FineBI文件不覆盖  
/webroot/WEB-INF/plugins| 作用：插件相关文件是否必须拷贝：必须拷贝，如不拷贝会影响插件相关功能的实现如有相同文件，请务必保留FineBI文件不覆盖。  
/webroot/WEB-INF/reportlets| 作用：FineReport模板存放目录是否必须拷贝：必须拷贝，如不拷贝会导致工程所有模板丢失如有相同文件，请务必逐一判断或在reportlets下为模板新建目录存放  
/webroot/WEB-INF/resources| 作用：保存了报表信息、配置信息是否必须拷贝：用户自行决定请务必**不要拷贝** 该目录下的FanRuan.lic文件到FineBI工程跨工程拷贝lic文件，会导致新老工程都可能无法使用该lic授权如需迁移，请在工程集成完毕后再进行  
/webroot/WEB-INF/schedule| 作用：定时调度生成的文件是否必须拷贝：用户自行决定如果不拷贝，定时任务挂载到决策平台的结果报表无法访问  
/webroot/WEB-INF/classes| 作用：工程调用的默认和自定义class文件是否必须拷贝：必须拷贝有可能存在自定义的class文件，如不拷贝会影响工程正常使用  
/webroot/WEB-INF/assets/temp_attach| 作用：读写缓存存储路径是否必须拷贝：必须拷贝该文件夹中存放着工程读写（图片）缓存，不拷贝可能会导致FR模板设置的背景图片预览为空  
/webroot/WEB-INF/assets/vcs| 作用：FineReport模板备份文件是否必须拷贝：用户自行决定如果工程不需要回退历史开发的FineReport模板，则无需拷贝  
/webroot/WEB-INF/assets/其他文件| 作用：通用的共享持久化目录是否必须拷贝：必须拷贝工程正常运行所需要的文件，如不拷贝会影响工程正常使用  
/webroot/backup| 作用：工程历史备份文件是否必须拷贝：用户自行决定，可存储在原始的目录下备份，可不拷贝  
/webroot/help| 作用：工程自定义内容是否必须拷贝：必须拷贝该文件夹中存放着自定义地图、自定义函数、定制css、定制js等文件，不拷贝会导致模板预览出现异常  
/webroot/logs| 作用：swift日志是否必须拷贝：用户自行决定如果不拷贝，会丢失工程历史操作日志（即logdb），「管理系统>平台日志」功能无数据如对历史使用情况无要求，无需拷贝如有相同 JAR 包，保留原先 FineBI 里的不替换  
### 3.3 资源迁移导入
如2.3节资源导出了相关配置，此时可以选择按需导入FineBI工程
### 3.4 授权迁移
如需要将FineReport工程的授权迁移到FineBI，由于需要增购FineBI相关功能点，请联系销售确认。
不可以直接将FineReport工程的授权lic放置到FineBI工程中
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：多产品连接工具插件](<index.php?doc-view-1179.html>)
[下一篇：FineReport 设计器远程连接 FineBI 工程 ![](/core/style/forward.png) ](<index.php?doc-view-931.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
