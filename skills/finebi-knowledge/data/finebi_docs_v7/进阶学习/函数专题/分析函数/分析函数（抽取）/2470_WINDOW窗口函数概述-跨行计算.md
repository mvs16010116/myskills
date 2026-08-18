---
title: WINDOW窗口函数概述-跨行计算
doc_id: 2470
url: https://help.fanruan.com/finebi/doc-view-2470.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:21
version: "7.X"
---

> 1. 概述注：本函数仅适用于自助分析主题。1.1 版本FineBI版本功能变动6.1.2-注：直连数据环境下，部分数据库不支持使用此函数，如 mysql、click&nbsp;house 建议切换成抽取

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# WINDOW窗口函数概述-跨行计算
[__](<doc-edit-2470.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[32](<edition-list-2470.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-05-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于自助分析主题。**
### 1.1 版本
FineBI版本  
| 功能变动  
---|---  
6.1.2| -  
注：直连数据环境下，部分数据库不支持使用此函数，如 mysql、click house 建议切换成抽取数据分析。
### 1.2 功能简介
WINDOW 窗口函数常用于行间计算的场景，在对数据进行分组、排序后，对窗口上下限内的数据进行计算。
#### 语法
**WINDOW_汇总方式(聚合方式(指标) ,[分组字段1, 分组字段2.... ],[排序字段1,排序方式,排序字段2, 排序方式...],[窗口上限,窗口下限])**
#### 参数  

窗口函数基于「[分析视图](<https://help.fanruan.com/finebi7.0/doc-view-829.html#de116f203db18dc1>)」进行计算，函数内的指标/分组字段/排序字段需要均为聚合性质，且维度字段均需要来源于分析视图 
参数| 说明  
---|---  
指标| 不可为空  
分组字段| 缺省则不按照任何字段分组   
排序字段| 缺省则按照默认顺序计算  
排序方式| 支持 "asc"、"desc" 两个关键词，分别对应升序和降序排序，如缺省需要缺省所有排序方式，缺省则按照排序字段升序进行计算  
窗口上限/下限| 支持 "first"、"last" ，分别代表组内第一行/组内最后一行；支持数值常量，0代表当前行，-n代表当前行的前n行，n代表当前行的后n行缺省则按照["first","last"]使用组内全部计算  
#### 返回值  

返回窗口中的所有行，对行内的指标依据「汇总方式」进行计算。
注：不同的 WINDOW 函数对应不同的汇总方式，汇总方式包括「求和，平均，最大值，最小值，标准差，方差」。除此以外，窗口函数还有 [RANK_AGG-按指定规则排序](<https://help.fanruan.com/finebi7.0/doc-view-2478.html>) 函数，支持对字段分组后按指定规则排序。详情见下文。
#### 函数类型
window函数| 场景  
---|---  
[WINDOW_SUM-跨行求和/求累计](<https://help.fanruan.com/finebi7.0/doc-view-2477.html>)| [比较当前节点和上一节点的转化率](<https://help.fanruan.com/finebi7.0/doc-view-2477.html#a0b4b7be27ea4b77>)[逐月展示前三个月销售额](<https://help.fanruan.com/finebi7.0/doc-view-2221.html>)  
[WINDOW_AVG-跨行求平均](<https://help.fanruan.com/finebi7.0/doc-view-2472.html>)| [求移动平均](<https://help.fanruan.com/finebi7.0/doc-view-2230.html>)  
  
[WINDOW_MAX-跨行求最大值](<https://help.fanruan.com/finebi7.0/doc-view-2473.html>)| -  
[WINDOW_MIN-跨行求最小值](<https://help.fanruan.com/finebi7.0/doc-view-2474.html>)| -  
[WINDOW_STDEV-跨行求标准差](<https://help.fanruan.com/finebi7.0/doc-view-2475.html>)| -  
[WINDOW_VAR-跨行求方差](<https://help.fanruan.com/finebi7.0/doc-view-2476.html>)| -  
[RANK_AGG-按指定规则排序](<https://help.fanruan.com/finebi7.0/doc-view-2478.html>)| [并列排名不占位](<https://help.fanruan.com/finebi7.0/doc-view-923.html>)[交叉表求横向排名](<https://help.fanruan.com/finebi7.0/doc-view-2478.html#7b543aba22fe6c53>)  
#### 说明
WINDOW 窗口函数不同汇总方式，可通过写不同公式控制窗口上下限内的数据进行计算。
注：每个单元格计算的窗口上下限的定义不一定相同。
类型| 数值| WINDOW_SUM -求和| WINDOW_AVG-求平均| WINDOW_MAX-求最大值| WINDOW_MIN-求最小值  
---|---|---|---|---|---  
A| 10| 50 =（B+C）| 25 =（B+C）/2| 30 =MAX（B+C）| 20 =MIN（B+C）  
B| 20| 60 =（A+B+C）| 20 =（A+B+C）/3| 30 =MAX（A+B+C）| 10 =MIN（A+B+C）  
C| 30| 60 =（A+B+C）  
| 20 =（A+B+C）/3| 30 =MAX（A+B+C）| 10 =MIN（A+B+C）  
D| 40| 60 =（A+B+C）  
| 20 =（A+B+C）/3| 30 =MAX（A+B+C）| 10 =MIN（A+B+C）  
E| 50| 140 =（B+C+D+E）  
| 35 =（B+C+D+E）/4| 50 =MAX（B+C+D+E）| 20 =MIN（B+C+D+E）  
F| 60| 120 =（C+D+E）| 40 =（C+D+E）/3| 60 =MAX（C+D+E）| 30 =MIN（C+D+E）  
### 1.3 应用场景
窗口函数能够单独输出字段或和 DEF 函数组合使用。对分析视图的字段进行计算时，窗口函数比使用 EARLIER 函数进行跨行计算更简单、更易理解、性能更优。
**一般场景**
WINDOW 函数基于分析视图进行聚合计算，即依据已生成的组件结果进行计算（不包含明细表）如：
  * 求累计  

  * 求组内累计
  * 求近三行移动平均
  * 求分组下近三行移动平均


**嵌套场景**
****
****
当 WINDOW 和 DEF 类函数嵌套使用时，基于 DEF 函数下的独立视图进行计算，这种情况下如果使用的是 DEF 函数（指定维度）可输出明细级别的字段。
DEF+WINDOW 的嵌套场景下支持在自助数据集和明细表中使用 WINDOW 函数。
## 2\. 使用位置
  
| 使用位置  
---|---  
自助数据集  
| [新增公式列](<https://help.fanruan.com/finebi7.0/doc-view-1526.html>)  
组件| [添加计算字段](<https://help.fanruan.com/finebi7.0/doc-view-118.html>)  
注：WINDOW 函数输出的是聚合字段，在自助数据集中不支持直接输出，需要与 DEF 函数组合后输出明细级别字段。
## 3\. 注意事项
  * WINDOW 基于分析视图进行计算，指标/分组字段/排序字段需要均为聚合性质，且维度字段均需要来源于分析视图 
  * WINDOW 函数输出的是聚合字段，在自助数据集中不支持直接输出，需要与 DEF 函数组合后输出明细级别字段。
  * 如果对于排序要求较高，建议把排序字段和排序方式都依次罗列到 WINDOW 函数中。未指定的字段按照默认顺序计算


**年月累计场景**
由于当前 WINDOW 计算时所使用的字段都是从待分析区进行选择，来对应分析区的字段。而我们分析区又支持日期分组、自定义维度分组。当一个字段被重复拖入分析区并设置多种分组方式时， WINDOW 计算会将字段设置的所有分组都带入计算。
例如，「合同签约时间」在分析区按「年」分组，然后再次拖入后按「月份」分组。WINDOW 函数计算的「合同签约时间」会按年月分组参与计算。如下图所示：
![2024-08-16_15-09-18.png](https://help.fanruan.com/core/style/lod.png)
如果我们要求按年分组下，各月的购买数量累计，需要**在待分析区域复制「合同签约时间」** 字段并重命名用于区分不同分组。
![2024-08-16_15-27-08.gif](https://help.fanruan.com/core/style/lod.png)
在分析区拖入字段「年、月」并依次设置分组。添加计算字段「购买数量组内累计值」，计算对「年」分组后，按月依次累计的购买数量。
2013 年的购买数量按月依次累计，效果如下图所示：
![2024-08-16_15-28-17.png](https://help.fanruan.com/core/style/lod.png)
## 4\. 示例
示例数据：[超市销售数据.xlsx](<doc-download-/finebi6.X/uploads/file/20240816/超市销售数据.xlsx> "下载资料")
1）制作分组表，拖入「订单日期、销售额」求不同年月的销售额情况。如下图所示：  

![2024-08-16_14-28-55.png](https://help.fanruan.com/core/style/lod.png)
2）计算近三个月销售额移动平均，如下图所示：
公式=WINDOW_AVG(SUM_AGG(销售额),[],[订单日期],[-2,0])
![2024-08-16_14-31-58.png](https://help.fanruan.com/core/style/lod.png)
公式内容  
| 说明| 备注  
---|---|---  
WINDOW_AVG(SUM_AGG(销售额))| 销售额跨行求平均| [WINDOW_AVG-跨行求平均](<https://help.fanruan.com/finebi7.0/doc-view-2472.html>)  
  
参数2：[]| 不对数据进行分组|   
  
参数3：订单日期  
| 按订单日期（年月）升序
  * 排序字段：订单日期
  * 排序方式：未写排序方式，因此默认升序排列

| 不写排序方式默认升序  
参数4：[-2,0]| 获取窗口范围内的数据
  * 窗口上限 -2：依据排列顺序从前两行取数
  * 窗口下限 0：取数取到当前行结束

| 按订单日期（年月）顺序获取前两行和当前行数据，求移动平均  
  
完成后，将字段拖入分组表，并设置数值格式为「万」。如下图所示：
![2024-08-16_14-33-55.png](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：CLEAN_WIDGET函数-清除组件过滤效果（只用于DEF类函数）](<index.php?doc-view-2408.html>)
[下一篇：WINDOW_AVG-跨行求平均 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2472.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
