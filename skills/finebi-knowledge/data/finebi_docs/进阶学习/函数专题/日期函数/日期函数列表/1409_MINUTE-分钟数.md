---
title: MINUTE-分钟数
doc_id: 1409
url: https://help.fanruan.com/finebi6.X/doc-view-1409.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:26
---

> 1. 抽取数据1）概述语法MINUTE(serial_number,格式)返回某一指定时间的分钟数，其值是介于0与59之间的一个整数参数1serial_number包含所求分钟数的时间&nbsp;参数2

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# MINUTE-分钟数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1409.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**  

语法  
| MINUTE(serial_number,格式)| 返回某一指定时间的分钟数，其值是介于0与59之间的一个整数  
---|---|---  
参数1| serial_number| 包含所求分钟数的时间   
  
参数2| 格式| 例如 HH:mm:ss  
**2）注意事项**  

  * 允许MINUTE(serial_number,格式)内参数为空，即MINUTE()，当参数为空时，取当前系统的服务器时间对应的分钟数。
  * 第一个参数缺省日期或文本类型，第二个缺省参数文本


**3）示例**
公式| 结果  
| 备注  
---|---|---  
MINUTE()| 36| 对应系统服务器时间为2020-10-23 15:36:25  
MINUTE("15:36:25")| 36|   
  
MINUTE("15:36:25","HH:mm:ss")| 36|   
  
## 2\. 实时数据
**1）概述**  

语法  
| MINUTE(serial_number)| 返回某一指定时间的分钟数，其值是介于0与59之间的一个整数  
---|---|---  
参数| serial_number| 包含所求分钟数的时间   
  
**2）注意事项**  

允许MINUTE(serial_number)内参数为空，即MINUTE()，当参数为空时，取当前系统的服务器时间对应的分钟数。
可使用缺省日期或一个文本类型参数。
**3）示例**
公式| 结果  
| 备注  
---|---|---  
MINUTE()| 36| 对应系统服务器时间为2020-10-23 15:36:25  
MINUTE("15:36:25")| 36|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：LUNAR-农历日期](<index.php?doc-view-1408.html>)
[下一篇：MONTH-日期中的月份 ![](/core/style/forward.png) ](<index.php?doc-view-1398.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
