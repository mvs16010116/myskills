---
title: Apache Phoenix数据连接
doc_id: 294
url: https://help.fanruan.com/finebi/doc-view-294.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:46
version: "7.X"
---

> 1. 概述1.1 版本&nbsp;FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何在 FineBI 中连接 Apache Phoenix 数据库。注：该数据库不支持使用直连属性的数据表2

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Apache Phoenix数据连接
[__](<doc-edit-294.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[34](<edition-list-294.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何在 FineBI 中连接 Apache Phoenix 数据库。
注：该数据库不支持使用直连属性的数据表
## 2\. 准备工作
### 2.1 版本和驱动
支持的数据库版本| 驱动下载链接| 支持数据库版本  
---|---|---  
1.2  
| [phoenix-4.12.0-HBase-1.2-client.jar](<https://fanruanbbs.obs.cn-east-2.myhuaweicloud.com/%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E9%99%84%E4%BB%B6/finebi/phoenix-4.12.0-HBase-1.2-client.jar>)| org.apache.phoenix.jdbc.PhoenixDriver  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：  

  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 若是用户名密码认证，需要收集用户名和密码；若是 Kerberos 认证，需要收集客户端 principal 和 keytab 密钥路径；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 APACHE Phoenix 的图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。
Hbase 支持 Kerberos 认证，Kerberos 认证方式详情可参见：[数据连接Kerberos认证](<https://help.fanruan.com/finebi7.0/doc-view-282.html?source=4>)
注：用户可以选择性修改高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html>) 4.3 节
![33.png](https://help.fanruan.com/core/style/lod.png)
4）点击「点击连接数据库」，连接成功后选择数据库模式（若不选则使用默认模式）。最后保存该数据连接，如下图所示：
![34.png](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：  

  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
## 5\. 注意事项
### 5.1 FineBI 一直处于启动页面
**问题现象：**  

将 phoenix-4.12.0-HBase-1.2-client.jar 放到目录%FineBI%\webapps\webroot\WEB-INF\lib后，重启 FineBI ，FineBI 一直处于启动页面。如下图所示：
![1586781481408884.png](https://help.fanruan.com/core/style/lod.png)
**解决方法：**
1）使用压缩工具打开 phoenix-4.12.0-HBase-1.2-client.jar 文件，进入 javax 文件，删除 el 和 servlet 文件，如下图所示：
![35.png](https://help.fanruan.com/core/style/lod.png)
3）重启 FineBI 即可。
### 5.2 查询语句
1）A join B on A.a=B.b，A B 不支持子查询。
2）尽量避免使用多层嵌套 SQL 语句。多层嵌套可能会 SQL 报错，如果用户原本的 SQL 数据集已经有 SQL 嵌套, 引擎开启实时数据时的查询可能会出现问题。
例如 SQL 语句 select T_2.a from ( select T_1.a from ( select * from A) T_1 ) T_2 会报错。
### 5.3 问题报错及解决方案 
1）描述：JDBC 访问数据库无法连接, 提示 get locations 错误或者 zookeeper 找不到对应的地址。
解决方法：
检查/etc/hosts 中的机器名对应IP是否为局域网IP；
检查/etc/hostname中机器名设置和/etc/hosts中是否配置一致；
检查 BI 所在机器 hosts 配置的 IP+ 机器名是否正确。
2）描述：BI 测试连接失败, 报错 Caused by: java.sql.SQLException: org.apache.hadoop.hbase.DoNotRetryIOException: java.lang.IllegalAccessError: tried to access method com.google.common.base.Stopwatch.<init>()V from class org.apache.hadoop.hbase.zookeeper.MetaTableLocator
解决方法：
将 guava 包替换为 [guava-16.0.1.jar](<http://www.finedevelop.com/download/attachments/17707197/guava-16.0.1.jar?version=1&modificationDate=1508406408000&api=v2>) 。
3）描述：BI 测试连接失败，报错：ERROR 726 (43M10): Inconsistent namespace mapping properties. Cannot initiate connection as SYSTEM:CATALOG is found but client does not have phoenix.schema.isNamespaceMappingEnabled enabledERROR 726 (43M10): Inconsistent namespace mapping properties. Cannot initiate connection as SYSTEM:CATALOG is found but client does not have phoenix.schema.isNamespaceMappingEnabled enabled报错截图：
![222](https://help.fanruan.com/core/style/lod.png)  

解决方法：
如果使用了 Hbase 中的自定义 namespace ，不仅仅使用 default ，那么在 Phoenix 中与之对应的是 schema 的概念。但是默认并没有开启，需要在 hbase-site.xml 中增加以下配置项：
![222](https://help.fanruan.com/core/style/lod.png)
具体代码如下所示：
[code]
    <property>  
        <name>phoenix.schema.isNamespaceMappingEnabled</name>  
        <value>true</value>  
    </property>  
    <property>  
        <name>phoenix.schema.mapSystemTablesToNamespace</name>  
        <value>true</value>  
    </property>
[/code]
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：INFORMIX数据连接](<index.php?doc-view-99.html>)
[下一篇：ClickHouse 数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1102.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
