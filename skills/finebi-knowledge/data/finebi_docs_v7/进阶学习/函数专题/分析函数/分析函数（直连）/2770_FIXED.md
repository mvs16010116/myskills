---
title: FIXED
doc_id: 2770
url: https://help.fanruan.com/finebi/doc-view-2770.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:27
version: "7.X"
---

> 1. 概述注：本函数仅适用于标准分析主题。FIXED 函数使用指定维度计算聚合指标值。该函数不会自动引用「分析区域」中已拖入的维度，因此在分析区域中增删维度不会影响函数的计算结果。语法{FIXED 维度

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FIXED
[__](<doc-edit-2770.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[7](<edition-list-2770.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-06-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于标准分析主题。**  

FIXED 函数使用指定维度计算聚合指标值。该函数不会自动引用「分析区域」中已拖入的维度，因此在分析区域中增删维度不会影响函数的计算结果。
**语法**  
| {FIXED 维度1,维度2...:指标聚合计算}| 根据当前分析维度，返回指标字段的汇总求和值，生成结果为一数据列，行数与当前分析维度行数一致  
---|---|---  
参数1| 维度| 1）指定需要执行计算的维度2）支持多个维度，维度之间以英文逗号隔开3）维度参数可为空，维度参数为空时，计算指标整表聚合  
参数2| 指标聚合计算| 1）支持各种聚合指标计算（如 SUM_AGG、COUNTD_AGG等）2）支持 LOD 表达式嵌套  
## 2\. 简单示例
为了让您快速了解 FIXED 函数的写法与作用，请参考以下常用场景示例：
场景  
| 公式| 描述  
---|---|---  
想知道每个客户在平台下了多少单  
| {FIXED 身份证号 : COUNTD_AGG(订单编号)}| 
  * 指定维度：身份证号
  * 聚合指标：countd_agg(订单编号)

数一数每个身份证号对应多少个不同的订单编号  
  
想知道平台总的销售额  
| {FIXED : SUM_AGG(销售额)}| 
  * 指定维度：无
  * 聚合指标：sum_agg(销售额)

由于没有指定维度，所以该公式求总销售额  
  
想知道每个省份的销售额| {FIXED 省份 : SUM_AGG(销售额)}| 
  * 指定维度：省份
  * 聚合指标：sum_agg(销售额)

计算每个省份的销售总额  
  
想知道每个省份下不同产品的销售额| {FIXED 省份, 产品 : SUM_AGG(销售额)}| 
  * 指定维度：省份 和 产品
  * 聚合指标：sum_agg(销售额)

计算每个省份下每个产品的销售额  
  
## 3\. 实操-计算转化率
示例，需要在下面这张表中计算出，每个省份下各客户细分类型的销售额，占对应客户细分类型总销售额的百分比。
也就是：百分比 = 每个省份下该客户细分类型的总销售额 / 该客户细分类型在所有省份中的总销售额
![](https://help.fanruan.com/core/style/lod.png)
示例数据（标准分析主题，示例数据需导入到数据库使用）：[超市销售数据..xlsx](<doc-download-/finebi/uploads/file/20260527/超市销售数据..xlsx> "下载资料")
1）新建一个标准分析主题，添加示例数据。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）拖入字段制作组件，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）添加计算字段，计算「细分销售额」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
4）添加计算字段，计算「每个省份细分销售额」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
5）计算占比= 每个省份细分销售额/细分销售额 ，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
6）将「细分销售额」和「占比」拖入表格，效果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：RANK_AGG-按指定规则排名](<index.php?doc-view-2478.html>)
[下一篇：EXCLUDE ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2771.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
