---
title: Tomcat配置SSL证书实现HTTPS访问
doc_id: 784
url: https://help.fanruan.com/finebi6.X/doc-view-784.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:29
---

> 本文为第三方解决方案或非产品相关操作指南，仅提供给具备自主开发能力的用户使用。若您的场景方案与文档不完全一致，请移步帆软社区提问：问答1. 概述启用 HTTPS 协议需要使用有效的 SSL 证书，证书中

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Tomcat配置SSL证书实现HTTPS访问
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[25](<edition-list-784.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-03-12 
[](<javascript:;>) [](<javascript:>)
**本文为第三方解决方案或非产品相关操作指南，仅提供给具备自主开发能力的用户使用。  
**
**若您的场景方案与文档不完全一致，请移步帆软社区提问：[**问答**](<https://bbs.fanruan.com/wenda>)**
  

  

## 1\. 概述
启用 HTTPS 协议需要使用有效的 SSL 证书，证书中包含的身份验证信息可帮助用户进行加密通信。
在单点登录认证系统中，证书是很重要的一把钥匙，客户端与服务器的交互安全靠的就是证书。
本文仅介绍CentOS系统下Tomcat如何安装SSL证书，以满足HTTPS访问的诉求。其他环境建议咨询你的证书签发机构进行安装。
## 2\. 在Tomcat安装SSL证书
### 2.1 获取证书
在配置证书前，首先需要申请证书。
用户需自行向 CA 厂商购买证书，证书认证一般都是由 VeriSign、GlobalSign 等国际公认的 CA 机构进行。
注：对于正式环境，不可使用 JDK 自带的 keytool 工具生成证书，会出现不安全提醒，导致工程嵌入第三方平台后无法访问。
### 2.2 上传证书
1）以管理员身份进入Tomcat安装目录，创建cert文件夹。  

2）以管理员身份进入%Tomcat_HOME%/cert文件夹，将证书文件上传到该文件夹。
注1：不同厂商的证书格式不完全相同，不一定和下图文件格式相同。
注2：如有密钥文件，请也同步上传到该位置。
![](/core/style/lod.png)
### 2.3 配置server.xml文件
1）以管理员身份进入%TOMCAT_HOME%/conf文件夹，使用文本编辑器打开server.xml文件。
2）在server.xml文件中，找到以下配置块：
<Connector port="8080" protocol="HTTP/1.1"  
connectionTimeout="20000"  
redirectPort="8443" />
在该配置块上方添加以下配置块，**请根据你的证书地址、证书格式和密码，修改keystoreFile、keystoreType和keystorePass** ：
  * keystoreFile 支持填写绝对路径或在 Tomcat 中的相对路径。
  * Connector port为你后续访问时所占的端口，请确保端口防火墙已开放，可正常访问。 如希望在访问时不添加端口，直接通过域名访问，请使用 HTTPS 的默认端口 443 。


<Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"  
maxThreads="150" SSLEnabled="true" scheme="https" secure="true"  
keystoreFile="/path/to/your/keystore/file"  
keystoreType="your_keystore_type"  
keystorePass="your_keystore_password"  
clientAuth="false" sslProtocol="TLS" />
![](/core/style/lod.png)
注1：不建议直接复制粘贴上文代码，可自行找寻文件中该配置库，去除相关代码注释，并修改证书说明即可。
注2：上文代码示例中，证书格式为.pfx格式。若证书格式为.crt，需要微调代码，示例如下：
<Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"  
maxThreads="150" SSLEnabled="true" scheme="https">  
<SSLHostConfig sslProtocol="TLS">  
<Certificate certificateFile="/opt/ssl_file/server.crt" certificateKeyFile="/opt/ssl_file/server.key" certificateChainFile="/opt/ssl_file/root.crt"   
type="RSA"/>  
</SSLHostConfig>  
</Connector>
3）保存并关闭server.xml文件
### 2.4 确认web.xml文件（可选）
如需配置HTTP请求自动跳转HTTPS，可执行本节操作。
1）以管理员身份进入%TOMCAT_HOME%/conf文件夹，使用文本编辑器打开web.xml文件。
2）在web.xml文件中，确认存在以下配置块，并确认<transport-guarantee>标签的值为CONFIDENTIAL即可：
<security-constraint>  
<web-resource-collection>  
<web-resource-name>Protected Context</web-resource-name>  
<url-pattern>/*</url-pattern>  
</web-resource-collection>  
<user-data-constraint>  
<transport-guarantee>CONFIDENTIAL</transport-guarantee>  
</user-data-constraint>  
</security-constraint>
![](/core/style/lod.png)
3）保存并关闭web.xml文件。
### 2.5 重启Tomcat
请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，重启Tomcat服务器，以使配置生效。
### 2.6 效果预览
使用浏览器访问https://your_domain:port，确保能够成功访问，如果网页地址栏出现小锁标志，表示证书已经安装成功。
  * your_domain是你的域名或IP地址。
  * 端口为2.3节配置的Connector port。


![](/core/style/lod.png)
## 3\. 注意事项
Tomcat 配置 SSL 证书实现 HTTPS 访问后，若要保证 Websocket 连接正常，需要配置 HTTPS 设置。
请先使用管理员账号登录数据决策系统，查看「管理系统>系统管理>常规」中是否出现 HTTPS 设置项。
  * 不出现：说明 Websocket 连接已正确配置，无需修改。
  * 出现：说明 Websocket 连接未正常配置，请参考文档修改：[HTTPS配置WebSocket](<https://help.fanruan.com/finebi6.X/doc-view-1509.html>)


![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：CAS单点登录插件](<index.php?doc-view-1071.html>)
[下一篇：SAML单点登录插件 ![](/core/style/forward.png) ](<index.php?doc-view-2689.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
