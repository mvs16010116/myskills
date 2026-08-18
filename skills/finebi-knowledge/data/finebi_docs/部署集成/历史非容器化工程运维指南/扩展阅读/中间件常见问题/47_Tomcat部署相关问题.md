---
title: Tomcat部署相关问题
doc_id: 47
url: https://help.fanruan.com/finebi6.X/doc-view-47.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:46
---

> 1.&nbsp;概述本文介绍&nbsp;工程部署到 Tomcat 中&nbsp;遇到的问题及解决方案。2.&nbsp;示例2.1 Windows 系统下&nbsp;CMD 窗口1）Windows 系统下

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Tomcat部署相关问题
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[9](<edition-list-47.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-06-16 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍 [工程部署到 Tomcat 中](<https://help.fanruan.com/finebi6.0/doc-view-45.html>) 遇到的问题及解决方案。  

## 2\. 示例
### 2.1 Windows 系统下 CMD 窗口
1）Windows 系统下的 CMD 窗口默认可编辑，如果鼠标点进窗口，会造成所有的 Java 线程阻塞，造成 Tomcat 假死宕机不能使用。此时需要在 Tomcat 的 CMD 界面点击「属性」。如下图所示：
![10.png](/core/style/lod.png)
2）取消勾选两个编辑选项，点击「确定」保存该属性，并重启 Tomcat 即可。如下图所示：
![11.png](/core/style/lod.png)
### 2.2 关于页面显示 HTTP Status 404
将安装的 JDK 目录lib下面的tools.jar拷贝到%Tomcat_home%/lib或%Tomcat_home%/webapps/webroot/WEB-INF/lib任一位置。
### 2.3 内存不足
**问题描述**
配置管理员密码出错或Java heap space。
**原因分析**
表示 Tomcat 的内存不足，需修改Tomcat 内存配置。
**解决方案**
修改内存的方法参见文档：[修改内存](<https://help.fanruan.com/finebi6.X/doc-view-56.html>)
### 2.4 7.0.100 版本的 Tomcat 部署
7.0.100 版本的 Tomcat 需要将web.xml放到%Tomcat_HOME%\webapps\webroot\WEB-INF下，否则会报错。
文件请参见：[web.xml](<doc-download-/finebi5.1/uploads/file/20210311/web.xml> "下载资料")
注：该 Tomcat 的 bug 已经在 7.0.103 中修复。
### 2.5 删除 1:1 关联时，前端报错 400
**问题描述**  

客户工程部署到 Tomcat 中，编辑和删除表的两条 1:1 的关联时，整个页面报错 400 。
**原因分析**
高版本 Tomcat（7.0.76以后）会严格按照对 RFC 3986 规范进行访问解析，导致修改关联时前端会报 400 。
**解决方案**
1）修改%Tomcat_HOME%/conf/server.xml文件，增加下面代码：
[code]
    maxpostsize="209715200"  
    maxHttpHeaderSize="16384"  
    relaxedPathChars="[]|"  
    relaxedQueryChars="[]|{}^\`"<>"  
    useBodyEncodingForURI="true"  
    URIEncoding="UTF-8"  
    
[/code]
如下图所示：  

![1618986877825038.png](/core/style/lod.png)
2）重启工程。
### 2.6 查看BI自带Tomcat版本
如果想要查看 FineBI 自带的 Tomcat 服务器的版本，可以按照如下步骤操作：  

1）使用压缩软件打开 %Tomcat_HOME%/lib/ 下的 catalina.jar 文件。
![1648448284678840.png](/core/style/lod.png)
2）双击打开 META-INF 文件夹，如下图所示：
![1648448354269033.png](/core/style/lod.png)
3）右键查看 MANIFEST.MF 文件，即可找到 Tomcat 版本信息，如下图所示：
![1648448469194870.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：清理Tomcat日志文件](<index.php?doc-view-2220.html>)
[下一篇：Weblogic部署相关问题 ![](/core/style/forward.png) ](<index.php?doc-view-48.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
