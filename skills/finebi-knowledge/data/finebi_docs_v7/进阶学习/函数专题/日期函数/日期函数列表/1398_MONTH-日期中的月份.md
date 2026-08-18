---
title: MONTH-日期中的月份
doc_id: 1398
url: https://help.fanruan.com/finebi/doc-view-1398.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:33
version: "7.X"
---

> 1.&nbsp;抽取数据1）概述语法MONTH:(serial_number,格式)返回日期中的月。月是介于1和12之间的一个数。参数1serial_number含有所求的月的日期.除了支持文本、日期类

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# MONTH-日期中的月份
[__](<doc-edit-1398.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1398.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2021-11-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
**1）概述**  

语法  
| MONTH:(serial_number,格式)| 返回日期中的月。月是介于1和12之间的一个数。  
---|---|---  
参数1| serial_number| 含有所求的月的日期.除了支持文本、日期类型，还支持1900年标准的系列数，例如输入35796为1998-01-01。   
  
参数2| 格式| 例如 yyyy-MM-dd  
**2）注意事项**  

  * 允许 MONTH(serial_number,格式)内参数为空，即 MONTH()，当参数为空时，取当前系统的服务器时间对应日期的月数。
  * 第一个缺省参数为日期或文本类型，第二个缺省参数为文本
  * 第二个参数支持yyyy-MM-dd格式  



**3）示例**
公式| 结果  
| 备注  
---|---|---  
MONTH()| 10| 对应系统服务器时间为2020-10-23 15:36:25。  
MONTH("2000/1/1")| 1|   
  
MONTH(35796)| 1|   
  
MONTH("1997-04-20","yyyy-MM-dd")| 4|   
  
## 2\. 实时数据
**1）概述**  

语法  
| MONTH:(serial_number)| 返回日期中的月。月是介于1和12之间的一个数。  
---|---|---  
参数| serial_number| 含有所求的月的日期.只支持文本、日期类型。  
**2）注意事项**  

  * 允许MONTH(serial_number)内参数为空，即MONTH()，当参数为空时，取当前系统的服务器时间对应日期的月数。
  * 可缺省日期或使用一个文本类型参数。
  * 第二个参数支持yyyy-MM-dd格式  



**3）示例**
公式| 结果  
| 备注  
---|---|---  
MONTH()| 10| 对应系统服务器时间为2020-10-23 15:36:25。  
MONTH("2000-01-01")| 1|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：MINUTE-分钟数](<index.php?doc-view-1409.html>)
[下一篇：MONTHDELTA-返回后几个月日期 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1401.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
