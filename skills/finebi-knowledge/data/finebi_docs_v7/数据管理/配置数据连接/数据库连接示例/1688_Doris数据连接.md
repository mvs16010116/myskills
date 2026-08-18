---
title: Doris数据连接
doc_id: 1688
url: https://help.fanruan.com/finebi/doc-view-1688.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:58
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动7.0-1.2 应用场景本文将介绍 FineBI 如何连接 Doris 数据库。2. 连接前准备2.1 数据库版本和驱动驱动支持的数据库版本com.mys

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Doris数据连接
[__](<doc-edit-1688.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[11](<edition-list-1688.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-03-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
7.0  
| -  
  
### 1.2 应用场景
本文将介绍 FineBI 如何连接 Doris 数据库。  

## 2\. 连接前准备
### 2.1 数据库版本和驱动
  

驱动  
| 支持的数据库版本  
---|---  
com.mysql.jdbc.Driver（已内置）| Doris 0.14 及以上版本  
数据连接 URL 格式：jdbc:mysql://ip:port/dbname
注：Doris存在多个节点，如需一个数据连接连接多个节点，在URL中填写节点统一入口即可。
### 2.2 准备工作
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的用户名和密码；
  * 数据库名称；  



## 3\. 具体连接操作
1）登录 FineBI ，选择「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）选择「所有」，找到 Doris 数据库，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）进入数据连接配置页面，配合 2.1 节的配置信息输入数据连接的相关信息，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
4）点击「测试连接」，成功后保存，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：华为FusionInsight ELK数据连接](<index.php?doc-view-299.html>)
[下一篇：Hadoop Hive数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-301.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
