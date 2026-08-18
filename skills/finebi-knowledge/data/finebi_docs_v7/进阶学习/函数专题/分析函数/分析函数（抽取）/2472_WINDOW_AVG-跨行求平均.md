---
title: WINDOW_AVG-跨行求平均
doc_id: 2472
url: https://help.fanruan.com/finebi/doc-view-2472.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:22
version: "7.X"
---

> 1. 概述注：本函数仅适用于自助分析主题。语法WINDOW_AVG(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])返回窗口

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# WINDOW_AVG-跨行求平均
[__](<doc-edit-2472.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-2472.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-05-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于自助分析主题。**
语法| WINDOW_AVG(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])| 
  * 返回窗口表达式的平均值
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
1）简单示例
公式| 结果| 备注  
---|---|---  
WINDOW_AVG(SUM_AGG(销售额), [ 城市 ],[SUM_AGG(销售额)],[-2,0])| 求“城市”组内连续三行销售额的平均值|   
  
WINDOW_AVG(SUM_AGG(销售额}),[],[年月],[-1,-1] )| 上月的销售额|   
  
WINDOW_AVG(SUM_AGG(销售额}),[],[年月],[-2,0] )| 近三个月销售额平均值|   
  
WINDOW_AVG(SUM_AGG(销售额),[地区,年份],[月份],[-2,0] )| 大区下当年近三个月的销售额平均值为保证数据准确，年份和月份的来源字段不同|   
  
2）更多示例：[求移动平均](<https://help.fanruan.com/finebi7.0/doc-view-2230.html>)
求近三月的移动平均数值。
![2024-08-13_16-17-39.png](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：WINDOW窗口函数概述-跨行计算](<index.php?doc-view-2470.html>)
[下一篇：WINDOW_SUM-跨行求和/求累计 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2477.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
