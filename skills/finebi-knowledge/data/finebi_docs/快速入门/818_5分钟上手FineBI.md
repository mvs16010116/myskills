---
title: 5分钟上手FineBI
doc_id: 818
url: https://help.fanruan.com/finebi6.X/doc-view-818.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:37
---

> 提示:如在线FineBI体验用户，可阅读「30秒快速了解在线FineBI功能界面」，迅速了解在线BI功能界面与基本操作。1. 概述[helpvideo]6006[/helpvideo]1.1 应用场景介

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 5分钟上手FineBI
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[46](<edition-list-818.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-09-03 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
如在线FineBI体验用户，可阅读[「30秒快速了解在线FineBI功能界面」](<https://help.fanruan.com/finebi6.X/doc-view-2679.html>)，迅速了解在线BI功能界面与基本操作。
## 1\. 概述
### 1.1 应用场景
介绍如何做一个简单分析，以使用 Excel 合同表为例，帮助业务人员快速上手 FineBI 。
![2024-07-15_14-39-24.png](/core/style/lod.png)
### 1.2 功能简介
完成示例制作需要经过 4 个流程：①新建分析主题；②添加数据；③分析数据；④分享协作。
### 1.3 示例数据
我们使用的是合同表的数据进行分析。点击下载并解压示例数据：[DEMO_CONTRACT.zip](<doc-download-/finebi6.X/uploads/file/20241106/DEMO_CONTRACT.zip> "下载资料")
点击进入在线DEMO体验查看：[点击进入](<https://pcdemo.finebi.com/webroot/decision#/directory?activeTab=7f4dc2f1-4287-4c6a-b2b2-696485d2be31>)
## 2\. 操作步骤
本文所有的操作，都在 FineBI 的「我的分析」中进行。  

### 2.1 新建分析主题
「分析主题」是你在 BI 中进行数据分析和可视化展示的核心元素。当你需要进行数据分析时，可以创建分析主题并在其中进行自己的业务分析，分析主题中支持进行数据处理、制作可视化图表和仪表板；同时「分析主题」支持不同用户之间进行协作编辑，极大的方便了用户对分析内容的共享。  

在「我的分析>全部分析」下「新建分析主题」。如下图所示：
**详情请参见：**[**分析主题**](<https://help.fanruan.com/finebi6.0/doc-view-1888.html>)
![2.1.png](/core/style/lod.png)
### 2.2 添加数据
新建分析主题后，会自动进入分析主题内的「添加数据」界面，也可点击「添加」上传数据。
选择「本地Excel文件>上传数据」。将本文 1.3 节的示例数据下载解压后上传。如下图所示：
注1：若上传失败，可能是 csv 文件格式导致。进入「管理系统>安全管理>安全防护 」，关闭「文件上传校验」。
注2：若依旧上传失败可查看文档排查原因：[Excel上传前确认工作](<https://help.fanruan.com/finebi6.X/doc-view-891.html#ddf4f5e51583e01d>)
![g1.gif](/core/style/lod.png)
### 2.3 分析数据
#### 2.3.1 编辑数据
1）数据上传成功后，我们可以直接编辑数据。如下图所示：
如果数据质量好，可以直接进行可视化，直接跳转到 2.3 节进行下一步。
![2.3.1.1.png](/core/style/lod.png)
FineBI 支持新增列、合并数据、分组汇总、过滤排序、字段设置等步骤。各编辑步骤操作请参见文档：[编辑数据概述](<https://help.fanruan.com/finebi6.0/doc-view-506.html>)
例如，我们分析不同产品的购买数量，需要使用「购买的产品」做维度对购买数量分析，需要改变字段类型。点击字段表头修改，完成后「保存并更新」。如下图所示：
![2.3.1.2.png](/core/style/lod.png)
完成数据编辑，接下来我们进入组件制作的学习。
#### 2.3.2 添加可视化组件
FineBI 支持用户将数据通过可视化图表呈现，更直观、深层次的观察数据，并支持在组件中对数据进行分析。接下来，我们将合同数据使用可视化图表展现。
  

**制作表格**  

我们先制作一张表格，展示合同明细信息。  

1）点击下方的「组件」即可添加可视化图表。
首先，将左侧字段拖入分析区域「合同类型、合同付款类型、合同ID、总金额」，然后选择图表类型「分组表」（默认分组表）。如下图所示：
![2.3.2.1.png](/core/style/lod.png)
点击表中「+」可以展开数据明细。
2）分析数据
在组件我们也可以分析数据，实现字段分组、排序过滤、快速计算、添加计算字段等操作。详情请参见：[制作第一个组件](<https://help.fanruan.com/finebi6.0/doc-view-1653.html>)
3）完成后，在页面底部，点击重命名组件为「合同表」。如下图所示：  

![2.3.2.2.png](/core/style/lod.png)
  
**制作图表**
接下来分析一下不同合同类型的购买数量。
制作图表步骤：先拖入字段，再选择图表类型。FineBI的表格和图形有多种呈现类型，点击即可切换。如下图所示：
![5.png](/core/style/lod.png)
1）完成后点击「添加组件」，继续添加图形。如下图所示：
![2022-11-25_17-59-20.png](/core/style/lod.png)
2）首先，拖入字段「合同类型、购买数量」发现表格展示的不够直观；然后，点击「柱形图」就清晰的将数据表达出来。如下图所示：
![g2.gif](/core/style/lod.png)
完成后重命名组件为「不同合同类型购买数量分析」，步骤同 2.3.1 节。
3）分析数据  

在组件我们也可以分析数据，实现字段分组、排序过滤、快速计算、添加计算字段等操作。详情请参见：[制作第一个组件](<https://help.fanruan.com/finebi6.0/doc-view-1653.html>)
  

#### 2.3.3 制作仪表板
1）完成组件分析后，可以点击分析主题底部「添加仪表板」。
![2.3.3.1.png](/core/style/lod.png)
2）我们可以将制作的表格图表，拖入仪表板中。并调整位置。如下图所示：
![g3.gif](/core/style/lod.png)
完成后，可进入「预览」，查看所有数据分析结果，完成仪表板制作。
3）在完成仪表板制作后，保存并更新分析主题。
注：如果不保存更新，则无法协作分享。
![2.3.3.3.png](/core/style/lod.png)
### 2.4 分享协作
FineBI 可以将分析主题制作好的内容分享给别人。
1）点击分析主题，可以邀请别人进行「协作」。例如，选择用户「admin」进行协作。如下图所示：
![2.4.1.png](/core/style/lod.png)
2）admin 用户在「我的分析」中「协作给我的」文件夹下即可找到「分析主题」查看并编辑。如下图所示：
![7.png](/core/style/lod.png)
## 3\. 更多
您已经学会了FineBI最核心的分析步骤，接下来可进入 [1小时入门BI案例](<https://help.fanruan.com/finebi6.X/doc-view-1727.html>) ，完整介绍 FineBI 的运用技巧，和分析方法。
或前往[FineBI学习路径](<https://edu.fanruan.com/studypath/finebi>)获取完整资料。
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [快速入门](<category-view-96>)
[![](/core/style/back.png)上一篇：FineBI界面介绍](<index.php?doc-view-263.html>)
[下一篇：FineBI词汇表 ![](/core/style/forward.png) ](<index.php?doc-view-829.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
