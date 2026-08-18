---
title: MONTHDELTA-返回后几个月日期
doc_id: 1401
url: https://help.fanruan.com/finebi6.X/doc-view-1401.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:28
---

> 1. 概述语法MONTHDELTA(date,delta)返回指定日期date后delta个月的日期。参数delta对于抽取数据 date除了支持文本、日期类型，还支持1900年系列数，例如35796为

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# MONTHDELTA-返回后几个月日期
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1401.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2021-06-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| MONTHDELTA(date,delta)| 返回指定日期date后delta个月的日期。  
---|---|---  
参数| delta| 对于抽取数据 date除了支持文本、日期类型，还支持1900年系列数，例如35796为1998-01-01。注：实时数据中 date 只支持文本、日期类型。   
  
## 2\. 注意事项
支持两个参数，第一个参数为日期或文本类型，第二个参数为数值类型。
## 3\. 示例
公式| 结果  
| 备注  
---|---|---  
MONTHDELTA("2008-08-08",4)| 2008-12-08|   
  
MONTHDELTA(35796,4)| 1998-05-01| 实时数据不支持该写法  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：MONTH-日期中的月份](<index.php?doc-view-1398.html>)
[下一篇：NOW-当前时间 ![](/core/style/forward.png) ](<index.php?doc-view-1415.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
