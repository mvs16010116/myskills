---
title: ENDWITH-判断字符串结束情况
doc_id: 1455
url: https://help.fanruan.com/finebi6.X/doc-view-1455.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:11
---

> 1. 概念语法ENDWITH(str1,str2)判断字符串 str1 是否以 str2 结束参数1str1字符串参数2str2字符串2. 注意事项str1 和 str2 都是大小写敏感的。支持使用两个

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# ENDWITH-判断字符串结束情况
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[5](<edition-list-1455.html>)
* 最近更新：[Ellie23](<user-space-1308124.html>) 于 2022-11-17 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法| ENDWITH(str1,str2)| 判断字符串 str1 是否以 str2 结束  
---|---|---  
参数1| str1| 字符串  
参数2| str2| 字符串  
## 2\. 注意事项
  * str1 和 str2 都是大小写敏感的。
  * 支持使用两个任意参数。
  * ENDWITH 函数为文本函数，仅能判断文本，不支持对时间类型进行判断。


## 3\. 示例
例如想要判断省份中的「自治区」。  

使用内置数据「分公司维度表」，输入公式：ENDWITH(省份,"自治区")，可以判断出「省份」字段是否是以「自治区」结尾的，如下图所示：
![](/core/style/lod.png)
将「省份」和「判断是否是自治区」字段拖入分组表，如果是自治区则返回1，否则返回0，如下图所示：  

![](/core/style/lod.png)
更多示例：
公式| 结果| 备注  
---|---|---  
ENDWITH("FineReport","Report")| true| -  
ENDWITH("FineReport","Fine")| false| -  
ENDWITH("FineReport","report")| false| -  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：EXACT-判断两文本是否相同](<index.php?doc-view-1460.html>)
[下一篇：CONCATENATE-合并字段 ![](/core/style/forward.png) ](<index.php?doc-view-1470.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
