---
title: YEARDELTA-某日期后几年
doc_id: 1417
url: https://help.fanruan.com/finebi6.X/doc-view-1417.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:36
---

> 1. 概述语法YEARDELTA(date, delta)返回指定日期后delta年的日期。参数date表示输入的日期。抽取数据中date除了支持文本、日期类型，还支持1900年的系列数，例如35796

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# YEARDELTA-某日期后几年
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1417.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| YEARDELTA(date, delta)| 返回指定日期后delta年的日期。  
---|---|---  
参数| date| 表示输入的日期。
  * 抽取数据中date除了支持文本、日期类型，还支持1900年的系列数，例如35796为1998-01-01   

  * 实时数据中只支持文本、日期类型。

  
## 2\. 注意事项
  * 支持两个参数，第一个参数为日期或文本类型，第二个参数为数值类型。


## 3\. 示例
公式| 结果  
| 备注  
---|---|---  
YEARDELTA("2008-10-10",10)| 2018-10-10|   
  
YEARDELTA(35796,10)| 2008-01-01| 实时数据不支持该写法  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：YEAR-返回年份](<index.php?doc-view-1400.html>)
[下一篇：常用日期公式 ![](/core/style/forward.png) ](<index.php?doc-view-1326.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
