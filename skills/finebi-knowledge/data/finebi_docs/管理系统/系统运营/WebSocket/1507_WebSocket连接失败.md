---
title: WebSocket连接失败
doc_id: 1507
url: https://help.fanruan.com/finebi6.X/doc-view-1507.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:30
---

> 1. WebSocket 连接失败现象1）管理员登录 FineBI&nbsp;系统，点击「管理系统&gt;智能运维&gt;负载管理」，「负载监控」Tab 下「负载」、「内存利用率」和「CPU 利用率」这

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# WebSocket连接失败
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[5](<edition-list-1507.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2023-06-19 
[](<javascript:;>) [](<javascript:>)
## 1\. WebSocket 连接失败现象
1）管理员登录 FineBI 系统，点击「管理系统>智能运维>负载管理」，「负载监控」Tab 下「负载」、「内存利用率」和「CPU 利用率」这三张图显示空白。
顶部弹出提示信息：Socket 未连接，实时内存显示等异常，相关端口可能未开放
2）管理员登录 FineBI 系统，点击「管理系统>智能运维>平台日志」，「访问统计」Tab 下「当前系统在线人数」无法正确显示。模板执行过程统计如内存、耗时等无法记录。
顶部弹出提示信息：Socket 未连接，系统访问用户统计等异常，请开启相关端口，相关端口可能未开放
3）用户点击「管理系统>数据连接」，进入数据连接编辑界面，可能存在多人同时编辑同一个数据连接的情况。
顶部弹出提示信息：Socket 未连接，可能存在多人同时编辑造成冲突，相关端口可能未开放
4）踢出登录失效，不能实时踢出，在框架内显示登录页面，即没有跳出框架直接跳转到登录界面。如下图所示：
注：该问题出现的场景：单一登录踢出、禁用用户、修改用户密码、修改认证方式、切换同步导入、平台使用用户禁用用户/打开限制开关，更换 Lic 等。
![](/core/style/lod.png)
5）用户收不到右下角消息弹窗且小铃铛处无消息提示，但是可以点击小铃铛进入消息面板查看。
6）登录超时，无法获取正确的 token 有效期
用户登录 FineBI 系统时，不勾选「保持登录状态」。登录超时设置为 1 小时，若用户在3点登录，3点20分在平台进行了操作。  

  * WebSocket 连接成功，应为 4 点 20 被踢出（平台无操作情况下）。
  * WebSocket 未连接，则不能重新获取 token ，4 点即被踢出。  



用户登录 FineBI 系统时，勾选「保持登录状态」，默认无操作 14 天后被踢出，若 14 天内在平台上操作，不能重新获取 token ，依旧 14 天后被踢出。
注1：2020-08-31 及之后的 JAR ，Websocket 未连接时，不会出现这个现象。
注2：2020-08-31 之前的 JAR ，若无法开放额外端口或不允许使用 socket，可以安装「[刷新登录状态插件](<https://help.fanruan.com/finebi6.0/doc-view-753.html>)」解决这个问题。
管理员登录平台后，顶部弹出提示信息：Socket 未连接，使用过程中将无法保持登录状态，相关端口可能未开放
每次刷新平台页面也会弹出提示，刷新指浏览器刷新如 F5。
注：2020-08-31 及之后的 JAR ，Websocket 未连接时，没有该提示。
7）在插件商城安装或者删除插件时没有成功或者失败的提示。
## 2\. 确认 Websocket 连接失败
用户可通过三种方法确认 Websocket 连接失败。
1）管理员登录 FineBI 系统，查看「管理系统>智能运维>负载管理>实时负载」下的三张图片，不显示则表示 WebSocket 未连接。
![](/core/style/lod.png)
2）F12 打开控制台，输入「Dec.socket.connected」，如果是「false」表示未连接。
![](/core/style/lod.png)
3）F12 打开控制台，如果有关于 48889（代理服务器默认端口号） 之类 Socket 端口的报错，那就是没有连接成功。
![](/core/style/lod.png)
## 3\. 直接访问工程连接失败
适用场景：未通过负载均衡访问工程，直接访问工程，websocket连接失败
请用户根据下文依次排查并优化。
### 3.1 确认端口是否被占用
通过「[填报修改fine_conf_entity](<https://help.fanruan.com/finebi6.X/doc-view-2157.html>) 」预览 fine_conf_entity 表中的以下字段，查看 WebSocket 端口/转发端口。
端口  
| JAR包| 参数名| 参数默认值  
---|---|---|---  
Websocket 端口| -| WebSocketConfig.port| ["48888", "49888"]  
Websocket 转发端口| 2019-11-08 之前| WebSocketConfig.requestPort| 48889  
2019-11-08 及之后| WebSocketConfig.requestPorts| 48889  
  
确认端口/转发端口是否被其他进程占用，若被占用且进程很重要，请更换其他可用端口。
超级管理员可通过填报的方式修改 WebSocket 端口/转发端口。重启服务器后设置生效。
注1：修改 fine_conf_entity 表字段值的方法请参考 [填报修改fine_conf_entity](<https://help.fanruan.com/finebi6.X/doc-view-2157.html>) 。
注2：超级管理员可以通过「[fine_conf_entity可视化配置插件](<https://help.fanruan.com/finebi6.0/doc-view-1235.html>)」查看、修改 WebSocket 端口，但不支持通过该插件查看、修改 WebSocket 转发端口
### 3.2 确认端口配置是否未生效
WebSocket 端口/转发端口的设置有一些注意事项，请确认是否正确的设置了端口号：
1）端口号可设置范围：1024~65535，若为多个值，设置格式为：[端口号1,端口号2,端口号3]。
2）建议「WebSocket转发端口」的值要多于集群节点数，保证每个节点都会选择当前可用的端口，不会因为端口占用而导致服务器无法启动。
3）建议「WebSocket端口」设置多个值，作为备用，防止一台服务器部署了多个工程，端口被占用。
4）不要设置端口号为服务器远程连接端口 3389。
5）如果工程和 nginx 负载均衡在一个环境下，不要重复设置某个端口号既是 WebSocket 端口，又是 WebSocket 转发端口。
6）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 字段后面有空格，配置不生效。
7）若 WebSocketConfig.port、WebSocketConfig.requestPort、WebSocketConfig.requestPorts 大小写错误，配置不生效。
8）WebSocketConfig.requestPort 和 WebSocketConfig.requestPorts 不能同时存在于 fine_conf_entity 表中，否则会出错。
### 3.3 确认端口是否对外开放
**排查步骤：**
若确定 WebSocket 端口/转发端口未被其他进程占用，请确定设置的端口是否对外开放。
  * linux：nc -vz -w 2 [ip] [port]
  * windows：telnet 服务器ip websocket端口


**解决方法：**
1）开放服务器的防火墙端口限制。
2）开启阿里云/华为云/微软云服务器的安全组端口限制。
3）关闭阿里云的健康检查。
### 3.4 确认是否为HTTPS环境
证书配置的https环境需要配置websocket，参考文档：[HTTPS环境配置WebSocket](<https://help.fanruan.com/finebi6.0/doc-view-1509.html>)
1）密钥路径：
  * Tomcat 配置中 server.xml 里面绝对路径/相对路径都可以。
  * FineBI 系统中「系统管理>常规>https 设置」中「SSL 密钥路径」只支持绝对路径。


2）设计器不支持配置 HTTPS，EXE 安装的 BI 不支持配置 HTTPS。
3）若 Nginx 配置了 https，那么就不要在「系统管理>常规>https」设置中进行配置。
4）工程配置了 https，http 和 https 都可以访问工程。但是 websocket 不能同时支持，https 连接正常，http 就会连接失败。
### 3.5 JAR 包冲突
**问题描述：**
工程下的 JAR 包出现冲突时，会出现服务器部署向导，提示「WebSocket 端口异常」，如下图所示：
![](/core/style/lod.png)
**解决方法：**
删除造成冲突的 JAR 包，杀死工程的进程，等待 2 分钟端口释放后，重启工程。
如果 Apache Impala 是从官网下载的，不要将 slf4j-log4j12-1.5.11.jar和slf4j-api-1.5.11.jar 放到%FineReport%\webapps\webroot\WEB-INF\lib下，否则会造 Websoket 端口异常。
### 3.6 确认服务器请求是否太慢
WebSocket 连接时间代码里设置的为 20 秒，请求时间超过的话，直接判定 WebSocket 连接失败。
### 3.7 查看控制台报错
F12 打开控制台，WebSocket 常见报错及可能原因如下：
  * net::ERR_SSL_PROTOCOL_ERROR：工程配置了https，websocket没有配置。
  * net::ERR_EMPTY_RESPONCE：服务器配置了https，但是用的http访问。
  * net::ERR_CONNECTION_REFUSED：端口未开放或者该端口没有被监听。
  * net::ERR_CONECTION_TIMEOUT：网络问题，域名解析速度慢。


### 3.8 浏览器缓存
**问题描述：** 同一台电脑上不同浏览器访问工程，有的websocket连接成功，有的连接失败。
**解决方法：** 清理浏览器缓存即可。
## 4\. 通过负载均衡访问工程连接失败
适用场景：通过负载均衡访问工程，websocket连接失败
请用户根据下文依次排查并优化。
### 4.1 确认服务器上访问websocket是否连接正常
在服务器上用 localhost 访问工程，确认websocket是否正常连接。
1）若websocket连接，进入 4.2 节排查步骤。
2）若websocket连接失败，请确认websocket端口是否被其他进程占用。
超级管理员可通过「[fine_conf_entity可视化配置插件](<https://help.fanruan.com/finereport/doc-view-2471.html>)」查看 WebSocket 端口/转发端口。
端口  
| JAR包| 参数名| 参数默认值  
---|---|---|---  
Websocket 端口| -| WebSocketConfig.port| ["48888", "49888"]  
Websocket 转发端口| 2019-11-08 之前| WebSocketConfig.requestPort| 48889  
2019-11-08 及之后| WebSocketConfig.requestPorts| 48889  
  
确认端口/转发端口是否被其他进程占用，若被占用且进程很重要，请更换其他可用端口。
超级管理员可通过「fine_conf_entity可视化配置插件」修改 WebSocket 端口。重启服务器后设置生效。
注：修改 FineDB 数据库表字段值的方法请参考 [FineDB 常用表字段修改](<https://help.fanruan.com/finereport/doc-view-2471.html>) 。
### 4.2 确认不通过负载服务器，直接访问工程是否连接正常
不通过负载均衡服务器，第三方电脑直接访问工程确认websocket是否连接正常。  

1）若直接访问工程websocket连接失败，则用本文第 3 章内容进行排查。
2）若直接访问工程websocket连接正常，通过负载服务器访问工程，websocket连接失败，则可确认是负载服务器配置问题，需要排查负载配置。
### 4.3 确认负载均衡服务器上监听端口是否正常
1）确认负载均衡服务器上用来监听容器端口、websocket端口的两个端口是否正常，有没有被其他进程占用。  

2）确认访问电脑>负载均衡服务器>工程websocket，这条路上的相关端口都是畅通的。
### 4.4 确认负载服务器转发配置是否正确
举例一个BI工程，用nginx进行转发映射。
tomcat端口默认8080，websocket端口默认48888，49888，websocket转发端口默认48889
用nginx进行转发时，可用nginx服务器上的任意空闲端口转发tomcat的8080端口，用nginx服务器上的48889端口转发工程的48888端口
参考文档：[Nginx.conf 配置手册](<https://help.fanruan.com/finereport/doc-view-2815.html>)
![](/core/style/lod.png)
注1：nginx用48889转发工程的48888，需保证访问电脑到nginx的48889是通的，nginx服务器到工程服务器的48888是通的。
F5等硬件负载和nginx使用原理相同，容器端口和websocket端口都要转发。  

注2：nginx转发websocket端口时，需要配置ip_hash，如下图所示：
![](/core/style/lod.png)
### 4.5 负载均衡相关配置限制
所有的负载均衡配置需注意：不要开启健康检测、是不是有安全组策略导致端口未开放、需要开启会话保持。
1）开放服务器的防火墙端口限制。
2）开启阿里云/华为云/微软云服务器的安全组端口限制。
3）关闭阿里云的健康检查。
4）F5硬件负载需要开启会话保持。
## 5\. 注意事项
1）重启工程时，需要杀死工程下运行的进程，等待 2 分钟端口释放后，再重启工程，否则有可能重启失败。
2）通过上文排查修改，websocket 可正常连接后，仅能获取之后的内存和 CPU 显示、平台日志等数据。历史数据无法恢复。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：不额外给WebSocket对外开放端口](<index.php?doc-view-1508.html>)
[下一篇：数据集更新情况 ![](/core/style/forward.png) ](<index.php?doc-view-2168.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
