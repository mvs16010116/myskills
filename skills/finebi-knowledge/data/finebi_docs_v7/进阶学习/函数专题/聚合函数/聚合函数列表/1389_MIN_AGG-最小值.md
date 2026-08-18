---
title: MIN_AGG-最小值
doc_id: 1389
url: https://help.fanruan.com/finebi/doc-view-1389.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:09
version: "7.X"
---

> 1. 概述语法MIN_AGG(array)根据当前分析维度，返回指标字段的最小值，生成结果为一数据列，行数与当前分析维度行数一致。参数array必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# MIN_AGG-最小值
[__](<doc-edit-1389.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1389.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| MIN_AGG(array)| 根据当前分析维度，返回指标字段的最小值，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
实时数据支持使用一个任意类型的参数。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段MIN_AGG(销量)返回的值为每日的最小值销量。
当用户横轴为维度字段'月'时，MIN_AGG(销量)返回的值为每月的最小值销量。
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：MAX_AGG-最大值](<index.php?doc-view-1390.html>)
[下一篇：AVG_AGG-平均值 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1393.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
