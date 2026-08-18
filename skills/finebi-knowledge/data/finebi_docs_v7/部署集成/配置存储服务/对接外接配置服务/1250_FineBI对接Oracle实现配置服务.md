---
title: FineBI对接Oracle实现配置服务
doc_id: 1250
url: https://help.fanruan.com/finebi/doc-view-1250.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:19
version: "7.X"
---

> 1. 概述帆软应用中，管理员往往会在平台设置用户、挂载目录、分配权限、设定定时调度。这些配置，均存储于配置库中。在正式环境下，用户可准备一个Oracle数据库，与帆软应用对接，用于配置存储。稳定的外部数

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接Oracle实现配置服务
[__](<doc-edit-1250.html>)
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[26](<edition-list-1250.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
帆软应用中，管理员往往会在平台设置用户、挂载目录、分配权限、设定定时调度。这些配置，均存储于配置库中。
在正式环境下，用户可准备一个Oracle数据库，与帆软应用对接，用于配置存储。稳定的外部数据库，可确保帆软应用在高负载下的稳定运行。
本文主要讲解帆软项目对接Oracle数据库，存储工程配置信息：
  * **用户可自行准备一个Oracle数据库的表空间**，并进行参数调优****
  * 在部署新项目/项目部署好后，可将项目与该配置库对接


## 2\. 准备配置库
用户需要自行准备并部署Oracle数据库和表空间。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅数据库官网获取其他帮助。
**如运维能力不足，推荐使用运维平台部署新项目时，勾选「部署MySQL8」即可，无需手动部署和调优。**
### 2.1 数据库版本
本文列出的是帆软测试通过的环境。
  * 本文未提及的更低版本，一般默认不支持，或存在一些漏洞，不建议使用
  * 本文未提及的更高版本，用户可自行测试验证。如果出现问题，付费用户可联系技术支持获取帮助。技术支持联系方式：「[服务平台](<https://service.fanruan.com/>)>在线支持」

数据库类型  
| 数据库版本| 说明  
---|---|---  
Oracle| Oracle单机：10g(10.2)、10.2.0.1.0| 需要手动上传驱动因此仅支持在项目部署好后对接  
Oracle单机：11g(11.0.2.1)、11g(11.0.2.4)、11.0.2.4、11.2.0.2.0  
12c、12c V12.2、19cOracle集群：11g、12c| 驱动已直接内置在工程中支持在部署新项目/项目部署好后对接  
### 2.2 服务器配置
配置类型  
| 最低配置| 推荐配置| 注意事项  
---|---|---|---  
内存| 1GB| 2GB| 内存，是指分配给配置库的内存，而非服务器的所有内存如有条件，建议配置库独占一台服务器如条件不足，至少确保部署配置库的服务器中，不部署帆软应用以外的任何内容，且确保分配给配置库的内存足够  
CPU| 4核| 8核| -  
网速  
| 50Mbps| 100Mbps| 配置库和应用工程、其他组件建议在同一网段，避免网络波动等问题配置库和应用工程、其他组件之间需要网络畅通，互相端口可访问  
finedb占用空间| 1GB| 2GB| 占用空间，请结合工程使用度进行调整建议根据推荐配置，增大1~2倍，预留足够空间  
服务器磁盘空间  
| 100GB| 200GB| -  
磁盘读写速度| 50MB/s| 100MB/s  
| -  
  
### 2.3 新建表空间
不同帆软工程，不可共用同一个数据库表空间作为配置库，否则数据可能会出现错乱。
因此建议在数据库中新建一个表空间，用于存储相关配置数据。
且该表空间内不建议存放其他任何数据，包括业务数据、日志数据等。
**1）新建表空间和对应用户**
步骤  
| 语句  
---|---  
语句示例| 新建一个名叫「FANRUAN」的用户，该用户密码为「123456」，该用户的默认表空间为「FINEDB」CREATE USER "FANRUAN" IDENTIFIED BY "123456" ACCOUNT UNLOCK DEFAULT TABLESPACE "FINEDB"  
注意事项| **1）用户名**
  * 创建用户是推荐操作，而非必须。也可选择直接创建表空间，并将其分配给已有的用户
  * 如数据库版本为Oracle12c，用户名必须以C##为前缀，否则无法正常使用
  * 由于数据库模式一般选择用户同名模式，因此用户名称建议仅包含数字、字母，不建议包含特殊字符

**2）用户密码**
  * 配置库对接成功后，请勿轻易修改所使用的数据库用户名和密码，否则会导致工程启动失败

**3）表空间名称**
  * 只允许包含数字、字母、下划线和「.」

  
**2）授予权限**
步骤  
| 语句  
---|---  
语句示例| 为用户「FANRUAN」分配表空间「FINEDB」的权限GRANT "CONNECT","RESOURCE" TO "FANRUAN" ALTER USER "FANRUAN" QUOTA UNLIMITED ON "FINEDB"  
注意事项| 用户至少需要具备 create、delete、alter、update、select、insert、index 权限  
### 2.4 准备配置库信息
请准备好表空间的相关信息，用于接入项目作为配置库。
设置项| 说明  
---|---  
数据库名称| 2.3节，在数据库新建的表空间名称表空间名称只允许包含数字、字母、下划线、「-」和「.」  
主机  
| 数据库所在服务器的IP  
端口| 数据库占用的服务器端口  
用户名| 数据库的用户名称1）所准备的用户需要具备 create、delete、alter、update、select、insert、index 权限，以满足配置表架构调整、配置信息调整等诉求2）如数据库版本为Oracle12c，用户名必须以C##为前缀，否则无法正常使用3）由于数据库模式一般选择用户同名模式，因此用户名称建议仅包含数字、字母，不建议包含特殊字符  
密码| 数据库的用户密码配置库对接成功后，请勿轻易修改所使用的数据库用户名和密码，否则会导致工程启动失败  
  
模式| 即为所准备的数据的用户名称  
  
## 3\. 项目接入配置库
支持在以下情况下接入Oracle配置库，请根据情况自行选择即可。
### 3.1 部署新项目时接入
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的Oracle数据库作为工程配置库。
  * 此情况下，请确保数据库表空间内容为空，不存在任何数据，否则无法成功对接。  

  * 此情况下，只支持对接11g、12c版本的Oracle数据库，不支持对接10g版本的Oracle数据库


1）外接配置库选择「对接已有外接配置库」。  

2）在「外接配置库」信息填写处：
  * 数据库类型：选择「oracle」
  * 驱动：无需调整，选择「oracle.jdbc.driver.OracleDriver」即可
  * 数据库名称、主机、端口、用户名、密码：填写第二章准备的配置库信息即可


3）选择「模式」：
  * 正确填写完上面的所有配置后，点击模式下拉框中的「点击连接数据库」，系统将自动连接该数据库并读取模式
  * 优先选择与数据库用户同名的模式


4）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。  

![](https://help.fanruan.com/core/style/lod.png)
### 3.2 运维平台集群管理接入
在运维平台的「集群管理」中，可为项目接入自备的Oracle数据库作为配置库。
#### 3.2.1 上传驱动（可选）
  * 如对接**11g、12c** 版本的Oracle数据库，请**直接跳过本节** ，驱动已直接内置在工程中。
  * 如对接**10g** 版本的Oracle数据库，请**务必执行本节** ，否则无法成功对接。


1）前往Oracle官网，下载ojdbc14.jar：[Oracle官网](<https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html>)
2）参考文档，将驱动上传到项目中：[驱动管理](<https://help.fanruan.com/finereport/doc-view-4165.html>)  

#### 3.2.2 确保单应用存活（多应用服务工程须完成，单应用服务工程无需）
对于多应用项目，需要确保接入/迁移配置服务时仅存活一个应用节点。
管理员登录运维平台，选中指定项目。点击「维护>组件管理」。检查是否有多个「bi-web」容器存活。
如果有，请点击容器的「停止」按钮，确保将其他「bi-web」容器关停至「exited」状态，仅保留一个容器存活。
![](https://help.fanruan.com/core/style/lod.png)
#### 3.2.3 配置外接配置库
1）管理员登录运维平台，选中指定项目。点击「维护>集群管理」，对「外接配置库」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
2）选择数据库类型：oracle
3）选择驱动：
数据库版本  
| 说明  
---|---  
11g、12c| 无需调整，选择「oracle.jdbc.driver.OracleDriver」即可  
10g| 选择驱动管理上传ojdbc14.jar时设置的驱动名称  
4）数据库名称、主机、端口、用户名、密码：填写第二章准备的配置库信息即可
5）选择「模式」：
  * 正确填写完上面的所有配置后，点击模式下拉框中的「点击连接数据库」，系统将自动连接该数据库并读取模式
  * 优先选择与数据库用户同名的模式


6）数据连接URL：支持手动编辑调整，支持多种写法，按需选择
类型  
| 写法  
---|---  
Oracle单机| jdbc:oracle:thin:@<host>:<port>:<SID>   
  
Oracle集群| jdbc:oracle:thin:@//<host>:<port>/<service_name>  
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.1)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.2)(PORT=1521)))(LOAD_BALANCE=yes)(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=xxrac)))  
7）选择是否「迁移数据至要启用的数据库」
情况| 新Oracle配置库情况  
  
---|---  
希望使用当前项目原有配置| 1）**必须勾选** 「迁移数据至要启用的数据库」2）项目与该配置库对接成功后，会将**工程原有配置** 数据，迁移到该表空间中3）无论准备的新Oracle表空间中是否有数据，均**会被清空，无法找回**  
希望使用其他项目配置（例如将正式环境配置，拷贝一份给测试环境使用）| 1）自行将准备的配置数据上传到新Oracle表空间中必须确保所准备的数据，对应的项目 JAR 包版本和当前项目的 **JAR 包版本完全一致** ，否则无法使用2）**不勾选** 「迁移数据至要启用的数据库」3）项目与该配置库对接成功后，会使用**表空间中的数据** ，作为项目的配置4）项目原有配置的对接信息，会备份到工程config目录下的db.properties.bak文件中  
8）点击「启用数据库」，提示「迁移成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
#### 3.2.4 确保多应用配置同步（多应用服务工程须完成，单应用服务工程无需）
**1）拷贝db.properties文件**
前往唯一存活的「bi-web」容器所在服务器，复制该组件外挂目录/config文件夹中的db.properties文件。
逐一粘贴到其他「bi-web」容器所在服务器的组件外挂目录/config文件夹中。
![](https://help.fanruan.com/core/style/lod.png)
**2）停止所有应用**
管理员登录运维平台，选中指定项目，点击「维护>组件管理」
请对「bi-web」组件进行一键「停止」，确保所有「bi-web」容器关停至「exited」状态。
![](https://help.fanruan.com/core/style/lod.png)
**3）启动所有应用**
管理员登录运维平台，选中指定项目，点击「维护>组件管理」。
请对「bi-web」组件进行一键「启动」，确保所有「bi-web」容器启动至「running」状态。
![](https://help.fanruan.com/core/style/lod.png)
### 3.3 管理系统接入配置库
在帆软应用的「管理系统>管理系统>常规」中，可接入自备的数据库作为配置库。
#### 3.3.1 上传驱动（可选）
  * 如对接**11g、12c** 版本的Oracle数据库，请**直接跳过本节** ，驱动已直接内置在工程中。
  * 如对接**10g** 版本的Oracle数据库，请**务必执行本节** ，否则无法成功对接。


1）前往Oracle官网，下载ojdbc14.jar：[Oracle官网](<https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html>)
2）参考文档，将驱动上传到项目中：[驱动管理](<https://help.fanruan.com/finereport/doc-view-4165.html>)  

#### 3.3.2 确保单应用存活（多应用服务工程须完成，单应用服务工程无需）
对于多应用项目，需要确保接入/迁移配置服务时仅存活一个应用节点。
管理员登录运维平台，选中指定项目。点击「维护>组件管理」。检查是否有多个「bi-web」容器存活。
如果有，请点击容器的「停止」按钮，确保将其他「bi-web」容器关停至「exited」状态，仅保留一个容器存活。
![](https://help.fanruan.com/core/style/lod.png)
#### 3.3.3 对接配置库
1）管理员登录帆软应用，点击「管理系统>管理系统>常规」。  

2）找到「外接数据库」，点击配置。
![](https://help.fanruan.com/core/style/lod.png)
3）选择数据库类型：oracle
4）选择驱动：
数据库版本  
| 说明  
---|---  
11g、12c| 无需调整，选择「oracle.jdbc.driver.OracleDriver」即可  
10g| 选择驱动管理上传ojdbc14.jar时设置的驱动名称  
5）数据库名称、主机、端口、用户名、密码：填写第二章准备的配置库信息即可
6）选择「模式」：
  * 正确填写完上面的所有配置后，点击模式下拉框中的「点击连接数据库」，系统将自动连接该数据库并读取模式
  * 优先选择与数据库用户同名的模式


7）数据连接URL：支持手动编辑调整，支持多种写法，按需选择
类型  
| 写法  
---|---  
Oracle单机| jdbc:oracle:thin:@<host>:<port>:<SID>   
  
Oracle集群| jdbc:oracle:thin:@//<host>:<port>/<service_name>  
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.1)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=x.x.x.2)(PORT=1521)))(LOAD_BALANCE=yes)(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=xxrac)))  
8）选择是否「迁移数据至要启用的数据库」
情况| 新Oracle配置库情况  
  
---|---  
希望使用当前项目原有配置| 1）**必须勾选** 「迁移数据至要启用的数据库」2）项目与该配置库对接成功后，会将**工程原有配置** 数据，迁移到该表空间中3）无论准备的新Oracle表空间中是否有数据，均**会被清空，无法找回**  
希望使用其他项目配置（例如将正式环境配置，拷贝一份给测试环境使用）| 1）自行将准备的配置数据上传到新Oracle表空间中必须确保所准备的数据，对应的项目 JAR 包版本和当前项目的 **JAR 包版本完全一致** ，否则无法使用2）**不勾选** 「迁移数据至要启用的数据库」3）项目与该配置库对接成功后，会使用**表空间中的数据** ，作为项目的配置4）项目原有配置的对接信息，会备份到工程config目录下的db.properties.bak文件中  
9）点击「启用数据库」，提示「迁移成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
#### 3.2.4 确保多应用配置同步（多应用服务工程须完成，单应用服务工程无需）
**1）拷贝db.properties文件**
前往唯一存活的「bi-web」容器所在服务器，复制该组件外挂目录/config文件夹中的db.properties文件。
逐一粘贴到其他「bi-web」容器所在服务器的组件外挂目录/config文件夹中。
![](https://help.fanruan.com/core/style/lod.png)
**2）停止所有应用**
管理员登录运维平台，选中指定项目，点击「维护>组件管理」
请对「bi-web」组件进行一键「停止」，确保所有「bi-web」容器关停至「exited」状态。
![](https://help.fanruan.com/core/style/lod.png)
**3）启动所有应用**
管理员登录运维平台，选中指定项目，点击「维护>组件管理」。
请对「bi-web」组件进行一键「启动」，确保所有「bi-web」容器启动至「running」状态。
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接MySQL实现配置服务](<index.php?doc-view-1249.html>)
[下一篇：FineBI对接SqlServer实现配置服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1251.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
