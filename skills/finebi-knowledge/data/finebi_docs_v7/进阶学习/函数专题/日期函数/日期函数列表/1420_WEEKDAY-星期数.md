---
title: WEEKDAY-星期数
doc_id: 1420
url: https://help.fanruan.com/finebi/doc-view-1420.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:40
version: "7.X"
---

> 1. 概述语法WEEKDAY(serial_number)获取日期并返回星期数。返回值为介于0到6之间的某一整数，分别代表星期中的某一天（从星期日到星期六）。参数serial_number表示输入的日期

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# WEEKDAY-星期数
[__](<doc-edit-1420.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1420.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-13 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| WEEKDAY(serial_number)| 获取日期并返回星期数。返回值为介于0到6之间的某一整数，分别代表星期中的某一天（从星期日到星期六）。  
---|---|---  
参数| serial_number| 表示输入的日期  
抽取数据中：除文本、日期类型，还支持1900年的系列数，例如35796为1998-01-01实时数据中：只支持文本、日期类型  
## 2\. 注意事项
  * 支持使用一个日期或文本类型参数。  



## 3\. 示例
公式| 结果  
| 备注  
---|---|---  
WEEKDAY("2005/9/10")| 6| （星期六）注：实时数据不支持2005/9/10 格式，需要改为 2005-09-10 格式。  
WEEKDAY("2005/9/11")| 0| （星期日）注：实时数据不支持2005/9/11 格式，需要改为 2005-09-11 格式。  
WEEKDAY(35796)| 4| （星期四）实时数据不支持该写法  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：WEEKDATE-指定周周几日期](<index.php?doc-view-1404.html>)
[下一篇：YEAR-返回年份 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1400.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
