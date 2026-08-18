---
title: FineBI对接单机Redis实现状态服务
doc_id: 1561
url: https://help.fanruan.com/finebi6.X/doc-view-1561.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:41
---

> 1. 概述1.1 应用场景Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。状态服务器主要用于存储和更新应用程序的状态数据，并允许多个客户端同时访问和修改这些

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI对接单机Redis实现状态服务
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
* 历史版本：[12](<edition-list-1561.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-12-02 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。
状态服务器主要用于存储和更新应用程序的状态数据，并允许多个客户端同时访问和修改这些数据。
Redis单机作为帆软集群的状态服务器，主要用于存储缓存登录、模板锁、SessionID、WebSocket 等，对所有的访问和操作进行验证。
## 2\. 准备单机Redis
用户需要自行准备并部署单机 Redis。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅 Redis 官网获取其他帮助。请参见：[Redis 官网](<https://redis.io/>)
**如运维能力不足，推荐使用运维平台部署新项目时，勾选「部署Redis单机」即可，无需手动部署和调优。**
### 2.1 服务器建议
配置类型| 说明  
---|---  
服务器数量| 如有条件，建议Redis独占一台服务器如条件不足，至少确保有一台服务器，部署且仅部署负载均衡、状态服务器、文件服务器、外接配置库组件，该服务器中不再部署其他内容  
物理内存| 4G+  
物理内存| 8G+  
CPU| 2.5GHz以上8核16线程  
可用磁盘空间| 100G以上其中根目录可用磁盘不可小于40G  
网络要求| 1）组件和应用工程、其他集群组件建议在同一网段，避免网络波动等问题2）组件和应用工程、其他集群组件如处于公网环境，带宽需在10M以上3）组件和应用工程、其他集群组件之间需要网络畅通，互相端口可访问  
### 2.2 版本要求
  * 建议部署最新版本的 Redis
  * 支持 5.0.4 及以上版本的 Redis


### 2.3 参数调优
  * 建议修改 redis.conf 配置文件中的以下内容。  

  * 修改后需要重启 Redis 生效，启动时需要指定该配置文件，例：./redis-server /usr/redis/redis.conf

修改/新增| 说明  
---|---  
**#** bind 127.0.0.1| 指定Redis监听的IP地址注释掉，代表被禁用，否则将只接受来自本机的连接  
protected-mode **no**|  配置Redis的安全模式no代表允许外部连接，此时帆软应用才能访问Redis服务  
daemonize **yes**|  配置Redis是否以守护进程方式运行yes代表redis在后台持续运行，不受用户登录或终端关闭影响  
maxmemory **4294967296**|  配置Redis实例最大内存限制推荐配置为4294967296（单位字节，即4GB）根据实际情况和系统资源，可进行调整  
maxmemory-policy **noeviction**|  配置达到最大内存限制时的处理策略noeviction，代表Redis内存达到最大限制时，Redis不会自动清理或删除任何键来释放内存，新的写入请求将会被拒绝这个选项用于保护 Redis 实例中的重要数据不被意外删除  
requirepass **admin**123456****|  配置Redis服务的密码  
可自行将admin123456修改为你的密码  
port **7001**|  修改Redis服务占用的端口  
默认端口为6379，请修改为任意端口  
请确保端口未被占用，且可被帆软应用所在服务器访问  
pidfile **/var/run/redis_7001.pid**|  指定PID文件的路径建议根据Redis服务器占用的端口调整  
logfile "**7001.log** "| 指定Redis服务器日志文件路径将日志信息写入到名为 "7001.log" 的文件中。通过查看日志文件，可以了解 Redis 服务器的运行状态、发现潜在的问题，并采取相应的措施进行修复  
### 2.4 准备Redis信息
请准备好 Redis 的主机IP、端口、密码，用于项目接入。
信息  
| 说明  
---|---  
主机| 即Redis所在服务器的内网IP地址  
端口| 即上文redis.conf文件中的port配置值默认为6379  
密码| 即上文redis.conf文件中的requirepass配置值默认无密码  
SSL| FineBI6.1.6/FineReport11.0.33/FineDataLink4.2.2.3 及之后版本，支持 Redis6.0 的 TLS 加密通信功能如所准备的 Redis 配置了 TLS 加密通信，可勾选此项注：当 Redis 服务使用自签名证书时，客户端连接会因证书不被 Java 信任库认可而报错。请将 Redis 的证书文件(redis.crt)导入到 Java 的信任库(cacerts)中  
ACL| FineBI6.1.8/FineReport11.0.22 及之后版本，支持 Redis6.0 的权限管理功能ACL如需使用，请准备好用户名，并在配置时勾选此项注1：如需使用 ACL，请确保 Redis 用户拥有以**{TX}_lock_** 和**{TX}_rwlock_** 为前缀的 key 的操作权限，否则集群将因无法锁定状态而启动失败。注2：FineDataLink暂不支持。  
## 3\. 集群接入单机Redis
本文仅讲解如何在集群配置中，使用「腾讯云Redis」作为状态服务器。集群其他配置步骤请参见：[平台配置集群](<https://help.fanruan.com/finebi6.X/doc-view-436.html>)
在帆软应用的「管理系统>集群管理」中，可接入自备的单机Redis作为状态服务器。
1）管理员登录帆软应用，点击「管理系统>智能运维>集群管理」。  

2）开启状态服务器，缓存系统下会出现「Redis单机」下拉选项。
输入第二章准备的Redis信息，点击「测试连接并保存」，即可使用该Redis单机，作为状态服务器。
注：如非首次接入Redis，而是切换Redis状态服务器。请在切换成功后，重启帆软集群，以确保各个节点的配置缓存更新。
![](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：平台配置集群](<index.php?doc-view-436.html>)
[下一篇：FineBI对接集群Redis实现状态服务 ![](/core/style/forward.png) ](<index.php?doc-view-1966.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
