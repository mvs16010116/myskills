---
title: EXCLUDE
doc_id: 2771
url: https://help.fanruan.com/finebi/doc-view-2771.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:28
version: "7.X"
---

> 1. 概述注：本函数仅适用于标准分析主题。EXCLUDE 函数用于从「分析区域」已有的维度中，排除指定的维度。系统在实际计算时，会将其余的视图维度作为分组依据来执行聚合。语法{EXCLUDE 维度1,维

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# EXCLUDE
[__](<doc-edit-2771.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[6](<edition-list-2771.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于标准分析主题。**
EXCLUDE 函数用于从「分析区域」已有的维度中，排除指定的维度。系统在实际计算时，会将其余的视图维度作为分组依据来执行聚合。
语法  
| {EXCLUDE 维度1,维度2...:指标聚合计算}| 根据当前分析维度，返回指标字段的汇总求和值，生成结果为一数据列，行数与当前分析维度行数一致  
---|---|---  
参数1| 维度| 1）指定需要排除的维度2）支持多个维度，维度之间以英文逗号隔开3）维度参数可为空，维度参数为空时，计算指标整表聚合  
参数2| 指标聚合计算| 1）支持各种聚合指标计算（如 SUM_AGG、COUNTD_AGG等）2）支持 LOD 表达式嵌套  
## 2\. 简单示例
为了快速了解 EXCLUDE 函数的写法与作用，请参考以下常用场景示例：
场景  
| **公式**|  描述  
---|---|---  
当前视图包含「地区、分类」![](https://help.fanruan.com/core/style/lod.png)需要忽略「分类」，计算每个大区的销售额| {EXCLUDE 分类 :SUM_AGG(销售额)}| 
  * 指定要排除的维度：分类
  * 聚合指标：SUM_AGG(销售额)}

计算出每个大区的销售额  
  
当前视图包含「记录人、合同类型」需要忽略合同类型的差异，计算每位记录人的总合同金额| {EXCLUDE 合同类型 :SUM_AGG(合同金额)}| 计算出每位记录人的总合同金额  
不排除任何维度，执行常规聚合| {EXCLUDE : SUM_AGG(合同金额)}| 按当前视图维度计算合同金额  
## 3\. 实操-加入平均值
我们可以很容易得出 2017 年每个季度各个大区的销售额。那如果如下图我们想加入「每个季度各大区平均销售额」，了解平均值多少的同时，还方便每个大区与平均值进行对比，该如何操做呢？
整理下思路：每个季度各大区的销售额=每个产品的总销售额/地区的个数
![](https://help.fanruan.com/core/style/lod.png)
1）新建一个标准分析主题，添加示例数据。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）选择图表类型为「自定义图表」，展示每个产品各地区的销售额是多少。如下图所示：
![2026-05-19_17-45-24.png](https://help.fanruan.com/core/style/lod.png)
3）添加计算字段，计算「产品的大区平均销售额」，如下图所示：
![2026-05-19_17-55-36.png](https://help.fanruan.com/core/style/lod.png)
公式| 描述  
---|---  
{ EXCLUDE 地区:SUM_AGG(销售额)}| 
  * 分析区域维度：产品、地区
  * 指定排除维度：地区

对每个产品的总销售额  
{ FIXED:COUNTD_AGG(﻿地区﻿)}| 
  * 指定维度：无

数一数整张表有多少个地区  
4）将「产品的大区平均销售额」拖入图表，在图表属性那里调整它的展现形式为「线」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
至此便完成了这个分析。
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FIXED](<index.php?doc-view-2770.html>)
[下一篇：INCLUDE ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2772.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
