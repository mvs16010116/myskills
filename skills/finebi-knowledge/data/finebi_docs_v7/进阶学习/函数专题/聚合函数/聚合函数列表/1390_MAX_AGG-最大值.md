---
title: MAX_AGG-最大值
doc_id: 1390
url: https://help.fanruan.com/finebi/doc-view-1390.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:08
version: "7.X"
---

> 1. 概述语法MAX_AGG(array)根据当前分析维度，返回指标字段的最大值，生成结果为一数据列，行数与当前分析维度行数一致。参数array必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# MAX_AGG-最大值
[__](<doc-edit-1390.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1390.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-02-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| MAX_AGG(array)| 根据当前分析维度，返回指标字段的最大值，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。array为非数值字段时只支持在def函数中使用。  
## 2\. 注意事项
  * 实时数据支持使用一个任意类型的参数。
  * 函数不支持在自助数据集使用。  



## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段MAX_AGG(销量)返回的值为每日的最大值销量。
当用户横轴为维度字段'月'时，MAX_AGG(销量)返回的值为每月的最大值销量。
### 3.1 计算当前维度下最大时间
你需要计算当前维度下的最大时间，例如「合同签约时间」每月数据中的最大时间，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
点击+，添加计算字段「最大时间」，输入公式：FORMAT(TODATE(MAX_AGG(DATETONUMBER(合同签约时间))),"YYYY-MM-dd HH:mm:ss")，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
公式说明：
公式  
| 说明  
---|---  
DATETONUMBER(合同签约时间)| 自1970年1月1日00:00:00GMT到「合同签约时间」经过的毫秒数。  
MAX_AGG(DATETONUMBER(合同签约时间))| 取当前维度下的最大毫秒数，返回数值类型  
TODATE(MAX_AGG(DATETONUMBER(合同签约时间)))| 将当前维度下的最大毫秒数转为「日期型」  
FORMAT(TODATE(MAX_AGG(DATETONUMBER(合同签约时间))),"YYYY-MM-dd HH:mm:ss")| 对日期型的最大合同签约时间修改格式为「年月日时分秒」格式  
将「合同签约时间」字段拖入横轴，并设置为按月分组，然后将「最大时间」也拖入横轴即可，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：SUM_AGG-求和](<index.php?doc-view-1385.html>)
[下一篇：MIN_AGG-最小值 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1389.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
