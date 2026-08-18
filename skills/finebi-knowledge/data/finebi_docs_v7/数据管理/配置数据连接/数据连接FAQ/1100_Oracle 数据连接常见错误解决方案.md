---
title: Oracle 数据连接常见错误解决方案
doc_id: 1100
url: https://help.fanruan.com/finebi/doc-view-1100.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:13
version: "7.X"
---

> 1.&nbsp;概述本文介绍&nbsp;Oracle 数据连接&nbsp;中一些报错及解决方案。注1：所有以 ORA 开头的报错都是 Oracle 数据库报错，可以通过在网络上对报错信息进行搜索，排查报

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Oracle 数据连接常见错误解决方案
[__](<doc-edit-1100.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[9](<edition-list-1100.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍 [Oracle 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-185.html>) 中一些报错及解决方案。
注1：所有以 ORA 开头的报错都是 Oracle 数据库报错，可以通过在网络上对报错信息进行搜索，排查报错。
注2：BI 平台 Oracle 连接池在一段时间没有使用会自动释放，之所以查看连接池有之前的连接，是因为后面用户连接时又重新启用，所以不会因为连接一直得不到释放而造成问题。
注3：在 Oracle 9i 版本中，精度为 0 的字段值会被识别成文本而不是数值「该字段值用 column.getSize() 计算得到的是 38 ，所以会被识别成文本属性」；其他版本的 Oracle 未有此现象出现。
## 2\. 单个数据连接连接多个Oracle数据库
**问题描述：**
通常，单个数据连接对应一个 Oracle 数据库，但是有时可能因为网络或者其他原因，数据库连接不上或不能工作了，则整个项目就不能运行了。
**解决方案：**
将两台 Oracle 数据库中，配置相同的数据库以及数据库登录的用户名和密码，然后通过配置url让这个数据连接能连接两台机器，即使用一个数据连接连多个数据库。
URL格式：
jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST =IP1)(PORT = 1521))(ADDRESS = (PROTOCOL = TCP)(HOST =IP2)(PORT = 1521))(LOAD_BALANCE=yes)(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = 数据库名)))
示例1：在 192.168.100.168 和 192.168.100.170 机器上都拥有数据库名为 orcl10g，那么数据连接的 URL 就改成：
jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST =192.168.100.168)(PORT = 1521))(ADDRESS = (PROTOCOL = TCP)(HOST =192.168.100.170)(PORT = 1521))(LOAD_BALANCE=yes)(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = orcl10g)))  
示例2：在 env.finedevelop.com对应55602 端口拥有一个数据库 initfantlam，同时对应 55502 端口也拥有一个数据库 initfantlam，那么数据库连接的就改成：
jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS = (PROTOCOL = TCP)(HOST =env.finedevelop.com)(PORT = 55602))(ADDRESS = (PROTOCOL = TCP)(HOST =env.finedevelop.com)(PORT = 55502))(LOAD_BALANCE=yes)(CONNECT_DATA =(SERVER = DEDICATED)(SERVICE_NAME = initfantlam)))
## 3\. ONS configuration failed
**问题描述：**  

Oracle19c 数据连接报错：create connection error java.lang.IllegalArgumentException: ONS configuration failed
**解决方案：**  

Linux/Unix 修改 startWebLogic.sh 文件，搜索「setDomainENV.sh」，在「.${DOMAIN_HOME}」这句的上一行插入「JAVA_OPTIONS="-Doracle.jdbc.fanEnabled = false"」
## 4\. Cannot get a connection
**问题描述：**
连接 Oracle 数据库时，后台日志报错「java.lang.RuntimeException: Query:Cannot get a connection, pool error Timeout waiting for idle object」
**解决方案：**
修改连接池，扩大连接池最大连接个数，修改方法详见 [配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html> "连接池属性") 中 4.2 节高级设置。
## 5\. 数据乱码
**问题描述：**
1）Oracle 数据预览时，数据乱码，日期错乱。
2）Oracle 数据连接，[添加 DB 表](<https://help.fanruan.com/finebi7.0/doc-view-887.html>) 时，表名/表头乱码。
### 5.1 数据库编码格式不一致
**原因分析：**  

数据库编码格式与数据连接编码格式不一致
**解决方案：**
1）确认数据库编码格式
select userenv('language') from dual
2）修改数据连接编码格式
若数据库编码格式为GBK，那么数据连接编码格式应该为GBK
若数据库编码格式为US7ASCII，那么数据连接编码格式应该为ISO-8859-1
因为US7ASCII字符集为ISO字符集的子集，这样可以保证不会乱码
### 5.2 数据库驱动不一致
不同数据库版本使用的驱动是有很大差别的。
请务必参考 [Oracle 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-185.html>) 选择适合自己数据库版本的驱动。
## 6\. listener does not currently know of SID given in connect descriptor
**问题描述：**
连接 Oracle 数据库时，后台日志报错「ORA-12505:TNS:listener does not currently know of SID given in connect descriptor The Connection descriptor used by the client was:172.30.10.15:1521:slsdb」
### 6.1 URL格式错误
**原因分析：**  

URL格式不正确。
**解决方案：**
调整数据连接的URL样式，修改为：
jdbc:oracle:thin:@localhost:1521:databaseName改成jdbc:oracle:thin:@localhost:1521/databaseName
### 6.2 sid_name 出错
**原因分析：**
slsdb 不是正确的 sid_name，可能是 service_name
**解决方案：**
1）看看数据连接的URL中，端口后面的sid是否写错。
2）在 Oracle 里面用 tnsping，检查一下 listener 启动了没有，再看看 listener config file 里面有没有写上SID。
3）到服务器上看一下 listener.ora，如
SID_LIST_LISTENER= (SID_DESC= (GLOBAL_DBNAME=oracle9i) (ORACLE_HOME=/opt/oracle9i/product/9.2.0) (SID_NAME=ORCL) )
URL 里面可能用的是上面的 GLOBAL_DBNAME 的值，就是用的 SERVICE_NAME，替换成 SID_NAME，也可以登录 sqlplus 服务器
$sqlplus/as sysdba SQL>SELECT * FROM V$instance;查看本机上sid的名字
### 6.3 连接数过多
**原因分析：**
连接数过多
**解决方案：**
1）查看连接数
sql>show user; 查看当前用户
select count(*) from v$process;–当前连接数
select value from v$parameter where name = 'processes' --数据库允许的最大连接数
2）对当前连接数进行修改，不超过最大连接数就可以：
SQL> alter system set processes = 2000 scope = spfile;
3）重启刷新数据库
## 7\. Oracle 11 无法读取 DB 表
**问题描述：**
Oracle11无法取 DB 表，日志报错如下图所示：
![3.png](https://help.fanruan.com/core/style/lod.png)
**解决方案：**
点击下载：[orai18n.jar](<doc-download-/uploads/file/20201021/orai18n.jar> "下载资料")，把orai18n.jar放到工程的webapps\webroot\WEB-INF\lib下，并重启工程。
## 8\. Got minus one from a read call
**问题描述：**  

数据连接失败，报错：Got minus one from a read call
![1603179045829725.png](https://help.fanruan.com/core/style/lod.png)
  

**原因分析：**
当连接数据库时，是通过连接池的机制进行连接的，数据库参数：max-session决定连接池的大小，而应用同样也有一个参数，这个参数表示它连接数据库连接池所占用的最少资源。
例如：总共有 10 个应用需要连接数据库，如果每个应用连接数据库的最小连接数为 10 ，那么10个应用总共会有 100 个连接，这样就要求数据库连接池的 max-session 必须大于100，否则就会报Got minus one from a read call的错误。
**解决方案：**
1）查看 processes 和 sessions 参数
show parameter processes
show parameter sessions
2）修改 processes 和 sessions 值
alter system set processes=300 scope=spfile;
alter system set sessions=335 scope=spfile;
3）重启 Oracle
shutdown immediate;
startup;
## 9\. 数据连接成功后无法选择模式
**问题描述：**  

Oracle 版本 9.2.0.4 ，使用 2020-01-15 的 JAR ，连接成功后无法选择模式，也不显示数值。
**原因分析：**
驱动版本不适配。  

**解决方案：**
根据实际情况换成支持的驱动，驱动下载链接：[驱动下载官方链接](<https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html>)
示例：换成 ojdbc6 驱动才可以正常显示数据和选择模式。
## 10\. No matching authentication protocol
**问题描述：**  

Oracel 连接报错：ORA-28040: No matching authentication protocol；
**原因分析：**
驱动版本不适配。
**解决方案：**
点击下载：[ojdbc7.jar](<doc-download-/uploads/file/20201021/ojdbc7.jar> "下载资料")，把 ojdbc7.jar 放到工程的webapps\webroot\WEB-INF\lib下，并重启工程。
## 11\. 监听进程不能解析在连接描述符中给出的 SERVICE_NAME
**问题描述：**
连接 Oracle 数据库时，日志报错：ORA-12514:TNS:监听进程不能解析在连接描述符中给出的 SERVICE_NAME
### 11.1 SID_NAME 跟安装 Oracle 时的 ORACLE_SID 相同
**原因分析：**  

SID_NAME 跟安装 Oracle 时的 ORACLE_SID 相同。
SERVICE_NAME=DBNAME.DB_DOMAINDBNAME 即是数据库名，它是 Oracle 数据库的内部标识，安装以后轻易不要修改。
**解决方案：**
1）重启oracle相关「服务」，重新进行连接尝试。
2）正确设置listener.ora文件，添加相应的实例名，重启数据库服务器，检查各项服务是否启动，尝试连接。
### 11.2 例程启动问题
**原因分析：**
例程启动有问题
**解决方案：**
1）启动oracle
net start oracleserviceorcl
2）cmd管理员运行，输入如下代码  

sqlplus /nolog
connect/as sysdba
ALTER USER SYSTEM IDENTIFIED BY newpass;
3）启动例程
sql> startup
## 12\. 数据连接偶发失败
**问题现象：**
正常运行工程，忽然全部 oracle 数据库连接不上，服务器上 telnet ，网络是通的，不是密码错误，本地用数据库工具也能连上。重启后能够恢复。
**问题原因：**
数据连接时，使用的驱动是内置驱动，该驱动主要适配 jdk1.4 的。
**解决方案：**
如果遇到以上问题，建议升级驱动。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：MySQL数据连接常见问题](<index.php?doc-view-2117.html>)
[下一篇：SQL Server数据连接常见问题 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2119.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
