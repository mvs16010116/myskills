---
title: Pivotal Greenplum Database数据连接
doc_id: 289
url: https://help.fanruan.com/finebi6.X/doc-view-289.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:07
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景Greenplum 数据库也简称 GPDB ，拥有很多丰富的特性，本章我们将介绍如何在 FineBI 中连接 Pivotal Gr

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Pivotal Greenplum Database数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[21](<edition-list-289.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-11-13 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0  
| -  
  
### 1.2 应用场景
Greenplum 数据库也简称 GPDB ，拥有很多丰富的特性，本章我们将介绍如何在 FineBI 中连接 Pivotal Greenplum Database 。
## 2\. 连接前准备
### 2.1 数据库版本和驱动
  

支持的数据库版本  
| 驱动下载  
| 驱动  
---|---|---  
5.0  
| 请根据数据库版本从 [官网](<https://central.sonatype.com/artifact/org.postgresql/postgresql/versions>) 下载对应插件| org.postgresql.Driver  
使用 postgresql 驱动，数据连接 URL 格式： jdbc:postgresql://ip:port/dbname?fineBIDialect=greenplum
  

使用 greenplum 驱动，数据连接 URL 格式： jdbc:pivotal:greenplum://ip:port;DatabaseName=xxx
### 2.2 准备工作
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.X/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的用户名和密码；


## 3\. 具体连接操作
1）点击「管理系统>数据连接>数据连接管理」，如下图所示：
![](/core/style/lod.png)
2）找到「Pivotal Greenplum Database」的图标，如下图所示：
![](/core/style/lod.png)
3）驱动选择 2.2 节上传的驱动，并输入 2.2 节收集的连接信息。trino 数据库需要选择要连接的模式，点击「点击连接数据库」连接成功后，选择模式。如下图所示：
![](/core/style/lod.png)
4）点击测试连接，成功后保存，如下图所示：
![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.X/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.X/doc-view-890.html>)


![](/core/style/lod.png)  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：IBM DB2数据连接](<index.php?doc-view-98.html>)
[下一篇：Apache Impala数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-293.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
