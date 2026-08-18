---
title: EXACT-判断两文本是否相同
doc_id: 1460
url: https://help.fanruan.com/finebi/doc-view-1460.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:15
version: "7.X"
---

> 1. 概述语法EXACT(text1,text2)检测两组文本是否相同。如果完全相同，EXACT 函数返回 TRUE ；否则，返回 FALSE&nbsp;参数1Text1需要比较的第一组文本参数2Tex

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# EXACT-判断两文本是否相同
[__](<doc-edit-1460.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1460.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| EXACT(text1,text2)| 检测两组文本是否相同。如果完全相同，EXACT 函数返回 TRUE ；否则，返回 FALSE   
---|---|---  
参数1| Text1| 需要比较的第一组文本  
参数2| Text2| 需要比较的第二组文本  
## 2\. 注意事项
  * EXACT 函数可以区分大小写，但忽略格式的不同。同时也可以利用 EXACT 函数来检测输入文档的文字。
  * 可使用两个任意类型参数。


## 3\. 示例
****
公式|  结果| 备注  
---|---|---  
EXACT("Spreadsheet","Spreadsheet")| TRUE |   
  
EXACT("Spreadsheet","S preadsheet")| FALSE |   
  
EXACT("Spreadsheet","spreadsheet")| FALSE |   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FIND-返回字符所在位置](<index.php?doc-view-1468.html>)
[下一篇：ENDWITH-判断字符串结束情况 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1455.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
