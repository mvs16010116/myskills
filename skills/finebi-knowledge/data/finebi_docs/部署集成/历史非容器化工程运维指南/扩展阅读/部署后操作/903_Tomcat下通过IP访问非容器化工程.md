---
title: Tomcat下通过IP访问非容器化工程
doc_id: 903
url: https://help.fanruan.com/finebi6.X/doc-view-903.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:35
---

> 提示:本文仅面向非运维平台部署的 FineBI6.0 项目。如需通过域名/IP访问运维平台部署的FineBI项目，详情请参见：使用IP/域名访问项目1. 概述1.1 问题描述通常在&nbsp;Tomca

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Tomcat下通过IP访问非容器化工程
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[15](<edition-list-903.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-03-24 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
本文仅面向**非运维平台部署** 的 FineBI6.0 项目。
如需通过域名/IP访问**运维平台部署** 的FineBI项目，详情请参见：[使用IP/域名访问项目](<https://help.fanruan.com/fineops/doc-view-138.html>)
  

## 1\. 概述
### 1.1 问题描述
通常在 [Tomcat 服务器部署](<https://help.fanruan.com/finebi6.0/doc-view-45.html>) 完成后，启动服务器，用户需要访问 URL：http://IP:端口/webroot/decision 方可进入数据决策系统。有时用户希望可以直接通过 IP 就能访问数据决策系统。
### 1.2 解决思路
通过修改端口号并建立虚拟目录来实现访问 IP（例如：http://localhost）即可直接进入数据决策系统。
## 2\. 操作步骤
以访问http://localhost为例进行介绍。
### 2.1 修改端口号
如果没有其他网络程序占用端口号 80，可以将 Tomcat 服务器的端口号设置为 80。
80 端口为默认端口，用户访问报表页面时就不需要再加上 Tomcat 服务器的端口号。  

1）打开%Tomcat_Home%\conf\server.xml文件，修改端口号 8080 为 80，如下图所示：
![1575268863332711.png](/core/style/lod.png)
代码如下所示：
[code]
    <Connector port="80" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />  
    
[/code]
2）重启 Tomcat 服务器，访问http://localhost/webroot/decision即可进入数据决策系统。
### 2.2 设置欢迎界面
每个 Web 服务器都有默认的欢迎界面，通过修改欢迎界面，以显示平台页面。
在%Tomcat_Home%/webapps/webroot目录下新建 a.html文件，作为 Web 服务器的默认主页。
#### 2.2.1 PC 端和 App 端设置界面
点击下载并解压，获得a.html：[a.zip](<doc-download-/finebi6.X/uploads/file/20250324/a.zip> "下载资料")
a.html 调用 iframe 集成界面，代码如下所示：
[code]
    <html>  
      <head>  
        <title>FineBI商业智能</title>  
        <link rel="stylesheet" type="text/css" href="/decision/file?path=/com/fr/web/core/css/leaflet.css&type=plain&parser=plain"/>  
      </head>  
      <body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">  
        <iframe id="reportFrame" src="decision" allowfullscreen="true"  
          name="itemslist" frameborder="0" width="100%" height="100%"></iframe>  
      </body>  
    </html>
[/code]
注：<link rel="stylesheet" type="text/css" href="/decision/file?path=/com/fr/web/core/css/leaflet.css&type=plain&parser=plain"/> 这行代码用于解决决策系统中图表工具栏全屏后地图显示异常的问题。
重启 Tomcat 服务器，访问http://localhost/webroot/a.html即可显示数据决策系统登录页面。
#### 2.2.2 HTML5 端设置界面
点击下载并解压，获得a.html：[a.rar](<doc-download-/finebi6.X/uploads/file/20250324/a.rar> "下载资料")
代码如下所示：  

[code]
    <html>  
      <head>  
        <title>FineReport报表</title>  
        <link rel="stylesheet" type="text/css" href="/decision/file?path=/com/fr/web/core/css/leaflet.css&type=plain&parser=plain"/>  
         <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1, maximum-scale=1.0, user-scalable=no">  
      </head>  
      <body leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">  
        <iframe id="reportFrame" src="decision" allowfullscreen="true"  
          name="itemslist" frameborder="0" width="100%" height="100%"></iframe>  
      </body>  
    </html>  
    
[/code]
注：HTML5 端设置时需要安装 [HTML5 端访问仪表板/工程](<https://help.fanruan.com/finebi6.0/doc-view-452.html>)
### 2.3 建立虚拟目录
通过修改配置文件建虚拟目录。
#### 2.3.1 调整工程路径
工程 webroot 默认放在%Tomcat_home%\webapps目录下，启动服务器时会加载该工程。建立虚拟目录后，启动 Tomcat 服务器时，通过配置文件会再次加载 webroot 工程。webroot工程加载两次，会出现报错、服务器闪退等情况。
因此用户需要将%Tomcat_Home%\webapps目录下的 webroot 工程移动到 Tomcat 部署目录以外的位置，并且需要与 Tomcat 工程在相同路径的磁盘下。
本文将%Tomcat_home%\webapps\webroot文件夹移动到D:\webroot路径。如下图所示：
![](/core/style/lod.png)
#### 2.3.2 修改 server.xml 文件
修改%Tomcat_Home%\conf\server.xml文件，在 server.xml 文件中 host 标签之间添加代码，如下图所示：
![](/core/style/lod.png)
代码如下所示：
[code]
    <Context path="" docBase="D:\webroot" debug="0" reloadable="false" />  
    
[/code]
说明：
参数| 说明  
---|---  
path| 虚拟目录的名字如果希望输入 IP 地址就显示主页，则该键值留为空  
docBase| 虚拟目录的路径本文 2.3.1 步骤中设置的 webroot 路径，本文为D:\webroot  
debug| 0  
reloadable| false  
#### 2.3.3 修改 web.xml 文件
修改 %tomcat_home%\conf\web.xml 路径下的 web.xml 文件。在web.xml文件末尾 </web-app> 标签之前，添加一段代码显示自定义欢迎界面 a.html，代码如下：
注：如果不存在该文件，请在webroot\WEB-INF 目录下新建 web.xml 文件。建议根据你的Tomcat版本，通过Tomcat官网获取相关原始文件。
[code]
    <welcome-file-list>  
      <welcome-file>index.html</welcome-file>  
      <welcome-file>index.htm</welcome-file>  
      <welcome-file>a.html</welcome-file>  
      <welcome-file>index.jsp</welcome-file>  
    </welcome-file-list>  
    
[/code]
如下图所示：
![](/core/style/lod.png)
### 2.4 效果预览
#### 2.4.1 PC 端
重启 Tomcat 服务器，访问 http://localhost，即可进入 a.html 页面，即可访问数据决策系统，如下图所示：
![1593761722367365.png](/core/style/lod.png)
注：本文访问本机，因此使用 http://localhost，实际访问地址为 http://IP 。
#### 2.4.2 移动端（HTML5 访问）  

重启 Tomcat 服务器，访问 http://IP ，如下图所示：
![1600072280154746.png](/core/style/lod.png)
注：App 端访问请参见本文 3.2 节。
## 3\. 输入服务器地址
### 3.1 远程设计
在使用报表 [远程设计](<https://help.fanruan.com/finereport/doc-view-1388.html>) 输入服务器地址的时候，webroot 需省去，decision 要保留，详情如下所示：
选项 | 值   
---|---  
主机名/IP| 根据实际情况填写  
端口号| 80  
Web应用| 空  
Servlet| decision  
用户名\密码| 根据实际情况填写  
配置工作目录示例如下图所示：
![](/core/style/lod.png)
### 3.2 App 端
移动端输入服务器地址的时候，webroot 需省去，decision 要保留。如下所示：
选项 | 值   
---|---  
主机名/IP| 根据实际情况填写  
端口号| 80  
Web 应用| 空  
Servlet| decision  
用户名\密码| 根据实际情况填写  
  
配置工作目录示例如下图所示：  

![1593762106229866.png](/core/style/lod.png)
## 4\. 注意事项
### 4.1 登录成功后首页报错 404
**问题描述**
通过 IP 成功访问数据决策系统后，首页报错 404 ，如下图所示：  

![](/core/style/lod.png)
**解决方案**
在「目录管理」节点中修改首页路径，将/webroot/Demo.html修改为/Demo.html，如下图所示：
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：修改非容器化工程端口号](<index.php?doc-view-326.html>)
[下一篇：Resin下通过IP直接进入平台系统界面 ![](/core/style/forward.png) ](<index.php?doc-view-666.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
