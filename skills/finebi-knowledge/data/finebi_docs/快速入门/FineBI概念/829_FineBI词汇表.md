---
title: FineBI词汇表
doc_id: 829
url: https://help.fanruan.com/finebi6.X/doc-view-829.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:37
---

> 1. 概述FineBI 作为一款自助式数据分析产品，提供丰富强大的功能让企业数据分析者，通过高效自助分析，进行数据决策。本文按照各个模块，对 FineBI 产品的特有概念进行解释说明，以便用户进行使用。

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI词汇表
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[46](<edition-list-829.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-09-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineBI 作为一款自助式数据分析产品，提供丰富强大的功能让企业数据分析者，通过高效自助分析，进行数据决策。
本文按照各个模块，对 FineBI 产品的特有概念进行解释说明，以便用户进行使用。
## 2\. 我的分析
![1663567259dfL7.png](/core/style/lod.png)
名词  
| 释义  
  
---|---  
[我的分析](<https://help.fanruan.com/finebi6.0/doc-view-1897.html>)| 用户个人分析资源存储空间，在「我的分析」中用户可以做全流程数据探索分析  
[分析主题](<https://help.fanruan.com/finebi6.0/doc-view-1888.html>)| FineBI 的核心模块，用户完成分析的最基本单元，在「分析主题」内用户可以对数据进行编辑、进行可视化分析以及输出仪表板，完整的分析在一个主题内实现。同时用户可以对主题进行协作，给其他人查看  
[协作](<https://help.fanruan.com/finebi6.X/doc-view-1895.html>)| 将文件夹或者分析主题协作给其他设计用户。
  * 被协作的用户能查看或者使用相关分析主题的内容；
  * 实现分析主题的协同编辑

  
  
![](/core/style/lod.png)
### 2.1 数据
名词  
| 释义  
  
---|---  
[过滤](<https://help.fanruan.com/finebi6.X/doc-view-507.html>)| FineBI 提供了数据过滤功能，业务人员可以对数据进行过滤并保存，以供后续分析使用。  
字段| 字段是数据表中的列，可视化组件制作就是将数据表中的字段拖入分析区域进行分析。因此，字段是实现可视化分析的基础  
[维度](<https://help.fanruan.com/finebi6.X/doc-view-2347.html#8ab5cc5ec8251279>)| 维度指我们分析数据的角度。从不同的维度去分析数据例如：分析不同月份/年份的销售额变化。维度是时间  
[指标](<https://help.fanruan.com/finebi6.X/doc-view-2347.html#8ab5cc5ec8251279>)  
| 「指标」是对维度的量化，维度讲究的是从不同的角度出发去分析数据，而指标就是不同维度分析出来的结果，这个结果可以是数值，也可以是比值例如：分析不同月份/年份的销售额变化。指标是销售额  
### 2.2 组件
名词  
| 释义  
  
---|---  
[数据可视化](<https://help.fanruan.com/dvg/doc-view-58.html>)| 数据可视化是指通过图表、图形、地图等视觉化方式将数据转化为易于理解和解读的可视形式。它利用视觉元素和交互性设计，帮助人们更好地理解和分析大量的数据，并从中发现模式、趋势、关联性和洞察力  
[组件](<https://help.fanruan.com/finebi6.X/doc-view-1650.html>)| 可视化组件是构成数据可视化系统或工具的独立模块或元素。它们是用于呈现和交互数据的基本构建块，可以在数据可视化应用程序中使用和组合，以创建丰富的界面和功能FineBI 用于数据分析的可视化组件包括[表格](<https://help.fanruan.com/finebi6.0/doc-view-1060.html>)、[图表](<https://help.fanruan.com/finebi6.0/doc-view-801.html>)、[时间过滤组件](<https://help.fanruan.com/finebi6.0/doc-view-135.html>)、[文本组件](<https://help.fanruan.com/finebi6.0/doc-view-141.html>)等，能够提供丰富的选择  
  
[聚合](<https://help.fanruan.com/finebi6.X/doc-view-2284.html>)| 聚合是若干行按照一定的标准变成一行，汇总到更高类别的行级别数据  
  * [指标聚合](<https://help.fanruan.com/finebi6.X/doc-view-332.html>)：指标聚合表示所有指标显示在同一值轴上，方便用户在同一个维度对比不同指标的大小和趋势
  * [聚合函数](<https://help.fanruan.com/finebi6.X/doc-view-4.html>)：对一组数据进行汇总。一般都是使用聚合函数汇总后的值进行再计算。且随着用户分析维度的切换，计算字段会自动跟随维度动态调整

  
[指标名称](<https://help.fanruan.com/finebi6.X/doc-view-110.html>)| 指标名称是图表内指标字段的字段名称；「指标名称」字段拖入对应的「图表属性」中（例如，颜色框），即可产生图例  
### 2.3 仪表板
名词  
| 释义  
  
---|---  
[过滤组件](<https://help.fanruan.com/finebi6.X/doc-view-382.html>)| 想要在查看仪表板时，可以灵活改变要过滤的值；或者需要同时对多个组件进行过滤使用该功能  
[联动](<https://help.fanruan.com/finebi6.X/doc-view-150.html>)| 联动可实现点击一个组件，仪表板内其他组件显示出相关数据  
[跳转](<https://help.fanruan.com/finebi6.X/doc-view-1595.html>)| 当用户需要从当前仪表板跳转到别的页面时（可以跳转到普通网页、其他仪表板、FineReport模板等），可以使用跳转功能  
[钻取](<https://help.fanruan.com/finebi6.X/doc-view-1630.html>)| 钻取可以让用户在查看仪表板时动态改变维度的层次，它包括向上钻取和向下钻取。比如可实现：查看省份数据时，可下钻查看到下方具体城市的数据  
## 3\. 公共数据
名词  
| 释义  
  
---|---  
[公共数据](<https://help.fanruan.com/finebi6.0/doc-view-264.html>)| 企业级数据，企业中需要公开提供给员工使用、查看的数据表存储空间。  
## 4\. 数据分析模型
名词  
| 释义  
  
---|---  
[AARRR模型](<https://help.fanruan.com/finebi6.X/doc-view-1256.html>)| AARRR 模型又叫海盗模型，是用户运营过程中常用的一种模型，解释了实现用户增长的 5 个指标：获客、激活、留存、收益、传播。从获客到传播推荐，整个 AARRR 模型形成了用户全生命周期的闭环模式，不断扩大用户规模，实现持续增长  
[RFM分析](<https://help.fanruan.com/finebi6.X/doc-view-703.html>)| RFM 分析是美国数据库营销研究所提出的一种简单实用客户分析方法，发现客户数据中有三个神奇的要素：
  * 最近一次消费时间（R）：客户距离最近的一次采购时间的间隔。
  * 最近一段时间内消费频次（F）：指客户在限定的期间内所购买的次数。
  * 最近一段时间内消费金额（M）:客户的消费能力，通常以客户单次的平均消费金额作为衡量指标。

  
通过三个关键指标对客户进行观察和分类，判断每类细分用户的价值。针对不同的特征的客户进行相应的营销策略。  
[ABC分析(帕累托)](<https://help.fanruan.com/finebi6.X/doc-view-702.html>)| 根据事物在技术或经济方面的主要特征，进行分类排队，分清重点和一般，从而有区别地确定管理方式。它把被分析的对象分成 A、B、C 三类，三类物品没有明确的划分数值界限  
  
[购物篮分析](<https://help.fanruan.com/finebi6.X/doc-view-1195.html>)| 通过研究用户消费数据，将不同商品之间进行关联，并挖掘二者之间联系的分析方法，即「购物篮分析」  
[杜邦分析](<https://help.fanruan.com/finebi6.X/doc-view-1138.html>)| 杜邦分析法利用几种主要的财务比率之间的关系来综合地分析企业的财务状况，用来评价公司盈利能力和股东权益回报水平，从财务角度评价企业绩效。其基本思想是将企业净资产收益率逐级分解为多项财务比率乘积，这样有助于深入分析比较企业经营业绩  
[KANO模型](<https://help.fanruan.com/finebi6.X/doc-view-1288.html>)| 是对用户需求分类和优先排序的有用工具，以分析用户需求对用户满意的影响为基础，体现了产品性能和用户满意之间的非线性关系  
[波士顿矩阵图](<https://help.fanruan.com/finebi6.X/doc-view-733.html>)| 波士顿矩阵（BCG Matrix），又称市场增长率-相对市场份额矩阵、波士顿咨询集团法、四象限分析法、产品系列结构管理法等。通过销售增长率（反映市场引力的指标）和市场占有率（反映企业实力的指标）来分析决定企业的产品结构  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [快速入门](<category-view-96>)
[![](/core/style/back.png)上一篇：5分钟上手FineBI](<index.php?doc-view-818.html>)
[下一篇：认识数据表 ![](/core/style/forward.png) ](<index.php?doc-view-2347.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
