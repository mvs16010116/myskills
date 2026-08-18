---
title: STDEV_AGG-标准差
doc_id: 1394
url: https://help.fanruan.com/finebi/doc-view-1394.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:13
version: "7.X"
---

> 1. 概述语法STDEV_AGG(array)根据当前分析维度，返回指标字段的标准差，生成结果为一数据列，行数与当前分析维度行数一致。参数array必须为非聚合函数公式返回的结果，可以是某指标字段、维度

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# STDEV_AGG-标准差
[__](<doc-edit-1394.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1394.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-10-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| STDEV_AGG(array)| 根据当前分析维度，返回指标字段的标准差，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
实时数据支持使用一个任意类型的参数。
注：FineBI 的 STDEV_AGG 函数与 Excel 里面的 STDEV.P() 函数功能相同。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段STDEV_AGG(销量)返回的值为每日的销量标准差。
当用户横轴为维度字段'月'时，STDEV_AGG(销量)返回的值为每月的销量标准差。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：VAR_AGG-方差](<index.php?doc-view-1392.html>)
[下一篇：MEDIAN_AGG-中位数 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1391.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
