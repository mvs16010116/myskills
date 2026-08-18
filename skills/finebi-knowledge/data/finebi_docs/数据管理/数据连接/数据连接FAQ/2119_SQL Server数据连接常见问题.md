---
title: SQL Server数据连接常见问题
doc_id: 2119
url: https://help.fanruan.com/finebi6.X/doc-view-2119.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:36
---

> 1.&nbsp;概述1.1 版本FineBI服务器版本6.01.2 应用场景本文介绍&nbsp;SQL Server数据连接&nbsp;中，常见的问题及排查步骤。2. TCP/IP 连接失败问题描述：连

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# SQL Server数据连接常见问题
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Suki陈](<user-space-1778923.html>)_
* 历史版本：[5](<edition-list-2119.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2024-03-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
  
---  
6.0  
### 1.2 应用场景
本文介绍 [SQL Server数据连接](<https://help.fanruan.com/finebi6.X/doc-view-100.html>) 中，常见的问题及排查步骤。
## 2\. TCP/IP 连接失败
**问题描述：**
连接 SQL Server 数据库时，报错「com.microsoft.sqlserver.jdbc.SQLServerException：到主机的 TCP/IP 连接失败」
![](/core/style/lod.png)
### 2.1 检查 URL 是否正确
1）确认数据连接的URL是否正确，包括IP、端口、数据库名称。如下图所示：
![](/core/style/lod.png)
2）去除数据连接的 URL 后面的 databaseName，测试是否成功。
如果成功，则问题来源于后面的实例名，否则问题是前面的 TCP/IP 连接。
![](/core/style/lod.png)
3）若检测到是实例名的问题，需要检查数据库实例名是否与 URL 中的 databaseName 一致。  

![](/core/style/lod.png)
4）修改数据连接的信息。数据连接的「数据连接URL」后加上ssl参数。
格式为：&sslProtocol=TLS
### 2.2 检查数据库配置
1）检查数据库是否启动
![](/core/style/lod.png)
2）检查是否允许远程连接服务器
进入数据库所在服务器查看对象资源管理器，检查是否允许远程连接。
![](/core/style/lod.png)
3）检查数据库用户状态
数据连接中使用的用户密码，需要授权允许连接到数据引擎，并且登录状态是已启用。
![](/core/style/lod.png)
4）检查 TCP/IP 协议是否启动
![](/core/style/lod.png)
5）检查网络配置  

打开 SQL server 配置管理器，检查 SQL server 网络配置是否启用 Named Pipes 和 TCP/IP 。  

![](/core/style/lod.png)
### 2.3 检查网络环境
双击「TCP/IP」或右键-属性查看对应的端口号是否正确。  

![](/core/style/lod.png)
### 2.4 检查是否安装 sp4
这个主要是 SQL server 2000，其他版本一般没有这个问题。sqlsp4 补丁就是 Microsoft SQL Server 2000 Service Pack 4 ，大多数版本为简体中文版。
sp4 包括用于以下 SQL Server 2000 组件的程序包，可在网络上寻找资源下载。
数据库组件（下载文件：SQL2000-KB884525-SP4-x86.EXE）：更新 SQL Server 2000 的 32 位数据库组件，包括数据库引擎、复制、客户端连接组件和工具。
Analysis Services 组件（下载文件：SQL2000.AS-KB884525-SP4-x86.EXE）：更新 SQL Server 2000 的 32 位 Analysis Services 组件。
SQL Server 2000 Desktop Engine (MSDE) 组件（下载文件：SQL2000.MSDE-KB884525-SP4-x86.EXE）：对于 SQL Server 2000 的 32 位 MSDE 组件：
安装新的 MSDE 实例；
升级现有 MSDE 实例；
更新使用合并模块的应用程序。
打 sp4 后一般会出现登录连接问题，看看SQL的服务有没有运行，没运行就去我的电脑>管理>服务里面，把 MSSQLSERVER 服务登录的用户名和密码改正确；有运行，进企业管理器，改 SQL 的登录方式为混合模式，设置sa密码，重新设置一次。 sqlserver 2000 sp3由于有 bug，很多服务器打不了补丁，说sa连接失败，所以直接安装 sp4 升级补丁，升级之前建议先备份数据库。
## 3\. SQL Server查询速度较慢
**问题描述：**  

使用 SQL Server 数据库，SQL 语句在数据库里查询异常的快，可是放到 FineBI 里面速度相对慢了。
### 3.1 SQL语句是否过于复杂
SQL Server 查询速度较慢，建议先检查 SQL 语句是否过于复杂、是否用了太多的链接查询，优化 SQL 语句来提高访问数据的速度。
### 3.2 网络是否稳定
在访问或导出数据量较大的仪表板时，还要检查网络速度，是否影响访问数据的快慢等。
### 3.3 SQLServer驱动包问题
排除以上因素，SQL Server 访问数据慢，那就是 SQL Server 驱动包的原因了。
工程环境下面默认有两个 SQL Server 驱动「sqljdbc.jar」和「jtds-1.2.2.jar」。
有的时候「sqljdbc.jar」查询速度比较慢，那么就可以尝试换下「jtds-1.2.2.jar」驱动。
![](/core/style/lod.png)
使用「 jtds-1.2.2.jar」驱动连接数据库时，数据库类型选择「其他JDBC」，手动输入「 URL 」和「驱动器」。
  * 驱动：net.sourceforge.jtds.jdbc.Driver
  * URL：jdbc:jtds:sqlserver://IP:端口号/databaseName


操作详情请参见： [配置数据连接入门](<https://help.fanruan.com/finebi6.X/doc-view-94.html>)
![](/core/style/lod.png)
## 4\. SQL SERVER多实例名
**问题描述：**  

一般安装SQL SERVER都是使用默认实例名，但是有时候有特殊情况不能使用默认实例名，或者多个实例的时候，就不一样了。
**解决方案：**
修改地址参数即可建立非默认实例名的链接。
默认的数据链接地址为：jdbc:sqlserver://localhost:1433;databaseName=数据库名
当非默认实例名时，修改为：jdbc:sqlserver://localhost\实例名:端口;databaseName=数据库名
注：非默认实例名使用的端口可能为1434，请注意防火墙之类是否有拦截或者占用
![](/core/style/lod.png)
## 5\. 数据乱码
**问题描述：**
SQL Server数据集预览时，数据乱码，日期错乱。
### 5.1 排查数据库排序规则
**原因分析：**  

SQL Server数据乱码主要受排序规则的影响，安装时系统默认的排序规则是拉丁文的排序规则。
安装时若没有考虑到这一点，安装完成后，就会造成在使用过程中出现乱码。
**解决方案：**
请绕过FineReport/FineBI，直接从数据库端用SQL取数，看看是否也会乱码。
若乱码，则需要修改排序规则。右键数据库，点击「属性>选项」，设置「排序规则」。如下图所示：
![](/core/style/lod.png)
### 5.2 排查编码是否一致
**原因分析：**
数据库编码格式与数据连接编码格式不一致
**解决方案：**
1）查询SQL Server数据库编码格式  

SELECT COLLATIONPROPERTY('Chinese_PRC_Stroke_CI_AI_KS_WS', 'CodePage');
2）查询结果编码对照如下，请参照调整帆软数据连接的编码：  
936 简体中文GBK  
950 繁体中文BIG5  
437 美国/加拿大英语  
932 日文  
949 韩文  
866 俄文  
65001 unicode UFT-8
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Oracle 数据连接常见错误解决方案](<index.php?doc-view-1100.html>)
[下一篇：DB2数据连接常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-2120.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
