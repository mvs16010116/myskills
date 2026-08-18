---
title: 容器Websocket方案
doc_id: 1861
url: https://help.fanruan.com/finebi6.X/doc-view-1861.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:27
---

> 1. 概述1.1 版本BI服务器版本5.1.201.2 应用场景为了降低Websocket配置难度，5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。该方案使用Web容器自带的W

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 容器Websocket方案
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[12](<edition-list-1861.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2023-03-31 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
BI服务器版本  
  
---  
5.1.20  
### 1.2 应用场景
为了降低Websocket配置难度，5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。
该方案使用Web容器自带的WebSocket进行连接，端口复用http端口。用户无需对外开启端口，无需任何手动配置。
当工程支持容器Websocket方案时，前台访问会优先使用新方案，失败后使用老socket.io方案进行重试。
## 2\. 方案执行步骤
容器Websocket方案的执行，需要满足以下一些条件和配置。
### 2.1 容器环境检验
容器Websocket方案，仅支持以下容器（容器环境一般是由用户自行准备，非FineBI自带）
容器| 版本| 说明  
---|---|---  
Tomcat| 支持Tomcat7.0.47~9.0 版本| -  
WebLogic| Weblogic12c及以上版本| 需要修改web.xml名称空间，其他不变<!--修改web-app如下-->  
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
xmlns="http://xmlns.jcp.org/xml/ns/javaee"  
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"  
id="WebApp_ID" version="3.1">  
WebSphere| WebSphere9及以上版本| -  
JBoss| eap6.4+wildly9+| **eap6.4需要修改配置** ：web-inf下新增jboss-web.xml<?xml version="1.0" encoding="UTF-8"?>  
<!--Enable WebSockets -->  
<jboss-web>  
<enable-websockets>true</enable-websockets>  
</jboss-web>修改${hboss_home}/standalone/configuration/standalone.xml将protocol="HTTP/1.1"修改为protocol="org.apache.coyote.http11.Http11NioProtocol"![](/core/style/lod.png)  
若当前工程所在容器环境满足条件，则「管理系统>系统管理>常规」页面不显示「WebSocket设置」。
![](/core/style/lod.png)
### 2.2 负载均衡配置
#### 2.2.1 Nginx
1）修改 http 配置
在每个 location 块下添加以下语句：
[code]
    proxy_set_header Upgrade $http_upgrade;  
    proxy_set_header Connection $http_connection;  
    
[/code]
![](/core/style/lod.png)
2）需检查 Nginx 是否进行过 WebSocket 配置
打开 nginx.conf 文件，查看是否出现以下内容：
[code]
    server {    
            #此处为websocket端口，如果是集群部署，FineReport工程为38889，FineBI工程为48889  
            listen 38889;                
            server_name 192.168.6.181;  
            location / {   
                 proxy_http_version 1.1;  
                 proxy_pass http://WBS.com;  
                 proxy_connect_timeout 75;  
                 proxy_read_timeout 400;  
                 proxy_send_timeout 400;  
                 #升级目标为$http_upgrade 值实际为websocket  
         proxy_set_header Upgrade $http_upgrade;  
                 #Connection设置升级  
         proxy_set_header Connection "upgrade";  
                 }  
            }
[/code]
若未出现以上内容，即未在 Nginx 中配置过 WebSocket ，可直接使用容器化 WebSocket 方案。
若出现以上内容，即曾在 Nginx 中配置过 WebSocket，需要删除以上内容。如下图所示：
![](/core/style/lod.png)
#### 2.2.2 traefik
无需额外配置，原ws配置保留/删除不影响容器化WebSocket方案生效。
#### 2.2.3 f5
无需额外配置，原ws配置保留/删除不影响容器化WebSocket方案生效。
### 2.3 浏览器环境
  * 容器化WebSocket方案支持 Chrome、FireFox、Edge、IE10 及以上版本浏览器。
  * 容器化WebSocket方案不支持 IE9 及以下版本浏览器


### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：Websocket简介](<index.php?doc-view-765.html>)
[下一篇：单机配置WebSocket端口 ![](/core/style/forward.png) ](<index.php?doc-view-1511.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
