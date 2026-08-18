---
title: Websphere升级最新的SDK
doc_id: 285
url: https://help.fanruan.com/finebi6.X/doc-view-285.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:48
---

> 1、描述前面我们介绍了如何将 WebSphere 的版本升级至 8.5.5.13，还需要将 SDK 升级至版本 8.0.5.17 才能进行 FineBI 应用部署。这里采用直接替换的方法升级。2、升级步

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Websphere升级最新的SDK
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[9](<edition-list-285.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-05-27 
[](<javascript:;>) [](<javascript:>)
## 1、描述
前面我们介绍了如何将 WebSphere 的版本升级至 8.5.5.13，还需要将 SDK 升级至版本 8.0.5.17 才能进行 FineBI 应用部署。这里采用直接替换的方法升级。
## 2、升级步骤
### 2.1 下载 SDK 安装包
从 IBM 官网下载最新的 SDK 安装包（需要用 8.0.5.10 及以后版本的）。
官网下载地址：<https://developer.ibm.com/javasdk/downloads/sdk8/>
已经下载好的 bin 文件： [https://pan.baidu.com/s/19XMvqCrfUs-aWeLDBhMQig](<https://pan.baidu.com/share/init?surl=9XMvqCrfUs-aWeLDBhMQig>) 密码: smmu
### 2.2 安装 SDK 最新版
将 bin 文件放到 Linux 中任意目录下，并进入相应的目录下执行命令：
[code]
    ./ibm-java-sdk-8.0-5.17-x86_64-archive.bin  
    
[/code]
### 2.3 查看当前 JDK 路径
1）启动 was 应用程序后，执行如下命令，查看启动日志：
[code]
    tail  -1000f  /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/startServer.log  
    
[/code]
查看当前 Java 路径和 SDK 版本，使用的 Java 路径为 /opt/IBM/WebSphere/AppServer/java_1.8_64，如下图：
![74.png](/core/style/lod.png)
2）执行命令ps -ef | grep websphere ，查看 was 的进程 id，然后 kill 进程并关掉应用程序；
将步骤 2 执行后的 Java 文件夹重命名为 java_1.8_64，替换 /opt/IBM/WebSphere/AppServer路径下的  java_1.8_64 文件夹即可
替换后启动 was 应用程序，再次查看启动日志，查看替换后的 SDK 版本为 8.0.5.17，表示 SDK 升级成功。
![26.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Websphere升级](<index.php?doc-view-284.html>)
[下一篇：Websphere部署使用常见报错 ![](/core/style/forward.png) ](<index.php?doc-view-633.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
