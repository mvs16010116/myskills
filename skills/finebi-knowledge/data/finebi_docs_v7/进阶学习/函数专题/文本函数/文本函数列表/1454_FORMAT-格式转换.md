---
title: FORMAT-格式转换
doc_id: 1454
url: https://help.fanruan.com/finebi/doc-view-1454.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:14
version: "7.X"
---

> 1. 概述在进行数据分析时，经常需要对某个数据进行格式调整的情形，在 FineBI 中有一个专门进行格式调整的函数：FORMAT。语法FORMAT(object,format)返回 object 的 f

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FORMAT-格式转换
[__](<doc-edit-1454.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1454.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
在进行数据分析时，经常需要对某个数据进行格式调整的情形，在 FineBI 中有一个专门进行格式调整的函数：FORMAT。
语法| FORMAT(object,format)| 返回 object 的 format 格式  
---|---|---  
参数1| object| 需要被格式化对象，可以是 String ，数字，Object (常用的有Date, Time)。注：实时数据只支持日期类型。  
参数2| format| 格式化的样式  
## 2\. 注意事项
  * 可使用两个参数，抽取数据第一个参数为任意类型，第二个参数类型为文本
  * 实时数据中第一个参数为日期类型，第二个参数为文本类型。
  * FORMAT 对日期的操作，日期的大小写必须按照年份小写 yy 或 yyyy，月份大写 M 或 MM，日期小写 d 或 dd。
  * [[直连]Kyligence企业版](<https://help.fanruan.com/finebi7.0/doc-view-1169.html>) 数据库不支持该函数。


## 3\. 示例
下文列出了常用的格式参数，包括日期格式和数据格式。  

以 2021-06-15 时间为例。
### 3.1 日期时间格式参数
格式参数  
| 输出  
---|---  
D  
| 166  
DD| 166  
M| 6  
MM| 06  
MMM| 六月  
MMMM| 六月  
YY| 21  
YYYY| 2021  
YYYYMM| 202106  
MM/dd/yyyy| 06/15/2021  
M-d-yy| 6-15-21  
EEEEE, MMMMM dd, yyyy| 星期二, 六月 15, 2021  
h:mm:ss a| 12:00:00 上午  
例如，需要去掉日期字段的小时数据。
创建新增公式列，命名并输入公式：TODATE(FORMAT(ingestTime,"yyyy-MM-dd"))。得到结果如下图所示：
![2022-08-30_15-50-09.png](https://help.fanruan.com/core/style/lod.png)
### 3.2 数值格式参数
以 1234.56 为例。  

参数格式  
| 公式| 输出  
---|---|---  
#,##0.00| FORMAT(1234.5, "#,##0.00")| 1234.50  
"#,##0| FORMAT(1234.5, "#,##0") | 1234  
￥#,##0.00| FORMAT(1234.5, "￥#,##0.00") | ￥1234.50  
0%| FORMAT(1.5, "0%") | 150%  
0.000%| FORMAT(1.5, "0.000%")| 150.000%  
##0.0E0| FORMAT(6789, "##0.0E0") | 6.789E3  
0.00E00| FORMAT(6789, "0.00E00")| 6.79E03  
  * 0 显示一数字，若此位置没有数字则补 0
  * # 显示一数字，若此位置没有数字则不显示
  * % 数字乘以 100 并在右边加上”%”号字符


### 3.3 其他组合函数使用
公式| 结果| 备注  
---|---|---  
FORMAT(date(2007,1,1), "EEEEE, MMMMM dd, yyyy")| 星期一，一月 01，2007|   
  
FORMAT(date(2007,1,13), "MM/dd/yyyy") | 01/13/2007|   
  
FORMAT(date(2007,1,13), "M-d-yy") | 1-13-07|   
  
FORMAT(time(16,23,56), "h:mm:ss a") | 4:23:56 下午|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：INDEXOF-返回指定位置的字符](<index.php?doc-view-1467.html>)
[下一篇：FIND-返回字符所在位置 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1468.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
