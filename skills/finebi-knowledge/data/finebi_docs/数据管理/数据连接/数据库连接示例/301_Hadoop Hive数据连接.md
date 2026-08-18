---
title: Hadoop Hive数据连接
doc_id: 301
url: https://help.fanruan.com/finebi6.X/doc-view-301.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:22
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景Hadoop 是个很流行的分布式计算解决方案，Hive是建立在 Hadoop 上的数据仓库基础构架。本文将介绍如何连接 Hadoo

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Hadoop Hive数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[39](<edition-list-301.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-07-01 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
Hadoop 是个很流行的分布式计算解决方案，Hive是建立在 Hadoop 上的数据仓库基础构架。
本文将介绍如何连接 Hadoop Hive 数据源。
注：该数据库不支持使用直连属性的数据表
## 2\. 准备工作
### 2.1 版本和驱动
**请根据数据库版本下载对应的驱动** ，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html?source=4>) 2.1 节  

注：在上传驱动包时，需要解压下面的「日志jar」文件，和驱动一起上传至 FineBI。
支持的数据库版本| 驱动包下载|  日志jar下载  
---|---|---  
hive_1.1  
Hadoop_Hive_1.2；hive2.3；  
hive2.1.2；hive2.1.1| 依据版本自行获取驱动，推荐 Hive 社区打包的：  
[hive-jdbc-standalone.jar](<https://repo1.maven.org/maven2/org/apache/hive/hive-jdbc/>)  
（帆软不提供驱动）  
| [日志jar.rar](<doc-download-/finereport/uploads/file/20211213/日志jar.rar> "下载资料")  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 若是用户名密码认证，需要收集用户名和密码；若是 Kerberos 认证，需要收集客户端 principal 和 keytab 密钥路径；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html?source=4>)
![](/core/style/lod.png)
2）找到 Hadoop Hive 数据库，如下图所示：
![](/core/style/lod.png)
3）切换驱动为「自定义」选择 2.1 节上传的驱动，并输入 2.2 节收集的连接信息，如下图所示：
Kerberos 认证方式详情可参见：[数据连接 kerberos 认证](<https://help.fanruan.com/finebi6.0/doc-view-282.html>)
![](/core/style/lod.png)
使用 Kerberos 认证需要注意以下事项：
  * 连接前请检查 /etc/hosts 中的机器名对应 IP 是否为局域网 IP；
  * 检查 /etc/hostname 中机器名设置和 /etc/hosts 中是否配置一致；
  * 检查 FineBI 所在机器 hosts 配置的 IP+ 机器名是否正确；
  * 某些情况下，尤其是非公网环境中，用户的客户端可能无法解析数据库服务端的主机名。在这种情况下用户需要配置客户端的 /etc/hosts 文件，添加远端映射：IP+主机名，例如： 192.168.5.206 centos-phoenix 。


4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：  

![](/core/style/lod.png)
## 4\. 添加数据库的表至FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加 SQL 数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)[](<https://help.fanruan.com/finereport/doc-view-106.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Doris数据连接](<index.php?doc-view-1688.html>)
[下一篇：Hbase数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-302.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
