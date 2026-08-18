---
title: AVG_AGG-平均值
doc_id: 1393
url: https://help.fanruan.com/finebi6.X/doc-view-1393.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:04
---

> 1. 概述语法AVG_AGG(array)根据当前分析维度，返回指标字段的汇总平均值，生成结果为一数据列，行数与当前分析维度行数一致。参数array必须为非聚合函数公式返回的结果，可以是某指标字段、维度

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# AVG_AGG-平均值
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1393.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2022-06-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| AVG_AGG(array)| 根据当前分析维度，返回指标字段的汇总平均值，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
实时数据中支持使用单个数值类型参数。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段 AVG_AGG(销量) 返回的值为每日的平均销量；
当用户横轴为维度字段'月'时，AVG_AGG(销量) 返回的值为每月的平均销量。
例如使用「合同信息」计算每年的平均合同金额，有两种计算方式。
### 3.1 方法一：使用 AVG_AGG 函数
创建计算字段「平均合同金额」，输入公式：AVG_AGG(合同金额)，并拖入分析栏，如下图所示：
![](/core/style/lod.png)
![](/core/style/lod.png)
### 3.2 方法二：使用汇总方式求平均
将「合同金额」拖入指标栏，点击「下拉>汇总方式>平均」，如下图所示：
![](/core/style/lod.png)
详情参见：[汇总方式求平均](<https://help.fanruan.com/finebi6.0/doc-view-130.html#5>)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：MIN_AGG-最小值](<index.php?doc-view-1389.html>)
[下一篇：COUNT_AGG-计数 ![](/core/style/forward.png) ](<index.php?doc-view-1386.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
