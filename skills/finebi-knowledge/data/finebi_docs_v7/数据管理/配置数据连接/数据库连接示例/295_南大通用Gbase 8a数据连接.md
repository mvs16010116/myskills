---
title: 南大通用Gbase 8a数据连接
doc_id: 295
url: https://help.fanruan.com/finebi/doc-view-295.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:54
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 功能简介本文将介绍如何连接 Gbase 8A 数据源。2. 准备工作2.1 版本和驱动下载驱动，并将其上传至 FineBI，如何上传可参见

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 南大通用Gbase 8a数据连接
[__](<doc-edit-295.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[23](<edition-list-295.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 功能简介
本文将介绍如何连接 Gbase 8A 数据源。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html?source=4>) 2.1 节
支持的数据库版本| 驱动包下载  
---|---  
Gbase 8A（基于mysql）| [gbase-connector-java-8.3.81.53-build52.8-bin.jar](<doc-download-/uploads/file/20191202/gbase-connector-java-8.3.81.53-build52.8-bin.jar> "下载资料")  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<http://help.finereport.com/doc-view-2457.html>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 Gbase 8A 图标，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。如下图所示：
注：编码「默认」即可，若出现乱码情况可以修改当前数据连接对应的编码。
![](https://help.fanruan.com/core/style/lod.png)
4）点击「测试连接」，若连接成功则点击「保存」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：Postgresql数据连接](<index.php?doc-view-290.html>)
[下一篇：Gbase 8S数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-296.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
