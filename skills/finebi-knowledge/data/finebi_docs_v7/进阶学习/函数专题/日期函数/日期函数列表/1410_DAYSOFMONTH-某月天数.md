---
title: DAYSOFMONTH-某月天数
doc_id: 1410
url: https://help.fanruan.com/finebi/doc-view-1410.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:27
version: "7.X"
---

> 1.&nbsp;抽取数据1）概述语法DAYSOFMONTH(date)返回从1900年1月后某年某月包含的天数。参数datedate除了支持文本、日期类型，还可以是系列数，如在1900年日期系统，199

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# DAYSOFMONTH-某月天数
[__](<doc-edit-1410.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1410.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-12-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**
语法  
| DAYSOFMONTH(date)| 返回从1900年1月后某年某月包含的天数。  
---|---|---  
参数| date| date除了支持文本、日期类型，还可以是系列数，如在1900年日期系统，1998年1月1日存为系列数35796。   
  
**2）注意事项**  

  * 支持一个日期或文本类型参数，超过则不合法


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DAYSOFMONTH("1900-02-01")| 28|   
  
DAYSOFMONTH("2008/04/04")| 30|   
  
DAYSOFMONTH(35796)| 31|   
  
## 2\. 实时数据
**1）概述**  

语法  
| DAYSOFMONTH(date)| 返回从1900年1月后某年某月包含的天数。  
---|---|---  
参数| date| date只支持文本、日期类型  
  
**2）注意事项**  

  * 支持一个日期或文本类型参数，超过则不合法


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DAYSOFMONTH("1900-02-01")| 28|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：DAY-日期中的日](<index.php?doc-view-1407.html>)
[下一篇：DAYSOFQUARTER-某季度天数 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1418.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
