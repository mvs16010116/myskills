---
title: [直连]Kyligence企业版数据连接
doc_id: 1169
url: https://help.fanruan.com/finebi6.X/doc-view-1169.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:30
---

> 1. 概述1.1 版本FineBI 版本JAR 包日期6.0-1.2 应用场景本文介绍 Kyligence 企业版数据源连接。仅支持 FineBI 直连版本。2. 连接前准备2.1 数据库版本和驱动支持

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# [直连]Kyligence企业版数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[9](<edition-list-1169.html>)
* 最近更新：[帆软用户aEcMI0N7Gz](<user-space-3206309.html>) 于 2025-06-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| JAR 包日期  
---|---  
6.0| -  
### 1.2 应用场景
本文介绍 Kyligence 企业版数据源连接。
仅支持 FineBI 直连版本。
## 2\. 连接前准备
### 2.1 数据库版本和驱动
  

支持的数据库版本| 驱动下载  
| 支持数据库版本  
---|---|---  
4.1 及以上版本| [Kyligence 官方下载链接](<https://download.kyligence.io/#/download>)| org.apache.kylin.jdbc.Driver  
数据连接 URL 格式：jdbc:kylin://hostname:port/database?fineBIDialect=kyligence
注：请用户根据自己的数据库版本，前往官网下载合适的驱动版本。
### 2.2 准备工作
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.X/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接操作
1）点击「管理系统>数据连接>数据连接管理」，如下图所示：
**![](/core/style/lod.png)**
2）找到「Kyligence」图标，如下图所示：  

![](/core/style/lod.png)
3）驱动选择 2.2 节上传的驱动，并输入 2.2 节收集的连接信息。为确保数据库取数正确性，直连版本数据连接 URL 需要增加：?fineBIDialect=kyligence，如下图所示：
注：用户可以选择性修改页面上其他高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi6.X/doc-view-94.html>) 4.2 节。![](/core/style/lod.png)
4）点击「测试连接」，成功后保存，如下图所示：  

![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.X/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.X/doc-view-890.html>)


![2.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：华为云DWS数据连接](<index.php?doc-view-440.html>)
[下一篇：阿里云Hologres数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-1347.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
