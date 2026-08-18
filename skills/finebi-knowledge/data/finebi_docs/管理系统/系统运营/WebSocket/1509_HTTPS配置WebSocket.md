---
title: HTTPS配置WebSocket
doc_id: 1509
url: https://help.fanruan.com/finebi6.X/doc-view-1509.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:28
---

> 1. 概述1.1 问题描述HTTP 是超文本传输协议，信息是明文传输的。HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，比 HTTP 协议安全。可以通过两种方法在

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# HTTPS配置WebSocket
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[8](<edition-list-1509.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-10-14 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 问题描述
HTTP 是超文本传输协议，信息是明文传输的。HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，比 HTTP 协议安全。
可以通过两种方法在 HTTPS 环境中配置 WebSocket，下面将详细介绍。
注：5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。推荐优先查看是否可使用该方案：[容器Websocket方案](<https://help.fanruan.com/finebi6.0/doc-view-1861.html>)
无需任何用户操作，无需任何手动配置，无需额外开启端口，系统可自动使用Web容器自带的WebSocket进行连接，端口复用http端口。
### 1.2 解决思路
方法一：如果没用 Nginx，可以直接在 Web 服务器上配置 SSL。
方法二：如果用了 Nginx 反向代理服务器，那么可以在 Nginx 上配置 SSL，而应用服务器如 Tomcat 不配置 SSL。这样客户端和 Nginx 之间走 https 通讯，Nginx 和 Tomcat 之间通过 proxy_pass 走 http 通讯。
注1：JAR 包时间在 2019-12-05 之后的工程，支持在数据决策系统中，通过可视化界面设置 WebSocket 。详情请参见：[常规 第三章](<https://help.fanruan.com/finereport/doc-view-2212.html>)
注2：11.0.2 及之后版本，新增一个容器 websocket 方案，帮助用户实现快速配置 websocket 端口。
若「管理系统>系统管理>常规」页面不显示Websocket设置项，说明此方案生效，Websocket 连接已正确配置，无需其他任何手动配置。
![2020-10-20_15-55-20.png](/core/style/lod.png)
## 2\. 方法一：未配置代理
以 Windows 系统下使用方法一配置 WebSocket 为例。
### 2.1 搭建 HTTPS 环境
搭建 HTTPS 环境的详细内容参见：[配置SSL证书实现HTTPS访问](<https://help.fanruan.com/finebi6.0/doc-view-784.html>)。
### 2.2 配置数据库
在 FineDB 的 fine_conf_entity 表中添加以下 4 个参数项，参数信息如下表所示：
参数项| 参数值   
---|---  
WebSocketConfig.protocol| ssl（默认）  
WebSocketConfig.keyStore| 来自%TOMCAT_HOME%\conf\server.xml中的 keystoreFile 字段的值  
WebSocketConfig.keyStorePassword| 来自%TOMCAT_HOME%\conf\server.xml中的 keystorePass 字段的值  
WebSocketConfig.keyStoreFormat| JKS（默认）   
WebSocketConfig.keyStore 和 WebSocketConfig.keyStorePassword 的配置如下图所示：
注：fine_conf_entity 表中的WebSocketConfig.keyStore的值必须是绝对路径，不可以是相对路径。
![1.png](/core/style/lod.png)
数据库表中新增信息如下图所示：
![1571810654997930.png](/core/style/lod.png)
配置完成之后，重启报表服务器即可生效。
注：Https 配置 WebSocket 后，Http下 WebSocket 会请求不到。
## 3\. 方法二：配置了代理
以 Linux+Nginx+Tomcat 下使用方法二配置 WebSocket 为例。
注：非必要请勿使用自签名证书，使用自签名证书有可能会导致部分记录丢失，详情请参见 4.1 节。
### 3.1 生成自签名的SSL证书
注：已有证书的可以跳过该步骤。
**1）安装 OpenSSL 并验证。**
# yum install openssl openssl-devel
# openssl version -a
**2）生成密钥文件 server.key。**
# openssl genrsa -des3 -out server.key 2048
生成密钥文件时会要求设置密码，设置好密码后需要记住这个密码。
![1.png](/core/style/lod.png)
这样就生成了 server.key 文件。此后用到了该文件会经常要求输入密码。如 Nginx 加载了该 server.key，启动时会要求输入密码。
![image2019-1-4_14-42-36.png](/core/style/lod.png)
如果嫌麻烦，可以用以下命令生成 server.key，这样就不再需要输入密码。
# openssl rsa -in server.key -out server.key
**3）生成服务器证书的申请文件 server.csr。**
# openssl req -new -key server.key -out server.csr
![image2019-1-4_15-4-42.png](/core/style/lod.png)
Country Name 填 CN，Common Name 填主机名，不填的话浏览器会提示不安全，其余均可为空。
**4）生成 CA 证书 ca.crt。**
# openssl req -new -x509 -key server.key -out ca.crt -days 3650
CA证书用于给自己的证书签名。
**5）生成服务器证书 server.crt。**
# openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
6）查看生成的5个文件，其中 server.crt 和 server.key 就是 Nginx 需要的证书文件。
![image2019-1-4_15-11-20.png](/core/style/lod.png)
### 3.2 Nginx配置HTTPS
HTTP 默认端口是 80，HTTPS 默认端口是 443。
Nginx配置完整版：[nginx-demo .conf](<doc-download-/uploads/file/20191025/nginx-demo .conf> "下载资料")
注意：修改 nginx.conf 后，重启 Nginx 时不要用 reload，要用 stop 和 start，否则配置可能不生效。
**1）配置 443 端口**
[code]
    server {  
            listen       443 ssl;  
            server_name  192.168.5.232;  
           
            ssl_certificate      /mnt/hgfs/share/keys/server.crt; #证书绝对路径  
            ssl_certificate_key  /mnt/hgfs/share/keys/server.key; #key绝对路径  
            ssl_session_cache    shared:SSL:1m; #储存SSL会话的缓存类型和大小    
            ssl_session_timeout  5m; #会话过期时间  
       
            ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP; #为建立安全连接，服务器所允许的密码格式列表  
            ssl_prefer_server_ciphers  on; #依赖SSLv3和TLSv1协议的服务器密码将优先于客户端密码  
           
            #禁止在header中出现服务器版本，防止黑客利用版本漏洞攻击  
            #server_tokens off;  
            #如果是全站 HTTPS 并且不考虑 HTTP 的话，可以加入 HSTS 告诉浏览器本网站全站加密，并且强制用 HTTPS 访问  
            #fastcgi_param   HTTPS               on;  
            #fastcgi_param   HTTP_SCHEME         https;  
           
            location / {  
                proxy_http_version 1.1;  
                proxy_set_header Connection "";  
       
                proxy_buffering off;  
                proxy_next_upstream http_500 http_502 http_503 error timeout invalid_header non_idempotent;  
       
                proxy_redirect off;  
                proxy_set_header Host $host;  
                proxy_set_header X-Real-IP $remote_addr;  
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
                # 把 HTTPS 的协议告知容器（如tomcat），否则容器可能认为是 HTTP 的请求  
                proxy_set_header X-Forwarded-Proto $scheme;  
                   
                proxy_connect_timeout    20;  
                proxy_read_timeout       1000;  
                proxy_send_timeout       300;  
       
                proxy_pass http://FR.com;  
            }  
         }  
    
[/code]
**2）配置 WebSocket 端口**
WebSocket 配置 HTTPS 很容易出问题，集群启动后，可在智能运维>内存管理中，看实时内存图是否显示。
[code]
    server {   
          listen       48889 ssl;              
          server_name  192.168.5.232;  
       
          ssl_certificate      /mnt/hgfs/share/keys/server.crt;  
          ssl_certificate_key  /mnt/hgfs/share/keys/server.key;  
       
          ssl_session_cache    shared:SSL:1m;  
          ssl_session_timeout  5m;  
       
          ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;  
          ssl_prefer_server_ciphers  on;  
          location / {  
              proxy_request_buffering off;  
              proxy_buffering off;  
              proxy_connect_timeout 20;  
              proxy_read_timeout 1000;  
              proxy_send_timeout       300;  
              proxy_http_version 1.1;  
              proxy_set_header Upgrade $http_upgrade;  
              proxy_set_header Connection "upgrade";  
              proxy_pass http://WBS.com;  
           }  
      }  
    
[/code]
Nginx 转发默认监听38889端口，节点的 WebSocket默认监听48888端口，可自行修改。转发端口是fine_conf_entity表中的参数项WebSocketConfig.requestPorts，且支持配置多个端口进行多次转发，如下所示：
id| value  
---|---  
WebSocketConfig.port| 48888  
WebSocketConfig.requestPorts| 48889  
转发端口可直接在前台进行配置，可参考文档：[常规 第三章](<https://help.fanruan.com/finebi6.0/doc-view-414.html>)
注：2019-09-27 及之前版本的 JAR 包，转发端口生效参数项是 WebSocketConfig.requestPort 且只支持一个端口。如下所示：  

id| value  
---|---  
WebSocketConfig.port| 48888  
WebSocketConfig.requestPort| 48889  
**3）配置 HTTP 强转 HTTPS**  

[code]
    rewrite ^(.*)$  https://$server_name$1 permanent;
[/code]
**4）Nginx 跨域设置**
[code]
    add_header access-control-allow-Headers X-Requested-With;
    add_header access-control-allow-Methods GET,POST,OPTIONS;
[/code]
注：Nginx 跨域配置不能加上「add_header access-control-allow-Origin *;」这个前端应该是已经有过配置，增加会导致前端无法选择跨域配置，而导致错误。
## 4\. 注意事项
### 4.1 部分浏览器设置不生效
**问题描述：**
使用方法二进行配置后，火狐浏览器访问还是空白，IE 浏览器访问模板没有记录。
这是因为自签名的证书不被浏览器信任，页面能访问是因为手动添加了例外，但是48888端口没有，所以浏览器拦截了 Socket 请求。
**解决方案：**
F12看一下拦截的请求，复制下来，直接访问一下48888端口添加安全例外或者手动添加。
![1552632213Ey2N4v2s.png](/core/style/lod.png)  
![1552632230ReRczyKU.png](/core/style/lod.png)  

这样浏览器就可以查看实时内存了，如下图所示：
![1552632336hewk50V0.png](/core/style/lod.png)  

### 4.2 其他
1）密钥路径：
  * Tomcat 配置中 server.xml 里面绝对路径/相对路径都可以。
  * 数据决策系统中「系统管理>常规>https 设置」中「SSL 密钥路径」只支持绝对路径。


2）设计器不支持配置 HTTPS，EXE 安装的 BI 不支持配置 HTTPS。
3）若 Nginx 配置了 https，那么就不要在「系统管理>常规>https」设置中进行配置。
4）Tomcat 工程配置了 https，http 和 https 都可以访问工程。但是 websocket 不能同时支持，https 连接正常，http 就会连接失败。
Nginx 工程无影响，websocket 可同时支持。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：集群配置WebSocket端口](<index.php?doc-view-1510.html>)
[下一篇：不额外给WebSocket对外开放端口 ![](/core/style/forward.png) ](<index.php?doc-view-1508.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
