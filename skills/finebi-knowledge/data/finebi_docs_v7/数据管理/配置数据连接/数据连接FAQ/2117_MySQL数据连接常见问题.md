---
title: MySQL数据连接常见问题
doc_id: 2117
url: https://help.fanruan.com/finebi/doc-view-2117.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:12
version: "7.X"
---

> 1.&nbsp;概述1.1 版本FineBI服务器版本6.01.2 应用场景本文介绍&nbsp;MySQL数据连接&nbsp;中，常见的问题及排查步骤。2. 数据乱码问题描述：MySQL数据集预览时，数

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# MySQL数据连接常见问题
[__](<doc-edit-2117.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Suki陈](<user-space-1778923.html>)_
* 历史版本：[8](<edition-list-2117.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
  
---  
6.0  
### 1.2 应用场景
本文介绍 [MySQL数据连接](<https://help.fanruan.com/finebi7.0/doc-view-183.html>) 中，常见的问题及排查步骤。
## 2\. 数据乱码
**问题描述：**
MySQL数据集预览时，数据乱码，日期错乱。
### 2.1 检查数据库字符集
**原因分析：**
MySQL 的字符集支持有两个方面：字符集(Character set)和排序方式(Collation)。
对于字符集的支持细化到四个层次：服务器(Server)， 数据库(Database)， 数据表(Table)， 连接(Connection)。
默认情况下，MySQL 的字符集是 latin1(ISO_8859_1)，为了防止出现数据乱码现象，MySQL 字符集应与平台保持一致，字符集(Character set)为 utf8，排序方式(Collation)为 utf8_general_ci
**排查步骤：**  

通过以下两条命令检查 MySQL 的字符集支持：
1）查看字符集：SHOW VARIABLES LIKE 'character%';
2）查看排序方式：SHOW VARIABLES LIKE 'collation_%';
**解决方案：**
修改 MySQL 的 my.ini 文件中的字符集键值。
default-character-set = utf8 character_set_server = utf8
修改完后，重启 MySQL 的服务。
service mysql restart
使用命令查看，发现数据库编码均已改成 UTF-8。
mysql> SHOW VARIABLES LIKE 'character%';
### 2.2 修改数据连接URL
修改数据连接的信息。
1）数据连接的「编码」类型设置为「默认」。
2）数据连接的「数据连接URL」后加后缀，如下图所示。格式为：
jdbc:mysql://hostname:port/database?generateSimpleParameterMetadata=true&useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
其中：
  * serverTimezone=Asia/Shanghai：设置以"上海时区"为准  

  * characterEncoding=utf8：编码转化


![](https://help.fanruan.com/core/style/lod.png)
### 2.3 检查服务器字体
**原因分析：**
系统未安装中文字体，所以只能乱码
**排查步骤：**
  * Windows系统：查看C:\WINDOWS\Fonts文件夹下的字体。
  * Linux系统：检查/usr/share/fonts文件夹下的字体。


**解决方案：**
服务器字体安装请参见：[服务器安装字体](<https://help.fanruan.com/finebi7.0/doc-view-1382.html>)。
## 3\. No suitable driver found for localhost
**问题描述：**
MySQL数据连接测试连接时，报错「No suitable driver found for localhost」。
### 3.1 URL格式错误
**原因分析：**
检查MySQL的数据连接URL格式是否为jdbc:mysql://<ip>:<port>/，若格式错误，则有可能出现该报错。
**解决方案：**  

请参考 [MySQL数据连接](<https://help.fanruan.com/finebi7.0/doc-view-183.html>) 修改数据连接URL格式。
### 3.2 驱动版本不匹配
**原因分析：**
工程中使用的MySQL驱动版本，与数据连接的MySQL数据库版本不匹配。
**解决方案：**
请参考 [MySQL数据连接](<https://help.fanruan.com/finebi7.0/doc-view-183.html>) 获取匹配版本的驱动并上传到工程中。
## 4\. Unknown system variable 'query_cache_size'
**问题描述：**
MySQL数据连接测试连接时，报错「Unknown system variable 'query_cache_size'」。
**原因分析：**
工程中使用的MySQL驱动版本，与数据连接的MySQL数据库版本不匹配。
query_cache_size参数在MySQL 8中已经移除，它存在于5.1.44版本驱动中。
**解决方案：**
请参考 [MySQL数据连接](<https://help.fanruan.com/finebi7.0/doc-view-183.html>) 获取匹配版本的驱动并上传到工程中。
## 5\. Access denied for user
**问题描述：**
MySQL数据连接测试连接时，报错「Access denied for user」。
**原因分析：**
数据库服务器拒绝了来源于这个IP的这个用户。
**解决方案：**
请排查数据连接中输入的用户名和密码是否正确。
请排查数据库所在服务器是否禁止工程所在服务器IP访问，请为工程所在服务器IP开启相关权限。
## 6\. The server time zone value 'XXX' is unrecognized
**问题描述：**
MySQL数据连接测试连接时，报错「The server time zone value 'XXX' is unrecognized」。
**原因分析：**
服务器的时区无法被识别或者代表不止一个时区，表示无法确定时区，需要指定。
解决方案：
修改数据连接的信息。数据连接的「数据连接URL」后加上时区参数。
格式为：&serverTimezone=UTC
## 7\. SSL连接报错
**问题描述：**
MySQL数据连接测试连接时，报错「Establishing SSL connection without server's identity verification is not recommended」
MySQL数据连接测试连接时，报错「Unsupported record version Unknown-0.0」  

**原因分析：**
Mysql数据库的SSL连接问题，提示警告不建议使用没有带服务器身份验证的SSL连接。
**解决方案：**
修改数据连接的信息。数据连接的「数据连接URL」后加上ssl使用参数。
格式为：&useSSL=false
## 8\. can not be represented as java.sql.Date
**问题描述：**
数据预览时报错「can not be represented as java.sql.Date」
**解决方案：**
修改数据连接的信息。数据连接的「数据连接URL」后加上参数。
格式为：zeroDateTimeBehavior=convertToNull
## 9\. wait millis 20000, active 0, maxActive 100
**问题描述：**
数据预览时数据集出错，日志报错「wait millis 20000, active 0, maxActive 100」。重新连接即可恢复。
**解决方案：**
修改数据连接的信息。数据连接的「数据连接URL」后加上参数。可根据SQL查询耗时，调大socketTimeout值。
格式为：&connectTimeout=5000&socketTimeout=5000
## 10\. last packet sent to the server was 9 ms ago
**问题描述：**
数据预览时数据集出错，报错last packet sent to the server was 9 ms ago
**原因分析：**
MySQL 连接时间限制
**解决方案：**
去掉 MySQL 连接的 url 后面的 ?serverTimezone=GMT%2B8&useSSL=false&useUnicode=true&characterEncoding=utf-8&autoReconnect=true&failOverReadOnly=false 这些参数
## 11\. this is incompatible with sql_mode=only_full_group_by
**问题描述：**
数据预览时数据集出错，报错:
错误代码:11300001 数据集配置错误 Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column '数据库名.表名.字段名' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
**原因分析：**
MySQL 数据库 5.7.5 之后的版本默认开启 only_full_group_by 模式。  

sql_mode 的 only_full_group_by 模式开启，会导致一些不规范的 SQL语 法不再被兼容，从而出现报错。
注：only_full_group_by 模式关闭，其实是比较冒险的一种设置，因为在这种设置下可以允许一些非法操作。
**排查步骤：**
1）检查 MySQL 数据库版本是否大于 5.7.5 。
[code]
    SELECT VERSION();  
    
[/code]
2）检查 sql_mode 是否开启了 only_full_group_by 模式。
[code]
    select @@GLOBAL.sql_mode;  
    
[/code]
**解决方案1：** 在 SQL 查询语句中不需要 group by 的字段上使用 any_value() 函数。any_value(field) 函数允许非分组字段的出现。
**解决方案2：** 通过 SQL 语句暂时性修改 sql_mode 值。
1）修改全局 sql_mode，只对新建数据库生效。
[code]
    SET @@global.sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';  
    
[/code]
2）对于已存在的数据库，则需要在对应的数据库下执行：
[code]
    SET sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';  
    
[/code]
**解决方案3：** 通过配置文件永久修改 sql_mode 值。
  * Windows系统：修改 my.ini 配置文件，在「mysqld」标签下追加内容。


[code]
    [mysqld]     
    sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION  
    
[/code]
  * Linux系统：编辑 my.cnf 配置文件，找到 sql_mode 的位置，删掉 only_full_group_by 。如果 my.cnf 文件中不存在 sql_mode，在「mysqld」标签下追加内容。


[code]
    [mysqld]  
    sql-mode=STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION  
    
[/code]
修改完后，重启 MySQL 服务。
[code]
    service mysql restart  
    
[/code]
## 12\. Unknown system variable 'query_cache_size'
**问题描述：**
通过proxy sql代理连接MySQL8.0报错Unknown system variable 'query_cache_size'
**原因分析：**
proxy sql最新内置的mysql版本是5的，所以需要修改它内置的MySQL版本才能连接。
**解决方案：**
查看proxy sql用的驱动版本，并改成对应版本的驱动:
查询版本语句：select * from global_variables where variable_name='mysql-server_version';
## 13\. This application has no explicit mapping for /error, so you are seeing this as a fallback
**问题描述：**
使用MySQL数据库的数据集查询，嵌入客户自己的平台后，报错：This application has no explicit mapping for /error, so you are seeing this as a fallback.There was an unexpected error (type=Internal Server Error, status=500).syntax error, error in :' 1=1 ${if(len(year) == 0,""," and D',expect VARIANT, actual VARIANT ${if(len(year) == 0,""," and DATE_FORMAT(tda.registerDate,'%Y') = '" +year+ "'")}
**原因分析：**
检查到数据集查询语句中有，使用${if()}函数进行参数设置，但是MySQL中没有这个语法
**解决方案：**
换成and IF('${year}' is null or '${year}' = '', 0 = 0, t.registerDate = '${year}') 
## 14\. Unable to load authentication plugin 'caching_ sha2_password'
**问题描述：**
MySQL 数据连接测试连接时，报错Unable to load authentication plugin 'caching_ sha2_password'
**原因分析：**  

不同版本 MySQL 的认证插件不同造成的连接失败。
MySQL 8.0.4 开始，MySQL 服务器的默认身份验证插件从 mysql_native_password 更改为 caching_sha2_password，如果驱动版本过低，则无法使用 MySQL 的身份验证插件。
**排查步骤：**
检查 MySQL 数据库版本是否高于 8.0.4，同时检查驱动版本是否是 5.X 版本，如果是则驱动版本过低。
**解决方案：**
从 [MySQL官网](<https://downloads.mysql.com/archives/c-j/>) 下载 MySQL 8.X 版本的驱动，并将其上传至 FineReport，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>) 2.1 节。
## 15\. Host 'xxx.xxx.xxx.xxx' is blocked because of many connection errors
**问题描述：**
MySQL 数据连接测试连接时，报错message from server: "Host 'xxx.xxx.xxx.xxx' is blocked because of many connection errors; unblock with 'mysqladmin flush-hosts'"
**原因分析：**
同一 IP 在短时间内连接 MySQL 数据库失败次数超过 max_connection_errors 参数设定值（MySQL 默认值为 10），从而被拒绝连接。
**排查步骤：**  

检查 max_connect_errors 的值是否过小：
[code]
    show global variables like '%max_connect_errors%';
[/code]
**解决方案：**
1）用户可以根据业务需求调整 max_connect_errors 的值，比如设置为 1000 ：  

[code]
    set global max_connect_errors=1000;
[/code]
2）查看是否修改成功：  

[code]
    show variables like '%max_connection_errors%';  
    
[/code]
3）进入 MySQL 控制台，清理 hosts 文件：
[code]
    flush hosts;  
    
[/code]
## 16\. Host 'xxx.xxx.xxxx.xxx' is not allowed to connect to this MySQL server
**问题描述：**
MySQL 数据连接测试连接时，报错message from server: "Host 'xxx.xxx.xxxx.xxx' is not allowed to connect to this MySQL server
**原因分析：**
数据库未允许来自该 IP 的客户端主机的访问。
**排查步骤：**
进入 MySQL 数据库执行：
[code]
    select host from mysql.user where user ='用户名';  
    
[/code]
如果显示值为 localhost，说明该数据库只允许 localhost 访问，需要开放其他 host 来源。
**解决方案1****：** 开放来自其他 host 的访问。
[code]
    GRANT ALL PRIVILEGES ON *.* TO '用户名'@'%' WITH GRANT OPTION;  
    FLUSH PRIVILEGES;
[/code]
****解决方案2****：**** 设置 host 为任意。
[code]
    update mysql.user set host='%' where user = '用户名';  
    FLUSH PRIVILEGES;  
    
[/code]
## 17\. net_write_timeout
**问题描述：**
数据更新失败，日志报错
错误代码:62400001 Application was streaming results when the connection failed. Consider raising value of 'net_write_timeout' on the server.
**原因分析：**
网络写入到数据库超时，MySQL 的默认为60s，当连接持续写入超过设置值时会被 MySQL 服务器断开。  

**排查步骤：**
检查 net_write_timeout 的值是否过小：  

[code]
    show global variables like '%timeout%';  
    
[/code]
**解决方案：**
1）调整写入数据库的逻辑，减少任务量，避免长时间占用连接。
2）根据实际情况调整 net_write_timeout 参数值：
[code]
    set global net_write_timeout = XXX;  
    
[/code]
## 18\. Packet for query is too large
**问题描述：**
MySQL 数据库连接失败，报错com.mysql.jdbc.PacketTooBigException: Packet for query is too large ( 4739923 > 1948576). You can change this value on the server by setting the max_ allowed_ packet' variable
**原因分析：**
本地 MySQL 数据库中「max_allowed_packet」值设置过小导致单个记录超过限制后写入数据库失败，且后续记录写入也会失败。
**解决方案1：**
MySQL 安装目录下的「my.ini」文件中的[mysqld] 字段中的「max_allowed_packet = 1M」修改为 500M ，重启 MySQL 即可。
**解决方案2：**
1）使用「set global max_allowed_packet = 524288000;」 语句将「max_allowed_packet」的值设置为 500 M。
2）使用「show VARIABLES like '%max_allowed_packet%';」 语句查看是否修改成功。
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：通用数据连接常见问题](<index.php?doc-view-760.html>)
[下一篇：Oracle 数据连接常见错误解决方案 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1100.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
