---
title: Agent 集成（beta）
doc_id: 2716
url: https://help.fanruan.com/finebi6.X/doc-view-2716.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:19
---

> 1. 概述该功能处于内测阶段，暂不提供技术支持服务。1.1 版本版本功能变动4.0-1.2 应用场景支持在 FineChatBI 中集成 Coze 和 FastGPT 的 Agent 应用。2. 添加

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Agent 集成（beta）
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[4](<edition-list-2716.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-01-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
![icon](/core/style/lod.png)
该功能处于内测阶段，暂不提供技术支持服务。
### 1.1 版本
版本  
| 功能变动  
---|---  
4.0  
| -  
### 1.2 应用场景
支持在 FineChatBI 中集成 Coze 和 FastGPT 的 Agent 应用。
## 2\. 添加 Agent
1）管理员进入「管理系统>智能问答配置」，在「Agent集成」启用后，点击「添加Agent配置」。如下图所示：  

![](/core/style/lod.png)
2）填入 Agent 相关信息，如下图所示：
![](/core/style/lod.png)
  

配置项  
| 描述  
---|---  
Agent 名称| Agent 显示名称，用于在聊天界面中识别  
头像| 上传图片作为 Agent 头像  
说明/描述| Agent 的说明或描述信息  
厂商| 选择 Agent 服务提供商，支持 Coze 和 FastGPT  
API URL| Coze API 接口地址：https://api.coze.cn/v3/chatFastGPT API 接口地址：https://doc.fastgpt.io/docs/introduction/development/openapi/chat  
API Token| Coze API Token 获取方式可参见 Coze 官方文档：[添加服务访问令](<https://www.coze.cn/open/docs/developer_guides/service_token>)[牌](<https://www.coze.cn/open/docs/developer_guides/service_token>)FastGPT API Token 获取获取方式可参见 FastGPT 官方文档。  
Bot ID| 智能体的唯一标识。开发页面 URL 中参数后的数字就是智能体ID。例如:https://www.coze.cn/space/341****/bot/73428668*****，bot_id 为 73428668*****。  
3）测试成功后点击「保存」，如下图所示：
  

![](/core/style/lod.png)
## 3\. 使用 Agent
展开右侧栏，点击 Agent 即可使用，如下图所示：
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：多语言配置](<index.php?doc-view-2683.html>)
[下一篇：最佳实践 ![](/core/style/forward.png) ](<index.php?doc-view-2574.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
