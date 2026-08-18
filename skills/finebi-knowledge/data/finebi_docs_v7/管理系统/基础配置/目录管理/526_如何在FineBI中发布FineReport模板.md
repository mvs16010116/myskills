---
title: 如何在FineBI中发布FineReport模板
doc_id: 526
url: https://help.fanruan.com/finebi/doc-view-526.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:27:31
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本功能变更7.0-1.2 问题描述FineBI 工程未集成 FineReport 工程的情况下，如何挂载/使用 FineReport 模板呢？1.3 解决思路有

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 如何在FineBI中发布FineReport模板
[__](<doc-edit-526.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[17](<edition-list-526.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
7.0| -  
### 1.2 问题描述
FineBI 工程未集成 FineReport 工程的情况下，如何挂载/使用 FineReport 模板呢？  

### 1.3 解决思路
有两种使用场景：
1）将 FineReport 模板挂载到 FineBI 工程目录中展示。
2）将 FineReport 模板通过仪表板的 Web 组件链接展示。
注：若 FineBI 工程和 FineReport 工程互通，也可在 FineBI 工程目录直接挂载 FineReport 模板的超链，本文不赘述此情况。
## 2\. 示例一：挂载到目录中
本章示例：在 FineBI 系统目录中，展示 FineReport 模板「简单填报示例.cpt」。
### 2.1 上传FineReport模板
通过运维平台「维护>文件管理」功能，将 FineReport 模板「简单填报示例.cpt」上传到 FineBI 工程的 reportlets 目录下。
注：若需要添加的报表A中添加了超链接，链接至另一报表B，需要将报表A和B同时上传至 FineBI 工程中。
![](https://help.fanruan.com/core/style/lod.png)
### 2.2 设置数据连接
在 FineBI 系统中，需要新增一个数据连接，和 FineReport 模板「简单填报示例.cpt」用到的数据连接完全一致，命名也必须完全相同。
1）管理员登录 FineBI 系统，点击「管理系统>数据连接>数据连接管理」。
2）点击「新建数据连接」，新建一个和「段落明细表」用到的数据连接完全一致的数据连接。
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 新增目录
1）管理员登录FineBI系统，点击「管理系统>目录管理」，选择想要挂出的对应目录后，点击「添加模板」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）选择路径
支持选择 FineBI 工程的 reportlets 文件夹及其子文件夹下的所有 FineReport 模板
本示例选择 FineReport 模板「简单填报示例.cpt」，点击「下一步」。
3）设置模板  

支持设置模板的挂出名称、描述、类型等、展示终端等信息，点击「确定」。
注：如模板预览类型为填报，FineBI工程必须购买了「数据录入」功能点，否则无法进行填报。详情请参见：[注册管理](<https://help.fanruan.com/finebi7.0/doc-view-177.html>) 。
  

![](https://help.fanruan.com/core/style/lod.png)
### 2.4 效果预览
打开目录，刷新，左侧目录树中显示刚刚添加的 FineReport 模板「简单填报示例.cpt」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 示例二：在组件中引用
本章示例：在 FineBI 的 Web 组件中，展示 FineReport 模板「简单填报示例.cpt」。
### 3.1 上传FineReport模板
通过运维平台「维护>文件管理」功能，将 FineReport 模板「简单填报示例.cpt」上传到 FineBI 工程的 reportlets 目录下。
注：若需要添加的报表A中添加了超链接，链接至另一报表B，需要将报表A和B同时上传至 FineBI 工程中。
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 设置数据连接
在 FineBI 系统中，需要新增一个数据连接，和 FineReport 模板「简单填报示例.cpt」用到的数据连接完全一致，命名也必须完全相同。
1）管理员登录 FineBI 系统，点击「管理系统>数据连接>数据连接管理」。
2）点击「新建数据连接」，新建一个和「段落明细表」用到的数据连接完全一致的数据连接。
![](https://help.fanruan.com/core/style/lod.png)
### 3.3 新建仪表板
用户登录 FineBI 系统，点击「我的分析」，点击「新建分析主题」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
无需选择数据，直接点击「取消」。添加一个「仪表板」，选择「其他>Web组件」，将其拖入仪表板中，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
为该 Web 组件添加超链接，示例链接为/webroot/decision/view/report?viewlet=简单填报示例.cpt&op=write
  * FR普通报表的模板链接为：/webroot/decision/view/report?viewlet=xxxxx.cpt
  * FR决策报表的模板链接为：/webroot/decision/view/report?viewlet=xxxxx.frm
  * FR大屏模板的模板链接为：/webroot/decision/decision/view/duchamp?viewlet=xxxx.fvs


xxxxx.cpt 对应为该模板保存在 reportlets 文件夹中的子路径和 cpt 文件名称。
  * 若模板文件位于 reportlets 下一级文件夹，例如模板简单填报示例.cpt位于/reportlets/test/demo文件夹中，则链接应当为/webroot/decision/view/report?viewlet=/test/demo/简单填报示例.cpt
  * 若模板需要填报预览，则需在链接添加后缀&op=write。例如简单填报示例.cpt为填报报表，则链接形式为/webroot/decision/view/report?viewlet=简单填报示例.cpt&op=write


![](https://help.fanruan.com/core/style/lod.png)
### 3.4 效果预览
保存仪表板，预览即可在该仪表板的Web组件中查看到FineReport模板「简单填报示例.cpt」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 注意事项
若模板不存放在当前 FineBI 工程中，而是在其他工程中。
当前工程以目录超链/Web组件超链调用其他工程的模板时，必须要关闭模板所在工程的「管理系统>安全管理>安全防护>Security Headers」的「点击劫持攻击防护」。
详情请参见：[安全防护](<https://help.fanruan.com/finebi7.0/doc-view-781.html>)  

![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：不同用户登录显示不同首页](<index.php?doc-view-844.html>)
[下一篇：用户管理 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-170.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
