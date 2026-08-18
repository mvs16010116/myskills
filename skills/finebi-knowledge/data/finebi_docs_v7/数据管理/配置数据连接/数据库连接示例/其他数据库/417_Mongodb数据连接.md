---
title: Mongodb数据连接
doc_id: 417
url: https://help.fanruan.com/finebi/doc-view-417.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:09
version: "7.X"
---

> 1. 概述1.1 预期效果MongoDB 是一个基于分布式文件存储的数据库，是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。 MongoDB 旨在为 WEB

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Mongodb数据连接
[__](<doc-edit-417.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[16](<edition-list-417.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-02-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 预期效果
MongoDB 是一个基于分布式文件存储的数据库，是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。 MongoDB 旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。本章实现将 FineBI 连接到 MongoDB 数据库。
### 1.2 解决思路
通过 FineBI 远程连接 FineReport 设计器，再将 FineReport 连接 MongoDB 实现数据集调用。
## 2\. 操作步骤
1）[远程连接 FineReport 设计器](<https://help.fanruan.com/finebi7.0/doc-view-931.html>)；
2）在 [FineReport 连接 MongoDB](<http://help.finereport.com/doc-view-1413.html>)；
3）创建 MongoDB 数据集并通过[服务器数据集](<https://help.fanruan.com/finebi7.0/doc-view-253.html>)将其添加至 BI 中使用；
## 3\. 注意事项
1）此数据连接仅支撑数据量不大，百万级别以下的情况。
2）由于mongodb是非关系型数据库，字段不对齐，可能存在缺失部分字段的情况。
FineBI通过第一行数据取字段信息，而mongodb字段不对齐，第一行数据缺失部分字段，此时没有办法保证获取完整字段。
用户可通过预览全部数据取到全部字段，但若数据量较大，出于性能考虑，不建议执行此操作。
示例：
第一行数据，字段c为空
![](https://help.fanruan.com/core/style/lod.png)
BI中缺失字段c  

![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：新SAP BW数据集插件](<index.php?doc-view-256.html>)
[下一篇：应用数据源 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2341.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
