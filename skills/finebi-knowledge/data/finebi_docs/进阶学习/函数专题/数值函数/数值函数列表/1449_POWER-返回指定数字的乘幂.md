---
title: POWER-返回指定数字的乘幂
doc_id: 1449
url: https://help.fanruan.com/finebi6.X/doc-view-1449.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:40
---

> 1. 概述语法POWER(number,power)返回指定数字的乘幂参数1number底数，可以为任意实数参数2power指数。参数number按照该指数次幂乘方。2. 注意事项&nbsp;支持两个数

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# POWER-返回指定数字的乘幂
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1449.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-04-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| POWER(number,power)| 返回指定数字的乘幂  
---|---|---  
参数1| number| 底数，可以为任意实数  
参数2| power| 指数。参数number按照该指数次幂乘方。  
## 2\. 注意事项
  * 支持两个数值参数。 
  * 可以使用符号“^”代替POWER，如: POWER(5,2)等于5^2。
  * 负数底数时，指数需为整数，否则报错。  



## 3\. 示例
公式  
| 结果| 备注  
---|---|---  
POWER(6,2)| 36| 6^2=6*6  
POWER(14,5)| 537824| 14^5=14*14*14*14*14  
POWER(4,2/3)| 2.52| 3√（4^2）即3√16  
POWER(3,-2/3)| 0.48| 3√（1/9）  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：PI-一个数学常量](<index.php?doc-view-1448.html>)
[下一篇：MOD-返回两数相除的余数 ![](/core/style/forward.png) ](<index.php?doc-view-1439.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
