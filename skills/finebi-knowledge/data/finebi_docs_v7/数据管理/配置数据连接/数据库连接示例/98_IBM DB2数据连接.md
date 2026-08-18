---
title: IBM DB2数据连接
doc_id: 98
url: https://help.fanruan.com/finebi/doc-view-98.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:42
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-6.0.3删除DB2内置驱动，需要使用到的用户手动上传1.2 应用场景本文将介绍如何连接 IBM DB2 。2. 连接前准备2.1 数据库版本和驱

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# IBM DB2数据连接
[__](<doc-edit-98.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[27](<edition-list-98.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0| -  
6.0.3| 删除DB2内置驱动，需要使用到的用户手动上传  
### 1.2 应用场景
本文将介绍如何连接 IBM DB2 。
## 2\. 连接前准备
### 2.1 数据库版本和驱动
  

支持的数据库版本| 驱动包下载| 驱动  
---|---|---  
V9.7；V8.2；V10.5；V11.1(直连适配版本为：DB2 V9)  | [db2 需解压.rar](<doc-download-/finebi6.X/uploads/file/20250123/db2 需解压.rar> "下载资料")| com.ibm.db2.jcc.DB2Driver  
数据连接 URL 格式：jdbc:db2://hostname:port/database
  

### 2.2 准备工作
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](https://help.fanruan.com/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：  

  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接操作
1）点击「管理系统>数据连接>数据连接管理>新建」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）找到「IBM DB2」的图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动选择 2.2 节上传的驱动，并输入 2.2 节收集的连接信息。IBM DB2 数据库需要选择要连接的模式，点击「点击连接数据库」连接成功后，选择模式。如下图所示：
注：用户可以选择性修改页面上其他高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html>) 4.2 节。
  

![28.png](https://help.fanruan.com/core/style/lod.png)
4）点击「测试连接」，若连接成果点击「保存」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：MySQL数据连接](<index.php?doc-view-183.html>)
[下一篇：Pivotal Greenplum Database数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-289.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
