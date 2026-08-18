---
title: WINDOW_STDEV-跨行求标准差
doc_id: 2475
url: https://help.fanruan.com/finebi/doc-view-2475.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:25
version: "7.X"
---

> 1. 概述注：本函数仅适用于自助分析主题。语法WINDOW_STDEV(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])返回

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# WINDOW_STDEV-跨行求标准差
[__](<doc-edit-2475.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-2475.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-05-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于自助分析主题。**
语法| WINDOW_STDEV(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])| 
  * 返回窗口表达式的标准差
  * window基于分析视图进行计算，指标/分组字段/排序字段需要均为聚合性质，且维度字段均需要来源于分析视图

  
---|---|---  
参数1| 指标| 不可为空  
参数2| 分组字段| 缺省则不按照任何字段分组  
参数3| 排序字段| 缺省则按照默认顺序计算  
参数4| 排序方式| 支持 "asc"、"desc" 两个关键词，分别对应升序和降序排序；如缺省需要缺省所有排序方式，缺省则按照排序字段升序进行计算  
**参数5**|  窗口上限/下限| 窗口计算范围，支持 "first"、"last" ，分别代表组内第一行/组内最后一行；支持数值常量；
  * 0 代表当前行
  * -n 代表当前行的前 n 行
  * n 代表当前行的后 n 行

缺省则按照["first","last"]使用组内全部计算  
## 2\. 注意事项
详情请参见：[WINDOW函数概述-注意事项](<https://help.fanruan.com/finebi7.0/doc-view-2470.html#ccc39a2096c7b9fc>)
## 3\. 示例
公式| 结果| 备注  
---|---|---  
WINDOW_STDEV(SUM_AGG(销售额), [ 城市 ],[SUM_AGG(销售额)],[-2,0])| 求“城市”组内连续三行销售额的标准差|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：WINDOW_MIN-跨行求最小值](<index.php?doc-view-2474.html>)
[下一篇：WINDOW_VAR-跨行求方差 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2476.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
