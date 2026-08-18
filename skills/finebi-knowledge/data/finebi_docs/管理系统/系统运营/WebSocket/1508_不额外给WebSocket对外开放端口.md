---
title: 不额外给WebSocket对外开放端口
doc_id: 1508
url: https://help.fanruan.com/finebi6.X/doc-view-1508.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:29
---

> 1. 概述1.1 版本FineBI服务器版本6.01.2 应用场景部分公司对于工程环境安全级别要求较高，对于开发端口限制较多。若只开放一个端口，WebSocket 往往无法正常连接。1.3 功能简介在不

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 不额外给WebSocket对外开放端口
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[5](<edition-list-1508.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-12-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
  
---  
6.0  
### 1.2 应用场景
部分公司对于工程环境安全级别要求较高，对于开发端口限制较多。
若只开放一个端口，WebSocket 往往无法正常连接。
### 1.3 功能简介
在不能申请开放 WebSocket 端口的情况下，可以将socket端口也转发到开放的端口下。
本文将简单介绍在 Linux+Nginx+Tomcat 环境下，如何仅开放一个端口8888，仍可正常使用 WebSocket。
注：FineBI 内置了一个容器Websocket方案。推荐优先查看是否可使用该方案：[容器Websocket方案](<https://help.fanruan.com/finebi6.0/doc-view-1861.html>)
无需任何用户操作，无需任何手动配置，无需额外开启端口，系统可自动使用Web容器自带的WebSocket进行连接，端口复用http端口。
## 2\. 示例
### 2.1 设置websocket转发端口
管理员登录FineBI系统，点击「管理系统>系统管理>常规」，设置websocket 请求端口。如下图所示：  

此处设置的端口即为工程唯一对外端口，可自行设置，本文以8888为例。
注1：集群环境会默认勾选「已配置代理服务器」，非集群环境需要手动勾选已配置代理服务器（表示已经配置nginx）。
注2：FineBI内置了一个容器 websocket 方案，帮助用户实现快速配置 websocket 端口。
若「管理系统>系统管理>常规」页面不显示 HTTPS 设置项，说明此方案生效，Websocket 连接已正确配置，无需其他任何手动配置。
![](/core/style/lod.png)
### 2.2 修改nginx.conf
Nginx 监听 server 块下加上对请求 url 包含 /socket.io/ 的分支判断处理，将socket端口转发到开放的8888端口下，详细的配置文件参考：
[code]
    ...  
    server {  
            listen 8888;#监听端口，这个要和上面的WebSocketConfig.requestPort一致  
            server_name _;  
            underscores_in_headers on;  
            location / {  
                proxy_http_version 1.1;  
                proxy_pass http://FR.com;  
                proxy_next_upstream http_500 http_502 http_503 http_504 error timeout invalid_header non_idempotent;  
                proxy_redirect off;  
                proxy_set_header Host $host;  
                proxy_set_header X-Real-IP $remote_addr;  
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
                proxy_set_header Connection "";  
                #proxy_set_header X-Forwarded-Proto "https";  
                proxy_connect_timeout 20;  
                proxy_read_timeout 1000;  
                proxy_send_timeout 300;  
            }  
            #这里匹配/socket.io/转发给websocket的upstream  
            location ^~ /socket.io/ {  
                proxy_pass http://WBS.com;  
                proxy_http_version 1.1;  
                proxy_set_header Upgrade $http_upgrade;  
                proxy_set_header Connection "upgrade";  
                proxy_connect_timeout 20;  
                proxy_read_timeout 1000;  
                proxy_send_timeout 300;  
            }  
            ...  
    }  
    ...  
    
[/code]
### 2.3 重启服务
重启 Nginx 和 FineBI 工程后，设置生效。
用户只需要开放 8888 端口，即可正常使用 BI 工程，正常使用 websocket。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：HTTPS配置WebSocket](<index.php?doc-view-1509.html>)
[下一篇：WebSocket连接失败 ![](/core/style/forward.png) ](<index.php?doc-view-1507.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
