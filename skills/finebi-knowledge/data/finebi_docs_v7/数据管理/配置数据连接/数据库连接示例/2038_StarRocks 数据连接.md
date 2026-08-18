---
title: StarRocks 数据连接
doc_id: 2038
url: https://help.fanruan.com/finebi/doc-view-2038.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:37
version: "7.X"
---

> 1. 概述1.1 版本&nbsp;FineBI 版本功能变动6.0.4-6.0.16支持选择 catalog（数据目录） ，方便用户从 StarRocks 的外部 catalog 取数1.2 应用场景本

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# StarRocks 数据连接
[__](<doc-edit-2038.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[17](<edition-list-2038.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-12-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0.4  
| -  
  
6.0.16| 支持选择 catalog（数据目录） ，方便用户从 StarRocks 的外部 catalog 取数  
### 1.2 应用场景
本文将介绍如何连接 StarRocks 数据库。  

## 2\. 连接前准备
### 2.1 数据库版本和驱动
支持的数据库版本  
| 对应驱动下载  
---|---  
无限制  
| 已内置，无需下载  
  
### 2.2 准备工作
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的用户名和密码；
  * Catalog 和 数据库名称  



## 3\. 具体连接操作
1）点击「管理系统>数据连接>数据连接管理>新建>文件夹或者数据连接」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
2）找到「StarRocks」图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）输入 2.2 节收集的连接信息，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
StarRocks 的 Catalog（数据目录）可用于访问内、外部源的数据（可参见：[catalog 简介](<https://docs.starrocks.io/zh/docs/data_source/catalog/catalog_overview/>)）。每个 StarRocks 集群都有且只有一个 internal catalog 名为 default_catalog。
  * 新建数据连接的 catalog 默认值为 default_catalog ，即系统默认访问 internal catalog 内部数据目录。
  * 6.0.16 之前的版本建立的数据连接，catalog 会显示为空，不影响正常使用。
  * 如下图，在 catalog 中填写一个外部数据目录 hive_test， 就可以连接到 hive_test ，并使用 [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>) 直接从中取数 。


![icon](https://help.fanruan.com/core/style/lod.png)提示:
catalog 中的表不支持和外部 Excel 表联合分析，若要进行联合分析请先配置加速引擎，详细请参见：[加速引擎](<https://help.fanruan.com/finebi7.0/doc-view-2258.html>)
4）点击「测试连接」，成功后「保存」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
![](https://help.fanruan.com/core/style/lod.png)
1）[添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
2）[添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)
使用 SQL 数据集取数时，需要带上 catalog 的信息（若空缺 catalog 信息，则默认访问 inter catalog），例如下图示例：select * from catalog.数据库名称.表名
  * catalog：hive_test
  * 数据库名称：tpch_10g
  * 表名：customer


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：Kerberos 驱动整理](<index.php?doc-view-1973.html>)
[下一篇：HSQL数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1710.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
