---
title: PERCENTILE_AGG-百分位数
doc_id: 1395
url: https://help.fanruan.com/finebi/doc-view-1395.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:14
version: "7.X"
---

> 1. 概述1.1 版本FineBI版本功能变动6.0-6.1.4支持抽取数据使用PERCENTILE_AGG()函数1.2 函数语法PERCENTILE_AGG(array,百分位)根据当前分析维度，从

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# PERCENTILE_AGG-百分位数
[__](<doc-edit-1395.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1395.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-28 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI版本  
| 功能变动  
---|---  
6.0| -  
6.1.4| 支持抽取数据使用PERCENTILE_AGG()函数  
  

### 1.2 函数
语法  
| PERCENTILE_AGG(array,百分位)| 根据当前分析维度，从给定表达式返回与指定数字对应的百分位处的值。数字必须介于 0 到 1 之间（含 0 和 1 ），例如 0.66，并且必须是数值常量。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。不支持插入文本和日期。  
## 2\. 注意事项
  * 支持使用两个数值类型参数，且第二个参数必须为常量。  

  * 直连仅支持以下数据库：Sybase IQ、Oracle、PostgreSQL（9.4或以上）、ClickHouse、Greenplum、Transwarp Inceptor、Redshift、MaxCompute、Teradata、Hologres、DB2（11.1或以上）、Hive、GaussDB(DWS)（8.1.1或以上）、Dremio。
  * 直连数据库为Redshift时，只能同时对同一字段做有序聚合计算（如求中位数、百分位），否则会发生错误。
  * 直连数据库为MaxCompute或Hive时，只能对整数字段做此种计算。


## 3\. 示例
### 3.1 求95%的销量
用户横轴为维度字段“日”时，纵轴的计算字段 PERCENTILE_AGG(销量,0.95) 返回的值为每日的95%的销量。 
当用户横轴为维度字段“月”时，PERCENTILE_AGG(销量,0.95) 返回的值为每月的95%的销量。如下图所示：
![2024-11-28_14-08-47.png](https://help.fanruan.com/core/style/lod.png)
![2024-11-28_14-11-38.png](https://help.fanruan.com/core/style/lod.png)
### 3.2 更多示例
如果你是人力资源经理，可以使用 PERCENTILE_AGG 了解员工的薪酬分布。
公式  
| 含义| 描述  
---|---|---  
PERCENTILE_AGG(工资,0.25)| 返回25th 的百分位数| 表示有 25% 的员工薪酬低于该值，用来了解底薪  
PERCENTILE_AGG(工资,0.5)| 返回50th 的百分位数| 表示有 50% 的员工薪酬低于该值，是薪酬分布中间点  
PERCENTILE_AGG(工资,0.9)| 返回90th 的百分位数| 表示有 90% 的员工薪酬低于该值，了解高收入的情况  
PERCENTILE_AGG 计算逻辑同 Excel 中的 Percentile。
若百分位不是 1/n 的倍数，函数 PERCENTILE_AGG 使用插值法来确定最终的百分位的值。 
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：MEDIAN_AGG-中位数](<index.php?doc-view-1391.html>)
[下一篇：APPROX_COUNTD_AGG-近似去重计数 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1396.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
