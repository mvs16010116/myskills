---
title: 数据连接 Kerberos 认证
doc_id: 282
url: https://help.fanruan.com/finebi/doc-view-282.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:36
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-6.0.2优化 Kerberos 认证方式，可在前端直接上传相关文件1.2 功能简介1）Kerberos 认证&nbsp;是 Hadoop 生态的

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 数据连接 Kerberos 认证
[__](<doc-edit-282.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[45](<edition-list-282.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-11-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
6.0.2  
| 优化 Kerberos 认证方式，可在前端直接上传相关文件  
### 1.2 功能简介
1）[Kerberos 认证](<https://baike.baidu.com/item/Kerberos%E8%AE%A4%E8%AF%81/9309861>) 是 Hadoop 生态的一种通用的认证方式。
2）配置 Kerberos 认证的方式有两种：
  * 直接使用数据连接配置界面中的 Kerberos 认证：主要用于 Hive、HBase 等驱动的认证连接。
  * 配置 JVM 参数后再进入数据连接配置界面进行认证：主要用于按要求填写数据连接配置界面认证成功，创建连接依然抛错的情况，比如 CDH 的 Impala 等数据库。


### 1.3 支持的数据库
支持的数据库类型如下，进行 Kerberos 认证的数据库，需要更换专用的驱动，URL 格式也要有所改变，详情请参见：[Kerberos 驱动整理](<https://help.fanruan.com/finereport/doc-view-4845.html>)
数据库  
---  
Apache Impala  
Hadoop Hive  
Spark  
Transwarp Inceptor（星环）  
  
Apache Phoenix  
HBase  
  
注：不支持多个 Kerberos 认证同时存在。例如：数据连接A 和 数据连接B 都需要进行 Kerberos 认证，那么这两个连接同一个时间内只能成功连接上一个。
### 1.4 数据连接前的准备工作
1）下载环境上的配置文件 krb5.conf、XXX.keytab、principal 。
2）principal 为注册过 KDC 的客户端名称。
3） XXX.keytab 为密钥表文件，需要在提供 Kerberos 服务的应用服务器上找到该文件的对应位置。在不同服务器上 keytab 的文件名称可能不一样，这里用 XXX 代替。
## 2\. 操作方式
这里以 Hive 为例。
### 2.1 配置 hosts 文件
配置本地 hosts 文件，例如在路径C:\Windows\System32\drivers\etc\hosts下配置远端映射：192.168.5.127 quickstart.cloudera 。映射格式为「 IP 机器名」。如下图所示：
注：对于运维平台部署的工程，如果需要使用kerberos认证，需要修改容器与宿主机的host，添加数据库和kerberos认证中心的域名。
![1574066211785589.png](https://help.fanruan.com/core/style/lod.png)
### 2.2 设置数据连接
1）参考 [Kerberos 驱动整理](<https://help.fanruan.com/finebi7.0/doc-view-1973.html>) 找到对应驱动，更改 URL 为对应格式，切换认证方式为 Kerberos。如下图所示：
![4.png](https://help.fanruan.com/core/style/lod.png)
2）上传「keytab」文件和「krb5.conf」文件。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）点击「测试连接」，连接成功如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 注意事项
### 3.1 检查服务器及认证信息
检查内容| 要求  
---|---  
检查 FineBI 服务器所在机器和数据库服务器的系统时间差| 通常要求时间差小于 5 分钟  
检查配置 FineBI 服务器所在机器的 hosts 文件| 需确认能通过主机名/域名 ping 通数据库服务器  
FineBI 自带的 zookeeper 包与数据库服务端的 zookeeper 版本需要匹配| 例如：华为 HD 平台连接可能会出现此类报错  
检查 principal 名称是否正确| principal 的格式通常为用户名/部门@公司，确认 principal 是否正确的方式是在数据库服务端 shell 执行klist 或者 kinit -k -t /path/to/keytab name_of_principal。或直接通过 beeline、impala-shell 等工具连接开启认证的服务，并查看对应的 principal 信息例如：Hive 服务对应 principal 为 hive /bigdata@XXX.COM，而 Impala 服务对应的 principal为impala/bigdata@XXX.COM。  
检查 FineBI 的工程路径| 确保不带有空格（如 tomcat 9），因为 Kerberos 认证不支持带有空格路径。  
### 3.2 无法连接处理方式
1）若连接失败，可与平台数据库管理员确认相关服务的安全认证配置是否正确，并联系帆软技术支持并提供相关报错日志（添加 JVM 安全调试参数，如下所示），数据平台数据库版本、对应驱动 JAR 包、相关连接信息、Java 认证连接测试代码或者能连接认证数据库的 shell 工具等。
jvm 安全调试日志参数：
[code]
    -Djava.security.debug=gssloginconfig,configfile,configparser,logincontext  
    -Djava.security.krb5.debug=true
[/code]
2）特殊情况下，如果 Windows 系统下无法连接，可以把 FineBI 测试服务器部署在 Linux 系统上。需保证该服务器能通过相关 shell 工具连上数据库，通过 klist 能看到已缓存的 kgt 信息。
### 3.3 报错
#### 3.3.1 Unable to obtain Principal Name for authentication
**问题描述：**
cdh 连接抛错：Unable to obtain Principal Name for authentication
**原因分析：**
JDK 默认安装的 JCE 不能处理超过 128 位的对称密钥。
**解决方案：**
更新 JRE 的 JCE 扩展包。
JCE 安装详情参见：[扩展包安装连接](<https://sourceforge.net/p/skcc/wiki/Install%20JDK8%20and%20JCE%20on%20Windows/>) 。通常直接到第 4 步即可，下载解压得到 JCE 扩展 JAR 包，然后到 JRE 的指定目录替换文件即可。
#### 3.3.2 GSS initiate failed
**问题描述：**
Transwarp Inceptor（星环）数据库报错 GSS initiate failed 。
**排查步骤：**
驱动本身做了静态全局的操作，kerberos 中心刷新后，驱动内部的静态全局还残留，故数据连接连不上。重启 BI 服务器查看是否依旧有该报错。若仍然有，采取下面的排查步骤：
  * （密码错误）keytab 文件与用户不匹配，可以在客户端服务器中kinit-k-t keytab用户进行检查。
  * 本地服务器和远程服务器的（时钟偏移）时间不匹配，请检查ntp到远程服务器。
  * （aes256不支持）默认情况下aes256不支持jdk/jre，需要从/opt/huawei/Bigdata/jdk/jre/lib/security路径中的远程服务器复制local_policy.jar和US_export_policy.jar。
  * （无规则）主体格式默认不支持，需要添加属性hadoop.security.auth_to_local（在core site.xml中）值规则：[1:$1]规则：[2:$1]。
  * （超时）无法连接到kdc服务器或网络中存在防火墙。


### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：配置数据连接入门](<index.php?doc-view-94.html>)
[下一篇：Kerberos 驱动整理 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1973.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
