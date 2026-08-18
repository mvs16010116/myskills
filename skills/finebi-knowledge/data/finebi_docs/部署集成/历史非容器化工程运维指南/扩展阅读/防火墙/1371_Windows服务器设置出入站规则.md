---
title: Windows服务器设置出入站规则
doc_id: 1371
url: https://help.fanruan.com/finebi6.X/doc-view-1371.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:45
---

> 1.&nbsp;概述1.1&nbsp;应用场景工程部署到 Windows&nbsp;系统中后，Windows&nbsp;系统需要开放工程端口，工程地址才能被其他电脑访问。1.2 Windows&nbsp

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows服务器设置出入站规则
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[1](<edition-list-1371.html>)
* 最近更新：[知识库](<user-space-567266.html>) 于 2021-06-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
工程部署到 Windows 系统中后，Windows 系统需要开放工程端口，工程地址才能被其他电脑访问。  

### 1.2 Windows 系统出入站规则简介
1）Windows 系统默认的规则：默认阻止入站连接，默认允许出站连接。也就是说，凡是入站连接，任何程序和端口都要在防火墙上配置入站规则，否则都会被禁止。  

2）Windows 防火墙的规则扫描有它自己特定的顺序，其优先级为：只允许安全连接>阻止连接>允许连接>默认规则（如果没有设置，那就是默认阻止）。
3）出站规则：出站规则来限制对外访问的，也就是说从本机发出的请求中，如果请求的对象是被禁止的，该请求会被拦截，表现方式就是断网。
4）入站规则：入站规则是用来限制远程主机访问本机的服务的，就是说，本机接收的请求中如果被请求的程序或具体端口是被限制的，该请求被拦截。
## 2\. 操作步骤
本文以设置入站规则为例，出站规则设置与入站规则设置步骤一致。
### 2.1 打开设置
打开「控制面板」>「系统和安全」>「Windows Defender 防火墙」>「高级设置」，如下图所示：
![45.png](/core/style/lod.png)
### 2.2 新建入站规则
#### 2.2.1 新建规则（以端口为例）
点击「入站规则>新建规则>端口」，如下图所示：
![46.png](/core/style/lod.png)
#### 2.2.2 指定端口
如下图所示：
注：选择「所有本地端口」，则表示所有端口都开放。
![1623050749756101.png](/core/style/lod.png)
#### 2.2.3 选择连接操作
如下图所示：  

![1623050883672325.png](/core/style/lod.png)
根据需求选择，这里需要开放端口，选择允许连接。
#### 2.2.4 选择规则生效范围  

如下图所示：  

![1623051041931059.png](/core/style/lod.png)
#### 2.2.5 定义规则名称
如下图所示：  

![1623051148512126.png](/core/style/lod.png)
### 2.3 效果查看
如下图所示：  

![51.png](/core/style/lod.png)
上述规则定义：远程主机访问本机服务，只允许访问开放的端口；访问其它端口的请求会被拦截。
## 3\. 注意事项
  * 出入站规则生效的前提是防火墙处于开启状态。
  * 云服务器需要额外设置安全组，开放相关端口。


### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux防火墙使用及配置](<index.php?doc-view-1372.html>)
[下一篇：清理Tomcat日志文件 ![](/core/style/forward.png) ](<index.php?doc-view-2220.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
