---
title: FineBI使用规范
doc_id: 2422
url: https://help.fanruan.com/finebi6.X/doc-view-2422.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:33
---

> 1. 概述1.1 问题描述在企业推广FineBI的过程中，除了不可或缺的运营动作，对系统的规范使用也是必不可少的管理。良好的使用规范可以保证BI平台的使用效率和性能，提升企业整体的数据利用能力；而与之相

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI使用规范
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[9](<edition-list-2422.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-06-13 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 问题描述
在企业推广FineBI的过程中，除了不可或缺的运营动作，对系统的规范使用也是必不可少的管理。良好的使用规范可以保证BI平台的使用效率和性能，提升企业整体的数据利用能力；而与之相反，不受控制的使用会使得平台内容冗余度不断增加、数据逐渐脱离管控、系统性能得不到最大化利用，给企业的BI使用带来障碍。
### 1.2 应用场景
FineBI建设推广关键阶段如下图所示：
![2024-05-28_14-28-44.png](/core/style/lod.png)
本系列文档列举出一些自助分析的使用规范，从**系统管理**(面向超管)、**数据 &权限管理**(面向超管&次管)、**开发过程管理**(面向用户)的角度叙述了企业在推动BI的过程中一些需要注意的事项，同时介绍了FineBI推广过程中建议的职能安排。
**企业在推进自助分析时，可参考本文内容，结合实际情况作出调整，并坚持推动规范落地、保证持续执行。**
## 2\. FineBI使用规范
规范| 描述| 主要内容（点击超链访问规范）  
---|---|---  
系统管理篇| 
  * **面向超级管理员**

此篇介绍了在FineBI系统搭建之后，超级管理员如何进行一些系统配置和设计，以保证FineBI的顺利使用| [**环境管理**](<https://help.fanruan.com/finebi6.X/doc-view-1845.html>)：包含正式环境和测试环境的论述[**用户管理**](<https://help.fanruan.com/finebi6.X/doc-view-1838.html>)：介绍了用户管理机制和思路[**数据管理**](<https://help.fanruan.com/finebi6.X/doc-view-1836.html>)：数据连接管理、数据策略选取、抽取数据策略、大数据量管理方案、一些性能相关的配置项[**流程管理**](<https://help.fanruan.com/finebi6.X/doc-view-1839.html>)**：** 数据发布、上报流程、资源交接和使用情况监控等流程管理方案  
数据体系&权限管理篇| 
  * **面向超级管理员与各部门次级管理员**

数据的管理是FineBI最为重要的内容之一，在企业中往往是由超级管理员和各业务部门的次级管理员一同负责数据体系的建设和维护FineBI从数据体系管理的角度可以分为文件夹、数据集、仪表板目录的管理机制，以及数据权限的控制流程及实施方案，在此篇中均有体现  
| [**数据体系**](<https://help.fanruan.com/finebi6.X/doc-view-1820.html>)：作为业务数据的集市，如何设计摆放规则以提升使用效率；数据集的命名以及管理规则[**目录管理**](<https://help.fanruan.com/finebi6.X/doc-view-1841.html#74b823b0523663ee>)：良好的目录管理可以提升用户的使用效率[**权限体系**](<https://help.fanruan.com/finebi6.X/doc-view-1822.html>)：
  * 权限分配策略：包括BI权限体系、常用的分配方案
  * 权限实施方案：可作为权限配置参考
  * 数据行列权限方案：列举细粒度控制数据权限的方案

  
开发过程管理篇| 
  * **面向BI设计用户**

在用户使用流程中，数据需求是多种多样的，用户开发的过程也是自由的对于数据开发和仪表板制作，FineBI产品有一些建议的配置限制，超过限制则可能会导致性能不佳，在本文中做了一些限制的整理和说明| [**用户准入管理**](<https://help.fanruan.com/finebi6.X/doc-view-2419.html#ec867666267fefba>) ：如何在源头上对用户做出要求[**用户开发流程**](<https://help.fanruan.com/finebi6.X/doc-view-2419.html#42d560b8ce53e473>)：开发过程的合规性
  * 权限申请
  * 数据开发与上架
  * 仪表板开发与发布

[**灵活开发与系统性能**](<https://help.fanruan.com/finebi6.X/doc-view-2419.html#5926835f89ce89f2>)：开发过程中，为了避免对系统性能造成影响，必须注意开发步骤的合理性
  * FineBI的合理性能表现(抽取数据)
  * 仪表板开发建议
  * 数据集开发建议

  
BI建设职能表| 
  * **面向所有人员  
**

FineBI的推广建设，离不开企业内各级人员的工作配合，在中大型企业内，不同的事务往往需要由不同的人员来执行，根据职能来分配。此篇给出了一些推荐的角色职能分配，在BI推广过程中都是必不可少的。| [**角色分配**](<https://help.fanruan.com/finebi6.X/doc-view-2426.html#275216377e9fbb36>)  
  
抽取数据使用规范| 
  * **面向超级管理员与各部门次级管理员  
**

在FineBI两种抽取模式中，直连模式的使用依赖的是数据库的计算能力，而抽取模式依赖的是FineBI本身的引擎能力。在抽取数据使用过程中如果不加以管理和限制，很可能出现各种性能问题。由于抽取数据的使用注意事项较多，因此此篇单独列出抽取数据的使用规范，给企业提供指导建议。| [**更新数据量**](<https://help.fanruan.com/finebi6.X/doc-view-1823.html#90d033883fff8f64>)：包括合理的数据量限制、如何进行风险管理[**更新设置**](<https://help.fanruan.com/finebi6.X/doc-view-1823.html#20dbd188aa7409c3>)：在更新策略、频率等方面做出有效的管理[**性能标准**](<https://help.fanruan.com/finebi6.X/doc-view-1823.html#71fbdb9c98f35de2>)：FineBI产品在抽取数据的性能表现以及影响因素  
FineBI分析工具使用规范思维导图如下图所示：  

![2024-05-29_13-50-03.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理员使用手册](<category-view-423>)
[![](/core/style/back.png)上一篇：FineBI自助分析建设流程](<index.php?doc-view-2426.html>)
[下一篇：FineBI自助分析建设方案 ![](/core/style/forward.png) ](<index.php?doc-view-1368.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
