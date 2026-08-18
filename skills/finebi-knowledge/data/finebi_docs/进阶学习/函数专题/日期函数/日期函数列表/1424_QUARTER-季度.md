---
title: QUARTER-季度
doc_id: 1424
url: https://help.fanruan.com/finebi6.X/doc-view-1424.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:30
---

> 1. 抽取数据1）概述语法QUARTER(serial_number,格式)返回时间所在季度，若无参数则返回当前服务器时间所在季度参数1serial_number可以为空，参数类型为任意参数2格式可以为

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# QUARTER-季度
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[3](<edition-list-1424.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-11-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**  

语法  
| QUARTER(serial_number,格式)| 返回时间所在季度，若无参数则返回当前服务器时间所在季度  
---|---|---  
参数1| serial_number| 可以为空，参数类型为任意  
参数2| 格式| 可以为空，参数类型为文本  
返回值| 数值| 返回数值  
**2）示例**  

公式| 结果  
| 备注  
---|---|---  
QUARTER()| 当前服务器时间所在季度|   
  
QUARTER("2017-03-07 00:00:00")| 1|   
  
QUARTER("2017/03/07")| 1  
|   
  
## 2\. 实时数据
**1）概述**  

语法  
| QUARTER:(serial_number)| 返回时间所在季度，若无参数则返回当前服务器时间所在季度  
---|---|---  
参数1| serial_number| 可以为空，参数类型为日期或文本  
返回值| 数值| 返回数值  
2**）示例**
公式| 结果  
| 备注  
---|---|---  
QUARTER()| 当前服务器时间所在季度|   
  
QUARTER("2017-03-07 00:00:00")| 1|   
  
QUARTER("2017/03/07")| 1|   
  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：NOW-当前时间](<index.php?doc-view-1415.html>)
[下一篇：SECOND-秒数 ![](/core/style/forward.png) ](<index.php?doc-view-1423.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
