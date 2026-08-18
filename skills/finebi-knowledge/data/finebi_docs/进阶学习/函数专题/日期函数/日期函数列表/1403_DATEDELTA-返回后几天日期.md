---
title: DATEDELTA-返回后几天日期
doc_id: 1403
url: https://help.fanruan.com/finebi6.X/doc-view-1403.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:19
---

> 1. 抽取数据1）概述语法DATEDELTA(date,deltadays)返回一个日期date后deltadays的日期。参数1datedate除了支持文本、日期类型，还支持1900年系列数，例如35

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# DATEDELTA-返回后几天日期
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1403.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2021-11-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**  

语法  
| DATEDELTA(date,deltadays)| 返回一个日期date后deltadays的日期。  
---|---|---  
参数1| date| date除了支持文本、日期类型，还支持1900年系列数，例如35796为1998-01-01。   
  
参数2| deltaDays| 可以为正值，负值，零  
**2）注意事项**  

  * 支持两个参数，第一个日期或文本类型参数，第二个参数为数值


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DATEDELTA("2008-08-08",-10)| 2008-07-29|   
  
DATEDELTA("2008-08-08",10)| 2008-08-18|   
  
DATEDELTA(35796,10)| 1998-01-11|   
  
[DATEDELTA](<https://help.fanruan.com/finebi6.0/doc-view-1403.html>)([TODAY](<https://help.fanruan.com/finebi6.0/doc-view-1421.html>)(),-1)| 昨天|   
  
## 2\. 实时数据
**1）概述**  

语法  
| DATEDELTA(date,deltadays)| 返回一个日期date后deltadays的日期。  
---|---|---  
参数1| date| 只支持文本、日期类型  
参数2| deltadays| 可以为正值，负值，零  
**2）注意事项**  

  * 支持两个参数，其中第一个参数为日期或文本类型，第二个参数为数值类型。


**3）示例**
公式| 结果  
| 备注  
---|---|---  
DATEDELTA("2008-08-08",-10)| 2008-07-29|   
  
DATEDELTA("2008-08-08",10)| 2008-08-18|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：DATEDIF-日期差](<index.php?doc-view-1402.html>)
[下一篇：DATESUBDATE-日期时间差 ![](/core/style/forward.png) ](<index.php?doc-view-1411.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
