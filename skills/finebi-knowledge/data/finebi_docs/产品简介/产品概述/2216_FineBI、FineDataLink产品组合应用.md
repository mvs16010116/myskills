---
title: FineBI、FineDataLink产品组合应用
doc_id: 2216
url: https://help.fanruan.com/finebi6.X/doc-view-2216.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:22
---

> 1. 概述FineBI 是新一代大数据分析的 BI 工具，旨在帮助企业的业务人员充分了解和利用他们的数据，自主分析得出结果，辅助企业业务决策。FineDataLink&nbsp;是一款低代码/高时效的企

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI、FineDataLink产品组合应用
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[8](<edition-list-2216.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-08-11 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineBI 是新一代大数据分析的 BI 工具，旨在帮助企业的业务人员充分了解和利用他们的数据，自主分析得出结果，辅助企业业务决策。
FineDataLink 是一款低代码/高时效的企业级一站式数据集成平台，处理数据更加高效、专业，可提高自助分析效率，优化 FineBI 使用体验。
![6.png](/core/style/lod.png)
## 2\. 产品简介与定位
维度  
| FineBI| FineDataLink  
---|---|---  
产品简介| 新一代自助大数据分析的 BI 工具，旨在帮助企业的业务部门用户充分了解和利用他们的数据，帮助企业做出明智的业务经营决策| 低代码 / 高时效的企业级一站式数据集成平台，让数据建设更加简单  
目标用户| 中大型企业业务人员、数据分析师| **目标用户特征：** 数据展示和分析前，需要进一步处理数据**目标用户职位：** 需要做数据处理的报表开发工程师，数据处理人员、数仓开发工程师、IT 人员  
核心功能| [自助数据集](<https://help.fanruan.com/finebi5.1/doc-view-825.html>)（BI 6.0 中为[编辑数据](<https://help.fanruan.com/finebi6.X/doc-view-825.html>)）、[仪表板](<https://help.fanruan.com/finebi6.X/doc-view-1514.html>)| [实时数据同步](<https://help.fanruan.com/finedatalink/doc-view-97.html?source=0&from=BI00>)、[ETL和ELT数据开发](<https://help.fanruan.com/finedatalink/doc-view-5.html?source=0&from=BI00>)、[数据服务](<https://help.fanruan.com/finedatalink/doc-view-249.html?source=0&from=BI00>)  
愿景| 上手简单，人人可分析| 让数据可以从任意终端到任意终端  
## 3\. FineDataLink 可以做什么
FineDataLink 致力于为企业、为数据开发者、为数据分析师、为数据资产管理者，结合数据库、上层通用协议、文件、消息队列、平台系统、应用等，打造一个具备开放的、一站式、标准化、可视化、高性能和可持续交付的自助化数据调度与治理平台。
FineDataLink 赋予用户仅通过单一平台，即可实现实时数据传输、数据调度、数据治理等各类复杂组合场景的能力，为企业业务的数字化转型提供支持。
详情请参见：[FineDataLink产品简介](<https://help.fanruan.com/finedatalink/doc-view-2.html?source=0&from=BI00>)
![7.png](/core/style/lod.png)
## 4\. FineDataLink 如何帮助业务人员处理数据
场景  
| FineBI 现状| FineDataLink 方案  
---|---|---  
大数据场景下，操作卡顿、更新慢| 
  * 数据总量 20-30 亿，加载更新速度很慢。一次更新时间约 7-8 小时，有可能第二天早上业务人员使用 BI 看板时，发现数据并没有更新完成；或更新报错想重新启动更新时，代价太大
  * 在「我的分析」中，表关联等数据操作非常卡顿
  * 基于大数据量表的自助分析数据集多，整体服务器压力极大

| **方案：** 使用 FDL 将大数据量明细表提前做聚合汇总，直接输出到 BI 数据集中**优势：** 更新性能提升 50% 以上；改造成本低；缩短更新频率  
数据集过多造成使用困难和卡顿| 
  * 数据集过多，目录太深，相似数据集难以区分，导致用户难以寻找
  * 在「我的分析」中，需要处理大量的数据关联场景，导致整体性能卡顿

| **方案：** 使用 FDL 将事实表和维度表提前做关联形成宽表，直接输出到 BI 数据集中；设计数据集命名规则，目录结构等业务包体系**优势：** 自助分析效率提升；优化使用体验  
无数仓，BI直接对接业务系统数据| 
  * BI 直接连接业务系统数据，会对业务系统造成性能压力，妨碍业务流程
  * 自助分析前需要进行必要的数据清洗

| **方案：**
  * 使用 FDL 的「[数据同步](<https://help.fanruan.com/finedatalink/doc-view-183.html?source=0&from=BI00>)/[数据转换](<https://help.fanruan.com/finedatalink/doc-view-10.html?source=0&from=BI00>)」功能将业务数据**定时同步** 到中间库中，再从中间库做数据开发直接输出到 BI 数据集中
  * 如果时效性高要求，可以加一层[数据管道](<https://help.fanruan.com/finedatalink/doc-view-97.html?source=0&from=BI00>)，**实时同步** 到中间库，实现读写分离，再从中间库做数据开发直接输出到 BI 数据集中

**优势：** 提供轻量化，敏捷的数仓替代方案；实现了与业务系统的读写分离，提升了自助分析时效性。  
接口数据难调用| 无法调用 API 数据| FDL 可为 BI 提供更多的数据源类型采集的能力，如 API 数据（企查查，金蝶云星空，分贝通等），MQTT 物联网数据（机器信息的OT 数据采集等），半结构化数据（XML，JSON等），消息中间件等等  
内部数据，外部系统难调用| BI 处理好的数据，无法给其他业务系统使用| 使用 FDL 的 [数据服务](<https://help.fanruan.com/finedatalink/doc-view-249.html?source=0&from=BI00>) 功能，将处理好的数据通过 API 分享给第三方应用系统，包括提供给 FR 使用  
## 5\. 如何体验 FineDataLink
Demo体验：[FineDataLink数据平台](<https://demo.finedatalink.com/>)
FineDataLink了解试用：[FineDataLink了解试用](<https://t6ixa9nyl6.jiandaoyun.com/f/6152dbd4a57b9b0008992c6a?ext=bihelp>)
## 6\. FineBI 与FineDataLink 组合使用示例
简介| 参考文档  
---|---  
主要介绍业务系统数据经过 FDL 处理落库后，FineBI 调用该数据进行自助分析的全流程，通过 FDL+BI 的组合方案解决自助数据集冗余杂乱、更新时间长、维护困难的问题| [FDL和FineBI组合应用示例](<https://help.fanruan.com/finedatalink/doc-view-78.html?source=0&from=BI00>)  
  

  

  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [产品简介](<category-view-626>)
[![](/core/style/back.png)上一篇：FineBI和FineReport的区别](<index.php?doc-view-279.html>)
[下一篇：报价咨询 ![](/core/style/forward.png) ](<index.php?doc-view-922.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
