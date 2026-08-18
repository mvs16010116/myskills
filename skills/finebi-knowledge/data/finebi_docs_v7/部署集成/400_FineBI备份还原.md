---
title: FineBI备份还原
doc_id: 400
url: https://help.fanruan.com/finebi/doc-view-400.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:11
version: "7.X"
---

> 1.&nbsp;概述1.1&nbsp;版本FineBI服务器版本功能变更7.0-1.2 应用场景备份工程的必要性在于保护数据、确保业务连续性和提供灵活性。1）数据保护：通过备份，管理员可以恢复丢失或损坏

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI备份还原
[__](<doc-edit-400.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[35](<edition-list-400.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-04 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本| 功能变更  
---|---  
7.0| -  
### 1.2 应用场景
备份工程的必要性在于保护数据、确保业务连续性和提供灵活性。
1）数据保护：通过备份，管理员可以恢复丢失或损坏的业务数据，确保数据的完整性和可用性。
2）业务连续性：通过备份，在发生灾难性事件时，管理员可以将工程恢复到之前的状态以继续运营业务，减少停机时间和数据损失。
3）版本控制和回退：通过备份，管理员可以创建不同时间点的工程快照，记录工程的状态和变更，便于版本控制、回退到旧版本或查找问题的更改。
4）环境迁移和部署：备份工程有助于在不同的环境中迁移和部署项目。通过备份，可以在新环境中恢复项目的完整结构和配置，简化迁移过程并减少错误。
5）安全性和合规性：通过备份，管理员可以将工程还原到之前的安全状态，保护数据的机密性和完整性，以遵守法规和安全标准。
总结而言，备份工程是确保数据安全、业务连续性和灵活性的关键步骤。无论是面临意外事件、需求变更还是灾难恢复，备份工程都是保护和恢复项目的可靠手段。
## 2\. 备份方案
**应用场景：**
定期自动对工程关键业务数据进行备份，防止工程出现意外，便于还原。
**备份方案：**
对于运维平台部署的帆软项目，运维平台提供「备份管理」功能。
支持一键备份，支持自动备份，可实现异地备份。支持一键还原、宕机还原。
详情请参见：[备份项目](<https://help.fanruan.com/fineops/doc-view-37.html>)、[还原项目](<https://help.fanruan.com/fineops/doc-view-142.html>)。
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 注意事项
**1）FineBI7.0不再支持使用「管理系统 >智能运维>备份还原」功能还原**
运维平台部署的帆软项目，无法使用「管理系统>智能运维>备份还原」功能，进行相关内容还原。
而FineBI7.0仅支持使用运维平台部署，因此不建议用户使用该功能进行备份和还原操作。帆软不提供相关操作说明。
![](https://help.fanruan.com/core/style/lod.png)
**2）备份内容须知**
  * 运维平台备份 FineBI 时，对于**自备的组件** 不会进行备份，也无法进行还原。建议用户在进行项目备份时，自行手动对这些组件进行备份，并在还原时同步还原。
  * 运维平台备份的 FineBI 内容，存放在运维平台的挂载目录下，因此建议将运维平台和项目分开部署在不同服务器上，实现异机备份。
  * 运维平台备份的 FineBI，并非完整的 FineBI，而是关键的配置。因此如需万无一失的备份，请自行对 FineBI 所有组件（包括bi、bi引擎、bi配置库、bi日志库、bi文件服务、bi数据存储组件等等）所在服务器创建工程快照


### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI与FineReport版本适配说明](<index.php?doc-view-1061.html>)
[下一篇：注册简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-187.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
