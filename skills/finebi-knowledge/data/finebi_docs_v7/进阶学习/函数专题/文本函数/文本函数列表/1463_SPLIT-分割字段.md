---
title: SPLIT-分割字段
doc_id: 1463
url: https://help.fanruan.com/finebi/doc-view-1463.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:05
version: "7.X"
---

> 1. 概念语法SPLIT(String1,String2 )返回由String2分割String1组成的字符串数组参数1String1以双引号表示的字符串参数2String2以双引号表示的分隔符。例如逗

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# SPLIT-分割字段
[__](<doc-edit-1463.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1463.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法| SPLIT(String1,String2 )| 返回由String2分割String1组成的字符串数组  
---|---|---  
参数1| String1| 以双引号表示的字符串  
参数2| String2| 以双引号表示的分隔符。例如逗号","  
## 2\. 注意事项
  * 不支持直连数据中使用。
  * 支持使用两个任意类型参数。
  * 6.0 公式不支持正则表达式  



## 3\. 示例
例如想要将「客户名称」xxx有限公司中的「有限公司」分割。
输入公式：SPLIT(客户名称,"有限公司")
![](https://help.fanruan.com/core/style/lod.png)
得到如下数据：
![](https://help.fanruan.com/core/style/lod.png)
更多示例：  

公式| 结果| 备注  
---|---|---  
SPLIT("hello,world,yes",",")| [hello,world,yes]| -  
SPLIT("this is very good"," ")| [this,is,very,good]| -  
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：STARTWITH-判断字符串 str1 是否以 str2 开始](<index.php?doc-view-1477.html>)
[下一篇：RIGHT-截取后几个字符串 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1465.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
