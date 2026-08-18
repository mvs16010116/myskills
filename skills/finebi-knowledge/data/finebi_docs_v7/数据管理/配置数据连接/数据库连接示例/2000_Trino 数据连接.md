---
title: Trino 数据连接
doc_id: 2000
url: https://help.fanruan.com/finebi/doc-view-2000.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:41
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0.3-1.2 应用场景本文将介绍如何连接 Trino 数据库。2. 连接前准备2.1 数据库版本和驱动支持的数据库版本对应驱动下载驱动390请根据数

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Trino 数据连接
[__](<doc-edit-2000.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[10](<edition-list-2000.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-11-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0.3  
| -  
  
### 1.2 应用场景
本文将介绍如何连接 Trino 数据库。
## 2\. 连接前准备
### 2.1 数据库版本和驱动
支持的数据库版本  
| 对应驱动下载| 驱动  
---|---|---  
390  
| [trino-jdbc-390.jar](<doc-download-/finebi6.X/uploads/file/20250123/trino-jdbc-390.jar> "下载资料")| io.trino.jdbc.TrinoDriver  
数据连接 URL 格式：jdbc:trino://hostname:port/database  

### 2.2 准备工作
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](https://help.fanruan.com/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接操作
1）点击「管理系统>数据连接>数据连接管理>新建」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
2）找到「trino」的图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动选择 2.2 节上传的驱动，并输入 2.2 节收集的连接信息。trino 数据库需要选择要连接的模式，点击「点击连接数据库」连接成功后，选择模式。如下图所示：
注：用户可以选择性修改页面上其他高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html>) 4.2 节。
![](https://help.fanruan.com/core/style/lod.png)
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：SQlite 数据连接](<index.php?doc-view-1976.html>)
[下一篇：MySQL数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-183.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
