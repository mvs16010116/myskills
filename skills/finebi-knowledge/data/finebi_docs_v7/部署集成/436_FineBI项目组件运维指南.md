---
title: FineBI项目组件运维指南
doc_id: 436
url: https://help.fanruan.com/finebi/doc-view-436.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:09
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本功能变更7.0-1.2 应用场景FineBI工程，不仅仅包括了 bi 本身，还包括配套的外接配置库、集群组件、运维组件等。本文简单介绍FineBI工程可自备切

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI项目组件运维指南
[__](<doc-edit-436.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[43](<edition-list-436.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-11-11 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
7.0| -  
### 1.2 应用场景
FineBI工程，不仅仅包括了 bi 本身，还包括配套的外接配置库、集群组件、运维组件等。
本文简单介绍FineBI工程可自备切换的组件。
  
| 组件  
  
---|---  
配置存储组件| 存储FineBI各个应用节点的配置信息和参数例如权限的分配、系统中的用户、定时调度的任务详情、平台中的目录  
日志存储组件| 记录FineBI中，用户的使用动作例如谁在什么时间编辑了什么主题，谁在什么时间查看了什么目录  
数据存储组件| 存储和共享FineBI中的数据资源  
状态服务组件| 监控每个节点及整个FineBI的运行状态、记录日志和错误信息、协调节点间的通信和任务分配等  
文件存储组件| 存储和共享FineBI各个应用节点中所需的文件和资源  
帆软内网关| 
  * 提供负载转发服务，项目其他组件服务的总入口
  * 启用 HTTPS 协议，配置 SSL 证书
  * 采集网关层面的链路信息

  
## 2\. 配置存储组件
**什么是配置存储组件：存储 FineBI 各个应用节点的配置信息和参 数。例如权限的分配、系统中的用户、定时调度的任务详情、平台中的目录**
帆软应用中，管理员往往会在平台设置用户、挂载目录、分配权限、设定定时调度。这些配置，均存储于配置库中。
在正式环境下，用户可准备一个数据库，与帆软应用对接，用于配置存储。稳定的外部数据库，可确保帆软应用在高负载下的稳定运行。
更多内容请参见：[配置存储组件简介](<https://help.fanruan.com/finebi/doc-view-1080.html>)
配置存储组件类型| 支持版本  
---|---  
**普通版FineBI  
**  
[帆软对接MySQL配置库](<https://help.fanruan.com/fineops/doc-view-156.html>)  
| **MySQL5：** 5.1.73、5.5.31、5.5.46、5.5.56、5.5.62、5.6.22、5.6.28、5.6.31、5.6.35、5.6.37、5.6.44、5.7.16、5.7.23、5.7.26、5.7.33**MySQL8：** 8.0.11、8.0.16、8.0.20、8.0.21、8.2（不支持8.0.19）**RDS MySQL：** 全版本  
[帆软对接Oracle配置库](<https://help.fanruan.com/fineops/doc-view-159.html>)  
| **Oracle单机：** 10g(10.2)、10.2.0.1.0、11g(11.0.2.1)、11g(11.0.2.4)、11.0.2.4、11.2.0.2.0、12c、12c V12.2、19c**Oracle集群：** 11g、12c  
[帆软对接SqlServer配置库](<https://help.fanruan.com/fineops/doc-view-160.html>)  
| 2000、2005、2008、2012、2014、2016、2017、2019  
[帆软对接DB2配置库](<https://help.fanruan.com/fineops/doc-view-161.html>)  
| 8.2、9.7、10.5、11.1  
[帆软对接PostgreSQL配置库](<https://help.fanruan.com/fineops/doc-view-162.html>)  
| 9.2.3、9.4.7、9.5.0、9.5.2、9.6.0、13.0  
**信创版FineBI**  
[配置达梦DM8外接数据库](<https://help.fanruan.com/fineXC/doc-view-9.html>)  
| 8.0  
[配置人大金仓KingBase8外接数据库](<https://help.fanruan.com/fineXC/doc-view-13.html>)  
| 8.0  
## 3\. 日志存储组件
**什么是日志存储组件：对项目中工程、外接数据库、业务库和其他集群组件的操作请求进行采集。**
基于安全性和合规性考虑。用户在 FineBI 工程中进行的操作，都应当以日志形式记录下来。  

更多内容请参见：[日志存储组件简介](<https://help.fanruan.com/finebi/doc-view-706.html>)
日志存储组件类型| 支持版本  
---|---  
[项目对接ElasticSearch实现日志存储服务](<https://help.fanruan.com/fineops/doc-view-198.html>)  
| 8.X  
## 4\. 数据存储组件
**什么是数据存储组件：用来存储FineBI中抽取的基础表和自助数据集数据，确保每个业务节点都可以访问并使用它们**
帆软推荐用户自备支持 S3 协议的云存储文件系统作为文件服务器。
数据存储组件类型  
| 支持版本  
---|---  
[项目对接华为云OBS实现数据存储服务](<https://help.fanruan.com/fineops/doc-view-203.html>)  
| -  
[项目对接阿里云OSS实现数据存储服务](<https://help.fanruan.com/fineops/doc-view-201.html>)  
| -  
## 5\. 状态服务组件
**什么是状态服务组件：监控每个业务节点及整个项目的运行状，存储缓存登录、模板锁、SessionID、WebSocket 等，对所有的访问和操作进行验证**
状态服务组件  
| 简介  
---|---  
[FineBI对接单机Redis实现状态服务](<https://help.fanruan.com/finebi/doc-view-1561.html>)  
| Redis单机模式是Redis最简单的部署方式，只部署一个 Redis 应用使用起来也最为简单，只有主机、端口、密码三个配置项
  * 易于配置和管理，无需考虑数据的分片和集群等问题，运维成本低
  * 可能会出现单点故障，单台服务器不能实现高可用性和负载均衡

  
[FineBI对接主从模式Redis集群实现状态服务](<https://help.fanruan.com/finebi/doc-view-1966.html>)  
| Redis集群是一种基于分片的Redis部署方式，它将数据分散到多个节点中，从而可以实现横向扩展和高可用性。
  * 主节点宕机后，对应从节点会被选举为新的主节点
  * 所有指向原主节点的客户端会被通知新的主节点的地址
  * 新的主节点会从其他从节点同步数据，以确保数据的一致性

  
[FineBI对接哨兵模式Redis集群实现状态服务](<https://help.fanruan.com/finebi/doc-view-1581.html>)  
| 相比于主从模式的Redis集群，哨兵模式是一种更加高可用的解决方案同时存在主节点、从节点和哨兵节点哨兵模式Redis集群对资源的要求比较多，运维成本也会更高  
[FineBI对接腾讯云Redis实现状态服务](<https://help.fanruan.com/finebi/doc-view-1136.html>)  
| 腾讯云数据库 Redis（TencentDB for Redis）是腾讯云打造的兼容 Redis 协议的缓存和存储服务支持主从热备，提供自动容灾切换、数据备份、故障迁移、实例监控、在线扩容、数据回档等全套的数据库服务  
## 6\. 文件存储组件
**什么是文件存储组件：用于存储和共享集群中所需的文件和数据资源，以确保每个节点都可以访问并使用它们**
**包括：assets、reportlets、reportlets_versions、resources、schedule、treasures、../backup 等文件夹**
注：**「节点间自动同步」不适用于运维平台部署的FineBI7.0集群。** 该功能只适用于历史已配置该项的集群工程，不再提供相关配置指导。
文档| 说明  
---|---  
[FineBI对接SFTP实现文件服务](<https://help.fanruan.com/finebi/doc-view-1567.html>)  
| SFTP是一种通过SSH协议进行加密的文件传输协议，部署简单，是Linux系统自带的，相对于FTP而言更加安全和稳定。  
[FineBI对接NAS实现文件服务](<https://help.fanruan.com/finebi/doc-view-1580.html>)  
| NAS是一种文件级别的存储设备，通过标准网络协议（如SMB/CIFS、NFS）进行文件存取，适合需要集中管理文件、备份和共享的大型组织。一个NAS文件系统，可以同时挂载到多个节点上，由这些节点共享访问，从而节约大量拷贝与同步成本。  
[FineBI对接阿里云OSS实现文件服务](<https://help.fanruan.com/finebi/doc-view-1270.html>)  
| 手动搭建本地 HDFS 文件系统，对于用户的运维能力要求过高，但用户又希望使用高可用的文件服务器。通过「S3 资源仓库」插件，帆软集群可对接支持 S3 协议的云存储文件系统作为文件服务器。支持的云存储文件系统包括：阿里云OSS、华为云OBS 、亚马逊云S3。其他自行搭建的 S3 平台不确保支持。  
[FineBI对接华为云OBS实现文件服务](<https://help.fanruan.com/finebi/doc-view-2676.html>)  
  
[FineBI对接MinIO实现文件服务](<https://help.fanruan.com/finebi/doc-view-2021.html>)  
| MinIO是一个灵活而强大的对象存储服务器，旨在提供高性能、可扩展和易于部署的分布式存储系统。MinIO使用的是S3协议，有着独特的文件存储逻辑。请勿直接使用FileZilla等FTP工具连接MinIO，进行文件的上传/下载。请通过浏览器访问MinIO服务器的地址，然后使用提供的Web界面进行文件的上传和下载。  
[FineBI对接FTP实现文件服务](<https://help.fanruan.com/finebi/doc-view-1564.html>)  
| FTP（File Transfer Protocol）是一种用于在计算机网络之间传输文件的标准协议，被大多数操作系统和 FTP 客户端支持，方便用户进行文件传输。注：FTP传输的数据和命令都是明文的，容易被窃听和篡改。推荐使用更安全的 SFTP 协议  
[FineBI对接HDFS实现文件服务](<https://help.fanruan.com/finebi/doc-view-1234.html>)| HDFS 作为文件服务器，可以保证模板等资源文件分布式存储，实现高可用  
## 7\. 负载均衡组件
运维平台部署的FineBI7.0项目，默认安装一个帆软内网关组件。
**作用：**
  * 提供负载转发服务，项目其他组件服务的入口
  * 启用 HTTPS 协议，配置 SSL 证书
  * 采集网关层面的链路信息


**说明：**  

支持安装单节点内网关/双节点内网关。
请注意，此处的双节点内网关，并非集群nginx，而是两个独立的nginx节点，当一个nginx宕机后，用户可通过另一个nginx访问项目
**注意：**
帆软内网关服务，对帆软业务进行了定制调整，以均衡的分发用户请求，提升性能，**因此不支持自备，不支持进行自定义修改**
如需使用F5、SLB、ELB等其他类型的负载均衡网关，可以自行配置转发，让客户端请求转发到自备网关，再转发到帆软项目内网关，再分发到各个应用节点上，帆软不提供相关配置指导。
## 8\. 其他集群配置说明
### 8.1 MQ内置
运维平台部署的项目，可能配置了 rocketmq 组件，rocketmq可替换状态服务组件 Redis 消息队列的一部分功能。
  * 若未配置rocketmq，默认使用redis。
  * 若配置了rocketmq，rocketmq和redis同时生效，负责不同功能。


![](https://help.fanruan.com/core/style/lod.png)
### 8.2 缓存模式
缓存，用于存储集群文件服务器中的高频访问资源文件，用于加速数据读取，减少重复 I/O 开销。
缓存的资源文件包括：reportlets 、resources 、assets 等文件夹
支持两种缓存模式：被动缓存和关闭缓存
  * 被动缓存：仅缓存已请求过的资源文件，命中缓存时直接返回；未命中时读取文件并更新缓存。适用于读多写少的正式环境。
  * 关闭缓存：每次请求均重新读取原始资源文件。适用于需要实时同步资源文件的开发环境，或对准确性要求极高的正式环境。


注：帆软不提供主动缓存，避免不必要的缓存占用。
![](https://help.fanruan.com/core/style/lod.png)
### 8.3 通信协议
TCP 和 UDP 是常用的网络传输协议，默认选用 TCP 协议。 
  * TCP：传输控制协议，是一种面向连接的协议，提供可靠的数据传输，适用于需要保证数据完整性和顺序的场景
  * UDP：用户数据报协议，是一种无连接的协议，提供较低的延迟和较少的开销，适用于对速度要求高且可以容忍部分数据丢失的场景


切换集群通信协议后，需要通过「运维平台>维护>组件管理」功能重启bi-web组件，方可生效。
![1612271382809171.png](https://help.fanruan.com/core/style/lod.png)
注1：阿里云、AWS 等云服务器不允许 UDP 组播方式，集群通信协议请选择 TCP。
注2：如果开启集群后只显示本工程的节点，说明所选通信协议无法生效。请更换集群通信协议，并重启bi-web组件。
![](https://help.fanruan.com/core/style/lod.png)
## 9\. 管理集群节点
### 9.1 开启集群
**FineBI7.0默认开启集群，且由于FineBI7.0采用存算分离架构，请切勿关闭集群。**
满足以下条件即可开启集群。
1）请确保配置了第二章外接配置库，不支持使用历史的内置配置库的情况下开启集群  

2）请确保配置了第五章状态服务器，不支持未对接状态服务的情况下开启集群
3）请确保第六章文件一致设置选择了「文件服务器共享」，不支持在「节点间同步」模式下开启集群
![](https://help.fanruan.com/core/style/lod.png)
### 9.2 节点管理
开启集群后，通过「运维平台>维护>组件管理」功能重启bi-web组件，可在「节点管理」界面查看到全部接入集群的bi-web服务。
**1）扩容bi-web服务数量**
如需增加bi-web服务，请使用运维平台实现，详情请参见：[集群项目扩容组件数量](<https://help.fanruan.com/fineops/doc-view-81.html>)
**2）修改节点信息**
不建议用户修改相关节点信息，对于运维平台部署的帆软应用，集群开启后可自动识别相关信息，无需手动修改。
**3） 节点异常提示**
节点与非协调者通信异常则会标红，请根据提示进行修复。
**4）刷新缓存**
如集群文件一致设置选择「文件服务器共享」，且缓存模式选择「被动缓存」，节点管理界面会出现「刷新缓存」的按钮。
当手动在文件服务器下增删改资源文件时，缓存层是无法感知到的，此时即可通过「刷新缓存」按钮手动清空缓存，确保获取最新资源文件
![](https://help.fanruan.com/core/style/lod.png)
## 10\. 设置集群异常提醒
开启「集群异常提醒」功能，可以在集群发生异常时及时提醒运维人员。
管理员登录FineBI系统，点击「管理系统>智能运维>集群配置>全局设置」。
支持设置多种集群异常提醒方式：「短信提醒」、「平台消息」、「邮件提醒」，设置完成后点击保存即可。
  * 如需使用短信提醒，需要先开启短信平台，详细点击 [短信](<https://help.fanruan.com/finebi6.0/doc-view-904.html>)
  * 如需使用邮件提醒，需要先配置邮件服务器，详细点击 [邮箱  
](<https://help.fanruan.com/finebi6.0/doc-view-1257.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI企业版部署指南](<index.php?doc-view-2108.html>)
[下一篇：FineBI版本升级简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-276.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
