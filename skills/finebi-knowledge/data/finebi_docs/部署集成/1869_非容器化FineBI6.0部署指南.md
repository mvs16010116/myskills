---
title: 非容器化FineBI6.0部署指南
doc_id: 1869
url: https://help.fanruan.com/finebi6.X/doc-view-1869.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:52
---

> 提示:帆软目前仅对外提供&nbsp;FineBI 6.1 的容器化部署方案。不再提供 Tomcat 部署包或手动部署工程，相关文档已停止维护。容器化部署方案可保障帆软应用稳定运行和全方位运维管理，建议生

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 非容器化FineBI6.0部署指南
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[7](<edition-list-1869.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-03-04 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
帆软目前仅对外提供 **FineBI 6.1 的容器化部署方案** 。不再提供 Tomcat 部署包或手动部署工程，相关文档已停止维护。
容器化部署方案可保障帆软应用稳定运行和全方位运维管理，建议生产环境用户迁移容器化，详情请参见：[迁移项目](<https://help.fanruan.com/fineops/doc-view-147.html>)
本文档仅面向历史**已进行**FineBI6.0** 非容器化部署**的客户。可参照本文索引，进行备份和测试工程的部署。
## 历史非容器化部署FineBI6.0方案
内容| 简介  
---|---  
**1\. 初识部署**  
[FineBI6.0非容器化工程部署原理](<https://help.fanruan.com/finebi6.X/doc-view-44.html>)  
| 1）工程部署的必要性/部署原理2）单机和集群的简介/区别/适用场景/组成部件3）抽取集群和直连集群的区别/抽取集群的优势4）各种部署方式的区别，什么是容器化部署？  
[FineBI6.0非容器化工程部署方案选择](<https://help.fanruan.com/finebi6.X/doc-view-1375.html>)  
| 1）根据用户并发数和数据使用量推荐单机/集群节点数2）根据各种部署方式的优缺点，选择适合自己的部署方式。  
单机：容器化部署、部署包部署、独立部署  
集群：容器化部署标准抽取集群、手动部署标准抽取集群、手动部署高可用抽取集群、手动部署标准直连集群  
[FineBI6.0非容器化工程部署推荐环境及配置](<https://help.fanruan.com/finebi6.X/doc-view-1577.html>)[FineBI6.0非容器化单机工程部署支持环境及配置](<https://help.fanruan.com/finebi6.X/doc-view-1585.html>)  
[FineBI6.0非容器化集群工程部署支持环境及配置](<https://help.fanruan.com/finebi6.X/doc-view-1574.html>)  
| 根据用户并发数和服务器资源，推荐不同的工程部署推荐环境  
**2\. 单机部署**  
  
[Linux下Tomcat服务器部署包部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-2058.html>)[Windows下Tomcat服务器部署包部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-2057.html>)| 部署包内置JDK、tomcat和FineBI工程，部署成本低  
[Linux下Tomcat独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-1333.html>)[Windows下Tomcat独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-45.html>)| 用户自行准备JDK、tomcat和FineBI工程，手动部署  
**3\. 集群部署  
**  
[Linux系统手动配置非容器化FineBI6.0标准抽取集群](<https://help.fanruan.com/finebi6.X/doc-view-1969.html>)  
| 面向需要使用抽取数据的工程手动部署集群节点和集群组件，部署环境和组件要求低，无法高可用  
[Linux系统手动配置非容器化FineBI6.0高可用抽取集群](<https://help.fanruan.com/finebi6.X/doc-view-1971.html>)  
| 面向需要使用抽取数据的工程手动部署高可用集群节点和集群组件，部署环境和组件要求高，支持高可用  
[Linux系统手动配置标准直连集群](<https://help.fanruan.com/finebi6.X/doc-view-1555.html>)| 面向只使用直连数据的工程手动部署集群节点和集群组件，部署环境和组件要求低，无法高可用  
**4\. 更多部署方案**  
[Weblogic独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-46.html>)[Wildfly(JBoss)9~18独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-49.html>)  
[Wildfly(JBoss)8独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-390.html>)  
[Websphere独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-655.html>)  
[Resin独立部署非容器化FineBI6.0](<https://help.fanruan.com/finebi6.X/doc-view-665.html>)| 其他中间件下的部署方案  
**5\. 部署后操作**  
[工程注册](<https://help.fanruan.com/finebi6.X/doc-view-2177.html>)| 介绍服务器的各种注册方式用户可根据自身环境选取合适的注册方式  
[产品安全加固指导手册](<https://help.fanruan.com/finereport/doc-view-4658.html>)| 参考文档提高产品安全性  
[运维监控指导手册](<https://help.fanruan.com/finebi6.X/doc-view-1853.html>)| 参考文档提高运维稳定性  
[运维平台](<https://help.fanruan.com/fineops/doc-view-1.html>)| 建议为集群配置运维平台工具  
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：抽取集群读写分离配置](<index.php?doc-view-2279.html>)
[下一篇：FineBI版本升级简介 ![](/core/style/forward.png) ](<index.php?doc-view-276.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
