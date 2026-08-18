---
title: DATESUBDATE-日期时间差
doc_id: 1411
url: https://help.fanruan.com/finebi6.X/doc-view-1411.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:20
---

> 1. 概述语法DATESUBDATE(date1,date2,op)返回两个日期之间的时间差。参数1date1date1,date2表示要输入的两个日期，当date1早于date2时，是负值；date1

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# DATESUBDATE-日期时间差
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1411.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-17 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| DATESUBDATE(date1,date2,op)| 返回两个日期之间的时间差。  
---|---|---  
参数1| date1| date1,date2表示要输入的两个日期，当date1早于date2时，是负值；date1晚于date2，是正值，若date1/2为数值，按照1900年的系列数逻辑处理，例如35796为1998-01-01。   
注：实时数据只支持文本、日期类型。  
参数2| date2  
参数3| op| 表示返回的时间单位："s"或"S"，以秒为单位。"m"或"M"，以分钟为单位。"h"或"H"，以小时为单位。"d"或"D"，以天为单位。"w"或"W"，以周为单位。  
## 2\. 注意事项
  * 抽取数据支持三个参数，前两个日期或文本类型参数，第三个要求文本；第三个参数支持S、M、H、D、W，不区分大小写
  * 实时数据中，第一、二个日期或文本类型参数，第三个是文本类型参数。


## 3\. 示例
公式| 结果  
| 备注  
---|---|---  
DATESUBDATE("2008-08-08","2008-06-06","h")| 1512|   
  
DATESUBDATE("2008-06-06","2008-08-08","H")| -1512|   
  
## 4\. 示例二
想要计算两个日期字段之间的间隔天数，例如「注册时间」和「合同签约时间」之间的间隔天数，新增一个字段，用 DATESUBDATE 函数计算两者的天数，公式为：DATESUBDATE(注册时间,合同签约时间,"D")，如下图所示：
![2.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：DATEDELTA-返回后几天日期](<index.php?doc-view-1403.html>)
[下一篇：DATETONUMBER-日期转化为13位时间戳 ![](/core/style/forward.png) ](<index.php?doc-view-1412.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
