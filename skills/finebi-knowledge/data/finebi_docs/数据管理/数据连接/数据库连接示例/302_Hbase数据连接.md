---
title: Hbase数据连接
doc_id: 302
url: https://help.fanruan.com/finebi6.X/doc-view-302.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:23
---

> 1. 概述1.1 版本&nbsp;FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 Hbase 数据源。注：该数据库不支持使用直连属性的数据表2. 准备工作2.1 版本和驱动&nbs

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Hbase数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[28](<edition-list-302.html>)
* 最近更新：[帆软用户aEcMI0N7Gz](<user-space-3206309.html>) 于 2025-06-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何连接 Hbase 数据源。
注：该数据库不支持使用直连属性的数据表
## 2\. 准备工作
### 2.1 版本和驱动
支持的数据库版本| 本文示例驱动下载| 支持数据库版本  
---|---|---  
1.2  
| [phoenix-4.12.0-HBase-1.2-client.jar](<https://fanruanbbs.obs.cn-east-2.myhuaweicloud.com/%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E9%99%84%E4%BB%B6/finebi/phoenix-4.12.0-HBase-1.2-client%20%281%29.jar>)  
| org.apache.phoenix.jdbc.PhoenixDriver  
注：该驱动包也需要放置到 hbase/lib 下，然后重启 Hbase ( 使用命令./stop-hbase.sh, 再./start-hbase.sh)
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：  

  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 若是用户名密码认证，需要收集用户名和密码；若是 Kerberos 认证，需要收集客户端 principal 和 keytab 密钥路径；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html?source=4>)
![](/core/style/lod.png)
2）找到 Hbase 的图标，如下图所示：
![](/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。
Hbase 支持 Kerberos 认证，Kerberos 认证方式详情可参见：[数据连接Kerberos认证](<https://help.fanruan.com/finebi6.0/doc-view-282.html?source=4>)
注：用户可以选择性修改高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi6.0/doc-view-94.html>) 4.3 节
![](/core/style/lod.png)
4）点击「点击连接数据库」，连接成功后选择数据库模式（若不选则使用默认模式）。最后保存该数据连接，如下图所示：
![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
## 5\. 注意事项
### 5.1 FineBI 一直处于启动页面
**问题现象：**  

phoenix-4.12.0-HBase-1.2-client.jar放入 FineBI 安装目录FineBI/webapps/WebReport/WEB-INF/lib后，重启 FineBI ，FineBI 一直处于启动页面。如下图所示：
![](/core/style/lod.png)
**解决方法：**
1）使用压缩工具打开phoenix-4.12.0-HBase-1.2-client.jar文件，进入javax文件，删除el和servlet文件，如下图所示：
![35.png](/core/style/lod.png)
3）重启 FineBI 。
### 5.2 添加数据集
Hbase 数据连接成功后，添加实时 SQL 数据集并制作自助数据集时，暂不支持数据库表中带有小写和特殊符号（如“.”)的字段名。若需要添加此类字段，建议使用抽取数据。  

### 5.3 JDBC 访问数据库无法连接
**问题现象：**
JDBC 访问数据库无法连接, 提示 get locations 错误或者 zookeeper 找不到对应的地址。
**解决方案：**
连接前请检查 /etc/hosts 中的机器名对应 IP 是否为局域网 IP；
检查 /etc/hostname 中机器名设置和 /etc/hosts 中是否配置一致；
检查 FineBI 所在机器 hosts 配置的 IP+ 机器名 是否正确。
本地连接时需要配置 /etc/hosts 文件，添加远端映射：IP+机器名，例如： 192.168.5.206 centos-phoenix
### 5.4 使用 SQuirrel 连接方法
**解决方案：**
参考 <http://phoenix.apache.org/installation.html#SQL_Client>，在 <https://sourceforge.net/projects/squirrel-sql/?source=typ_redirect> 下载 SQuirrel ，默认安装后，将 phoenix-xxxx-client.jar 放到%SQuirrel_HOME%/lib下，启动 SQuirrel 后, 先添加驱动再添加 Alias 即可。
## 6\. 连接异常问题
### 6.1 问题描述
连接华为大数据平台 Hbase 数据库异常，使用帮助文档中的驱动，会报错：Unable to find org.apache.hadoop.hbase.ipc.NettyRpcClient ，NettyipcCilent 方法找不到，如下图所示：
![3.png](/core/style/lod.png)
### 6.2 原因分析
当前数据库环境对 configration 有额外配置，按以往方式连接会出现配置文件读取异常。
### 6.3 解决方案
调整配置文件和连接 URL 的写法，解决校验问题，实现数据库直连。
  * 修改配置文件：将使用的配置方法写入到 Hbase-siste.xml 中，再放入到相关的 jar 包中
  * 修改 URL ：Hbase数据连接 URL 格式改为：jdbc:phoenix:quorum:port/database:pricinpal:keytabPath，通过解析 URL 可以得到相关属性，并且会优先使用 URL 中得到的属性配置。


### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Hadoop Hive数据连接](<index.php?doc-view-301.html>)
[下一篇：KINGBASE数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-304.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
