---
title: DATETONUMBER-日期转化为13位时间戳
doc_id: 1412
url: https://help.fanruan.com/finebi6.X/doc-view-1412.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:20
---

> 1. 抽取数据1）概述语法DATETONUMBER(date)返回自1970年1月1日00:00:00GMT经过的毫秒数。参数date5.1.12 以及之后的版本 date 只可以为文本、日期，按照19

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# DATETONUMBER-日期转化为13位时间戳
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[3](<edition-list-1412.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2021-12-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
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
  
## 2\. 实时数据
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
[![](/core/style/back.png)上一篇：DATESUBDATE-日期时间差](<index.php?doc-view-1411.html>)
[下一篇：DAY-日期中的日 ![](/core/style/forward.png) ](<index.php?doc-view-1407.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
