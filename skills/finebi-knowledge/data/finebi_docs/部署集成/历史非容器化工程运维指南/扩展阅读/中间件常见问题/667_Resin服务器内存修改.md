---
title: Resin服务器内存修改
doc_id: 667
url: https://help.fanruan.com/finebi6.X/doc-view-667.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:49
---

> 1. 概述1.1 问题描述用户工程部署在 Resin 容器中，若遇到以下问题：报错：java.lang.OutOfMemoryError:PermGen space或者java.lang.OutOfMe

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Resin服务器内存修改
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[5](<edition-list-667.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2022-01-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 问题描述
用户工程部署在 Resin 容器中，若遇到以下问题：
  * 报错：java.lang.OutOfMemoryError:PermGen space或者java.lang.OutOfMemoryError:Java heap space。
  * 打开报表经常出现等待排队中。
  * 想调整 Resin 容器的默认内存。


可参考本文方法解决。
### 1.2 解决思路
修改%Resin_HOME%\conf下的resin.xml文件或resin.properties文件。
## 2\. 操作步骤
适用于 Resin 4.0.4 及以上版本。
### 2.1 方案一：修改 resin.xml 文件
1）打开%Resin_HOME%\conf\resin.xml文件，在<cluster id="app">标签内增加：
[code]
    <server-default>  
            <jvm-arg>-Xms8192m</jvm-arg>  
            <jvm-arg>-Xmx8192m</jvm-arg>  
            <jvm-arg>-XX:PermSize=256m</jvm-arg>  
            <jvm-arg>-XX:MaxPermSize=256m</jvm-arg>  
     </server-default>  
    
[/code]
如下图所示：
![1641793792161665.png](/core/style/lod.png)
2）重启 Resin 服务器。管理员进入平台，点击「管理系统>智能运维>内存管理」，可以看到实时内存情况。如下图所示：
![14.png](/core/style/lod.png)
### 2.2 方案二：修改 resin.properties 文件
1）打开%Resin_HOME%\conf\resin.properties文件，增加一行jvm_args : -Xms8192m -Xmx8192m -XX:PermSize=256m -XX:MaxPermSize=256m。如下图所示：
![1641794589717861.png](/core/style/lod.png)
2）重启 Resin 服务器。管理员进入平台，点击「管理系统>智能运维>内存管理」，可以看到实时内存情况。如下图所示：
![14.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Websphere部署使用常见报错](<index.php?doc-view-633.html>)
[下一篇：Tomcat中指定日志/临时文件路径 ![](/core/style/forward.png) ](<index.php?doc-view-438.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
