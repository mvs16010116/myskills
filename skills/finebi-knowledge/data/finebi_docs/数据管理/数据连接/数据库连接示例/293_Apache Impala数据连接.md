---
title: Apache Impala数据连接
doc_id: 293
url: https://help.fanruan.com/finebi6.X/doc-view-293.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:08
---

> 1.&nbsp;概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 Apache Impala 数据源。注：Impala里存在多个数据库，一个数据连接只能连接一个数据库

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Apache Impala数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[43](<edition-list-293.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-05-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0  
| -  
  
### 1.2 应用场景
本文将介绍如何连接 Apache Impala 数据源。  

注：Impala里存在多个数据库，一个数据连接只能连接一个数据库，不支持单个数据连接连接多个数据库。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html?source=4>) 2.1 节
  

支持的数据库版本 | 驱动包链接  
---|---  
Impala 2.2Impala 2.3Impala 2.8Impala 2.9Impala 2.10| [ImpalaJDBC41.zip](<doc-download-/finebi6.X/uploads/file/20240523/ImpalaJDBC41.zip> "下载资料")(用于仅加载当前方式 上传驱动）[ImpalaJDBC41.zip](<doc-download-/finebi6.X/uploads/file/20250522/ImpalaJDBC41.zip> "下载资料")（用于优先加载当前方 式上传驱动）  
Impala 2.10 kudu1.5|  [ClouderaImpalaJDBC41_2.5.43.rar](<doc-download-/uploads/file/20191202/ClouderaImpalaJDBC41_2.5.43.rar> "下载资料")  
  
在上传ImpalaJBDC41驱动时，如果选择优先加载当前方式上传驱动，那么需要删除ImpalaJBDC41驱动包中slf4j-api-1.7.36.jar文件；如果选择仅加载当前方式上传驱动，则保留ImpalaJBDC41驱动包中slf4j-api-1.7.36.jar文件。如下图所示：
  

![](/core/style/lod.png)
![](/core/style/lod.png)
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 若是用户名密码认证，需要收集用户名和密码；若是 Kerberos 认证，需要收集客户端 principal 和 keytab 密钥路径；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html?source=4>)
![](/core/style/lod.png)
2）选择 APACHE IMPALA 图标，如下图所示：  

![](/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。若用户需要在直连版本下使用该数据连接，需要在 URL 后增加后缀参数 ;UseNativeQuery=1 ，如下图所示：
Kerberos 认证方式详情可参见：[数据连接 kerberos 认证](<https://help.fanruan.com/finebi6.0/doc-view-282.html?source=4>)
![](/core/style/lod.png)
![](/core/style/lod.png)
若 Impala 数据库存在认证，则需要在 URL 后加入AuthMech参数，不同参数值代表了不同的认证，如下表所示： 
注：若数据库没有用户名密码时不需要加该参数。
值| 含义  
---|---  
3| username and password（用户名密码认证）  
  
2| username（用户名认证）  
  
1|  kerberos（Kerberos认证）  
  
0| 不认证   
  
URL 格式为：jdbc:impala://ip:port/dbname;authmech=n（ n 可以等于 0、1、2、3 分别代表上面的认证方式）
  * 用户名密码认证：AuthMech 参数值为 3 ，则 URL 格式为：jdbc:impala://ip:port/dbname;authmech=3
  * 用户名认证：AuthMech 参数值为 2 ，则 URL 格式为：jdbc:impala://ip:port/dbname;authmech=2
  * Kerberos 认证：AuthMech 参数值为 1 ，则 URL 格式为：jdbc:impala://ip:port/dbname;authmech=1


若数据库的认证方式为 Kerberos 认证，除了要加 AuthMech 参数，需填入注册过 kdc 的客户端名称、keytab 密钥路径和 Kerberos 认证对应 URL（加上AuthMech、KrbHostFQDN、KrbServiceName 三个参数）
参数| 值| 含义  
---|---|---  
AuthMech| 1  
| Kerberos 认证  
KrbHostFQDN| impala server 为 krb5.conf 文件中 admin_server 的值| 指定连接哪台服务器的 Impala  
KrbServiceName|  对应的服务名| 服务器的别名，请参见 [参数含义](<https://www.simba.com/products/Impala/doc/v1/JDBC_InstallGuide/content/jdbc/options/authmech.htm>)  
URL 格式为：jdbc:impala://ip:port/default;AuthMech=1;KrbHostFQDN=hostalias;KrbServiceName=impala  

例如：jdbc:impala://192.168.5.127:21050/default;AuthMech=1;KrbHostFQDN=quickstart.cloudera;KrbServiceName=impala，具体请参见 [数据连接Kerberos认证](<https://help.fanruan.com/finebi6.0/doc-view-282.html?source=4>)
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![73.png](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
## 5\. 注意事项
### 5.1 数据库注意点
  * 连接 Apache Impala 数据库时，FineBI 在数据查询的时候忽略大小写，字段查询结果都为小写。
  * impala 不支持 date 类型，支持 timestamp。
  * impala 不支持多个 distinct count，多个去重记录数预览 SQL 会报错。


### 5.2 版本升级后连接失败
**问题描述：**
升级后连接失败并报错：Error initialized or created transport for authentication: java.io.IOException，如下图所示：
![29.png](/core/style/lod.png)
**原因分析：**
升级后，Jass 代码内置造出的 .ini 文件会丢失掉，导致连接失败。
升级后 
**解决方案：**
将 Kerberos 认证的方式更改为第二种，详情可参见：[Kerberos 认证方式二](<https://help.fanruan.com/finebi6.0/doc-view-282.html#5>)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Pivotal Greenplum Database数据连接](<index.php?doc-view-289.html>)
[下一篇：达梦数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-1712.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
