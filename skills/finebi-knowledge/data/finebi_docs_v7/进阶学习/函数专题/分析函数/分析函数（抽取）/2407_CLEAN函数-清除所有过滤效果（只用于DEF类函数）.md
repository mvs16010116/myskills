---
title: CLEAN函数-清除所有过滤效果（只用于DEF类函数）
doc_id: 2407
url: https://help.fanruan.com/finebi/doc-view-2407.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:20
version: "7.X"
---

> 1. 概述全部 CLEAN 视频课程请参考：CLEAN函数注：本函数仅适用于自助分析主题。[helpvideo]10572[/helpvideo]1.1 版本FineBI版本功能变动6.1-1.2 语法

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# CLEAN函数-清除所有过滤效果（只用于DEF类函数）
[__](<doc-edit-2407.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[13](<edition-list-2407.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-05-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
全部 CLEAN 视频课程请参考：[CLEAN函数](<https://edu.fanruan.com/video/776>)  

**注：本函数仅适用于自助分析主题。**
### 1.1 版本
FineBI版本  
| 功能变动  
---|---  
6.1| -  
### 1.2 语法
clean的对象是字段，效果是在当前 def 的计算中忽略该字段上的过滤效果。
语法  
| CLEAN(字段1,字段2,字段3....)/CLEAN("ALL")| 当前 [分析函数](<https://help.fanruan.com/finebi7.0/doc-view-1993.html>) 计算中忽略指定字段生成的所有过滤效果  
---|---|---  
参数| 字段1,字段2,字段3....| 需要忽略过滤效果的字段
  * 支持任意类型的维度/指标字段，包括计算指标
  * 当CLEAN中的参数为“ALL”时，清除分析函数中所有字段生成的过滤效果
  * 参数不支持缺省 

  
## 2\. 注意事项
  * CLEAN函数只能用于 def/def_add/def_sub 中，作为一个独立的过滤条件。例如： DEF(SUM_AGG(指标),[省份,城市],[CLEAN(城市)])


## 3\. 计算逻辑
### 3.1 计算范围
**1）clean（字段1,字段2,字段3....）**
clean函数将清除掉字段所做的过滤。示例如下：
范围| 过滤条件| 组件的计算字段| 结果  
---|---|---|---  
组件| 在过滤器添加「城市」字段
  * 过滤1：城市不等于无锡 
  * 过滤2：销售额>100 

| def(sum_agg(销售额),[城市],[clean(城市)])| 忽略**城市** 字段的所有过滤条件  
  
仪表板| 文本下拉过滤：城市=苏州、无锡、常州  
  
**2）clean（all）**
当前 [分析函数](<https://help.fanruan.com/finebi7.0/doc-view-1993.html>) 运算的结果不受到任何过滤效果影响（不包括仪表板/组件外的过滤，如权限过滤和定时调度的过滤）
**3）总结**
因此，CLEAN函数作用范围如下：
范围| 字段过滤| **CLEAN( 字段1,字段2,字段3....)**| CLEAN("ALL")  
---|---|---|---  
组件| 
  * 过滤器
  * 钻取

| 忽略字段过滤效果生效| 忽略分析函数所有字段过滤效果  
仪表板| 
  * 联动
  * 跳转
  * 过滤组件

| 
  * 仅过滤组件忽略字段过滤效果生效

（不包括下拉树/列表树/树标签/复合过滤组件）
  * 联动、跳转产生的过滤 CLEAN（字段1，字段2...）不生效

| 忽略分析函数所有字段过滤效果  
### 3.2 在DEF计算中的逻辑
**1） clean与内层def和同层def过滤条件的关系**
因为def中的过滤仅影响当前def的计算，因此clean不会清除内层和外层def的过滤条件
例如：
层级  
| 计算字段| 公式  
---|---|---  
1| A| def(sum_agg(),[],销售额>100)  
2| B| def(sum_agg(A),[],[**clean(销售额)**])  
3| C| def(sum_agg(B),[],[销售额<300])  
此时，clean 不会对1、3层级的销售额过滤产生影响。  

**2） clean与同层的过滤处于平级的状态**
clean与同层的过滤处于平级的状态，即clean会把上面层级的过滤清掉，同层的过滤正常进行。
例如，def(sum_agg(订单金额),[],[ **clean(月)** ,**月****=7**])，过滤器绑定「月」过滤 ，此时，DEF 计算仅使用「月=7」进行过滤。
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 案例应用
### 4.1 示例
示例数据：[产品销售情况.xlsx](<doc-download-/finebi6.X/uploads/file/20240508/产品销售情况.xlsx> "下载资料")
1）上传数据并分析产品销售情况。拖入「订单金额」修改汇总方式为「最大值」得到单笔订单销售额最大值。如下图所示：  

![2024-05-08_14-02-40.png](https://help.fanruan.com/core/style/lod.png)
2）只想分析 7 月的订单销售数据。在过滤器中拖入「订单日期」，年月过滤，选择「2022年7月」。如下图所示：
![2024-05-08_14-08-53.png](https://help.fanruan.com/core/style/lod.png)
此时，我们希望增加一列历史订单单笔最大金额和7月的数据进行对比。添加计算字段「历史单笔订单最大金额」。如下图所示：
![2024-05-08_14-26-20.png](https://help.fanruan.com/core/style/lod.png)
场景| 公式| 描述  
---|---|---  
计算结果不会受到订单日期过滤的影响| CLEAN(订单日期)| 组件过滤器、仪表板过滤组件对「订单日期」过滤都不会变化计算结果  
求产品订单金额的历史最大值| DEF_ADD(MAX_AGG(订单金额﻿}),[],[CLEAN(﻿订单日期﻿)])| 维度：产品指标：订单金额条件：忽略订单日期过滤条件  
组件中的如下图所示：
![2024-05-08_14-27-07.png](https://help.fanruan.com/core/style/lod.png)
仪表板中效果如下图所示：
![2024-05-08_14-29-35.png](https://help.fanruan.com/core/style/lod.png)
  

### 4.2 更多示例
公式  
| 结果| 备注  
---|---|---  
DEF(SUM_AGG(指标),[省份,城市],[CLEAN(城市)])| 在DEF计算中忽略「城市」字段产生的所有过滤效果| 忽略城市字段在过滤器/钻取/过滤组件产生的过滤（不包含树过滤组件以及复合过滤控件）  
DEF_ADD(SUM_AGG(指标),[维度1，维度2，...],[CLEAN("ALL")])| 在DEF_ADD计算中忽略全部的过滤效果| 忽略所有字段在过滤器/联动/钻取/跳转/过滤组件产生的过滤  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：EARLIER-获取当前行的值（只用于DEF类函数）](<index.php?doc-view-1991.html>)
[下一篇：CLEAN_WIDGET函数-清除组件过滤效果（只用于DEF类函数） ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2408.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
