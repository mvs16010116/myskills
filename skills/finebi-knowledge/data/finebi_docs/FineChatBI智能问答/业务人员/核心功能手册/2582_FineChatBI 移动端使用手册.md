---
title: FineChatBI 移动端使用手册
doc_id: 2582
url: https://help.fanruan.com/finebi6.X/doc-view-2582.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:08
---

> 1. 概述1.1 版本FineChatBI版本功能变动V3.27.0移动端支持切换问答模式V3.28.0移动端支持对标签提问V3.29.0移动端适配数据解读功能V3.30.0移动端适配归因分析V3.34

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineChatBI 移动端使用手册
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[20](<edition-list-2582.html>)
* 最近更新：[Aria.Han](<user-space-2499654.html>) 于 2026-03-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineChatBI版本| 功能变动  
---|---  
V3.27.0| 移动端支持切换问答模式  
  
V3.28.0| 移动端支持对标签提问  
  
V3.29.0| 移动端适配数据解读功能  
  
V3.30.0| 移动端适配归因分析  
V3.34.0| 移动端界面优化  
  
V4.0| 移动端新增历史问答记录  
V4.3  
| 移动端智能模式支持思维链条&消歧  
V4.4| 移动端适配追问功能  
### 1.2 应用场景
本文将介绍移动端如何进入 FineChatBI 进行提问。
注：FineChatBI 不支持 app 访问。
## 2\. 提问入口
### 2.1 入口一：通过移动端浏览器访问
1）在移动端浏览器中点击链接：http://IP:端口号/webroot/decision，先访问移动端 FineBI 平台。
2）点击右下角「FineChatBI」入口，如下图所示：
![](/core/style/lod.png)
### 2.2 入口二：通过链接直接访问
在移动端可以通过链接直接访问 FineChatBI ，在工程基础链接后添加后缀后缀 /ai/conversation/chat/mobile：http://IP:端口号/webroot/decision/ai/conversation/chat/mobile
例如，如果您的工程链接是 http://192.168.1.1:8080/webroot/decision，则在移动端可以通过以下链接直接访问问答BI：http://192.168.1.1:8080/webroot/decision/ai/conversation/chat/mobile
![](/core/style/lod.png)
### 2.3 入口三：集成到办公平台后，在办公平台访问
管理员将 FineChatBI 集成至企业微信、钉钉、飞书等办公平台后（详情请参见：[iFrame 嵌入集成](<https://help.fanruan.com/finebi6.X/doc-view-2622.html>)），可以直接在这些应用的工作台中访问和使用 FineChatBI 。
![3.png](/core/style/lod.png)
## 3\. 操作步骤
### 3.1 选择提问数据
界面顶部显示当前提问数据，点击切换按钮即可选择其他提问数据。如下图所示：
![](/core/style/lod.png)
### 3.2 查询历史会话
点击左上方按钮，即可查看历史会话，如下图所示：
![](/core/style/lod.png)
### 3.3 问答设置
在移动端提问界面，点击设置，对「数据范围、问答模式、语言、歧义词确认记录」进行修改。如下图所示：
![](/core/style/lod.png)
## 4\. 进行提问
### 4.1 数据解读
移动端在 V 3.29.0 适配了数据解读功能，如下图所示：  

注：管理员需在 [开启大模型功能](<https://help.fanruan.com/finebi6.X/doc-view-2633.html>) 中提前开启数据解读。
![](/core/style/lod.png)
### 4.2 归因分析
移动端在 V3.30.0 适配了归因分析功能（功能详情：[归因分析](<https://help.fanruan.com/finebi6.X/doc-view-2650.html>)），如下图所示：  

注：管理员需在 [开启大模型功能](<https://help.fanruan.com/finebi6.X/doc-view-2633.html>) [](<https://help.fanruan.com/finebi6.X/doc-view-2633.html#2674bb6d88ec4bc7>) 中提前开启归因分析。
![](/core/style/lod.png)
### 4.3 追问
移动端在 V4.4 适配了追问功能，即，支持与大模型进行多轮对话，如下图所示：  

注：管理员需在 [开启大模型功能](<https://help.fanruan.com/finebi6.X/doc-view-2633.html>) [](<https://help.fanruan.com/finebi/doc-view-2631.html#aa4480449ccd16f1>) 中提前配置追问轮次次数。
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：FineChatBI 名词解释](<index.php?doc-view-2682.html>)
[下一篇：准备提问数据 ![](/core/style/forward.png) ](<index.php?doc-view-2573.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
