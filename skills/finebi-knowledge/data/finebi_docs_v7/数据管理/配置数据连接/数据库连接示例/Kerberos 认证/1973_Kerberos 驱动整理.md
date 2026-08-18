---
title: Kerberos 驱动整理
doc_id: 1973
url: https://help.fanruan.com/finebi/doc-view-1973.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:36
version: "7.X"
---

> 1. 概述1.1 应用场景Kerberos 认证时，需要将数据库驱动和 URL 按本文进行更改。1.2 注意事项本文整理 Kerberos 认证驱动配置方法，适用于常见环境标准需求。若客户环境已内置支持

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Kerberos 驱动整理
[__](<doc-edit-1973.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[5](<edition-list-1973.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-07-29 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
Kerberos 认证时，需要将数据库驱动和 URL 按本文进行更改。
### 1.2 注意事项
本文整理 Kerberos 认证驱动配置方法，适用于常见环境标准需求。
若客户环境已内置支持且能直接认证，无需依赖本文驱动；认证有问题或需跨平台、多版本统一管理的，可参考本文配置。
## 2\. 驱动整理
数据库驱动  
| URL格式| 驱动下载| 注意点  
---|---|---|---  
TRANSWARP INCEPTOR（星环）  
| jdbc:hive2://ip:port/database;principal=hive/service@REALM;authentication=kerberos;kuser=pricipal;keytab=keytab路径| [transwrap.zip](<doc-download-/finebi6.X/uploads/file/20250123/transwrap.zip> "下载资料")| URL 中的 principal：
  * 由三部分组成：xxx/xxx@xxx
  * service 不是 IP 名，而是机器名
  * 该 principal 需满足 hive-site.xml 文件中的规则  


  
Spark| jdbc:hive2://ip:port/database;principal=hive/service@REALM| hive通用版本：[hive.zip](<doc-download-/finebi6.X/uploads/file/20250123/hive.zip> "下载资料")hive 2.x版本：[hive2.x.zip](<doc-download-/finebi6.X/uploads/file/20250123/hive2.x.zip> "下载资料")hive 3.x版本：[final.zip](<doc-download-/finebi6.X/uploads/file/20250123/final.zip> "下载资料")  
  
hive（单节点）| jdbc:hive2://ip:port/database;principal=hive/service@REALM  
Apache Impala| jdbc:impala://ip:port/database;AuthMech=1;KrbHostFQDN=quickstart.cloudera;KrbServiceName=impala| [impala](<https://helpfile.obs.cn-east-3.myhuaweicloud.com/%E9%A9%B1%E5%8A%A8/impala.zip>)  
| 保证 KrbHostFQDN、KrbServiceName 两个参数拼接的 principal 能够通过认证  
FusionInsight HD| jdbc:hive2://zkhost:port/,zkhost:port,zkhost:port/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2;principal=hive/service@REALM| [zookeeper](<https://helpfile.obs.cn-east-3.myhuaweicloud.com/%E9%A9%B1%E5%8A%A8/HD.zip>)  
| 
  * 确认 zookeeper 需要 Kerberos认证，可以通过查看zookeeper jar 包版本确认。
  * 确认使用的是数据库自带的 zookeeper jar包
  * 检查 zookeeper 的相关配置  


  
hive（zookeeper形式，常用于集群）  
Phoenix| jdbc:phoenix:quorum:port/database:pricinpal:keytabPath| [phoenix](<https://helpfile.obs.cn-east-3.myhuaweicloud.com/%E9%A9%B1%E5%8A%A8/phoenix-4.12.0-HBase-1.2-client.jar>)  
| 
  * url中最好包含principal和keytab
  * 明确 zookeeper 是否需要进行认证，若无需认证则将 zookeeper.sasl.client 系统参数设置为 false；需要 sasl 认证，则需要注意设置正确的principal
  * 如果 hbase.zookeeper.quorum参数值是主机名，则需要在 hosts 中配置映射

  
HBase| jdbc:phoenix:quorum:port/database:pricinpal:keytabPath| [hbase.zip](<doc-download-/finebi6.X/uploads/file/20250123/hbase.zip> "下载资料")  
  

  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：数据连接 Kerberos 认证](<index.php?doc-view-282.html>)
[下一篇：StarRocks 数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2038.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
