---
title: Nginx常见报错及解决方案
doc_id: 536
url: https://help.fanruan.com/finebi6.X/doc-view-536.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:49
---

> 1.&nbsp;概述本文汇总使用 Nginx 过程中常见报错及解决方案。2.&nbsp;示例2.1&nbsp;Cannot read property &#39;length&#39; of undef

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Nginx常见报错及解决方案
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[11](<edition-list-536.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-04-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文汇总使用 Nginx 过程中常见报错及解决方案。  

## 2\. 示例
### 2.1 Cannot read property 'length' of undefined
**问题描述：**
当用户不想要暴露自身服务器的地址时，通常会使用 Nginx 反向代理服务器，使用过程中出现请求报错，如下图所示：  

![QQ截图20190929090207.png](/core/style/lod.png)  

**原因分析：**
该问题是由于 FineBI 默认的请求端口号为 48888（单机）或者 48889（集群），若 Nginx 中配置的端口号不为该端口，则无法将信息转发到正确的请求端口上，因此需要在 FineBI 中将信息请求端口修改为与 nginx 中配置的一致。
**解决方案：**
1）连接 FineDB 数据库，在数据库表 fine_conf_entity 加一下字段（或者改一下）WebSocketConfig.requestPort，将其修改为与 Nginx 中配置的端口一致即可。比如 Nginx 中的端口配置为 8089 ，则我们可修改WebSocketConfig.requestPort为 8089 ，如下图所示：
![222](/core/style/lod.png)  

2）修改完成后重启 FineBI 即可。
### 2.2 permission denied
**问题描述：**
集群环境，有线网络正常，无线网络登录页面空白，但是节点可以正常登录。
日志文件如下图所示：
![11.png](/core/style/lod.png)
**原因分析：**
Nginx 无权限读取数据流。
**解决方案：**
修改 nginx.conf ，将用户组改成 root ，并且取消注释。如下图所示：
![1603095337682109.png](/core/style/lod.png)
### 2.3 https protocol requires SSL
**问题描述：**  

启动时报错：  

nginx:[emerg]https protocol requires SSL support in /usr/nginx/conf/nginx.conf:39
**原因分析：**  

nginx.conf 中配置了 HTTPS，但 Nginx 未配置 SSL 模块。
**解决方案：**
给 Nginx 增加 SSL 模块，请参见 [配置 SSL 证书实现 HTTPS 访问](<https://help.fanruan.com/finebi6.0/doc-view-784.html>)
### 2.4 Nginx 编译缺乏依赖
**问题描述：**
报错：SSL modules require the OpenSSL library
如下图所示：
![1603096371969177.png](/core/style/lod.png)
**原因分析：**
Nginx 在编译一些模块时，需要三个依赖库：PCRE、zlib、OpenSSL
**解决方案：**
[code]
    yum -y install gcc pcre pcre-devel zlib zlib-devel openssl openssl-devel  
    
[/code]
### 2.5 Nginx 入口访问平台空白
**问题描述：**
Nginx 入口访问平台空白，日志显示写缓存文件失败，如下图所示：
![13.png](/core/style/lod.png)
**解决方案：**  

如果启动 Nginx 的用户有对应目录读写权限，则可能是磁盘空间不足引起，可用df -h指令查看。
nginx.conf 中关闭 acces.log ，避免日志过大，把磁盘空间占完。
### 2.6 集群环境/服务器经常出现卡慢
**问题描述：**  

集群环境，服务器经常出现卡慢。
**解决方案：**
由于磁盘空间不足，nginx.conf 中关闭 acces.log ，避免日志过大，把磁盘空间占完。
### 2.7 Nginx 配置外网后端口丢失
**问题描述：**  

用户做了 Web 集群，现在做了外网映射，访问 URL 能登录到登录页面，但是点击登录之后，映射的端口号不见了，跳转之后就直接报 404 。
**原因分析：**  

登陆跳转后，host 变动，导致端口丢失。
**解决方案：**
Nginx 修改 head 的 host 字段（proxy_set_header Host）为实际外部访问的地址，如下图所示：
![14.png](/core/style/lod.png)
### 2.8 Nginx 配置无法访问 CSS 和 JS 等静态资源
**问题描述：**
访问类似localhost:8080\WebReport\ReportServer，页面空白，控制台报错：Failed to load resource:the server responded with a status of 404(not Found)
![16.png](/core/style/lod.png)
原因分析：
Nginx入口：http://localhost/reportService/WebReport/decision
Tomcat：http://ip:port/WebReport/decision
用户在 Nginx 在匹配 /reportService 转发给后端 Tomcat 处理，而后端返回资源请求时不带 /reportService，导致重定向到了 Nginx 静态资源路径，访问报错。
Nginx 配置：
![1603098476510572.png](/core/style/lod.png)
![18.png](/core/style/lod.png)
**解决方案：**  

**方案一：Nginx 层面**  

拦截/WebReport/decision，重定向为/reportService/WebReport/decision
需要注意以下两点：
  * rewrite 是 301 重定向，return 是 307 重定向。
  * server_name 为 localhost 时，通过 127.0.0.1 访问，重定向后会有跨域报错，ajax error。


![19.png](/core/style/lod.png)
**方案二：Tomcat 层面**  

设置虚拟目录，使得 Tomcat url 变为：http://ip:port/reportService/WebReport/decision
具体步骤
（1）将工程移出 webapp，避免重复加载；
（2）修改tomcat conf/server.xml，docbase 为工程绝对路径
![20.png](/core/style/lod.png)
（3）修改 nginx.conf，去掉斜杠
注：带斜杠时，是将/reportService/后面的请求转发给后面。
**![21.png](/core/style/lod.png)**
### 2.9 413 (Request Entity Too Large)
问题描述：**  
**
部署了集群，使用 Nginx 进行负载均衡。拥有导出权限的用户全局导出 Excel/Pdf 时提示导出无权限，导出失败。通过 F12 查看前端报错，发现报错： 413 (Request Entity Too Large) 。如下图所示：
![14.png](/core/style/lod.png)
**原因分析：**  

Nginx 中设置了默认的文件大小限制，若上传的文件超过这个默认设置的大小，就会被 Nginx 限制而无法上传。
**解决方案：**  

修改 Nginx 中文件大小限制。
1）打开 Nginx 配置文件 nginx.conf，路径一般是：%nginx%/nginx.conf
2）修改该文件中的 client_max_body_size 对应值，该值对应 Nginx 允许最大上传的大小，如下图所示：
![222](/core/style/lod.png)
注：这个参数的作用为设置最大允许的客户端请求主体大小，该值大小具体多少根据业务需求调整。
3）保存后重启 Nginx ，问题解决。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Keepalived+Nginx部署方案](<index.php?doc-view-1965.html>)
[下一篇：抽取集群常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-1970.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
