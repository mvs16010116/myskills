---
title: [App]iOS设备越狱环境检测
doc_id: 982
url: https://help.fanruan.com/finebi/doc-view-982.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:16
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本App 版本6.0V11.0.681.2 问题描述iOS 设备越狱后，处于不安全的环境下，各种恶意程序都容易运行在越狱环境之中。在越狱环境中运行帆软 App，难以

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# [App]iOS设备越狱环境检测
[__](<doc-edit-982.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[2](<edition-list-982.html>)
* 最近更新：[Alicehyy](<user-space-504714.html>) 于 2022-11-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| App 版本  
---|---  
6.0| V11.0.68  
### 1.2 问题描述
iOS 设备越狱后，处于不安全的环境下，各种恶意程序都容易运行在越狱环境之中。
在越狱环境中运行帆软 App，难以保证程序使用过程中数据的安全性。
### 1.3 解决思路
登录帆软 App 时，将自动检测设备是否越狱并提醒。
## 2\. 帆软 App
App 默认检测 iOS 设备是否越狱，对于越狱设备，弹出提示框：当前设备已越狱，存在因病毒软件而导致的信息泄露的风险。
点击确定可继续运行 App。如下图所示：
![image.png](https://help.fanruan.com/core/style/lod.png)
## 3\. 打包 App
[用户自定义打包](<https://help.fanruan.com/finebi7.0/doc-view-344.html>) 的 App，默认检测 iOS 设备是否越狱。对于越狱设备，弹出提示框：当前设备已越狱，无法使用。
点击确定退出 App。如下图所示：
![image.png](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：[App]虚拟网设置](<index.php?doc-view-959.html>)
[下一篇：[APP]常用 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-949.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
