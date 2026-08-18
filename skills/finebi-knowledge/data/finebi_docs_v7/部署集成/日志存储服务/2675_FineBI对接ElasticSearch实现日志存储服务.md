---
title: FineBI对接ElasticSearch实现日志存储服务
doc_id: 2675
url: https://help.fanruan.com/finebi/doc-view-2675.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:30
version: "7.X"
---

> 提示：本文仅面向运维平台部署的 FineBI7.0 。1. 概述Elasticsearch 是一个分布式、开源的搜索和分析引擎，能够以近实时的方式处理海量数据的存储、检索和分析。Elasticsearc

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接ElasticSearch实现日志存储服务
[__](<doc-edit-2675.html>)
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[2](<edition-list-2675.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-12-16 
[](<javascript:;>) [](<javascript:>)
![icon](https://help.fanruan.com/core/style/lod.png)**提示：**本文仅面向运维平台部署的 FineBI7.0 。****
  

## 1\. 概述
Elasticsearch 是一个分布式、开源的搜索和分析引擎，能够以近实时的方式处理海量数据的存储、检索和分析。
Elasticsearch 凭借其灵活性、扩展性和高性能，逐渐成为日志管理、监控、安全分析等领域的核心工具。
对于运维平台部署的帆软项目，支持对接ElasticSearch组件作为日志存储，对项目中工程、外接数据库、业务库和其他集群组件的请求进行采集。
本文讲解帆软项目如何对接ElasticSearch，作为日志服务：
  * 用户可**自行准备一个ElasticSearch** ，并进行参数调优
  * 在部署新项目/项目部署好后，可将项目与该日志服务对接


## 2\. 确认帆软项目
### 2.1 使用前须知
**1）数据连接日志库**  

在使用 ElasticSearch 作为日志服务后，如需连接日志库取数分析。
  * 优先推荐使用 FineDataLink 连接 ElasticSearch 进行取数分析，详情请参见：[配置Elasticsearch数据源](<https://help.fanruan.com/finedatalink/doc-view-756.html>)
  * 如需通过 [数据连接](<https://help.fanruan.com/finereport/doc-view-891.html>) 方式在 FineBI 中查看操作日志，需要依赖插件，请联系帆软技术支持获取。技术支持联系方式：「[服务](<https://service.fanruan.com/>)>在线支持」


**2）日志记录连续性**
为了确保日志记录不发生中断，请确保以下几点：
  * 请勿暂停ElasticSearch，否则可能会导致项目操作日志丢失。对于自备ElasticSearch，建议配置为**开机自启动**
  * 请勿停用/卸载「管理系统>插件管理>我的插件」中，默认安装的「logdb的ElasticSearch实现」插件


**3）历史日志迁移**
对于历史非运维平台部署的项目，在升级/迁移为运维平台部署后，如将日志服务从Swift更改为ElasticSearch，历史日志无法自动迁移。
  * 如有备份要求，请在迁移前，使用 [平台日志同步到其他数据库插件](<https://help.fanruan.com/finereport/doc-view-3609.html>) ，将历史日志导出到自备的相关数据库中。
  * 如有合并要求，请联系帆软技术支持获取相关帮助。技术支持联系方式：「[服务](<https://service.fanruan.com/>)>在线支持」


### 2.2 确认安装插件
帆软项目与**ElasticSearch** 的对接，依赖「logdb的ElasticSearch实现」插件。运维平台部署的项目，默认已安装该插件。
管理员登录帆软应用，点击「管理系统>插件管理>我的插件」，可查看是否正常启用「logdb的ElasticSearch实现」插件。
如已卸载，需要重新安装，插件获取请联系技术支持。技术支持联系方式：「[服务平台](<https://service.fanruan.com/>)>在线支持」、电话「400-811-8890」
插件安装方法参照： [插件管理](<https://help.fanruan.com/finebi/doc-view-459.html>)
注：V2.29.0及之后版本的运维平台，对接或部署的帆软项目，内置的「logdb的ElasticSearch实现」插件版本在V1.0.17及以上，支持上传SSL连接证书和查看ElasticSearch接入状态。
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 准备ElasticSearch
用户需要自行准备并部署ElasticSearch**。**
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅相关官网获取其他帮助。
**如运维能力不足，推荐使用运维平台部署新项目时，**在「日志服务」中勾选「部署ElasticSearch」即可** ，无需手动部署和调优。**
### 3.1 ElasticSearch要求
要求  
| 说明  
---|---  
版本要求| 对于用户自备的ElasticSearch，仅支持**8.X 版本**  
运行要求| 部署/对接成功后，请勿暂停ElasticSearch，否则可能会导致项目操作日志丢失因此建议为ElasticSearch服务配置**开机自启动**  
防火墙端口| 请确保帆软项目所在服务器，与ElasticSearch服务所在机器和端口内网互通  
### 3.2 ElasticSearch信息
请准备好以下ElasticSearch信息
信息  
| 说明  
---|---  
链接地址| ElasticSearch的访问地址，形如：http://IP:port默认端口为9200  
用户名| ElasticSearch用户名默认用户名为elastic  
密码| ElasticSearch用户的密码  
SSL连接证书| 如ElasticSearch配置了https，可上传证书证书请自行准备，帆软不提供相关指导  
## 4\. 项目接入ElasticSearch服务
支持在以下情况下接入 ElasticSearch 作为日志服务，请根据情况自行选择，任选其一即可。
### 4.1 部署新项目时接入
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的 ElasticSearch 作为项目日志服务。
1）日志服务选择「对接已有日志服务」。
2）在「日志服务」信息填写处，填写3.2节准备的**ElasticSearch信息** 。
3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 4.2 运维平台集群管理接入
项目部署成功后，在运维平台的「集群管理」中，可为项目接入自备的ElasticSearch作为日志服务。
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「日志服务器」进行配置。
3）填写3.2节准备的ElasticSearch信息。
4）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
5）切换至「组件管理」，重启工程组件，以使ElasticSearch作为文件服务生效。
![](https://help.fanruan.com/core/style/lod.png)
### 4.3 管理系统接入
在帆软应用的「管理系统>系统管理>常规」中，可为项目接入自备的ElasticSearch作为日志服务。
1）管理员登录帆软应用，点击「管理系统>系统管理>常规」。
2）在「ElasticSearch连接配置」中，填写3.2节准备的ElasticSearch信息。
3）点击「保存」按钮，等待当前接入状态为「已连接」，即代表ElasticSearch作为文件服务生效。
注1：V2.29.0及之后版本的运维平台，对接或部署的帆软项目，内置的「logdb的ElasticSearch实现」插件版本在V1.0.17及以上，支持上传SSL连接证书和查看ElasticSearch接入状态。
注2：如ElasticSearch配置了https，可上传证书。证书请自行准备，帆软不提供相关指导。
![](https://help.fanruan.com/core/style/lod.png)
4）前往运维平台，选择指定项目，点击「维护>组件管理」，重启工程组件，以使ElasticSearch作为文件服务生效。
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：日志存储组件简介](<index.php?doc-view-706.html>)
[下一篇：日志库表结构 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1134.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
