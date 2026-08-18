---
title: FineBI对接哨兵Redis实现状态服务
doc_id: 1581
url: https://help.fanruan.com/finebi6.X/doc-view-1581.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:42
---

> 1. 概述1.1 应用场景Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。相比于集群模式模式的Redis，哨兵模式是一种更加高可用的解决方案，同时存在主节点

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI对接哨兵Redis实现状态服务
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
* 历史版本：[13](<edition-list-1581.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-12-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
Redis是一种快速、灵活和可靠的键值存储数据库，适合处理高性能、实时和高并发的数据访问场景。
相比于集群模式模式的Redis，哨兵模式是一种更加高可用的解决方案，同时存在主节点、从节点和哨兵节点。
哨兵模式Redis作为帆软高可用集群的状态服务器，主要用于存储缓存登录、模板锁、SessionID、WebSocket 等，对所有的访问和操作进行验证。
节点  
| 作用| 数量  
---|---|---  
主节点（Master）| 负责处理写操作将数据复制到从节点| 1  
从节点（Slave）| 负责处理读操作从主节点复制数据在主节点失效时可以提升为新的主节点| ≥1  
哨兵节点（Sentinel）| 负责监控主节点与从节点的状态在主节点失效时进行自动故障转移需要至少三个哨兵节点以确保高可用性和正确的故障转移投票机制| ≥3的奇数  
  
### 1.2 功能简介
本文主要讲解帆软集群与哨兵模式Redis的对接：
  * **用户可自行准备一个 哨兵模式Redis**，并进行参数调优****
  * 在项目部署好后，可将集群项目与该Redis对接


## 2\. 准备哨兵模式Redis
用户需要自行准备并部署哨兵模式Redis**。**
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅 Redis 官网获取其他帮助。请参见：[Redis 教程](<https://redis.io/topics/cluster-tutorial>)
**如运维能力不足，推荐使用运维平台部署新项目时，勾选「部署Redis单机」即可，无需手动部署和调优。**
### 2.1 服务器建议
哨兵模式Redis对资源的要求比较多，运维成本也会更高。
下表列出每个服务器的配置建议：
配置类型| 说明  
---|---  
服务器数量| 请根据「主节点+从节点+哨兵节点」的节点数量准备服务器个数
  * 主节点数量为1
  * 从节点数量≥1
  * 哨兵节点数量为奇数，至少大于3

哨兵节点数量越多，系统的容错能力越强，但同时也会增加管理和通信的开销
  * 如有条件，建议每个Redis节点独占一台服务器
  * 如条件不足，至少确保所用服务器，部署且仅部署负载均衡、状态服务器、文件服务器、外接配置库组件，不再部署其他内容

  
物理内存| 8G+  
CPU| 2.5GHz以上8核16线程  
可用磁盘空间| 100G以上其中根目录可用磁盘不可小于40G  
网络要求| 1）组件和应用工程、其他集群组件建议在同一网段，避免网络波动等问题2）组件和应用工程、其他集群组件如处于公网环境，带宽需在10M以上3）组件和应用工程、其他集群组件之间需要网络畅通，互相端口可访问  
### 2.2 版本要求
  * 建议部署最新版本的 Redis
  * 支持 5.0.4 及以上版本的 Redis


### 2.3 参数调优
下文以一个「1主2从3哨兵」的哨兵模式Redis为例，讲述必要的配置内容调整。
（仅列出帆软所需内容，其他部分请自行调整）  

节点类型  
| 地址  
---|---  
主节点| 服务器：192.168.101.91端口：7001  
从节点| 服务器：192.168.101.92端口：7002| 服务器：192.168.101.93端口：7003  
哨兵节点| 服务器：192.168.101.94端口：27004| 服务器：192.168.101.95端口：27005| 服务器：192.168.101.96端口：27006  
**1）主节点配置redis.conf**
  * 建议修改 Redis 主节点的 redis.conf 配置文件中的以下内容。  

  * 修改后需要重启 Redis节点 生效，启动时需要指定新的配置文件，例：./redis-server /home/redis/redis.conf
  * 表格中的端口和密码等配置，请按照实际情况调整

修改/新增| 说明  
---|---  
**#** bind 127.0.0.1| 指定Redis监听的IP地址注释掉，代表被禁用，否则将只接受来自本机的连接  
protected-mode **no**|  配置Redis的安全模式no代表允许外部连接，此时帆软应用才能访问Redis服务  
daemonize **yes**|  配置Redis是否以守护进程方式运行yes代表redis在后台持续运行，不受用户登录或终端关闭影响  
maxmemory **2147483648**|  配置Redis实例最大内存限制推荐配置为2147483648（单位字节，即2GB）根据实际情况和系统资源，可进行调整  
maxmemory-policy **noeviction**|  配置达到最大内存限制时的处理策略noeviction，代表Redis内存达到最大限制时，Redis不会自动清理或删除任何键来释放内存，新的写入请求将会被拒绝这个选项用于保护 Redis 实例中的重要数据不被意外删除  
requirepass **admin**123456****|  配置Redis主节点的访问密码，可自行修改请确保各个Redis主节点、从节点的任何密码，**完全一致，否则无法与帆软应用对接**  
port **7001**|  修改Redis服务占用的端口  
默认端口为6379，请修改为任意端口  
请确保端口未被占用，且可被帆软应用所在服务器访问  
pidfile **/var/run/redis_7001.pid**|  指定PID文件的路径建议根据Redis服务器占用的端口调整  
logfile "**7001.log** "| 指定Redis服务器日志文件路径将日志信息写入到名为 "7001.log" 的文件中。通过查看日志文件，可以了解 Redis 服务器的运行状态、发现潜在的问题，并采取相应的措施进行修复  
dbfilename **7001dump.rdb**|  指定RDB（Redis DataBase）快照文件的名称当Redis进行持久化时，将内存中的数据快照保存到该文件建议根据Redis服务器占用的端口调整文件名  
appendfilename **"7001appendonly.aof"**|  指定AOF（Append Only File）文件的名称当Redis使用AOF进行持久化时，将所有的写操作日志写入该文件建议根据Redis服务器占用的端口调整文件名  
cluster-enabled **no**|  确认是否启用Redis集群模式no代表Redis不以集群模式运行，否则哨兵将无法正常工作  
**2）从节点配置redis.conf**  

  * 建议修改 Redis 从节点的 redis.conf 配置文件中的以下内容。  

  * 修改后需要重启 Redis节点 生效，启动时需要指定新的配置文件，例：./redis-server /home/redis/redis.conf
  * 表格中的端口和密码等配置，请按照实际情况调整

修改/新增| 说明  
---|---  
**#** bind 127.0.0.1| 指定Redis监听的IP地址注释掉，代表被禁用，否则将只接受来自本机的连接  
protected-mode **no**|  配置Redis的安全模式no代表允许外部连接，此时帆软应用才能访问Redis服务  
daemonize **yes**|  配置Redis是否以守护进程方式运行yes代表redis在后台持续运行，不受用户登录或终端关闭影响  
maxmemory **2147483648**|  配置Redis实例最大内存限制推荐配置为2147483648（单位字节，即2GB）根据实际情况和系统资源，可进行调整  
maxmemory-policy **noeviction**|  配置达到最大内存限制时的处理策略noeviction，代表Redis内存达到最大限制时，Redis不会自动清理或删除任何键来释放内存，新的写入请求将会被拒绝这个选项用于保护 Redis 实例中的重要数据不被意外删除  
requirepass **admin**123456****|  配置Redis从节点的访问密码，可自行修改请确保各个Redis主节点、从节点的任何密码，**完全一致，否则无法与帆软应用对接**  
port **7002**|  修改Redis服务占用的端口  
默认端口为6379，请修改为任意端口  
请确保端口未被占用，且可被帆软应用所在服务器访问  
pidfile **/var/run/redis_7002.pid**|  指定PID文件的路径建议根据Redis服务器占用的端口调整  
logfile "**7001.log** "| 指定Redis服务器日志文件路径将日志信息写入到名为 "7001.log" 的文件中。通过查看日志文件，可以了解 Redis 服务器的运行状态、发现潜在的问题，并采取相应的措施进行修复  
dbfilename **7001dump.rdb**|  指定RDB（Redis DataBase）快照文件的名称当Redis进行持久化时，将内存中的数据快照保存到该文件建议根据Redis服务器占用的端口调整文件名  
appendfilename **"7001appendonly.aof"**|  指定AOF（Append Only File）文件的名称当Redis使用AOF进行持久化时，将所有的写操作日志写入该文件建议根据Redis服务器占用的端口调整文件名  
cluster-enabled **no**|  确认是否启用Redis集群模式no代表Redis不以集群模式运行，否则哨兵将无法正常工作  
replicaof **192.168.101.91 7001**|  输入主节点的IP和端口  
请将IP与端口自行调整  
masterauth **admin123456**|  输入主节点的requirepass请确保各个Redis主节点、从节点的任何密码，**完全一致，否则无法与帆软应用对接**  
  
**3）哨兵节点配置sentinel.conf**
  * 建议修改各个 Redis 哨兵节点的 sentinel.conf 配置文件中的以下内容。
  * 请切勿配置Redis哨兵节点的访问密码！！！否则无法与帆软应用对接
  * 修改后需要重启哨兵节点生效，启动时需要指定新的配置文件，例：redis-sentinel /home/redis/sentinel.conf
  * 表格中的端口等配置，请按照实际情况调整

修改/新增| 说明  
---|---  
**#** bind 127.0.0.1| 指定哨兵监听的IP地址注释掉，代表被禁用，否则将只接受来自本机的连接  
protected-mode **no**|  配置哨兵的安全模式no代表允许外部连接，此时帆软应用才能访问Redis服务  
port **27004**|  指定哨兵监听的端口默认是26379，请修改为任意端口  
请确保端口未被占用，且可被帆软应用所在服务器访问  
dir **/tmp/redis**|  指定哨兵数据保存的目录  
logfile **/home/redis/sentinel.log**|  指定哨兵日志文件生成路径  
sentinel monitor **mymaster 192.168.101.91 7001 2**|  监控主节点格式：sentinel monitor <master-name> <ip> <port> <quorum>
  * <master-name>：主节点的自定义名称，只能由字母A-Z、数字0-9 、字符".-_"组成
  * <ip>：主节点的IP地址
  * <port>：主节点的端口号
  * <quorum>：判断主节点失效所需的最少哨兵数量

  
sentinel auth-pass **mymaster admin123456**|  配置主节点的身份验证密码格式：sentinel auth-pass <master-name> <password>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <password>：输入主节点的requirepass。请确保各个Redis主节点、从节点的任何密码，**完全一致，否则无法与帆软应用对接**

  
sentinel down-after-milliseconds **mymaster 5000**|  判断主节点失效所需的时间当超过配置时间，无法连接主服务器，哨兵节点将判定主Redis失效格式：sentinel down-after-milliseconds <master-name> <time>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <time>：判断主节点失效所需的时间，单位毫秒

  
sentinel failover-timeout **mymaster 60000**|  指定从节点选举为新主节点的超时时间格式：sentinel failover-timeout <master-name> <milliseconds>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <milliseconds>：从节点选举为新主节点的超时时间，单位毫秒

  
sentinel notification-script **mymaster /home/redis/notification.sh**|  指定配置通知脚本的路径格式：sentinel notification-script <master-name> <script-path>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <script-path>：当主节点状态变化时，哨兵节点会执行的脚本路径

  
sentinel client-reconfig-script **mymaster**/home/redis** /reconfig.sh**| 指定配置客户端重定向脚本的路径格式：sentinel client-reconfig-script <master-name> <script-path>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <script-path>：当主从切换完成后，哨兵节点会执行的脚本路径，用于通知客户端新的主节点地址

  
sentinel parallel-syncs **mymaster 1**|  配置从节点参数格式：sentinel parallel-syncs <master-name> <number>
  * <master-name>：主节点的名字（和监控配置中的名字一致）
  * <number>：同时向主节点同步的从节点数目

  
### 2.4 准备Redis信息
请准备好Redis的主机IP、端口、密码，用于项目接入。
信息  
| 说明  
---|---  
密码| 即上文redis.conf和sentinel.conf文件中的<requirepass>配置值请确保各个Redis主节点、从节点的任何密码，**完全一致，否则无法与帆软应用对接** 请确保Redis哨兵节点**未设置密码** ，否则无法与帆软应用对接  
主节点名| 即上文sentinel.conf文件中的<master-name>配置值  
主机| 准备所有节点的服务器IP、port（包括主节点、从节点、哨兵节点）如只输入一个哨兵节点的主机和端口，虽然能自动获取Redis所有节点，但当该哨兵节点宕机后，无法获取其他节点的状态  
端口  
ACL| FineReport 11.0.22 / FineBI 6.1.8 及之后版本支持 Redis6.0 的权限管理功能ACL如需使用，请准备好用户名，并在配置时勾选此项注1：如需使用 ACL，请确保 Redis 用户拥有以**{TX}_lock_** 和**{TX}_rwlock_** 为前缀的 key 的操作权限，否则帆软集群将因无法锁定状态而启动失败。注2：FineDataLink暂不支持。  
## 3\. 集群接入哨兵Redis
支持在以下情况下接入哨兵模式Redis，请根据情况自行选择即可。
注：FineReport11.0.12 / FineBI6.0.7 以下版本项目，与 Redis 哨兵对接，依赖 [Redis哨兵模式](<https://market.fanruan.com/plugin/1db2d8f7-4729-4570-958e-dac8f0f5aa3f>) 插件，该插件默认安装。
如插件被删除，则无法对接。如已对接时删除/禁用该插件，尽管工程可以正常登录，但无法确保业务完全正常。
请在帆软应用「管理系统>插件管理」中安装/启用 V1.0.5 及以上版本的Redis哨兵模式插件。  

### 3.1 运维平台集群管理接入
在运维平台的「集群管理」中，可为项目接入自备的哨兵模式Redis作为状态服务器。
1）管理员登录运维平台，选中指定项目。点击「维护>集群管理」。
2）对「状态服务器」进行配置。
![](/core/style/lod.png)
3）填写相关信息，点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
  * 缓存系统：选择「Redis哨兵」
  * 密码：填写第二章准备的密码  

  * 主机、端口：填写第二章准备的所有节点的IP、port信息
  * ACL：按需选择，填写第二章准备的信息


![](/core/style/lod.png)
### 3.2 管理系统集群管理接入
注：仅非运维平台部署的帆软项目， 可通过管理系统修改集群配置。运维平台部署的帆软项目请勿使用本节方案。
在帆软应用的「管理系统>集群管理」中，可接入自备的哨兵模式Redis作为状态服务器。
1）管理员登录帆软应用，点击「管理系统>智能运维>集群配置」。  

2）开启状态服务器，点击「编辑」填写相关信息，点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
  * 缓存系统：选择「Redis哨兵」
  * 密码：填写第二章准备的密码  

  * 主机、端口：填写第二章准备的所有节点的IP、port信息
  * ACL：按需选择，填写第二章准备的信息


注：如非首次接入Redis，而是切换Redis状态服务器。请在切换成功后，重启帆软集群，以确保各个节点的配置缓存更新。
![](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineBI对接集群Redis实现状态服务](<index.php?doc-view-1966.html>)
[下一篇：FineBI对接腾讯云Redis实现状态服务 ![](/core/style/forward.png) ](<index.php?doc-view-1136.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
