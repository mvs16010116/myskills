---
title: CLEAN_WIDGET函数-清除组件过滤效果（只用于DEF类函数）
doc_id: 2408
url: https://help.fanruan.com/finebi6.X/doc-view-2408.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:15
---

> 1. 概述1.1 版本FineBI版本功能变动6.1-1.2 语法语法CLEAN_WIDGET(字段1,字段2,字段3....)/CLEAN_WIDGET(&quot;ALL&quot;)当前分析函数计

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# CLEAN_WIDGET函数-清除组件过滤效果（只用于DEF类函数）
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-2408.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI版本  
| 功能变动  
---|---  
6.1| -  
### 1.2 语法
语法  
| CLEAN_WIDGET(字段1,字段2,字段3....)/CLEAN_WIDGET("ALL")| 当前分析函数计算中忽略指定字段在组件中生成的过滤效果  
---|---|---  
参数| 字段1,字段2,字段3....| 需要忽略过滤效果的字段
  * 支持任意类型的维度/指标字段，包括计算指标
  * 当 CLEAN_WIDGET 中的参数为“ALL”时，清除分析函数中所有字段在组件中生成过滤效果
  * 参数不支持缺省

  
## 2\. 注意事项
  * 只能用于 def/def_add/def_sub 中，作为一个独立的过滤条件。 


## 3\. 和CLEAN函数的区别
3.1 计算范围  

两者区别主要体现在忽略的过滤效果范围不同。CLEAN_WIDGET 只清除组件内产生的过滤效果，对仪表板中的过滤效果不生效。
范围| 字段过滤| CLEAN_WIDGET (字段1,字段2,字段3....)| CLEAN_WIDGET ("ALL")  
---|---|---|---  
组件| 
  * 过滤器
  * 钻取

| 忽略字段过滤效果| 忽略分析函数所有字段过滤效果  
仪表板| 
  * 联动
  * 跳转
  * 过滤组件

| 正常产生过滤效果| 正常产生过滤效果  
### 3.2 在DEF中的计算逻辑
与 CLEAN 函数逻辑一致。详情参见：[CLEAN函数](<https://help.fanruan.com/finebi6.X/doc-view-2407.html>)
## 4\. 示例 
公式  
| 结果| 备注  
---|---|---  
DEF(SUM_AGG(指标),[省份,城市],[CLEAN_WIDGET(城市)])| 在DEF计算中忽略组件中「城市」字段产生的过滤效果|   
  
DEF_ADD(SUM_AGG(),[],[CLEAN_WIDGET("ALL")])| 在DEF_ADD计算中忽略组件中全部的过滤效果|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：CLEAN函数-清除所有过滤效果（只用于DEF类函数）](<index.php?doc-view-2407.html>)
[下一篇：WINDOW窗口函数概述-跨行计算 ![](/core/style/forward.png) ](<index.php?doc-view-2470.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
