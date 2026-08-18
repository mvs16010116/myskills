---
title: 单机配置WebSocket端口
doc_id: 1511
url: https://help.fanruan.com/finebi6.X/doc-view-1511.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:27
---

> 1. 概述1.1 版本BI 服务器版本5.11.2 应用场景本文将介绍在单机环境下，如何配置 WebSocket 端口。注：5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。推荐

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 单机配置WebSocket端口
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[3](<edition-list-1511.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-05-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
BI 服务器版本  
---  
5.1  
### 1.2 应用场景
本文将介绍在单机环境下，如何配置 WebSocket 端口。
注：5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。推荐优先查看是否可使用该方案：[容器Websocket方案](<https://help.fanruan.com/finebi6.0/doc-view-1861.html>)
无需任何用户操作，无需任何手动配置，无需额外开启端口，系统可自动使用Web容器自带的WebSocket进行连接，端口复用http端口。
## 2\. 示例
### 2.1 修改字段值
超级管理员可通过「fine_conf_entity可视化配置插件」修改 WebSocket 端口。重启服务器后设置生效。
注：修改 FineDB 数据库表字段值的方法请参考 [FineDB 常用表字段修改](<https://help.fanruan.com/finereport/doc-view-2471.html>) 。
端口| JAR 包| ID| 默认值| 设置范围| 是否支持设置多个值  
---|---|---|---|---|---  
Websocket 端口| -| WebSocketConfig.port| ["48888", "49888"]| 参数值为端口数组["port1","port2"]port均属于区间(1024,65535]| 支持  
Websocket 转发端口| 2019-11-08 之前| WebSocketConfig.requestPort| 48889| 支持  
2019-11-08 及之后| WebSocketConfig.requestPorts| 48889| 支持  
设置端口号时有一些注意事项：
1）端口号可设置范围：1024~65535，若为多个值，设置格式为：[端口号1,端口号2,端口号3]。
2）建议「WebSocket端口」设置多个值，作为备用，防止一台服务器部署了多个工程，端口被占用。
3）不要设置端口号为服务器远程连接端口 3389。
4）不要重复设置某个端口号既是 WebSocket 端口，又是 WebSocket 转发端口。
5）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 字段后面有空格，配置不生效。
6）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 大小写错误，配置不生效。
7）WebSocketConfig.requestPort 和 WebSocketConfig.requestPorts 不能同时存在于 fine_conf_entity 表中，否则会出错。
### 2.2 开放端口
  * 若防火墙开启，可关闭防火墙，或者单独开放端口。
  * 若云服务器有安全组或者类似的内容，需要设置端口对外开放。


### 2.3 重启工程
重启 FineBI 工程。
重启工程时，需要杀死工程下运行的进程，等待 2 分钟端口释放后，再重启工程，否则有可能重启失败。
### 2.4 效果预览
按照WebSocket端口>>WebSocket转发端口的顺序，即如果使用默认值端口，按照「48888，49888，48889」的顺序依次尝试监听。
  * 如果有一个端口建立监听成功，则不再尝试其他端口。


![](/core/style/lod.png)
  * 如果所有端口都无法与系统服务器建立监听，会进入部署向导页面，引导修改监听端口列表，相关功能会受到影响。
  * 此时请重新配置WebSocket端口和WebSocket转发端口，直到有可用端口。


![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：容器Websocket方案](<index.php?doc-view-1861.html>)
[下一篇：集群配置WebSocket端口 ![](/core/style/forward.png) ](<index.php?doc-view-1510.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
