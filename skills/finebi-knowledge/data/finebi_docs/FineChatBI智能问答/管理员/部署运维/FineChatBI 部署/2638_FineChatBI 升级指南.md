---
title: FineChatBI 升级指南
doc_id: 2638
url: https://help.fanruan.com/finebi6.X/doc-view-2638.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:21
---

> 1. 运维平台升级适用于使用运维平台部署 FineBI 的用户。情况1：V3.21.0 及以上版本升级至最新版本1）将 FineBI 项目升级到 6.1.6 及以上版本，请参考：外网升级运维项目&nbs

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineChatBI 升级指南
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[30](<edition-list-2638.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-03-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 运维平台升级
**适用于使用运维平台部署 FineBI 的用户。**
**情况1：V3.21.0 及以上版本升级至最新版本**
1）将 FineBI 项目升级到 6.1.6 及以上版本，请参考：[外网升级运维项目](<https://help.fanruan.com/fineops/doc-view-53.html>) / [内网升级运维项目](<https://help.fanruan.com/fineops/doc-view-55.html>)。
2）推送最新的 AI 镜像包和更改镜像版本到运维平台仓库，参考： [运维平台为FineBI部署AI服务](<https://help.fanruan.com/fineops/doc-view-206.html>) 2.3 节。
3）管理员登录运维平台，选择运维项目，点击「维护>组件管理」，找到待更新的 AI 组件，点击「更新」。
4）更新 BI 智能问答插件，详情请参见：[更新BI智能问答插件](<https://help.fanruan.com/finebi6.X/doc-view-2585.html#7bcd678d028185c0>)。
**情况2：V3.20.0 及以下版本升级至 最新版本**
1）V3.27.0 适配 FineBI 6.1.6 及以上版本  ，升级前请确认 FineBI 已更新至 6.1.6 版本。
2）中止并删除 fine_ai 容器。
[code]
    docker stop fine_ai
[/code]
[code]
    docker rm fine_ai
[/code]
3）中止并删除 fine-chat-bi-parser-base 容器（语义解析小模型）。
[code]
    docker stop fine-chat-bi-parser-base
[/code]
[code]
    docker rm fine-chat-bi-parser-base
[/code]
4）使用运维平台重新部署 FineChatBI：[运维平台为FineBI部署AI服务](<https://help.fanruan.com/fineops/doc-view-206.html>)。
**特别注意：从 V3.21.0 开始，所有使用运维平台部署 FineBI 的用户必须使用运维平台重新部署 FineChatBI 。**
## 2\. 传统部署升级
1）重新部署 FineAI，详情请参见：[部署新版本FineAI](<https://help.fanruan.com/finebi6.X/doc-view-2585.html#b513ce4426ef20c4>) 。
2）重新部署新版本的语义解析小模型，详情请参见：[部署新版本语义解析小模型](<https://help.fanruan.com/finebi6.X/doc-view-2585.html#2b212ba92494feac>)。
3）更新 BI 智能问答插件，详情请参见：[更新BI智能问答插件](<https://help.fanruan.com/finebi6.X/doc-view-2585.html#7bcd678d028185c0>)。
### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：FineChatBI 部署](<index.php?doc-view-2642.html>)
[下一篇：推理大模型 ![](/core/style/forward.png) ](<index.php?doc-view-2680.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
