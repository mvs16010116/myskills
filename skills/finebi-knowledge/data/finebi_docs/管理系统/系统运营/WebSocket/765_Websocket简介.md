---
title: Websocket简介
doc_id: 765
url: https://help.fanruan.com/finebi6.X/doc-view-765.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:26
---

> 1. 概述1.1&nbsp;版本FineBI服务器版本功能变更6.0-1.2 功能简介本文将从以下几点为大家介绍websocket。1）为什么要设置websocket2）不设置websocket会怎么样

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Websocket简介
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Hanzhen](<user-space-87500.html>)_
* 历史版本：[21](<edition-list-765.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本| 功能变更  
---|---  
6.0| -  
### 1.2 功能简介
本文将从以下几点为大家介绍websocket。
1）为什么要设置websocket
2）不设置websocket会怎么样
3）怎么设置websocket
4）websocket设置不生效怎么排查
## 2\. WebSocket的作用
WebSocket可以让服务器端主动向客户端推送数据。
在WebSocket API中，客户端和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。
WebSocket 主要用于刷新 token、用户被踢出、平台消息、内存和 CPU 显示、平台日志处当前系统在线人数、数据连接编辑状态的确定。
## 3\. WebSocket 端口配置
### 3.1 默认端口
FineBI 工程默认配置了 WebSocket 端口和 WebSocket 转发端口。
根据不同的工程环境，两个端口的生效顺序不完全相同。按照生效顺序，会依次尝试监听，如果有一个端口监听成功，则不再尝试其他端口。
端口| ID| 默认值| **是否支持****设置多个值**  
---|---|---|---  
Websocket 端口| WebSocketConfig.port| ["48888", "49888"]| 支持  
Websocket 转发端口| WebSocketConfig.requestPorts| 48889| 支持  
### 3.2 配置方法
用户可根据自己的工程情况选择合适的 WebSocket 端口配置方法，详情请参见下表：
方案| 场景| 配置方法  
---|---|---  
容器Websocket方案| FineBI内置了一个容器Websocket方案无需任何用户操作，系统可自动使用Web容器自带的WebSocket进行连接，端口复用http端口
  * 只需用户环境满足生效条件，则自动使用该方案
  * 若用户环境不满足生效条件，则可考虑自行配置socket.io方案

| [容器Websocket方案](<https://help.fanruan.com/finebi6.0/doc-view-1861.html>)  
socket.io方案| 单机环境配置 WebSocket 端口| [单机配置WebSocket端口](<https://help.fanruan.com/finebi6.0/doc-view-1511.html>)  
  
集群环境配置 WebSocket 端口| [集群配置WebSocket端口](<https://help.fanruan.com/finebi6.0/doc-view-1510.html>)  
  
HTTPS 环境配置 Websocket 端口| [HTTPS环境配置WebSocket](<https://help.fanruan.com/finebi6.0/doc-view-1509.html>)  
  
仅对外开放一个端口| [不额外给WebSocket对外开放端口](<https://help.fanruan.com/finebi6.0/doc-view-1508.html>)  
  
## 4\. Websocket 连接失败
如果按照 3.2 节的 WebSocket 端口配置方法配置后，websocket仍然连接失败，请参考文档排查：[WebSocket连接失败](<https://help.fanruan.com/finebi6.0/doc-view-1507.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：BI模板访问socket插件](<index.php?doc-view-2087.html>)
[下一篇：容器Websocket方案 ![](/core/style/forward.png) ](<index.php?doc-view-1861.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
