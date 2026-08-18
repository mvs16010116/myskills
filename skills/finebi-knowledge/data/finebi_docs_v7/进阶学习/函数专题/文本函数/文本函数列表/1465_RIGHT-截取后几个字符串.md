---
title: RIGHT-截取后几个字符串
doc_id: 1465
url: https://help.fanruan.com/finebi/doc-view-1465.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:06
version: "7.X"
---

> 1. 概述语法RIGHT(text,num_chars)根据指定的字符数从右开始返回文本串中的最后一个或几个字符参数1Text包含需要提取字符的文本串参数2Num_chars指定 RIGHT 函数从文本

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# RIGHT-截取后几个字符串
[__](<doc-edit-1465.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[5](<edition-list-1465.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| RIGHT(text,num_chars)| 根据指定的字符数从右开始返回文本串中的最后一个或几个字符  
---|---|---  
参数1| Text| 包含需要提取字符的文本串  
参数2| Num_chars| 指定 RIGHT 函数从文本串中提取的字符数，Num_chars 不能小于 0  
## 2\. 注意事项
  * 支持使用两个参数，第一个为任意类型，第二个为数值类型，可以缺省。
  * 如果 num_chars 大于文本串长度，RIGHT 函数将返回整个文本。如果不指定 num_chars ，则默认值为 1 。


## 3\. 示例
公式| 结果| 备注  
---|---|---  
RIGHT("It is interesting",6)| esting|   
  
RIGHT("Share Holder")| r|   
  
RIGHT("Huge sale",4)| sale|   
  
### 3.1 年月日时分秒字段只显示时分秒
新增列，输入新增列名并输入公式：RIGHT(搜索时间,8)，得到只保留时分秒的数据，如下图所示：
![2022-08-30_16-16-33.png](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：SPLIT-分割字段](<index.php?doc-view-1463.html>)
[下一篇：REPLACE-替换指定位置字符 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1469.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
