---
title: Resin下通过IP直接进入平台系统界面
doc_id: 666
url: https://help.fanruan.com/finebi6.X/doc-view-666.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:36
---

> 1. 概述实现在浏览器输入 IP，例如localhost/.a.jsp，可以直接访问平台系统，不必采用http://localhost:8080/webroot/decision来访问。2. 方法一按照

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Resin下通过IP直接进入平台系统界面
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[6](<edition-list-666.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-05-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
实现在浏览器输入 IP，例如localhost/.a.jsp，可以直接访问平台系统，不必采用http://localhost:8080/webroot/decision来访问。
## 2\. 方法一
按照文档：[Resin 服务器部署](<https://help.fanruan.com/finebi6.0/doc-view-665.html>)部署好 5.1 的 BI 工程。
### 2.1 修改端口号
检查是否有其他应用占用了 80 端口，如果没有就可以开始修改 Resin 的端口号了。
以 Resin4 修改端口号为例。
文本编辑器打开%Resin_HOME%\conf\resin.properties，将 app.http 和 web.http 的配置信息从默认的 8080 改为 80 即可。
![Snag_6fa7204.png](/core/style/lod.png)
### 2.2 创建欢迎页面
在 Resin 的%Resin_HOME%\webapps\ROOT目录下新建一个以 UTF-8 格式编码的 a.jsp 文件。
![Snag_6ffc2cb.png](/core/style/lod.png)
代码如下：
[code]
    <%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%><html>     
     <head>          
     <title>FineBI</title>      
     <meta http-equiv="Content-Type" content="text/html;   
     charset=utf-8"></head>      
     <body>          
     <iframe id="reportFrame" src="webroot/decision?op=fs"              
     name="itemslist" frameborder="0" width="100%" height="100%"></iframe>      
     </body></html>  
    
[/code]
### 2.3 访问决策系统
创建完成后，重启 Resin 服务器，就可以通过http://localhost/a.jsp访问 op=fs 了。效果如下：
注：op=fs 指的就是访问平台系统。
![Snag_b7a97a9.png](/core/style/lod.png)
## 3\. 方法二
按照方法一完成 2.1 和 2.2 的操作。 
修改%Resin_HOME%\conf\app-default.xml文件，在文件内找到 <welcome-file-list> 标签，在标签内第一行新增<welcome-file>a.jsp</welcome-file>。
注：%Resin_HOME%\webapps\ROOT\下默认有一个 index.jsp 文件，如果不是在第一行新增 a.jsp，默认打开的还是 index.jsp。
![222](/core/style/lod.png)  
保存上述配置文件，重启 Resin 后，在浏览器内输入http://localhost或者http://服务器的ip，就可以直接显示 op=fs 界面了。
![Snag_b7e48ea.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Tomcat下通过IP访问非容器化工程](<index.php?doc-view-903.html>)
[下一篇：Linux下Tomcat开机自启动 ![](/core/style/forward.png) ](<index.php?doc-view-1878.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
