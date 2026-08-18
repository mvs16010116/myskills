---
title: CONCATENATE-合并字段
doc_id: 1470
url: https://help.fanruan.com/finebi6.X/doc-view-1470.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:12
---

> 1. 概述语法CONCATENATE(text1,text2,...)将数个字符串合并成一个字符串参数1Text1,text2,...需要合并成单个文本的文本项2. 注意事项可使用多个任意类型参数3.

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# CONCATENATE-合并字段
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1470.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-08-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| CONCATENATE(text1,text2,...)| 将数个字符串合并成一个字符串  
---|---|---  
参数1| Text1,text2,...| 需要合并成单个文本的文本项  
## 2\. 注意事项
可使用多个任意类型参数
## 3\. 示例
例如，创建新增列将省份城市合并成一个字段，输入公式：CONCATENATE(省份,城市)，得到结果如下图所示：
![2022-08-30_16-32-03.png](/core/style/lod.png)
更多示例：
公式| 结果| 备注  
---|---|---  
CONCATENATE("Average ","Price")| Average Price|   
  
CONCATENATE("1","2")| 12|   
  
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：ENDWITH-判断字符串结束情况](<index.php?doc-view-1455.html>)
[下一篇：CODE-返回数值代码 ![](/core/style/forward.png) ](<index.php?doc-view-1474.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
