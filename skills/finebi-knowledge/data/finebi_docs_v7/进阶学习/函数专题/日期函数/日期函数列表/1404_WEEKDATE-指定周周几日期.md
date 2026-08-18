---
title: WEEKDATE-指定周周几日期
doc_id: 1404
url: https://help.fanruan.com/finebi/doc-view-1404.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:40
version: "7.X"
---

> 1. 概述语法WEEKDATE(year,month,weekOfMonth,dayOfWeek)返回指定年月的指定周的周几的具体日期。参数1year年参数2month月参数3weekOfMonth月的

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# WEEKDATE-指定周周几日期
[__](<doc-edit-1404.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1404.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2021-11-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| WEEKDATE(year,month,weekOfMonth,dayOfWeek)| 返回指定年月的指定周的周几的具体日期。  
---|---|---  
参数1| year| 年  
  
参数2| month| 月  
参数3| weekOfMonth| 月的指定周  
参数4| dayOfWeek| 返回指定年月的指定周的周几的具体日期  
## 2\. 注意事项
  * 抽取数据支持设置四个数值/文本参数。
  * 实时数据中支持使用四个数值类型参数。


## 3\. 示例
公式  
| 结果| 备注  
---|---|---  
WEEKDATE(2009,10,2,1)| 2009-10-04| 返回的是2009年的10月的第二个周的第一天即星期天的日期  
WEEKDATE(2009,12,1,-1)| 2009-12-05| 返回的是2009年的12月的第一个周的最后一天即星期六的日期  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：WEEK-求周数](<index.php?doc-view-1419.html>)
[下一篇：WEEKDAY-星期数 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1420.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
