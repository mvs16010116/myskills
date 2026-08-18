---
title: Windows系统搭建Web集群
doc_id: 1571
url: https://help.fanruan.com/finebi6.X/doc-view-1571.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:55
---

> 1. 概述本文介绍如何在 Windows 系统中配置集群。注：相比于Windows系统，Linux在稳定性、安全性、可定制性和可靠性等方面的优势，使得它成为推荐的最佳选择。因此推荐在Linux系统部署F

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统搭建Web集群
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[11](<edition-list-1571.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-11-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍如何在 Windows 系统中配置集群。
注：
相比于Windows系统，Linux在稳定性、安全性、可定制性和可靠性等方面的优势，使得它成为推荐的最佳选择。
因此推荐在Linux系统部署FineBI正式工程：[Linux系统手动配置标准抽取集群](<https://help.fanruan.com/finebi6.X/doc-view-1969.html>)
## 2\. 操作步骤
### 2.1 基础环境准备
部署集群之前，请确保已准备好集群工程所需的环境：[Web集群环境准备](<https://help.fanruan.com/finebi6.0/doc-view-1574.html>)
注： WebLogic 单机集群和 WebLogic 双机集群是 WebLogic 自身的集群，非帆软集群方案，不推荐使用。
### 2.2 部署 FineBI 工程
各集群节点服务器中，将 FineBI 工程部署到容器中。
部署容器介绍如下表所示：  

部署容器| 推荐版本| 已验证版本| 参考文档  
---|---|---|---  
Tomcat| Tomcat8.x、Tomcat9.x注：不支持 Tomcat 8.0.32 版本| Tomcat8.0、Tomcat8.5、Tomcat9.0| [Windows下Tomcat服务器独立部署](<https://help.fanruan.com/finebi6.0/doc-view-45.html>)  
WebLogic| WebLogic 12.2.1.*及以上| WebLogic 12.2.1.3.0| [Weblogic服务器部署](<https://help.fanruan.com/finebi6.0/doc-view-46.html>)  
### 2.3 配置外接数据库
选择某个节点上的工程作为主节点工程，配置外接数据库。
外接数据库支持的类型及版本如下表所示：
数据库类型 |  支持数据库版本| 配置方法  
---|---|---  
MySQL| 5.1.73、5.5.31、5.5.46、5.5.56、5.6.22、5.6.31、5.7.16| [配置MySQL5外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-1248.html>)  
SQL Server| 2000、2005、2008、2012、2014、2016| [配置SQL Server外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-1251.html>)  
  
Oracle| 10g、11g、12c| [配置Oracle外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-1250.html>)  
DB2| 9.7、8.2、11.1| [配置DB2外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-1252.html>)  
  
### 2.4 安装配置集群组件
#### 2.4.1 安装配置文件服务器并启动
在不开启文件服务器的时候，会默认使用节点间同步的方式保证集群的文件一致性，不过当节点之间存在网络通信问题时，节点间有可能会出现同步延迟的问题。
对于 Windows 集群来说，手动修改某个节点上的文件，无法及时同步到其他节点，建议通过远程设计而避免直接操作节点文件。
为了避免出现此类问题，建议使用文件服务器：[Windows 系统配置 FTP 服务](<https://help.fanruan.com/finebi6.0/doc-view-1562.html>)
注：「节点间自动同步」不适用于多节点，否则会因节点间通信问题影响使用，仅两个节点时使用，大于两个节点时需使用「文件服务器」。
#### 2.4.2 安装配置状态服务器并启动
状态服务器支持 Redis 单机和 Redis 集群两种方案，Redis 集群相比单机模式可以保证状态服务器的高可用，不过对服务器资源有一定要求，并且会增加运维成本，请自行选择。
Redis 单机：[Windows 系统安装配置单机 Redis](<https://help.fanruan.com/finebi6.0/doc-view-1557.html>)
Redis 集群：帆软官方暂未测试在 Windows 系统下部署 Redis 集群。
#### 2.4.3 安装配置负载均衡并启动
负载均衡是集群方案中不可缺少，且独立于工程的一部分。若具备运维能力，可自行选择合适的软硬件负载均衡，目前有客户使用的负载均衡包括 treafik、 Nginx、F5、AWS ELB、NetScaler，帆软的基础方案基于 treafik，对于非 treafik 的负载均衡，须自行操作配置，参考文档：[负载均衡配置指导](<https://help.fanruan.com/finebi6.0/doc-view-1964.html>)
【推荐】Treafik：[Windows系统安装配置Treafik](<https://help.fanruan.com/finebi6.0/doc-view-1584.html>)
Nginx：[Windows系统安装配置Nginx](<https://help.fanruan.com/finebi6.0/doc-view-1534.html>)
注：Nginx 作为负载均衡在 Linux 系统上具备很好的并发性能，并且占用极小的内存。但是在 Windows 系统上并不支撑较高并发，所以在 Windows 系统上选用 Nginx 作为负载均衡，需要考虑并发情况，若并发需求低于 300，部署集群仅以热备为目的，则可选用 Nginx 作为负载均衡，若并发需求超过 300，则不建议使用 Nginx，须换用其他负载均衡。
### 2.5 平台配置集群
主节点工程参考 [平台配置集群](<https://help.fanruan.com/finebi6.0/doc-view-436.html>) 文档配置集群，当第一个节点出现后，将第一个节点的工程包（webroot）拷贝到其他服务器下，然后启动这些服务器，新的节点就会加入节点管理中。
注：使用 [本地机器信息认证方式 ](<https://help.fanruan.com/finebi6.0/doc-view-188.html>)注册的集群工程，增加节点后需要重新对集群工程进行注册。
## 3\. 注意事项
### 3.1 更换 FTP 路径
**问题描述**  

集群工程搭建好后，由于磁盘空间不足需要更换 FTP 文件服务器路径。
**解决方案**
1）把原路径下的所有文件都拷贝到新的目录下，并给新文件夹赋权限。详情请参见：[Linux 系统安装配置 FTP](<https://help.fanruan.com/finebi6.0/doc-view-1564.html>)、[Windows 系统配置 FTP 服务](<https://help.fanruan.com/finebi6.0/doc-view-1562.html>)  
2）修改平台上的文件服务器路径并保存。
3）重启集群的每一个节点，重启集群工程注意事项请参见：[配置开启集群](<https://help.fanruan.com/finebi6.0/doc-view-436.html>) 文档的 3.7 节内容。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统配置使用SFTP](<index.php?doc-view-1563.html>)
[下一篇：FineBI文件权限及系统命令需求说明 ![](/core/style/forward.png) ](<index.php?doc-view-1373.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
