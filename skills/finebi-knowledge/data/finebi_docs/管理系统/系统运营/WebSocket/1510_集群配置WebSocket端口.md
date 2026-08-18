---
title: 集群配置WebSocket端口
doc_id: 1510
url: https://help.fanruan.com/finebi6.X/doc-view-1510.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:28
---

> 1. 概述1.1 版本BI 服务器版本5.11.2 应用场景本文将介绍在集群环境下，如何配置 WebSocket 端口。注：5.1.20 及之后版本的BI工程，新增了一个容器Websocket方案。推荐

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 集群配置WebSocket端口
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[2](<edition-list-1510.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-05-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
BI 服务器版本  
---  
5.1  
### 1.2 应用场景
本文将介绍在集群环境下，如何配置 WebSocket 端口。
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
2）建议「WebSocket转发端口」的值要多于集群节点数，保证每个节点都会选择当前可用的端口，不会因为端口占用而导致服务器无法启动。
3）建议「WebSocket端口」设置多个值，作为备用，防止一台服务器部署了多个工程，端口被占用。
4）不要设置端口号为服务器远程连接端口 3389。
5）如果工程和 nginx 负载均衡在一个环境下，不要重复设置某个端口号既是 WebSocket 端口，又是 WebSocket 转发端口。
6）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 字段后面有空格，配置不生效。
7）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 大小写错误，配置不生效。
8）WebSocketConfig.requestPort 和 WebSocketConfig.requestPorts 不能同时存在于 fine_conf_entity 表中，否则会出错。
### 2.2 修改集群转发策略
在负载均衡层面配置 Websocket 的转发策略为粘滞，详情请参见：[负载均衡配置指导](<https://help.fanruan.com/finereport/doc-view-2819.html>)
### 2.3 修改集群监听端口
nginx.conf 文件中，server 的 listen 端口需要与「WebSocket 转发端口」配置一致，详情请参见：[Linux 系统安装配置 Nginx 4.1 节](<https://help.fanruan.com/finereport/doc-view-2644.html>)
例如用设置的 Websocket 转发端口（WebSocketConfig.requestPort默认48889）转发 Websocket 端口（WebSocketConfig.port默认 48888 ）
以下示例为工程服务器 IP 为 192.168.6.171，Nginx 服务器 IP 为 192.168.6.181，如下图所示：
[code]
    #用户或者用户组 默认为nobody  
    #user  root;  
    #允许进程数量，建议设置为cpu核心数或者auto自动检测，注意Windows服务器上虽然可以启动多个processes，但是实际只会用其中一个  
    worker_processes  auto;  
    #自动根据CPU数目绑定CPU亲缘性，nginx1.9.10及以上版本才能用  
    #worker_cpu_affinity  auto;  
    #error日志存放位置  
    error_log  logs/error.log;  
    #error_log  logs/error.log  notice;  
    #error_log  logs/error.log  info;  
    #PID存放位置  
    #pid        logs/nginx.pid;  
    #工作模式及连接数上限  
    events {  
        #每个worker_processes的最大连接数，Windows服务器无论这里设置多大实际都只有1024  
        #并发数是 worker_processes 和 worker_connections 的乘积  
        worker_connections  1024;  
    }  
    http {  
        #设定mime类型,类型由mime.type文件定义  
        include       mime.types;  
        #默认文件类型，默认为text/plain  
        default_type  application/octet-stream;  
        #日志格式  
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '  
                          '$status $body_bytes_sent "$http_referer" '  
                          '"$http_user_agent" "$http_x_forwarded_for" $upstream_addr';  
        #access_log确定了Nginx是否保存访问日志，将这个设置为关闭可以降低磁盘IO而提升速度  
        access_log  off;  
        #access_log  logs/access.log  main;  
        #sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件，  
        #对于普通应用，必须设为 on,  
        #如果用来进行下载等应用磁盘IO重负载应用，可设置为 off，  
        #以平衡磁盘与网络I/O处理速度，降低系统的uptime.  
        sendfile        on;  
        #tcp_nopush     on;  
        #http长连接(client <-> nginx)超时时间，请求完成之后连接保持的时间  
        keepalive_timeout  65s;  
        #types_hash_max_size越小，消耗的内存就越小，但散列key的冲突率可能上升  
        types_hash_max_size 2048;  
        #开启gzip压缩  
        #gzip  on;  
        #gzip_disable "MSIE [1-6].";  
        #设定请求缓冲  
        client_header_buffer_size    512k;  
        large_client_header_buffers  4 512k;  
        #允许用户最大上传数据大小，根据业务需求调整上传文件大小限制  
        client_max_body_size 100M;  
           
        upstream FR.com {  
            #max_fails=n fail_timeout=m 表示m时间内超时n次失败尝试，将会在接下来m时间内标记此节点不可用（m时间过后无论此节点是否启动都会被重新标记为可用状态）  
            #其中fails为“失败尝试”，失败尝试由下面server配置中，proxy_next_upstream指令定义  
            server 192.168.6.171:8080 max_fails=15 fail_timeout=300s;  
      
            keepalive 300;   
            #其它server参数说明：  
            #down 标记服务器挂掉  
            #backup 备份服务器，当主服务器（例如上面的95和96）不可用时才加入服务器；  
            #weight=number 权重，默认为1  
            #内置负载均衡策略有ip hash、轮询、加权轮询（设置server的weight值）  
            #ip_hash;  
            #↓====================主动健康检查模块配置====================↓#  
            ## interval：向后端发送的健康检查包的间隔，单位ms。  
            ## fall(fall_count): 如果连续失败次数达到fall_count，服务器就被认为是down  
            ## rise(rise_count): 如果连续成功次数达到rise_count，服务器就被认为是up。  
            ## timeout: 后端健康请求的超时时间，单位ms。  
            ## type：健康检查包的类型，现在支持tcp、udp、http类型  
            #check interval=2000 rise=5 fall=10 timeout=10000 type=http;  
            # 检查请求, 7-16之前的persist版本，只能使用 /webroot/decision/system/info HTTP;  
            #check_http_send "GET /webroot/decision/system/health HTTP/1.0\r\n\r\n"; # 检查请求  
            #check_http_expect_alive http_2xx http_3xx; #该指令指定HTTP回复的成功状态，默认认为2XX和3XX的状态是健康的。  
            #↑====================主动健康检查模块配置====================↑#  
        }  
        upstream WBS.com {   
            server 192.168.6.171:48888 max_fails=15 fail_timeout=300s;  
            #这里必须使用ip_hash  
        ip_hash;  
        }  
        server {  
            listen       8123;   
            server_name  192.168.6.181;  
            #nginx默认不转发带下划线的header，比如请求的header中有_device_这个header，转发到负载服务器时默认会丢弃  
            #可以在http或者http -> server这两个上下文中加入一条属性  
            underscores_in_headers on;  
            #charset koi8-r;  
            #access_log  logs/host.access.log  main;  
            #↓====================主动健康检查模块监测页面====================↓#  
            #location /status {  
            #    healthcheck_status html;  
            #}  
            #↑====================主动健康检查模块监测页面====================↑#  
            #根/下的请求默认转发到的位置，即端口后面跟的请求全部转发到如下反向代理  
            location / {  
                #对于HTTP代理，proxy_http_version指令应该设置为“1.1”，同时“Connection”头的值也应被清空（如下proxy_set_header Connection ""）  
                proxy_http_version 1.1;  
                #定义转发到的服务器（组）  
                proxy_pass http://FR.com;  
                #设置nginx转发时转发到下一个服务器的条件，此处设置将未成功请求（proxy_next_upstream定义的40x， 50x等）传递到下一步进行处理  
                # 失败尝试说明：50x和429在此配置会被当作fail，error，timeout并 invalid_header无论配置与否都被认为fail，http_403 and http_404配置与否都不是fail。  
                # error:与后端服务器建立连接、传递请求、读取请求头发生的错误  
                # timeout:与后端服务器建立连接、传递请求、读取请求头超时，设置在proxy_next_upstream_timeout和proxy_next_upstream_tries（默认值都是0）  
                # invalid_header:服务器返回非法或者为空  
                proxy_next_upstream http_500 http_502 http_503 http_504 http_403 http_404 http_429 error timeout invalid_header non_idempotent;  
                #proxy_next_upstream_timeout 0;  
                #proxy_next_upstream_tries 0;  
                #重定向，参数off将在这个字段中禁止所有的proxy_redirect指令  
                proxy_redirect off;  
                #请求头的一些设置，语法proxy_set_header [field] [value];  
                #$host为请求的主机名称（即nginx代理服务器）， $server_port为主机端口（即nginx端口），如果有外网映射，这里应改写 外网地址:外网端口 形式（不要带协议）  
                proxy_set_header Host $host:$server_port;  
                #这里$remote_addr客户端ip地址  
                proxy_set_header X-Real-IP $remote_addr;  
                #这里$proxy_add_x_forwarded_for是代理层级，如果由多层代理，这里就写client，proxy1，proxy2，这里应该是client即客户端ip  
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
                #与后端服务器的连接不需要保持  
            proxy_set_header Connection "";  
                #NGINX会缓冲来自代理服务器的响应。响应存储在内部缓冲区中，并且在收到整个响应之前不会发送到客户端。  
                #缓冲有助于优化慢客户端的性能，如果响应从NGINX同步传递到客户端，则会浪费代理服务器时间。  
                #但是，当启用缓冲时，NGINX允许代理服务器快速处理响应，而NGINX将响应存储的时间与客户端下载它们所需的时间相同  
                #是否开启缓冲，默认开启  
                #proxy_buffering off;  
                #设置缓冲区的大小为size  
                #proxy_buffer_size     64k;  
                #每个连接设置缓冲区的数量和大小，proxy_buffers [number] [size];  
                #proxy_buffers         32 64k;  
                #当开启缓冲响应的功能以后，在没有读到全部响应的情况下，写缓冲到达一定大小时，nginx一定会向客户端发送响应，直到缓冲小于此值  
                #proxy_busy_buffers_size 64k;  
                #连接到代理服务器超时时间，默认60s，不能超过75s  
                #不宜太长或者太短，配合max_fails和fail_timeout设置  
                #并发量高的情况下，服务器压力过大时容易出现超时，可以考虑max_fails和fail_timeout设置大一点，减少nginx错误踢出节点的几率  
                proxy_connect_timeout    75;  
                #读取超时，默认60s，如果在超时时间内服务器未返回任何数据，视为超时。如果没有大数据量计算或导出的模板，则建议配置不超过100s,如果有大数据量计算或导出的模板，则根据最长耗时的模板时间进行配置。  
                proxy_read_timeout       400;  
                #写入超时，默认60s，如果在超时时间内服务器未收到数据表示超时，视为超时。如果没有大数据量计算或导出的模板，则建议配置不超过100s,如果有大数据量计算或导出的模板，则根据最长耗时的模板时间进行配置。  
                proxy_send_timeout       400;  
            }  
            #定义404页面  
            #error_page  404              /404.html;  
            # redirect server error pages to the static page /50x.html  
            #定义50x页面  
            error_page   500 502 503 504  /50x.html;  
            location = /50x.html {  
                root   html;  
            }  
        }  
        server {    
            #此处为websocket端口，如果是集群部署，FineReport工程为38889，FineBI工程为48889  
            listen 48889;                
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
### 2.4 开放端口
  * 若防火墙开启，可关闭防火墙，或者单独开放端口。
  * 若云服务器有安全组或者类似的内容，需要设置端口对外开放。


### 2.5 重启工程
重启 nginx 和 FineBI 工程。
重启工程时，需要杀死工程下运行的进程，等待 2 分钟端口释放后，再重启工程，否则有可能重启失败。
### 2.6 效果预览
按照WebSocket转发端口>>WebSocket端口的顺序，即如果使用默认值端口，按照「48889，48888，49888」的顺序依次尝试监听。
  * 如果有一个端口建立监听成功，则不再尝试其他端口。


![](/core/style/lod.png)
  * 如果所有端口都无法与系统服务器建立监听，会进入部署向导页面，引导修改监听端口列表，相关功能会受到影响。


![](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：单机配置WebSocket端口](<index.php?doc-view-1511.html>)
[下一篇：HTTPS配置WebSocket ![](/core/style/forward.png) ](<index.php?doc-view-1509.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
