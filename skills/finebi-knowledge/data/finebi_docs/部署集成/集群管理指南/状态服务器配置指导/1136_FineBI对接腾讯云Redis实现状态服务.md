---
title: FineBI对接腾讯云Redis实现状态服务
doc_id: 1136
url: https://help.fanruan.com/finebi6.X/doc-view-1136.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:43
---

> 1. 概述1.1 应用场景Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。腾讯云数据库 Redis（TencentDB for Redis）是腾讯云打造的兼

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI对接腾讯云Redis实现状态服务
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[6](<edition-list-1136.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-04-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。
腾讯云数据库 Redis（TencentDB for Redis）是腾讯云打造的兼容 Redis 协议的缓存和存储服务，支持主从热备，提供自动容灾切换、数据备份、故障迁移、实例监控、在线扩容、数据回档等全套的数据库服务。
腾讯云Redis作为帆软集群的状态服务器，主要用于存储缓存登录、模板锁、SessionID、WebSocket 等，对所有的访问和操作进行验证。
## 2\. 使用前提
如需将帆软工程与腾讯云Redis对接，必须检查工程版本与必要插件。
### 2.1 确认帆软工程版本
管理员登录帆软系统，点击「管理系统>注册管理>版本信息」，查看工程小版本号。  

  * 请确保 FineReport 版本在11.0及以上
  * 请确保 FineBI 版本在 6.0.17 及以上
  * 不支持 FineDataLink 工程


![](/core/style/lod.png)
### 2.2 安装腾讯云Redis插件
帆软集群与腾讯云Redis的对接，依赖「腾讯云Redis」插件。
该插件需要管理员自行安装。
点击下载插件：[腾讯云 Redis 插件](<https://market.fanruan.com/plugin/9408a126-dcdb-45a5-97f3-340560cc765b>)
插件安装请参见：[插件管理](<https://help.fanruan.com/finebi6.X/doc-view-459.html>)  

![](/core/style/lod.png)
注：在使用腾讯云Redis作为状态服务器时，如卸载/禁用「腾讯云Redis」插件，可能会导致工程状态异常。
  * 负载均衡入口不可用
  * 节点访问正常
  * 状态服务器显示关闭状态


若重新配置其他类型的状态服务器，集群恢复。
若启用/重新安装「腾讯云Redis」插件，将自动连接到之前的腾讯云Redis，集群恢复。
## 3\. 准备腾讯云Redis
用户需要自行准备并部署腾讯云Redis**。**
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅腾讯云官网获取其他帮助。请参见：[云数据库 TencentDB for Redis](<https://cloud.tencent.com/product/crs>)
**如运维能力不足，推荐使用运维平台部署新项目时，勾选「部署Redis单机」即可，无需手动部署和调优。**
### 3.1 准备腾讯云Redis
对于腾讯云Redis的购买、部署、使用，帆软不提供相关资料和指导，仅对必要内容进行指明。
请查阅腾讯云官网获取其他帮助。请参见：[云数据库 TencentDB for Redis](<https://cloud.tencent.com/product/crs>)
  * 请确保腾讯云数据库 Redis 为 4.0 集群版。
  * 请确保准备的腾讯云Redis 分片数量为 1 。


### 3.2 准备Redis信息
请准备好Redis的主机IP、端口、密码，用于项目接入。
信息  
| 说明  
---|---  
主机| 在 [腾讯云 Redis 控制台](<https://console.cloud.tencent.com/redis> "https://console.cloud.tencent.com/redis") 的实例详情页面，找到「网络信息」内容，即可查看内网IPv4地址和端口![571fbaf47f5e587dff99442c5e0b002c.png](/core/style/lod.png)  
端口  
密码| 请准备腾讯云Redis的默认账号的密码即在购买并创建 Redis 实例时，设置的访问实例的密码如未配置密码，则无需准备  
## 4\. 集群接入腾讯云Redis
支持在以下情况下接入腾讯云Redis，请根据情况自行选择即可。
### 4.1 运维平台集群管理接入
在运维平台的「集群管理」中，可为项目接入自备的腾讯云Redis作为状态服务器。
1）管理员登录运维平台，选中指定项目。点击「维护>集群管理」。
2）对「状态服务器」进行配置。
![](/core/style/lod.png)
3）填写相关信息，点击「保存」，提示「测试连接成功」，即代表可正常对接。
  * 缓存系统：选择「腾讯云Redis」
  * 主机、端口、密码：填写第三章准备的Redis信息
  * ACL：请勿勾选，ACL 是 Redis6.0 的特性，腾讯云 Redis 无法使用


![](/core/style/lod.png)
### 4.2 管理系统集群管理接入
在帆软应用的「管理系统>集群管理」中，可接入自备的腾讯云Redis作为状态服务器。
1）管理员登录帆软应用，点击「管理系统>智能运维>集群管理」。  

2）开启状态服务器，缓存系统下会出现「腾讯云Redis」下拉选项。
输入第三章准备的Redis信息，点击「测试连接并保存」，即可使用腾讯云Redis作为状态服务器。
注：如非首次接入Redis，而是切换Redis状态服务器。请在切换成功后，重启帆软集群，以确保各个节点的配置缓存更新。
![](/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineBI对接哨兵Redis实现状态服务](<index.php?doc-view-1581.html>)
[下一篇：集群项目对接FTP ![](/core/style/forward.png) ](<index.php?doc-view-1564.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
