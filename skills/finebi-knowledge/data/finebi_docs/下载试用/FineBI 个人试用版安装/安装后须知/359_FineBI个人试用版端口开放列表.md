---
title: FineBI个人试用版端口开放列表
doc_id: 359
url: https://help.fanruan.com/finebi6.X/doc-view-359.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:29
---

> 1. 概述在安装完成 FineBI 后，服务器需要开放一些端口供系统监听使用。对于服务器安全要求高的客户来说，在启动之前需要保证这些端口的开放，否则 FineBI 无法正常启动。2. Spider 单机

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI个人试用版端口开放列表
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[28](<edition-list-359.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-12-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
在安装完成 FineBI 后，服务器需要开放一些端口供系统监听使用。对于服务器安全要求高的客户来说，在启动之前需要保证这些端口的开放，否则 FineBI 无法正常启动。
## 2\. Spider 单机部署开放端口
端口|  作用|  备注 | 是否开放  
  
---|---|---|---  
37799| http 监听端口BI 的 Web 端对外开放的端口| 端口可修改，参考 [修改 FineBI 端口号](<https://help.fanruan.com/finebi6.0/doc-view-326.html>) | 开放。否则无法正常访问页面  
800080018002| 计算引擎端口| FineBI6.1独有，需要确保未被占用| 无需开放  
8005| 远程关闭 Tomcat 服务端口| 端口可修改，可在%FineBI%/server/conf中的server.xml中修改 | 无需开放。默认监听地址127.0.0.1  
8009| Tomcat AJP 端口反向代理 Tomcat| 端口可修改，可在%FineBI%/server/conf中的server.xml中修改 | 无需开放。老版本 Tomcat 建议直接修改 server.xml 屏蔽  
17777| BI 的 spark.driver 端口| 端口可修改（端口被占用会自动递增），参考 [填报修改fine_conf_entity](<https://help.fanruan.com/finebi6.X/doc-view-2157.html>) 修改spark_driver_port | 无需开放。默认监听地址127.0.0.1  
17778| BI 的 spark.blockManager 端口| 端口可修改(端口被占用会自动递增），参考 [填报修改fine_conf_entity](<https://help.fanruan.com/finebi6.X/doc-view-2157.html>) 修改spark_blockManager_port | 无需开放。默认监听地址127.0.0.1  
48888| 平台的 WebSocket 端口| 端口可修改，详情参见：[Websocket简介](<https://help.fanruan.com/finebi6.X/doc-view-765.html>)注：WebSocket 协议建立在 TCP 之上。| 开放。不开影响 socket 通信，访问可能异常断开  
随机| 防破解用的端口| 不需单独开放，不影响 BI 使用 | 无需开放  
注：若使用了 Nginx 服务器，则可能需要单独修改 Requestport，详情参见：[Nginx 常见报错及解决方案](<https://help.fanruan.com/finebi6.0/doc-view-536.html>)。 
### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：FineBI初始化设置](<index.php?doc-view-262.html>)
[下一篇：FineBI个人试用版安装目录结构 ![](/core/style/forward.png) ](<index.php?doc-view-355.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
