---
title: APPROX_COUNTD_AGG-近似去重计数
doc_id: 1396
url: https://help.fanruan.com/finebi6.X/doc-view-1396.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:09
---

> 1. 概述当计算数据非常大时，传统的精确的去重计数可能算不出来，使用近似的去重计数可以很快计算出结果。语法APPROX_COUNTD_AGG(array)根据当前分析维度，动态返回某字段的近似去重计数，

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# APPROX_COUNTD_AGG-近似去重计数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1396.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2023-02-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
当计算数据非常大时，传统的精确的去重计数可能算不出来，使用近似的去重计数可以很快计算出结果。
语法  
| APPROX_COUNTD_AGG(array)| 根据当前分析维度，动态返回某字段的近似去重计数，生成结果为一动态数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
  * 仅支持直连数据中使用。
  * 本函数仅支持以下数据库系统：CLICKHOUSE、ORACLE（12c r1，12.1.0.2及以上）、SQLSERVER（2019及以上）、PRESTO、REDSHIFT、VERTICA。当数据库系统为REDSHIFT时，由于REDSHIFT的限制，只能同时对同一个字段做需要排序的聚合操作（如求去重计数、中位数、百分位、近似去重计数），同时对2个或以上的字段做此种聚合操作会发生错误。当数据库系统为VERTICA时，由于VERTICA的限制，只能同时使用（精确）去重计数或近似去重计数中的一个。
  * 支持使用一个任意类型的参数。


## 3\. 示例
用户横轴为维度字段"日"时，纵轴的计算字段 APPROX_COUNTD_AGG() 返回的值为每日的销量的近似去重个数。
当用户横轴为维度字段"月"时，APPROX_COUNTD_AGG() 返回的值为每月的销量的近似去重个数。
例如对单据编码计算每天的近似去重计数，如下图所示：
![](/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：PERCENTILE_AGG-百分位数](<index.php?doc-view-1395.html>)
[下一篇：DEF类函数概述 ![](/core/style/forward.png) ](<index.php?doc-view-1993.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
