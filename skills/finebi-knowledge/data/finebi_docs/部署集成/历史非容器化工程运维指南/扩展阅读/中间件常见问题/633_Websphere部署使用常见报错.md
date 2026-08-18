---
title: Websphere部署使用常见报错
doc_id: 633
url: https://help.fanruan.com/finebi6.X/doc-view-633.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:49
---

> 1.&nbsp;概述本文介绍 FineBI 部署到&nbsp;WebSphere 后，遇到的问题及解决方案。2.&nbsp;示例2.1&nbsp;报错 404问题现象WebSphere 部署后输入访问地

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Websphere部署使用常见报错
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[9](<edition-list-633.html>)
* 最近更新：[HeroZ](<user-space-1842712.html>) 于 2023-02-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍 FineBI 部署到 WebSphere 后，遇到的问题及解决方案。
## 2\. 示例
### 2.1 报错 404
**问题现象**
WebSphere 部署后输入访问地址，报错 Error 404：java.io.FileNotFoundException: SRVE0190E: 找不到文件：/decision，如下图所示：
![1.png](/core/style/lod.png)  

**原因分析**
查看 WebSphere 客户端是否安装了 OS（AIX），WebSphere 的 OS（AIX）对应的语言环境是否与 FineBI 使用不一致。
**解决方案**
比如查看 WebSphere 的 OS（AIX）的语言环境，默认情况下如下所示：
[code]
    LANG=C LC_COLLATE="C"  
    LC_CTYPE="C"  
    LC_MONETARY="C"  
    LC_NUMERIC="C"  
    LC_TIME="C"  
    LC_MESSAGES="C"  
    LC_ALL=  
    
[/code]
该语言环境 C 与 FineBI 中默认不一致，需要修改其为 en_US.UTF-8 ，并重启 WebSphere 服务器。  

### 2.2 ERRORCODE=-4220，SQLSTATE=22021
**问题现象**
直接安装的 FineBI 能连上 IBM DB2 数据库，打包部署到 WebSphere 中后，连不上 DB2 数据库，报错：ERRORCODE=-4220，SQLSTATE=22021，如下图所示：
![1.png](/core/style/lod.png)  

![1.png](/core/style/lod.png)  

**原因分析**
当应用程序使用用于 JDBC 和 SQLJ 的 IBM 数据服务器驱动程序(也称为 JCC 驱动程序)并使用代码集 UTF-8 (代码页 1208 )连接到数据库时，它会抛出一个包含“捕获 java.io”的消息的 SqlException 。如果查询的字符列中的数据包含的字节序列不是有效的 UTF-8 字符串，则 CharConversionException”和 ERRORCODE=-4220 。
**解决方案**
「导航到服务器 > WebSphere application Servers > server_name > Java和流程管理 > 流程定义 > Java虚拟机」，勾选「调试方式」，在通用 JVM 参数中加入参数：-Ddb2.jcc.charsetDecoderEncoder = 3，如下图所示：
![1.png](/core/style/lod.png)  

添加成功后，重启 WebSphere，重新连接 IBM DB2 数据库即可。  

### 2.3 NO target servlet configgred for uri:/webroot/decision
**问题现象**
WebSphere 在成功部署 FineBI 工程后，输入访问地址（“服务器IP”+“端口”+“工程文件名”+“decision”）访问时，页面报错Error 404：com. ibm. ws. webcontainer. servlet. exception. NoTargetForURLException: No target servlet configured for uri: /webroot/decision，如下图所示：
![1.png](/core/style/lod.png)  

**原因分析**
按照 [Linux 系统 Websphere 服务器部署](<https://help.fanruan.com/finebi6.0/doc-view-655.html>) 部署时，在为 Web 模块映射上下文根，将上下文根改为工程名步骤时，可能填的非 webroot 工程名，则在输入访问地址时，使用 webroot 工程文件名访问就会报错 NO target servlet configgred for uri:/webroot/decision ，如下图所示：
![1.png](/core/style/lod.png)  

**解决方案**
确定在步骤 7：为 Web 模块映射上下文根时输入的上下文根，比如上下文根输入的地址为/home/wasadmin，则在部署成功后的访问地址需要使用：http://ip:port/home/wasadmin/decision，如下图所示：
![1.png](/core/style/lod.png)  

### 2.4 权限配置无法选择含有中文的登录用户所在字段数据表
**问题现象**  

[根据登录者信息查看对应数据](<https://help.fanruan.com/finebi6.0/doc-view-892.html>) 只能选择系统用户名，无法选择含有中文的「登录用户所在字段」数据表。
**原因分析**
WebSphere 服务器编码问题。
**解决方案**
修改 WebSphere 编码为 UTF-8。
1）进入「服务器>服务器类型>WebSphere Application Server>SuiteServer>进程定义> Java 虚拟机」，
将通用 JVM 参数修改为 -Dfile.encoding=UTF-8 -Ddefault.client.encoding=UTF-8，如下图所示：
![12.png](/core/style/lod.png)
2）进入目录%IBM%WebSphere/AppServer/profiles/AppSrv01/config/cells/10Cell01/nodes/10Node01/servers/SuiteServer
修改其中的 server.xml 中的参数genericJvmArguments="-Dfile.encoding=UTF-8 -Ddefault.client.encoding=UTF-8"
### 2.5 发送邮件失败
**问题描述**
FineBI 部署在 WebSphere 中，选择任意 BI 模板，执行定时调度任务，收不到邮件信息，显示邮件发送失败。如下图所示：
[code]
    javax.net.ssl.SSLException: Connection has been shutdown: javax.net.ssl.SSLHandshakeException: com.ibm.jsse2.util.h: PKIX path building failed: java.security.cert.CertPathBuilderException: PKIXCertPathBuilderImpl could not build a valid CertPath.; internal cause is:  
    java.security.cert.CertPathValidatorException: The certificate issued by CN=DigiCert Global Root CA, OU=www.digicert.com, O=DigiCert Inc, C=US is not trusted; internal cause is:  
    java.security.cert.CertPathValidatorException: Certificate chaining error  
    
[/code]
关键报错：  

[code]
    The certificate issued by CN=DigiCert Global Root CA, OU=www.digicert.com, O=DigiCert Inc, C=US is not trusted；  
    
[/code]
**原因分析**  

WebSphere 环境下没有添加对 Digicert CA 证书的信任。
**解决方案**
从 IE 浏览器中下载 Digicert CA 证书，然后在 WebSphere 环境中添加该证书，重启 WebSphere 即可。
1）打开「IE浏览器>设置>Internet选项>内容>证书>受信任的根证书颁发机构>DigiCert Global Root CA」，颁发者也是 DigiCert Global Root CA 的证书，导出该证书，选择DER 编码二进制格式。如下图所示：
![1611910476642175.png](/core/style/lod.png)
已下载的证书 digicert.cer 文件：[证书文件.zip](<doc-download-/finebi5.1/uploads/file/20210129/证书文件.zip> "下载资料")
2）导出后，把该文件上传到 WebSphere 服务器（每个节点）的任意目录下，如/home目录。
3）登录 WebSphere 控制台，选择「安全性>SSL证书和密钥管理>密钥库和证书」，如下图所示：
![1611911528314094.png](/core/style/lod.png)
4）点击NodeDefaultTrustStore，如下图所示：
![1611911580665960.png](/core/style/lod.png)
5）点击签署者证书，如下图所示：
![1611911630491430.png](/core/style/lod.png)
6）然后点击「添加」按钮，输入别名（可随意写），文件名写前面上传到服务器的证书文件的完整路径，如 /home/digicert.cer，数据类型选择二进制 ER 数据，然后点击应用。如下图所示：  

![1611910945201505.png](/core/style/lod.png)
7）应用完成后点击保存到配置，然后重启 WebSphere ，登录 BI ，再发送邮件即可成功
注：其它节点也要部署该证书。
![1611911049936376.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Websphere升级最新的SDK](<index.php?doc-view-285.html>)
[下一篇：Resin服务器内存修改 ![](/core/style/forward.png) ](<index.php?doc-view-667.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
