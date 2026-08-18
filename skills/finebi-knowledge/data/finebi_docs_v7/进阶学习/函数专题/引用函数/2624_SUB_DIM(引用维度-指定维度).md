---
title: SUB_DIM(引用维度-指定维度)
doc_id: 2624
url: https://help.fanruan.com/finebi/doc-view-2624.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:42
version: "7.X"
---

> 1. 概述1.1 版本FineBI版本功能变动7.0-1.2 函数简介语法SUB_DIM(维度字段1，维度字段2...)返回指定视图中除去函数声明的其他维度指定视图定义：&nbsp;使用在 DEF 维度

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# SUB_DIM(引用维度-指定维度)
[__](<doc-edit-2624.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[18](<edition-list-2624.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI版本| 功能变动  
---|---  
7.0| -  
  
### 1.2 函数简介
语法  
| SUB_DIM(维度字段1，维度字段2...)| 返回指定视图中除去函数声明的其他维度指定视图定义： 
  * 使用在 DEF 维度参数中，指定为外部视图
  * 使用在其他场景下，指定为当前所在视图

  
---|---|---  
参数| 维度字段1，维度字段2...| 支持书写多个维度表达式，表达式之间通过“，”进行区分参数可以为空，为空则输出指定视图的全部维度   
### 1.3 注意事项
函数需要配合 DEF/WINDOW/FIELD_IN 使用。
## 2\. 示例
下载示例数据：[表格图表_办公用品销售数据.xlsx](<doc-download-/finebi/uploads/file/20251127/表格图表_办公用品销售数据.xlsx> "下载资料")
### 2.1 配合 WINDOW 实现组内行间计算 
#### 2.1.1 应用场景
例如月累计销售额场景中，不同角色和分析需求关注的维度不同，需要依据不同的分析需求调整维度，查看月累计销售额。
角色/场景| 分析需求| 维度  
---|---|---  
cfo  
| 分析地区月累计销售额| 省份、城市  
进货预测| 分析商品月累计销售额| 大类、产品名称  
WINDOW 的分组维度没法动态的随着用户在分析区的调整保持始终正确的逻辑，维度在省份、城市和大类、产品名称间切换时，需更改计算字段。
运用 SUB_DIM 函数后，无需调整计算字段，只需更换维度，即可查看相应的月累计销售额。
#### 2.1.2 实现思路
[WINDOW_SUM](<https://help.fanruan.com/finebi7.0/doc-view-2477.html>) 配合 [SUB_DIM](<https://help.fanruan.com/finebi7.0/doc-view-2624.html>) 实现组内行间计算，用「一份数据模型」适应不同维度的月累计销售额展示需求
月累计销售额动态字段=WINDOW_SUM(SUM_AGG(销售额),[SUB_DIM(签约时间)],[签约时间],["first",0]) 
#### 2.1.3 操作步骤
1）准备分析维度：
在分析区依次拖入维度字段「省份」「城市」「签约时间」，并设置「签约时间」按「年月」分组。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）计算组内年月累计销售额：
添加计算字段，计算动态月累计销售额，如下图所示：
组内年月累计销售额=WINDOW_SUM(SUM_AGG(销售额),[SUB_DIM(签约时间)],[签约时间],["first",0]) 
![](https://help.fanruan.com/core/style/lod.png)
步骤  
| 公式| 说明  
---|---|---  
计算指标：销售额之和| SUM_AGG(销售额)| 基础聚合函数，计算销售额的总和详情见文档：[聚合函数概述](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4#>)  
按分析区维度字段分组（排除签约时间）| [SUB_DIM(签约时间)]| SUB_DIM 通常表示返回外部视图的维度，且需排除函数声明里的维度。此处返回分析区除了签约时间的字段：省份、城市，在 WINDOW 函数中按省份、城市分组![](https://help.fanruan.com/core/style/lod.png)  
指定按签约时间排序| [签约时间]| 按签约时间进行升序排列详情见文档：[WINDOW_SUM-跨行求和/求累计](<https://help.fanruan.com/finebi7.0/doc-view-2477.html>)  
求累计| ["first",0]| 窗口范围参数，定义窗口的起始和结束位置"first"表示从分区的第一行开始0 表示到当前行结束详情见文档：[WINDOW_SUM-跨行求和/求累计](<https://help.fanruan.com/finebi7.0/doc-view-2477.html>)  
计算指定窗口范围内的汇总值| WINDOW_SUM(SUM_AGG(销售额),[SUB_DIM(签约时间)],[签约时间],["first",0]) | 
  * 返回窗口表达式的合计值
  * WINDOW 基于分析视图进行计算，指标/分组字段/排序字段需要均为聚合性质，且维度字段均需要来源于分析视图

详情见文档：[WINDOW_SUM-跨行求和/求累计](<https://help.fanruan.com/finebi7.0/doc-view-2477.html>)  
  
3）将「组内年月累计销售额」拖入分析区，完成分析。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
#### 2.1.4 效果预览
计算指定窗口范围内的累计值。可查看每个月省份到城市的组内累计销售额，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
维度切换：例如切换「签约时间」前的维度为「大类」「产品名称」，会自动展示每个产品的月累计销售额，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 2.2 配合DEF+EARLIER实现组内行间计算 
#### 2.2.1 应用场景
例如月累计销售额场景中，不同角色和分析需求关注的维度不同，需要依据不同的分析需求调整维度，查看月累计销售额。
角色/场景| 分析需求| 维度  
---|---|---  
cfo| 分析地区月累计销售额| 省份、城市  
进货预测| 分析商品月累计销售额| 大类、产品名称  
DEF+EARLIER 的分组维度没法动态的随着用户在分析区的调整保持始终正确的逻辑，维度在省份、城市和大类、产品名称间切换时，需更改计算字段。
运用 SUB_DIM 函数后，无需调整计算字段，只需更换维度，即可查看相应的月累计销售额。
#### 2.2.2 实现思路
[DEF](<https://help.fanruan.com/finebi7.0/doc-view-1987.html?source=4>)+[EARLIER](<https://help.fanruan.com/finebi7.0/doc-view-1991.html?source=4>) 配合 [SUB_DIM](<https://help.fanruan.com/finebi7.0/doc-view-2624.html>) 实现组内行间计算，用「一份数据模型」适应不同维度的月累计销售额展示需求
月累计销售额动态字段=DEF_ADD(SUM_AGG(销售额),[],[EARLIER(SUB_DIM(签约时间-月))=SUB_DIM(签约时间-月),月份<=EARLIER(月份)])
#### 2.2.3 操作步骤
1）处理数据表：
我们希望由小月份到大月份对销售额进行累计，为了能够月份之间方便进行比较，我们可以在处理数据表的时候就提取「年份」「月份」。
点击获取时间，获取「订单日期」的年份，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
点击获取时间，获取「订单日期」的月份，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
完成后点击保存更新。
2）准备分析维度：
复制两次「签约时间」维度，重命名为「签约时间-年」「签约时间-月」
在分析区依次拖入维度字段「省份」「城市」「签约时间-年」「签约时间-月」，并设置「签约时间-年」按「年」分组，「签约时间-月」按「月份」分组，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）计算组内年月累计销售额：
添加计算字段，计算动态月累计销售额。如下图所示：
组内年月累计=DEF_ADD(SUM_AGG(销售额),[],[EARLIER(SUB_DIM(签约时间-月))=SUB_DIM(签约时间-月),月份<=EARLIER(月份)])
![](https://help.fanruan.com/core/style/lod.png)
步骤| 公式| 说明  
---|---|---  
计算销售额之和| SUM_AGG(销售额)| 基础聚合函数，计算销售额的总和详情见文档：[聚合函数概述](<https://help.fanruan.com/finebi7.0/doc-view-4.html?source=4#>)  
获取分析维度| []| 自动获取分析区拖入的维度字段  
进行条件分组并获取组内指定行的销售额| [EARLIER(SUB_DIM(签约时间-月))=SUB_DIM(签约时间-月),月份<=EARLIER(月份)]注：当 SUB_DIM() 位于 DEF 的 非维度参数时 ，返回当前视图维度。示例返回的是 **DEF_ADD 维度参数引用的分析区字段 - 「签约时间-月」**| 
  * EARLIER(SUB_DIM(签约时间-月))=SUB_DIM(签约时间-月)：除了「签约时间-月」外，按分析区内其余维度分组
  * 月份<=EARLIER(月份)：获取当前月份及之前的月份销售额，对其求和时得到累计值
  * 详情见文档：[EAELIER](<https://help.fanruan.com/finebi7.0/doc-view-1991.html?source=4>)

  
计算分组下按月累计销售额| DEF_ADD(SUM_AGG(销售额),[],[EARLIER(SUB_DIM(签约时间-月))=SUB_DIM(签约时间-月),月份<=EARLIER(月份)])| 满足过滤条件并按分析区域中的维度对指标进行计算详情见文档：[DEF_ADD](<https://help.fanruan.com/finebi7.0/doc-view-1987.html?source=4>)  
#### 2.2.4 效果预览
将「组内年月累计」拖入分析区，完成分析，可查看每个月省份到城市的累计销售额，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
维度切换：例如切换「签约时间-年」「签约时间-月」前的维度为「大类」「产品名称」，会自动展示每个产品的月累计销售额，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：ADD_DIM(引用维度+指定维度)](<index.php?doc-view-2623.html>)
[下一篇：FIELD_IN(判断数组是否属于) ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2638.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
