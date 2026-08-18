---
title: TRUNC-返回指定位数
doc_id: 1433
url: https://help.fanruan.com/finebi6.X/doc-view-1433.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:33
---

> 1. 概述语法TRUNC(number,num_digits)将数字的一定位数截去，返回整数或小数。&nbsp;参数1number需要截尾取整的数字。参数2num_digits用于指定取整精度的数字。2

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# TRUNC-返回指定位数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-1433.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| TRUNC(number,num_digits)| 将数字的一定位数截去，返回整数或小数。   
---|---|---  
参数1| number| 需要截尾取整的数字。  
参数2| num_digits| 用于指定取整精度的数字。  
## 2\. 注意事项
  * 支持两个数值参数，第二个可缺省，缺省后为整数。


## 3\. 示例
公式  
| 结果| 备注  
---|---|---  
TRUNC(8.9)| 8|   
  
TRUNC(-8.9)| -8|   
  
TRUNC(-8.98,1)| -8.9|   
  
TRUNC(PI())| 3|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：MAX-返回最大值](<index.php?doc-view-1431.html>)
[下一篇：TAN-正切值 ![](/core/style/forward.png) ](<index.php?doc-view-1452.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
