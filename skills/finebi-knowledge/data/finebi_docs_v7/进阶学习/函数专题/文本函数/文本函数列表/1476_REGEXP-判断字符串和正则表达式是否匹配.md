---
title: REGEXP-判断字符串和正则表达式是否匹配
doc_id: 1476
url: https://help.fanruan.com/finebi/doc-view-1476.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:08
version: "7.X"
---

> 1. 抽取数据1.1 用法一1）概述语法REGEXP(str, pattern)字符串 str 是否与正则表达式 pattern 相匹配参数1str字符串参数2pattern正则表达式2）注意事项若要使

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# REGEXP-判断字符串和正则表达式是否匹配
[__](<doc-edit-1476.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1476.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-08-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 抽取数据
### 1.1 用法一
**1）概述**
语法| REGEXP(str, pattern)| 字符串 str 是否与正则表达式 pattern 相匹配  
---|---|---  
参数1| str| 字符串  
参数2| pattern| 正则表达式  
**2）注意事项**
  * 若要使用\字符，需要再添加一个反斜杠。所以当公式为regexp(字符串,"\d")时会提示不合法，需写成regexp(字符串,"\\\d")，如下图所示：


![](https://help.fanruan.com/core/style/lod.png)
  

  * 两个文本类型参数  



**3）示例**
公式| 结果| 备注  
---|---|---  
REGEXP("aaaaac","a*c")| true|   
  
REGEXP("abc","a*c")| false|   
  
本文以 \d 和 \w 为例，在编辑数据中使用该函数，其中 \d 表示匹配数字，\w 表示匹配字母或数字或下划线或汉字，如下图所示：  

![1623297122X6d4.png](https://help.fanruan.com/core/style/lod.png)
  

更多正则表达式示例详情参见：[正则表达式示例](<https://help.fanruan.com/finebi7.0/doc-view-1155.html>)
### 1.2 用法二
**1）概述**
语法| REGEXP(str, pattern, intNumber)| 字符串 str 是否与具有给定模式 intNumber 的正则表达式 pattern 相匹配  
---|---|---  
参数1| str| 字符串  
参数2| pattern| 正则表达式  
参数3| intNumber| 给定模式  
**2）注意事项**  

intNumber 的模式如下所示 ：
通过设置intNumber为两种模式之和可以同时开启多种模式，如intNumber=1+2=3则表示同时开启 Unix行模式及不区分大小写的匹配模式
**intNumber 模式**| **概念**  
---|---  
intNumber=1 | UNIX_LINES 启用Unix行模式，在此模式下，"."、"^"、"$"的行为中仅识别" "行结束符  
intNumber=2| CASE_INSENSITIVE 启用不区分大小写的匹配。默认情况下，不区分大小写的匹配假定仅匹配US-ASCII字符集中的字符。可以通过指定UNICODE_CASE模式连同此模式来启用Unicode感知的、不区分大小写的匹配。  
intNumber=4| COMMENTS 启用允许使用空格和注释模式。此模式将忽略空格和在结束行之前以#开头的嵌入式注释。  
intNumber=8| MULTILINE 启用多行模式  
intNumber=16| LITERAL 启用文本分析的模式。启用此模式后，输入字符串就会作为字面值字符序列来对待。输入序列中的元字符或转义序列不具有任何特殊意义。CASE_INSENSITIVE 模式和 UNICODE_CASE 模式在与此模式一起使用时将对匹配产生影响。其他模式下无影响。  
intNumber=32| DOTALL 启用dotall模式，表达式"."可以匹配任何字符，包括行结束符。默认情况下，此表达式不匹配行结束符。  
intNumber=64| UNICODE_CASE 启用Unicode感知的大小写折叠。指定此模式并同时制定CASE_INSENSITIVE模式时，不区分大小写的匹配将以符合Unicode标准的方式完成。  
intNumber=128| CANON_EQ 启用规范等效模式，启用此模式后，当且仅当其完整规范分解匹配时，两个字符才可视为匹配。  
  * 支持前两个参数为文本，第三个参数为数值类型**  
**


**3）示例**
公式| 结果| 公式说明  
---|---|---  
REGEXP("Aaaaabbbbc","a*b*c", 3)| true| 表示同时开启 Unix行模式及不区分大小写的匹配模式。因此返回 true  
REGEXP("Aaaaabbbbc","a*b*c", 1)| false| 表示同时开启 Unix行模式，由于区分大小写，因此返回 false  
REGEXP("Abc","abc", 2)| true| 表示开启不区分大小写模式，因此返回 true  
REGEXP("Abc","abc", 2)，如下图所示：  

![1623297137YJXx.png](https://help.fanruan.com/core/style/lod.png)
## 2\. 直连版本
**1）概述**
语法| REGEXP(str,pattern)| 字符串str是否与正则表达式pattern相匹配  
---|---|---  
参数1| str| 字符串  
参数2| pattern| 正则表达式  
**2）注意事项**
第一个参数为文本类型，第二个参数为文本类型。
[SAP Sybase](<https://help.fanruan.com/finebi7.0/doc-view-307.html>) 数据库和 [Microsoft SQL Server](<https://help.fanruan.com/finebi7.0/doc-view-100.html>) 数据库不支持该函数。
**3）示例**
公式| 结果| 备注  
---|---|---  
REGEXP("aaaaac","a*c")| true|   
  
REGEXP("abc","a+c")| false|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：REPEAT-重复显示文本](<index.php?doc-view-1462.html>)
[下一篇：PROPER-转换文本大小写 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1475.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
