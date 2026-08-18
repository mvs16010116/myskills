---
title: NUMTO-数字转中文格式
doc_id: 1456
url: https://help.fanruan.com/finebi6.X/doc-view-1456.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:05
---

> 1. 概述语法NUMTO(number,bool)或 NUMTO (number)返回 number 的中文表示参数1number数字参数2boolean其中boolean用于选择中文表示的方式，当bo

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# NUMTO-数字转中文格式
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1456.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2023-07-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| NUMTO(number,bool)或 NUMTO (number)| 返回 number 的中文表示  
---|---|---  
参数1| number| 数字  
参数2| boolean| 其中boolean用于选择中文表示的方式，当boolean缺省时采用默认方式显示。默认为 false  
## 2\. 注意事项
  * 支持设置两个参数，第一个参数为数值类型，第二个缺省参数可为布尔类型。
  * 直连数据不支持该函数。
  * 参数中的true(TRUE)、false（FALSE），同时支持大小写。


## 3\. 示例
想要将「总金额」修改为中文形式，例如 120000，希望展示为：十二万，可使用公式：NUMTO(总金额)，如下图所示：
![2022-08-30_15-57-25.png](/core/style/lod.png)
更多示例：
公式| 结果| 备注  
---|---|---  
NUMTO(2345,true)| 二三四五|   
  
NUMTO(2345,false)| 二千三百四十五|   
  
NUMTO(2345)| 二千三百四十五|   
  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：PROPER-转换文本大小写](<index.php?doc-view-1475.html>)
[下一篇：MID-返回指定位置字符串 ![](/core/style/forward.png) ](<index.php?doc-view-1459.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
