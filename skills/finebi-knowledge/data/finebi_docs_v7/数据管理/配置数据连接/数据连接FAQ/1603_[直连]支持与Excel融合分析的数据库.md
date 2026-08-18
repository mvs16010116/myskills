---
title: [直连]支持与Excel融合分析的数据库
doc_id: 1603
url: https://help.fanruan.com/finebi/doc-view-1603.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:17
version: "7.X"
---

> 1. 概述所有数据库中的抽取数据表都可以和 Excel 表进行关联、左右合并、上下合并这些融合分析。只有部分数据库的直连数据表可以与 Excel 进行&nbsp;关联、左右合并、上下合并&nbsp;、其

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# [直连]支持与Excel融合分析的数据库
[__](<doc-edit-1603.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[25](<edition-list-1603.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
所有数据库中的抽取数据表都可以和 Excel 表进行关联、左右合并、上下合并这些融合分析。
只有部分数据库的直连数据表可以与 Excel 进行 [关联](<https://help.fanruan.com/finebi7.0/doc-view-78.html>)、[左右合并](<https://help.fanruan.com/finebi7.0/doc-view-512.html?source=4>)、[上下合并](<https://help.fanruan.com/finebi7.0/doc-view-513.html?source=4>) 、[其他表添加列](<https://help.fanruan.com/finebi/doc-view-1998.html>) 其余数据库正在逐步适配中。
## 2\. 支持融合的数据库
只有直连属性的 Excel 可以与直连数据表进行融合分析，所以我们添加的 Excel 也需要是直连属性的。
将属性设置为「直连数据」，再添加Excel ，如下图所示：
![2026-05-26_18-02-03.png](https://help.fanruan.com/core/style/lod.png)
Excel 与直连数据融合分析的时候，系统会自动给 Excel 在数据库中建表。比如说需要让 Excel 与 Oracle 数据库的表做融合分析，系统就会在 Oracle 中给 Excel 建一张表。不同的数据库采用不同建表方式，分为两类：
注：连接数据库时，需要注意填写的用户有此数据库的「建表、更新、数据行插入、删除」权限，否则无法进行融合分析
Excel 建表分类  
| 概念  
---|---  
实体表| 系统给 Excel 建的表会一直留在数据库之中。
  * 进行一次融合分析，系统就会在数据库中给 Excel 建一张表，由于实体表不会自动删除，所以会越来越占磁盘空间；且 Excel 表会无序散布在数据库里，管理员不方便直接在数据库中对这些 Excel 进行管理。
  * 若要删掉这些实体表：保证建立数据连接的账号有删表权限，然后在 FineBI 里面删除 Excel 且确保回收站中也不保留。

  
临时表（推荐）|  数据库与 FineBI 断开连接后，系统给 Excel 在数据库建的表会被自动删除。  
直连版本下，支持与 Excel 进行 [关联](<https://help.fanruan.com/finebi7.0/doc-view-78.html>)、[左右合并](<https://help.fanruan.com/finebi7.0/doc-view-512.html?source=4>)、[上下合并](<https://help.fanruan.com/finebi7.0/doc-view-513.html?source=4>) 的数据库如下表所示。[其他表添加列](<https://help.fanruan.com/finebi/doc-view-1998.html>) 以用户实际实现情况为准。
数据库| 数据库版本| Excel数据库建表方式  
| FineBI 开始支持的版本  
---|---|---|---  
[Microsoft SQL Server 2016](<https://help.fanruan.com/finebi7.0/doc-view-100.html?source=4>)  
| V2016  
| 临时表| 5.1.12  
[Oracle 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-185.html?source=4>)   
| V11  
| 临时表| 5.1.12  
[Pivotal Greenplum Database](<https://help.fanruan.com/finebi7.0/doc-view-289.html?source=4>)  
| V9  
| 临时表| 5.1.12  
  
[Apache Impala](<https://help.fanruan.com/finebi7.0/doc-view-293.html?source=4>)  
| V2| 实体表| 5.1.15  
[SAP Sybase](<https://help.fanruan.com/finebi7.0/doc-view-307.html?source=4>)   
| IQ 16.0| 临时表| 5.1.16  
[Postgresql数据连接](<https://help.fanruan.com/finebi7.0/doc-view-290.html>)  
| V9  
| 临时表| 5.1.16  
[ClickHouse 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-1102.html>)  
| 20.1.8.41| 实体表| 5.1.17  
[Presto数据连接](<https://help.fanruan.com/finebi7.0/doc-view-305.html>)  
| V0.218| 实体表| 5.1.17  
[GaussDB 200数据连接](<https://help.fanruan.com/finebi7.0/doc-view-439.html>)  
| gaussdb 200| 临时表| 5.1.17  
[MySQL 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-183.html?source=4>)  
| V5.1V5.5、V5.5.5、V5.5.46V5.6.22、V5.6.28、V5.6.29、V5.6.31、V5.6.34、V5.6.35、V5.6.37V5.7、V5.7.16 V6.5V8.0| 临时表| 5.1.19  
[阿里云Hologres数据连接](<https://help.fanruan.com/finebi7.0/doc-view-1347.html?source=4>)  
| 无版本限制| 实体表| 5.1.19  
[doris 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-1688.html>)  
| 无版本限制| 实体表| 5.1.23  
[SAP HANA数据连接](<https://help.fanruan.com/finebi7.0/doc-view-306.html>)| V4.5.1| 临时表| 5.1.27、5.1.18.27  
[StarRocks 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-2038.html>)  
| 无限制| 实体表| 6.0.4  
[Gbase8A 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-295.html>)  
| 81| 临时表| 6.0.6  
[阿里云AnalyticDB](<https://help.fanruan.com/finebi7.0/doc-view-291.html>)|   
| 实体表| 6.0.8  
[TiDB数据连接](<https://help.fanruan.com/finebi7.0/doc-view-1640.html>)  
| V5.2.0| 实体表| 6.0  
其中 presto 和 impala 数据库中的数据表若与 Excel 进行融合分析，融合分析后得到的新表会写入到用户的数据库中。  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：更换表的数据库来源](<index.php?doc-view-810.html>)
[下一篇：驱动管理 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1540.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
