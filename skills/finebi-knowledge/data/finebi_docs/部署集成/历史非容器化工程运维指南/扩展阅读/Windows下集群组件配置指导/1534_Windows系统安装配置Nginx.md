---
title: Windows系统安装配置Nginx
doc_id: 1534
url: https://help.fanruan.com/finebi6.X/doc-view-1534.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:52
---

> 1. 概述Nginx 作为负载均衡在 Linux 系统上具备很好的并发性能，并且占用极小的内存。但是在 Windows 系统上并不支撑较高并发，所以在 Windows 系统上选用 Nginx 作为负载均

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统安装配置Nginx
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[6](<edition-list-1534.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-06-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
Nginx 作为负载均衡在 Linux 系统上具备很好的并发性能，并且占用极小的内存。
但是在 Windows 系统上并不支撑较高并发，所以在 Windows 系统上选用 Nginx 作为负载均衡，需要考虑并发情况。
若并发需求低于 300，部署集群仅以热备为目的，可选用 Nginx 作为负载均衡，若并发需求超过 300，则不建议使用 Nginx，须换用其他负载均衡。
详情见 Nginx 官方说明：<http://nginx.org/en/docs/windows.html>
## 2\. 安装步骤
### 2.1 下载 Nginx
可转至官方页面进行下载：<http://nginx.org/>  

版本推荐1.21及以上版本，优先使用最新版本
### 2.2 安装 Nginx
下载好的 Nginx 包，可以放到自己便于管理的目录进行解压，例如 D 盘，解压后即可使用。如下图所示：
![1627543697141873.png](/core/style/lod.png)
### 2.3 启动 Nginx
#### 2.3.1 运维命令
Windows+R 输入 cmd 进行以下编译，按照本文档部署的 Nginx 应用，请使用下面的运维命令。
1）进入 Nginx 目录，如下图所示：
![1558948026225407.png](/core/style/lod.png)  

2）启动、关闭 Nginx 。如下所示：
[code]
    start nginx       #启动 nginx  
    nginx -s reload     #重启 nginx  
    nginx -s stop     #快速停止 nginx  
    nginx -s quit     #完整有序地停止 nginx  
    
[/code]
#### 2.3.2 测试是否安装成功
在浏览器的地址栏输入http://ip:nginx端口号，例如：http://192.168.61.253:80，页面出现 Nginx 即为安装成功。如下图所示：
![1627543940844642.png](/core/style/lod.png)
## 3\. 修改配置
要想使用 Nginx 搭配 Web 容器发挥负载均衡的作用，必须还要对 Nginx 进行配置，下面提供通用配置和自定义配置。
Nginx 配置具体步骤请参见：[Linux系统安装配置Nginx](<https://help.fanruan.com/finebi6.0/doc-view-1532.html>) 文档的第三章、第四章的内容。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统安装配置Traefik](<index.php?doc-view-1584.html>)
[下一篇：Windows系统安装配置单机Redis ![](/core/style/forward.png) ](<index.php?doc-view-1557.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
