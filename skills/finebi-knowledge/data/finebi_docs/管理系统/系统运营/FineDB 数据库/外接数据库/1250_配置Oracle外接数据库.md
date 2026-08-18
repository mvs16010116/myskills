---
title: 配置Oracle外接数据库
doc_id: 1250
url: https://help.fanruan.com/finebi6.X/doc-view-1250.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:10
---

> 1.&nbsp;概述1.1&nbsp;版本FineBI服务器版本功能变更6.0-1.2 功能简介BI 系统配置外接数据库后，遇到集群环境或数据量较大情况时，可保证 BI 系统的稳定性。用户可在「初始化时

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 配置Oracle外接数据库
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[26](<edition-list-1250.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2025-07-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
6.0| -  
### 1.2 功能简介
BI 系统配置外接数据库后，遇到集群环境或数据量较大情况时，可保证 BI 系统的稳定性。
用户可在「初始化时」配置外接数据库或在「平台中」配置 Oracle 版本的外接数据库。
注：若配置了外接数据库，请勿轻易修改外接数据库的用户名和密码，否则会导致工程启动失败。
如需修改，请参照：[修改外接数据库账号密码](<https://help.fanruan.com/finebi6.0/doc-view-1332.html>) 。
## 2\. 数据库配置
### 2.1 数据库版本
外接数据库支持的类型及版本如下表所示：
数据库类型| 支持数据库版本  
---|---  
Oracle单机| 10g(10.2)、10.2.0.1.011g(11.0.2.1)、11g(11.0.2.4)、11.0.2.4、11.2.0.2.012c、12c V12.2、19c  
Oracle集群| 11g、12c  
### 2.2 硬件配置
配置类型  
| 最低配置| 推荐配置  
---|---|---  
内存| 1GB| 2GB  
CPU| 4核| 8核  
网速  
| 50Mbps| 100Mbps  
finedb占用空间| 1GB| 2GB  
服务器磁盘空间| 100GB| 200GB  
磁盘读写速度| 50MB/s| 100MB/s  
注1：占用空间需要结合使用度进行调整，可以根据webapps/webroot/WEB-INF/embed/finedb文件夹大小配置，并根据实际大小预估未来使用大小，增大1~2倍。
注2：推荐内存为预留给工程配置库的内存。
注3：外接数据库尽量和 BI 工程在同一网段，避免网络波动等问题。
### 2.3 新建数据库
#### 2.3.1 新建账户  

对于 Oracle 数据库，配置前最好单独建一个账户（新建一个表空间，并指定为该用户默认表空间）。
新建用户：
CREATE USER "FINEDB" IDENTIFIED BY "123456" ACCOUNT UNLOCK DEFAULT TABLESPACE "USERS"  
注：oracle12c版本用户名需要以C##为前缀。
注：SQL 语句中的 FINEDB 为模式名，需要在本文 3.2.1 节步骤中填入。
授予权限：  
GRANT "CONNECT","RESOURCE" TO "FINEDB"  
ALTER USER "FINEDB" QUOTA UNLIMITED ON "USERS"
#### 2.3.2 新建表空间
在 Oracle 中新建用于存储迁移数据的 FineDB 表空间。
注1：不同 FineBI 工程，不可共用同一个外接 FineDB 表空间，否则数据可能会出现错乱。
注2：在迁移 FineDB 数据库时要求使用的表空间最好是空的。
### 2.4 更换驱动
数据库版本| 更换驱动  
---|---  
10g| 需要更换内置驱动：1）从 [Oracle 官网](<http://www.oracle.com/technetwork/database/application-development/jdbc/downloads/index.html>) 下载ojdbc14.jar驱动包。2）关闭 FineBI 工程。3）删除工程webapps\webroot\WEB-INF\lib目录下的ojdbc8.jar驱动包。4）将ojdbc14.jar驱动包上传至工程webapps\webroot\WEB-INF\lib目录下。5）重启 FineBI 工程。  
11g、12c| 无需更换内置驱动FineBI 内置的ojdbc8.jar驱动包满足使用需求  
## 3\. 配置外接数据库
### 3.1 外接数据库配置入口
外接数据库的配置入口，有三种形式：  

1）超级管理员第一次登录数据决策系统时，即可为系统配置外接数据库。如下图所示：
![](/core/style/lod.png)
2）对于使用内置数据库的系统，管理员登录数据决策系统，点击「管理系统>系统管理>常规>外接数据库>待配置」，可为系统第一次配置外接数据库。如下图所示：
![](/core/style/lod.png)
3）对于已启用外接数据库的系统，管理员登录数据决策系统，点击「管理系统>系统管理>常规>外接数据库>已配置」，可为系统迁移至新的外接数据库。如下图所示：
![](/core/style/lod.png)
### 3.2 配置外接数据库
进入到外接数据库配置界面后，选择数据库类型，输入实际数据库相应的信息即可。如下图所示：
![](/core/style/lod.png)
#### 3.2.1 设置项
各设置项说明如下表所示：
设置项| 说明  
---|---  
数据库类型| 选择 oracle  
驱动| 无需修改，会自动配置  
数据库名称| 填写实例名称只允许包含数字、字母、下划线和「.」  
用户名/主机/密码/端口| 根据本地数据库实际情况填写主机名称只允许包含数字、字母、下划线、「-」和「.」用户需要具备 create、delete、alter、update、select、insert、index 权限  
模式| 仅支持下拉选择模式正确填写完上面几项设置后，点击模式下拉框中的「点击连接数据库」，系统将自动连接该数据库并读取模式，选择即可（尽量选择和数据库用户的名字相同的模式）注：若提示数据库连接失败，请检查上面几项设置。![](/core/style/lod.png)  
数据连接URL| 数据库连接 URL 支持三种写法：1）Oracle单机jdbc:oracle:thin:@<host>:<port>:<SID>  
2）Oracle 集群写法一：jdbc:oracle:thin:@//<host>:<port>/<service_name>写法二：jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.1)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.2)(PORT=1521)))(LOAD_BALANCE=yes)(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=xxrac)))注：10.0.11 版本之后的工程，支持集群写法二。  
#### 3.2.2 迁移数据至要启用的数据库
用户可根据自身需求选择是否勾选「迁移数据至要启用的数据库」按钮。具体如下：
**1）勾选「迁移数据至要启用的数据库」，新外接数据库为空**
点击「启用新数据库」后，会将原 finedb 数据库的平台数据迁移到新外接数据库中。
**2）勾选「迁移数据至要启用的数据库」，新外接数据库中已存在平台数据**
点击「启用新数据库」后，跳出提示「该数据库已存在平台数据，导入数据前将清空原有平台数据，确认连接该数据库？」。
点击「确定」将清空原有平台数据，将原 finedb 数据库的平台数据迁移到新外接数据库中。
![](/core/style/lod.png)
**3）不勾选「迁移数据至要启用的数据库」**，新外接数据库为空****
点击「启用新数据库」后，跳出提示「目标数据库为新数据库，将当前数据迁移至目标数据库后方能使用」。
点击「确定」，将原 finedb 数据库的平台数据迁移到新外接数据库中。
![](/core/style/lod.png)
**4）不勾选「迁移数据至要启用的数据库」，新外接数据库中已存在平台数据**
点击「启用新数据库」后，5.1.15 及之后版本的 BI 工程会自动检测目标数据库中数据对应的 JAR 包版本和当前工程的 JAR 包版本是否一致。
  * 若不一致，则跳出提示「无法启用！启用新数据库需要的工程版本：XXX。当前工程版本：XXX。请确保工程版本一致！」。无法进行外接数据库配置。


![](/core/style/lod.png)
  * 若 JAR 包版本一致，且原 finedb 数据库为内置数据库，则直接启用新外接数据库。
  * 若 JAR 包版本一致，且原 finedb 数据库为外接数据库，迁移前将自动备份原数据库的配置信息，在webapps\webroot\WEB-INF\config目录下生成db.properties.bak文件，并直接启用新外接数据库。如下图所示：


![](/core/style/lod.png)
### 3.3 迁移成功
等待一段时间，迁移成功后，根据迁移时的情况，可能会跳出不同的弹窗提示。
**1）新外接数据库，使用了原 finedb 数据库的数据。**
则提示「已成功启用目标数据库」。点击「确定」即可，迁移成功。如下图所示：
![](/core/style/lod.png)
**2）新外接数据库，使用了该数据库中原有的数据，且原 finedb 数据库为内置数据库。**
则提示「已成功切换至目标数据库！新旧数据库若存在数据差异可能影响系统运行，建议重启工程以确保正常使用」。
点击「确定」后，重启报表工程，方迁移成功。如下图所示：
![](/core/style/lod.png)
**3）新外接数据库，使用了该数据库中原有的数据，且原 finedb 数据库为外接数据库。**
则跳出两个提示：
  * 已成功切换至目标数据库！新旧数据库若存在数据差异可能影响系统运行，建议重启工程以确保正常使用
  * 原数据库配置已备份至config文件夹下，如有需要可以使用备份文件还原数据库配置  



点击「确定」后，重启报表工程，方迁移成功。如下图所示：
![](/core/style/lod.png)
![1611286418590120.png](/core/style/lod.png)
### 3.4 删除内置库数据连接
「内置 FineDB 数据库」为HSQL数据库，使用时会建立内存数据库，数据量大时会占用大量内存。
因此配置完外接数据库后，请检查数据连接中是否存在「内置 FineDB 数据库」的数据连接。
若存在相关数据连接，请及时删除，否则会持续占用服务器内存。
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：配置MySQL8外接数据库](<index.php?doc-view-1249.html>)
[下一篇：配置SQL Server外接数据库 ![](/core/style/forward.png) ](<index.php?doc-view-1251.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
