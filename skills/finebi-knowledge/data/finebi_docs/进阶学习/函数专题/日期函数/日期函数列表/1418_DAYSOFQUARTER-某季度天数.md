---
title: DAYSOFQUARTER-某季度天数
doc_id: 1418
url: https://help.fanruan.com/finebi6.X/doc-view-1418.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:22
---

> 1. 抽取数据1）概述语法DAYSOFQUARTER(date)返回从 1900 年 1 月后某年某季度的天数参数date抽取数据除了支持文本、日期类型，还可以是系列数，如在1900年日期系统，1998

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# DAYSOFQUARTER-某季度天数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1418.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**
语法  
| DAYSOFQUARTER(date)| 返回从 1900 年 1 月后某年某季度的天数  
---|---|---  
参数| date| 抽取数据除了支持文本、日期类型，还可以是系列数，如在1900年日期系统，1998年1月1日存为系列数35796。  
**2）注意事项**
  * 只支持一个日期或文本类型参数


**3）示例**
公式  
| 结果| 备注  
---|---|---  
DAYSOFQUARTER("2009-02-01")| 90|   
  
DAYSOFQUARTER("2009/05/05")| 91|   
  
DAYSOFQUARTER(35796)| 90|   
  
## 2\. 实时数据
**1）概述**
语法| DAYSOFQUARTER(date)| 返回从1900年1月后某年某季度的天数  
---|---|---  
参数| date| 只支持文本、日期类型  
**2）注意事项**
  * 只支持一个参数，该参数为日期或文本类型。


**3）示例**
公式  
| 结果| 备注  
---|---|---  
DAYSOFQUARTER("2009-02-01")| 90|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：DAYSOFMONTH-某月天数](<index.php?doc-view-1410.html>)
[下一篇：DAYSOFYEAR-一年的天数 ![](/core/style/forward.png) ](<index.php?doc-view-1399.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
