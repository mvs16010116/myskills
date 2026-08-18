---
title: WINDOW_SUM-跨行求和/求累计
doc_id: 2477
url: https://help.fanruan.com/finebi6.X/doc-view-2477.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:16
---

> 1. 概述语法WINDOW_SUM(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])返回窗口表达式的合计值window基于分

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# WINDOW_SUM-跨行求和/求累计
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[5](<edition-list-2477.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-10-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| WINDOW_SUM(指标,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])| 
  * 返回窗口表达式的合计值
  * window基于分析视图进行计算，指标/分组字段/排序字段需要均为聚合性质，且维度字段均需要来源于分析视图

  
---|---|---  
参数1| 指标| 不可为空  
参数2| 分组字段| 缺省则不按照任何字段分组  
参数3| 排序字段| 缺省则按照默认顺序计算  
参数4| 排序方式| 支持 "asc"、"desc" 两个关键词，分别对应升序和降序排序；如缺省需要缺省所有排序方式，缺省则按照排序字段升序进行计算  
参数5| 窗口上限/下限| 窗口计算范围，支持 "first"、"last" ，分别代表组内第一行/组内最后一行；支持数值常量；
  * 0 代表当前行
  * -n 代表当前行的前 n 行
  * n 代表当前行的后 n 行

缺省则按照["first","last"]使用组内全部计算  
## 2\. 注意事项
详情请参见：[WINDOW函数概述-注意事项](<https://help.fanruan.com/finebi6.X/doc-view-2470.html#ccc39a2096c7b9fc>)
## 3\. 示例
  

公式| 结果| 备注  
---|---|---  
WINDOW_SUM(SUM_AGG(销售额), [ 城市 ],[SUM_AGG(销售额)],[-2,0])| 求“城市”组内连续三行销售额的合计值|   
  
WINDOW_SUM(SUM_AGG(销售额),[],[SUM_AGG(销售额)],["first",0])| 按照销售额大小求累计|   
  
WINDOW_SUM(SUM_AGG(销售额),[产品],[月份],["first",0])| 不同产品的月累计情况|   
  
  

例如，我们已经在组件中，制作了分组表，如下图所示：
![1723462880307616.png](/core/style/lod.png)
基于分析视图的「合同付款类型」分组，根据「总金额」升序，得到组内累计值。
「合同金额组内累计值」公式：WINDOW_SUM(SUM_AGG(﻿总金额﻿),[合同付款类型﻿],[SUM_AGG(﻿总金额﻿),"asc"],["first",0])
![1723466188921898.png](/core/style/lod.png)
## 4\. 比较当前节点和上一节点的转化率
很多时候我们都需要获取错行值，比如计算上一个日期与下一个日期的差，又比如计算上一步数据到下一步数据的转化率。
这里以计算转化率为例，我们需要获取「上一行」的值，便于我们两列相除。
  

![2024-08-14_14-18-24.png](/core/style/lod.png)
示例数据：[汽车行业销售漏斗.xlsx](<doc-download-/finebi6.X/uploads/file/20240814/汽车行业销售漏斗.xlsx> "下载资料")
### 4.1 分析各节点客户数
分析关键节点的客户数，并降序排列。如下图所示：
![2024-08-14_14-21-00.png](/core/style/lod.png)
### 4.2 求上一行的值
添加计算字段，求每个关键节点上一行的客户数。如下图所示：
上一行客户数=WINDOW_SUM(SUM_AGG(﻿客户数﻿),[],[SUM_AGG(客户数﻿),"desc"],[-1,-1])
![2024-08-14_14-33-03.png](/core/style/lod.png)
把「上一行的客户数」拖入组件中。如下图所示：
![1723617103554820.png](/core/style/lod.png)
### 4.3 求转化率
最后，转化率=SUM_AGG(客户数)/上一行的客户数，求出每个节点的转化率情况。如下图所示：
![2024-08-14_14-35-52.png](/core/style/lod.png)
将「每个节点转化率」拖入组件分析区域，完成分析。如下图所示：
![2024-08-14_14-37-32.png](/core/style/lod.png)
## 5\. 逐月展示近三月的销售总额
详情请参见：[逐月展示前三个月销售额](<https://help.fanruan.com/finebi6.X/doc-view-2221.html>)
![2024-08-15_15-46-47.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：WINDOW_AVG-跨行求平均](<index.php?doc-view-2472.html>)
[下一篇：WINDOW_MAX-跨行求最大值 ![](/core/style/forward.png) ](<index.php?doc-view-2473.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
