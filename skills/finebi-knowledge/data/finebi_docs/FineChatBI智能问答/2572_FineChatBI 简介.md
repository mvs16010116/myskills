---
title: FineChatBI 简介
doc_id: 2572
url: https://help.fanruan.com/finebi6.X/doc-view-2572.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:01
---

> 1. 概述FineChatBI&nbsp;是帆软新推出的一款利用人工智能技术，可帮助用户通过对话实现可信查数，进一步降低数据分析门槛。试用入口：FineChatBI 试用若想正式部署使用，请拨打电话：4

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineChatBI 简介
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[15](<edition-list-2572.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineChatBI 是帆软新推出的一款利用人工智能技术，可帮助用户通过对话实现可信查数，进一步降低数据分析门槛。
  * 试用入口：[FineChatBI 试用](<https://pcdemo.finebi.com/webroot/decision?menu=chatbiintro>)
  * 若想正式部署使用，请拨打电话：400-811-8890


## 2\. 功能定位
FineChatBI 可「降低数据消费门槛」方向，服务于一线业务人员：
  * 用户能够通过提问的方式获得可信的数据结果。
  * 能够利用FineBI的数据分析底座完成业务分析闭环。


![1\(1\).gif](/core/style/lod.png)
## 3\. 人员定位
FineChatBI 使用中有三种人员角色：业务人员、数据产品经理、管理员  

  * **业务人员** ：使用 FineChatBI 进行提问，快速获取所需的数据洞察，从而解决实际的业务问题。
  * **数据产品经理** ：负责深入了解业务人员的分析需求，根据这些需求搜集、整理和准备提问所需的数据。此外，数据产品还负责进行智能问答配置，优化系统的问答逻辑和算法，提高 FineChatBI 的智能性和准确性，使业务人员能够获得更优质的提问体验。
  * **管理员** ：负责 FineChatBI 系统的正常运行和安全管理。


![](/core/style/lod.png)
## 4\. 功能概述
### 4.1 使用主题模型定义数据源
FineChatBI 基于 FineBI 底座，利用 BI 的主题模型，通过在主题中设置表与表之间的模型关系，实现高效的多表分析。
FineChatBI 依据用户的选择的分析主题进行回答，从而提升数据质量和问答可信度，有效避免答非所问。
![1\(2\).gif](/core/style/lod.png)
### 4.2 意图解析与调整
FineChatBI 支持通过自然语言提问，进行专业数据分析。
用户可以自定义图表类型，也可在过程中对指标口径进行修改，从而实现即时的过程纠偏。
![998.gif](/core/style/lod.png)
### 4.3 问答思路拆解及问题推荐
FineChatBI 将意图模糊的问题通过大模型进行解析，生成分析思路、可视化组件和推荐问题。
![](/core/style/lod.png)
### 4.4 字段联想与匹配
FineChatBI 会对输入的问题自动切词，输入过程中会触发联想匹配字段供用户选择，通过切词可保障问题识别的准确性。
![](/core/style/lod.png)
### 4.5 归因分析
多维度拆解分析是定位问题原因的有效方法之一，但拆解维度过多时，分析易失焦，要么无法定位问题根源，要么陷入 “各维度都可能有问题” 的困境。
FineChatBI 支持归因分析，可直接响应 “2024 年 9 月份销售额为什么这么高” 这类问题，快速挖掘关键影响因子。用户也可点击图表中的指标值，定位影响该指标的重要因子，进而针对性拆解维度开展分析，提升分析效率，并生成归因分析报告。
![](/core/style/lod.png)
### 4.6 钻取分析
FineChatBI 支持用户在问答的对话中，通过点击图表组件上的数据点，选择对应的维度进行「数据钻取」，从而进行深入分析。
![1\(7\).gif](/core/style/lod.png)
### 4.7 多轮问答
FineChatBI 支持在问答中不断进行分析，通过问答渐渐明晰数据分析的结果。在业务应用中用户经常携带着模糊但连贯的业务分析思路进行分析，智能问答 BI可以通过逐渐连续的问答，帮助用户逐步获取数据分析思路，渐进地揭示分析结果。
![1\(8\).gif](/core/style/lod.png)
### 4.8 预测问法
FineChatBI 支持通过折线图对数据进行预算，帮助业务人员对未来的趋势走向进行预测分析。
注：历史数据越多预测准确率越高。
![1\(9\).gif](/core/style/lod.png)
### 4.9 生成仪表板
FineChatBI 支持将问答的可视化组件生成仪表板进行保存，以便于进行后续更深入的分析或将分析内容进行发布展示。
![1\(10\).gif](/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：高级商务风优化指南](<index.php?doc-view-2323.html>)
[下一篇：FineChatBI 更新日志 ![](/core/style/forward.png) ](<index.php?doc-view-2594.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
