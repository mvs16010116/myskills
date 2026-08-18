---
title: SQlite 数据连接
doc_id: 1976
url: https://help.fanruan.com/finebi6.X/doc-view-1976.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:04
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 sqlite 数据库。2. 准备工作2.1 版本与驱动驱动下载驱动名BI&nbsp;内置 sqlite-jdb

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# SQlite 数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[8](<edition-list-1976.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-09-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0  
| -  
  
### 1.2 应用场景
本文将介绍如何连接 sqlite 数据库。
## 2\. 准备工作
### 2.1 版本与驱动
驱动下载  
| 驱动名  
---|---  
BI 内置 sqlite-jdbc.jar 驱动包，无需下载| org.sqlite.JDBC  
URL格式： jdbc:sqlite:[PATH_TO_DB_FILES]  
若内置的驱动被误删，可重新下载： [sqlite-jdbc.jar](<doc-download-/finebi6.X/uploads/file/20250123/sqlite-jdbc.jar> "下载资料") （驱动上传方式可参见：[驱动管理](<https://help.fanruan.com/finereport/doc-view-4165.html>)）
### 2.2 下载驱动文件
在连接数据库之前，请收集以下信息：
  * 数据库的存储路径
  * 数据库的用户名和密码


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，如下图所示：
![](/core/style/lod.png)
2）找到「Sqlite」的图标，如下图所示：
![](/core/style/lod.png)
3）输入用户名和密码，输入数据连接URL。如下图所示：
  * 若数据库的路径为 C:\Users\86150\Downloads\FRDemo.db，则 URL 修改为 jdbc:sqlite:C:\Users\86150\Downloads\FRDemo.db
![](/core/style/lod.png)  

  * 若数据库在工程中，例如 FR 内置数据库在工程中的位置为%FineReport_10.0%\webapps\webroot\help，则 URL 也可写相对路径：jdbc:sqlite://${ENV_HOME}/../help/FRDemo.db
  * 若数据库与工程不在同一服务器下，需要共享网络路径，并将上面的路径替换。


![](/core/style/lod.png)
4）点击「测试连接」，成功连接后点击「保存」。如下图所示：
注：SQLite 数据库在获取连接时，若 URL 中 PATH 路径下没有数据库时，会自动在此路径下创建数据库，因此会出现实际 PATH 路径下没有 SQLite 数据库也会连接成功的现象。
![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：  

  * [添加数据库表](<https://help.fanruan.com/finebi6.X/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.X/doc-view-890.html>)


![52.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Tbase 数据连接](<index.php?doc-view-1974.html>)
[下一篇：Trino 数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-2000.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
