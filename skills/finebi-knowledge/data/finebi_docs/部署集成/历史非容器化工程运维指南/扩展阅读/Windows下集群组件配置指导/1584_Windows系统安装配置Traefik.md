---
title: Windows系统安装配置Traefik
doc_id: 1584
url: https://help.fanruan.com/finebi6.X/doc-view-1584.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:52
---

> 1. 概述Traefik 是一款反向代理、负载均衡应用，使用 Golang 实现。Traefik 和 Nginx 最大的不同是，它支持自动化更新反向代理和负载均衡配置。学习视频：【windows系统安装

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统安装配置Traefik
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[4](<edition-list-1584.html>)
* 最近更新：[HeroZ](<user-space-1842712.html>) 于 2023-02-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
Traefik 是一款反向代理、负载均衡应用，使用 Golang 实现。Traefik 和 Nginx 最大的不同是，它支持自动化更新反向代理和负载均衡配置。
学习视频：[【windows系统安装配置treafik】](<http://bbs.fanruan.com/lesson-973.html>)
注：Traefik 是 Go 语言编写的单一可执行文件，无需安装，只需在命令行里执行命令就可以。
## 2\. 操作步骤
### 2.1 下载 traefik
Traefik：[traefik_windows-amd64.rar](<doc-download-/finebi6.X/uploads/file/20220722/traefik_windows-amd64.rar> "下载资料")
通用配置文件：[traefik.rar](<doc-download-/finebi5.1/uploads/file/20210817/traefik.rar> "下载资料")
上面压缩包下载后，将包内文件traefik.toml和traefik_windows-amd64.exe解压到同一目录下，如下图所示：  

![1629163202870922.png](/core/style/lod.png)
### 2.2 traefik 配置
更改traefik.toml文件中的 ip 和端口，如果修改了工程路径（默认是 /webroot/decision），配置文件中也要修改。如下图所示：
![1629168765190192.png](/core/style/lod.png)
### 2.3 启动 traefik
注：启动 traefik 前，集群节点工程也需启动。
1）方法一：powershell 启动
[code]
    ./traefik_windows-amd64.exe --configFile=traefik.toml  
    
[/code]
![1571643220812899.png](/core/style/lod.png)
2）方法二：cmd启动
[code]
    traefik_windows-amd64.exe --configFile=traefik.toml  
    
[/code]
![1571643235109720.png](/core/style/lod.png)
### 2.4 查看节点健康状态
1）访问http://ip:dashboard端口号/dashboard，页面如下图所示：
![2.png](/core/style/lod.png)
2）访问http://ip:dashboard端口号/dashboard/status，页面如下图所示：
![1629167788666828.png](/core/style/lod.png)
## 3\. 常见问题
1）**启动报错，绑定端口失败：** 其他程序占用了端口，请换用端口或者结束占用端口的进程。
2）**没有权限：** Windows使用管理员用户打开命令行，Linux 赋予执行权限。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：JDK 升级及注意事项](<index.php?doc-view-1617.html>)
[下一篇：Windows系统安装配置Nginx ![](/core/style/forward.png) ](<index.php?doc-view-1534.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
