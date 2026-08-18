---
title: INCLUDE
doc_id: 2772
url: https://help.fanruan.com/finebi/doc-view-2772.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:29
version: "7.X"
---

> 1. 概述注：本函数仅适用于标准分析主题。INCLUDE 函数会基于当前分析区域已有的维度，加上 INCLUDE 中指定的维度一起执行聚合。语法{EXCLUDE 维度1,维度2...:指标聚合计算}根据

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# INCLUDE
[__](<doc-edit-2772.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[4](<edition-list-2772.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于标准分析主题。**
INCLUDE 函数会基于当前分析区域已有的维度，加上 INCLUDE 中指定的维度一起执行聚合。
**语法**  
| {EXCLUDE 维度1,维度2...:指标聚合计算}| 根据当前分析维度，返回指标字段的汇总求和值，生成结果为一数据列，行数与当前分析维度行数一致  
---|---|---  
**参数1**|  维度| 1）指定需要排除的维度2）支持多个维度，维度之间以英文逗号隔开3）维度参数可为空，维度参数为空时，计算指标整表聚合  
**参数2**|  指标聚合计算| 1）支持各种聚合指标计算（如 SUM_AGG、COUNTD_AGG等）2）支持 LOD 表达式嵌套  
## 2\. 简单示例
为了快速了解 INCLUDE 函数的写法与作用，请参考以下常用场景示例，当前视图有省份字段：
![](https://help.fanruan.com/core/style/lod.png)
**公式**|  描述  
---|---  
{INCLUDE :SUM_AGG(销售额)}| 
  * 指定维度：无
  * 分析区域维度：省份  


计算出每个省份的销售额  
{INCLUDE 客户名称 :SUM_AGG(销售额)}| 
  * 指定维度：客户名称
  * 分析区域维度：省份

计算不同省份下的每个客户的销售额  
相对于 FIXED 来说，INCLUDE 的优势在于：它可以通过拖拽灵活调整维度，从而快速的获得不同的分析结果。  

若上面这个例子，我想求「各个地区的销售额」和「各个地区下每个客户的销售额」：
  * 使用 INCLUDE 函数： 仅需要将分析区域的维度字段从「省份」切换为「地区」
  * 使用 FIXED 函数，需要重新定义函数：DEF(SUM_AGG(销售额),[地区])、DEF(SUM_AGG(销售额),[地区,客户名称])


分析是个探索的过程，我们需要不断的去切换维度更改分析角度发现问题，这时候使用 INCLUDE 可以帮助你提高分析效率。
## 3\. 实操-求不同省份的客均销售额
示例，计算出每个省份的客均销售额。
获取示例数据（标准分析主题，示例数据需导入到数据库后直连使用）：[超市销售数据.xlsx](<doc-download-/finebi/uploads/file/20260519/超市销售数据.xlsx> "下载资料")
1）新建一个标准分析主题，添加示例数据。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）添加计算字段，计算「客户销售额」，公式如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）选择柱形图，将「省份」和「客户销售额」拖入组件，如下图所示： 
  * 函数指定维度：客户名称
  * 分析区域维度：省份


该公式计算的是各省份下各客户的销售额。  
当前图表的汇总方式为「求和」，因此每个柱子展示的是该省份下所有客户销售额的汇总值。
![](https://help.fanruan.com/core/style/lod.png)
4）要展示各省份下客户销售额的平均值，可将汇总方式改为「平均」。
![2026-05-19_17-07-24.png](https://help.fanruan.com/core/style/lod.png)
最终效果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：EXCLUDE](<index.php?doc-view-2771.html>)
[下一篇：DEF函数应用合集 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2173.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
