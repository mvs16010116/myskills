---
title: RANDBETWEEN-返回两个数相同整数部分
doc_id: 1435
url: https://help.fanruan.com/finebi6.X/doc-view-1435.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:37
---

> 1. 概述语法RANDBETWEEN(value1,value2)返回value1和value2之间的一个随机整数当两个数整数部分相同时，返回两个数相同整数部分。参数value1,value2value

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# RANDBETWEEN-返回两个数相同整数部分
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1435.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2022-07-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| RANDBETWEEN(value1,value2)| 返回value1和value2之间的一个随机整数当两个数整数部分相同时，返回两个数相同整数部分。  
---|---|---  
参数| value1,value2| value1,value2任意数值  
## 2\. 注意事项
  * 支持两个数值参数。 


## 3\. 示例
公式| 结果  
---|---  
RANDBETWEEN(12.333,13.233)| 只会返回13。  
RANDBETWEEN(11.2,13.3)| 有可能返回12或者13。  
RANDBETWEEN(12.333,12.233)| 只会返回12。  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：SIN-正弦值](<index.php?doc-view-1451.html>)
[下一篇：RADIANS-将角度转换成弧度 ![](/core/style/forward.png) ](<index.php?doc-view-1450.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
