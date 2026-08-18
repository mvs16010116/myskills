---
title: BI函数与Excel函数对应
doc_id: 1349
url: https://help.fanruan.com/finebi/doc-view-1349.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:21:58
version: "7.X"
---

> 1. 概述FineBI 支持多种函数和功能的使用，这些函数或者功能在使用方式上与常用的 Excel 函数有一些不同，本文提供对比说明，帮助有 Excel 使用基础的用户快速上手使用 BI 中的函数与功能

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# BI函数与Excel函数对应
[__](<doc-edit-1349.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[23](<edition-list-1349.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2024-11-01 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineBI 支持多种函数和功能的使用，这些函数或者功能在使用方式上与常用的 Excel 函数有一些不同，本文提供对比说明，帮助有 Excel 使用基础的用户快速上手使用 BI 中的函数与功能。
## 2\. 聚合函数
FineBI 函数/功能| Excel 函数| 函数说明  
  
---|---|---  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4##3>)[SUM_AGG](<https://help.fanruan.com/finebi7.0/doc-view-1385.html>)| SUM()| 求一组数据的和  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4##17>)[AVG_AGG](<https://help.fanruan.com/finebi7.0/doc-view-1393.html>)| AVERAGE()| 求一组数据平均数  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html#9>)[MAX_AGG](<https://help.fanruan.com/finebi7.0/doc-view-1390.html>)  
| MAX()| 求一组数据最大值  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html#5>)[MIN_AGG](<https://help.fanruan.com/finebi7.0/doc-view-1389.html>)| MIN()| 求一组数据最小值  
[COUNT_AGG](<https://help.fanruan.com/finebi7.0/doc-view-1386.html>)| COUNT()| COUNT 函数计算包含数字的单元格个数以及参数列表中数字的个数  
**注意事项：**
用 COUNT_AGG 函数计算的有金额的单元格行数，即非空的金额的单元格个数，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
也可以直接用 [记录数](<https://help.fanruan.com/finebi7.0/doc-view-362.html>) ，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 统计函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
IF(boolean,number1/string1,number2/string2)| IF(logical_test, value_if_true, [value_if_false])| 条件判断  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4##3>)[DEF](<https://help.fanruan.com/finebi7.0/doc-view-1986.html>) / [DEF_ADD](<https://help.fanruan.com/finebi7.0/doc-view-1987.html>) 与 SUM_AGG 合并使用例如，计算出 省份为云南、分类为家具 的销售额DEF(SUM_AGG(销售额),[],[省份="云南"，分类="家具"])| SUMIF/SUMIFS| 条件汇总  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html#7>)[](<https://help.fanruan.com/finebi7.0/doc-view-1386.html>)[DEF](<https://help.fanruan.com/finebi7.0/doc-view-1986.html>) / [DEF_ADD](<https://help.fanruan.com/finebi7.0/doc-view-1987.html>) 与 COUNTD_AGG 合并使用例如，计算出 省份为云南 的订单数量DEF(COUNTD_AGG(订单编号),[],[省份="云南"]）| COUNTIF/COUNTIFS| 条件计数  
[](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4##17>)[DEF](<https://help.fanruan.com/finebi7.0/doc-view-1986.html>) / [DEF_ADD](<https://help.fanruan.com/finebi7.0/doc-view-1987.html>) 与 AVG_AGG 合并使用例如，计算出家具类别平均一单的销售额DEF(AVG_AGG(销售额),[],[分类="家具"])| AVERAGEIF/AVERAGEIFS| 条件求平均  
  

## 4\. 逻辑函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
[IF](<https://help.fanruan.com/finebi7.0/doc-view-1377.html>) 函数嵌套使用| IFS| 检查是否满足一个或多个条件，且返回符合第一个 TRUE 条件的值  
不支持| NOT| 对其参数的逻辑求反   
使用 IF 和其他函数嵌套满足  
| IFERROR| IFERROR 返回公式计算结果为错误时指定的值；否则，它将返回公式的结果。  
[AND](<https://help.fanruan.com/finebi7.0/doc-view-1383.html>)| AND| 逻辑与  
[OR](<https://help.fanruan.com/finebi7.0/doc-view-1384.html>)| OR| 逻辑或  
IFERROR 函数在 BI 中应用的示例，示例已知销售额和销量，需要计算对应产品的销售单价。  

示例数据：[销售情况.xlsx](<doc-download-/finebi5.1/uploads/file/20210611/销售情况.xlsx> "下载资料")
上传数据至 FineBI 中，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
使用数据集创建仪表板后，添加计算字段，输入公式：IF(SUM_AGG(销量)=0,"计算有误",SUM_AGG(销售额)/SUM_AGG(销量))，
由于需要计算销售单价，需要使用聚合函数SUM_AGG(销售额)/SUM_AGG(销量)，同时为保证计算结果的正确性，需要使用 IF 函数，判断销量是否为0，由于 IF 函数不能同时使用聚合和非聚合函数，因此进行的判断也要使用(SUM_AGG(销量)=0 格式，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
将「产品」和新增字段拖入分析栏，得到结果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
公式  
| 说明| 结果  
---|---|---  
IF(SUM_AGG(销量)=0,"计算有误",SUM_AGG(销售额)/SUM_AGG(销量))| 如果销量=0，则除法无法生效，输出“计算有误”| 计算有误  
如果销量不等于0，则输出计算结果| 0  
333.333333333  
## 5\. 引用函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
先用数据集排序，数据集/仪表板用IF函数写判断赋值| match| 找等于/接近查询值的位置行数  
MATCH 函数在 BI 中应用的示例：
例如需要计算升序排名在第1位的合同金额，可以先使用数据集进行排名，然后使用函数返回指定数据，结果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 6\. 文本函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
[LEN](<https://help.fanruan.com/finebi7.0/doc-view-1472.html>)| LEN| 求字段长度  
[LEFT](<https://help.fanruan.com/finebi7.0/doc-view-1457.html>)不支持 LEFTB| LEFT、LEFTB| 左截取  
[RIGHT](<https://help.fanruan.com/finebi7.0/doc-view-1465.html>)不支持 RIGHTB| RIGHT、RIGHTB| 右截取  
  
[MID](<https://help.fanruan.com/finebi7.0/doc-view-1459.html>)不支持 midb| mid、midb| MID 返回文本字符串中从指定位置开始的特定数目的字符  
[TRIM](<https://help.fanruan.com/finebi7.0/doc-view-1453.html>)| Trim| 清除文本首尾所有的空格  
[FIND](<https://help.fanruan.com/finebi7.0/doc-view-1468.html>)不支持 Findb| Find、Findb| 找字符位置  
不支持查字符位置可用 find 代替使用| search，searchb| 找字符位置  
1）[CONCATENATE](<https://help.fanruan.com/finebi7.0/doc-view-1470.html>)2）数据集>分组汇总>字符串拼接注：concatenate 函数拼接时默认返回文本类型字段。| concatenate| 将数个字符串合并成一个字符串  
1）添加计算指标用 IF 函数进行数值转指定文本2）[CONCATENATE](<https://help.fanruan.com/finebi7.0/doc-view-1470.html>) 拼接后返回的默认就是文本类型，不需要使用text转换。| text  
| TEXT 函数可通过格式代码向数字应用格式，进而更改数字的显示方式。   
## 7\. 数值函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
[ROUND](<https://help.fanruan.com/finebi7.0/doc-view-1379.html>)| round| ROUND 函数将数字四舍五入到指定的位数  
[MOD](<https://help.fanruan.com/finebi7.0/doc-view-1439.html>)| mod| 返回两数相除的余数。 结果的符号与除数相同。  
不支持，可通过添加计算字段换算| conver| 度量值转换  
添加计算指标，两字段直接相乘即可| sumproduct| 返回相应范围或数组的个数之和。 默认操作是乘法  
[RANK_ANLS](<https://help.fanruan.com/finebi7.0/doc-view-1216.html>)| rank| 返回一列数字的数字排位  
[](<https://help.fanruan.com/finebi7.0/doc-view-131.html>)[表格汇总方式](<https://help.fanruan.com/finebi7.0/doc-view-130.html>)  
| SUBTOTAL|  返回列表或数据库中的分类汇总  
## 8\. 日期函数
FineBI 函数/功能| Excel 函数| 函数说明  
---|---|---  
[](<https://help.fanruan.com/finebi7.0/doc-view-7.html#47>)[WEEKDAY](<https://help.fanruan.com/finebi7.0/doc-view-1420.html>)[](<https://help.fanruan.com/finebi7.0/doc-view-7.html#47>)注：默认返回值为介于 0 到 6 之间的某一整数，分别代表星期中的某一天（从星期日到星期六）。| WEEKDAY| 返回对应于某个日期的一周中的第几天  
[DATEDIF](<https://help.fanruan.com/finebi7.0/doc-view-1402.html>)(start_date,end_date,unit)| DATEDIF| 返回两个指定日期间的天数、月数或年数  
[](<https://help.fanruan.com/finebi7.0/doc-view-7.html#35>)[DATE](<https://help.fanruan.com/finebi7.0/doc-view-1414.html>)  
| DATE| 返回特定日期的系列数  
[](<https://help.fanruan.com/finebi7.0/doc-view-7.html#49>)[TODAY](<https://help.fanruan.com/finebi7.0/doc-view-1421.html>)  
| TODAY| 获取当前日期  
[YEAR](<https://help.fanruan.com/finebi7.0/doc-view-1400.html>)| year| 返回某年包含的天数  
## 9\. 运算符
含义| FineBI 写法  
| Excel 写法  
---|---|---  
不等于| !=| <>  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：【函数学习路径】](<index.php?doc-view-1709.html>)
[下一篇：函数计算格式 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
