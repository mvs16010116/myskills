---
title: FineChatBI 简介
doc_id: 2572
url: https://help.fanruan.com/finebi/doc-view-2572.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:06
version: "7.X"
---

> 1. 概述FineChatBI&nbsp;是帆软新推出的一款利用人工智能技术，可帮助用户通过对话实现可信查数，进一步降低数据分析门槛。2. 功能定位FineChatBI 可「降低数据消费门槛」，服务于一

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineChatBI 简介
[__](<doc-edit-2572.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[9](<edition-list-2572.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineChatBI 是帆软新推出的一款利用人工智能技术，可帮助用户通过对话实现可信查数，进一步降低数据分析门槛。
## 2\. 功能定位
FineChatBI 可「降低数据消费门槛」，服务于一线业务人员：
  * 通过提问的方式获得可信的数据结果。
  * 能够利用 FineBI 的数据分析底座完成业务分析闭环。


![1\(1\).gif](https://help.fanruan.com/core/style/lod.png)
## 3\. 功能概述
### 3.1 使用数据中心准备数据源
FineChatBI 基于 BI 底座，管理员在 FineBI 中搭建指标（[指标中心简介](<https://help.fanruan.com/finebi7.0/doc-view-2646.html>)），用户可基于指标中心进行提问。
![](https://help.fanruan.com/core/style/lod.png)
管理员将指标添加到预加载数据列表后，用户即可基于此直接进行提问。
### 3.2 意图解析与调整
FineChatBI 支持通过自然语言提问来自动生成相应的业务分析图表。用户可以自定义图表生成规则，以便在问答过程中随时对指标口径进行修改，从而实现即时的过程纠偏。
![26.gif](https://help.fanruan.com/core/style/lod.png)
### 3.3 问答思路拆解及相似问题推荐
FineChatBI 将意图模糊的问题通过模型与相似问题进行解析，依据可靠性最高的回答生成分析思路与可视化组件进行展示。
用户可以通过对解析思路进行分析来判断分析结果是否合需求，若不符合需求，可点选生成的推荐问题进行提问。
![](https://help.fanruan.com/core/style/lod.png)
### 3.4 模糊字段联想与匹配
FineChatBI 对所输入的问题进行解析，如果识别到模糊不确定的字段，则会触发联想匹配字段枚举值，并返回给用户进行确认，从而进⼀步提升问答精准度。
![1\(5\).gif](https://help.fanruan.com/core/style/lod.png)
### 3.5 归因分析
多维度拆解分析是定位问题原因的有效分析方法之一，而当分析时拆解的维度过多时，分析就失去了焦点，要么找不到出现问题的原因，要么感觉每个维度都可能有问题。
FineChatBI 支持对如下问题进行归因分析，挖掘关键影响因子，点击指标值，找到影响该指标值的重要因子，针对性拆解维度进行分析，提高分析效率。
1）包含时间及单个指标问题，可以自动检测异常点。例如：2023年每个月的销售额。
2）包含单个分组及单个指标的问题，可以通过点击组件上的点进行归因分析。例如：每个城市的销售额。
3）可以通过问答，对段状或者点状时间及指标进行归因分析。例如：2023年9月的销售额为什么这么高？ 
![1\(6\).gif](https://help.fanruan.com/core/style/lod.png)
### 3.6 明细下钻
FineChatBI 支持用户在问答的对话中，通过点击图表组件上的数据点，选择对应的维度进行明细下钻，从而进行深入分析。同时支持在归因分析后，可以针对不同的维度进行明细下钻分析。
![1\(7\).gif](https://help.fanruan.com/core/style/lod.png)
### 3.7 多轮问答
FineChatBI 支持在问答中不断进行分析，通过问答渐渐明晰数据分析的结果。在业务应用中用户经常携带着模糊但连贯的业务分析思路进行分析，智能问答 BI可以通过逐渐连续的问答，帮助用户逐步获取数据分析思路，渐进地揭示分析结果。
![1\(8\).gif](https://help.fanruan.com/core/style/lod.png)
### 3.8 预测问法
对于复杂数据的进行分析时，FineChatBI 支持通过折线图对数据进行预算，帮助业务人员对未来的趋势走向进行预测分析。
注：历史数据越多预测准确率越高。
![1\(9\).gif](https://help.fanruan.com/core/style/lod.png)
### 3.9 生成仪表板
FineChatBI 支持将问答的可视化组件生成仪表板进行保存，以便于进行后续更深入的分析或将分析内容进行发布展示。
![1\(10\).gif](https://help.fanruan.com/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-763>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：高级商务风优化指南](<index.php?doc-view-2323.html>)
[下一篇：FineChatBI 更新日志 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2594.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
