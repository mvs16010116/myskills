---
title: DATETONUMBER-日期转化为13位时间戳
doc_id: 1412
url: https://help.fanruan.com/finebi/doc-view-1412.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:26
version: "7.X"
---

> 1. 什么是时间戳？时间戳（Timestamp）是计算机中表示时间的一种方式，指从 1970 年 1 月 1 日 00:00:00 UTC（称为 Unix 纪元）开始，到某一时刻所经过的总秒数或毫秒数。

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# DATETONUMBER-日期转化为13位时间戳
[__](<doc-edit-1412.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1412.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-26 
[](<javascript:;>) [](<javascript:>)
## 1\. 什么是时间戳？
时间戳（Timestamp）是计算机中表示时间的一种方式，指从 1970 年 1 月 1 日 00:00:00 UTC（称为 Unix 纪元）开始，到某一时刻所经过的总秒数或毫秒数。
例如，时间戳 1748275200 表示从 1970 年 1 月 1 日零点起，已经过去了约 17.48 亿秒，对应的实际时间为 2026 年 5 月 26 日。
由于时间戳是一个统一的数值，不受地区、语言、格式和时区差异的影响，因此被广泛应用于数据库存储、系统日志、接口传输等场景，便于时间数据的存储、比较与计算。
常见的时间戳分为两种：
  * **秒级时间戳** ：10 位数字，精确到秒
  * **毫秒级时间戳** ：13 位数字，精确到毫秒


## 2\. 抽取数据
**1）概述**  

语法  
| DATETONUMBER(date)| 返回自1970年1月1日00:00:00GMT经过的毫秒数。  
---|---|---  
参数| date| 5.1.12 以及之后的版本 date 只可以为文本、日期，按照1900年的系列数逻辑处理，例如35796为1998-01-01。   
**2）注意事项**  

  * 支持一个日期或文本类型参数，超过则不合法


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DATETONUMBER("2008-08-08")| 1,218,124,800,000|   
  
DATETONUMBER(35796)| 883,612,800,000|   
  
## 3\. 实时数据
**1）概述**  

语法  
| DATETONUMBER(date)| 返回自1970年1月1日00:00:00GMT经过的毫秒数。  
---|---|---  
参数| date| date：只支持文本、日期类型。  
**2）注意事项**  

  * 支持一个日期或文本类型参数，超过则不合法。


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DATETONUMBER("2008-08-08")| 1,218,124,800,000|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：DATESUBDATE-日期时间差](<index.php?doc-view-1411.html>)
[下一篇：DAY-日期中的日 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1407.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
