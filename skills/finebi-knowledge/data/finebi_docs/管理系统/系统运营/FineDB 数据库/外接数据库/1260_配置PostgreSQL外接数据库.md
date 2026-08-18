---
title: 配置PostgreSQL外接数据库
doc_id: 1260
url: https://help.fanruan.com/finebi6.X/doc-view-1260.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:12
---

> 1.&nbsp;概述1.1&nbsp;版本FineBI服务器版本功能变更6.0-6.0.18FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除&nbsp

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 配置PostgreSQL外接数据库
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[17](<edition-list-1260.html>)
* 最近更新：[Tracy.Wang](<user-space-2679113.html>) 于 2024-09-04 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本| 功能变更  
---|---  
6.0| -  
6.0.18| FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除 postgresql 相关驱动用户如需使用相关数据连接（postgresql、华为DWS等），必须确保已通过驱动管理手动上传相关驱动。  
### 1.2 功能简介
BI 系统配置外接数据库后，遇到集群环境或数据量较大情况时，可保证 BI 系统的稳定性。
用户可通过安装「PostgreSQL外置数据库」插件，在数据决策系统中配置 PostgreSQL 类型的外接数据库。
注：若配置了外接数据库，请勿轻易修改外接数据库的用户名和密码，否则会导致工程启动失败。
如需修改，请参照：[修改外接数据库账号密码](<https://help.fanruan.com/finebi6.0/doc-view-1332.html>) 。
### 1.3 注意事项
若工程配置了虚拟目录，即：[Tomcat 下通过 IP 直接访问数据决策系统](<https://help.fanruan.com/finebi6.0/doc-view-903.html>)，在安装插件前，需要修改服务器配置文件。
打开%tomcat_home%\conf\server.xml文件，修改reloadable=false，如下图所示：
![](/core/style/lod.png)
## 2\. 数据库配置
准备将平台数据要迁移到的数据库，建议用户新建一个空的数据库（数据库大小请参考本文 2.2 节）。
注：不同 FineBI 工程，不可共用同一个外接数据库，否则数据可能会出现错乱。
### 2.1 数据库版本
外接数据库支持的类型及版本如下表所示：
PostgreSQL外置数据库插件版本| 数据库类型  
| 数据库版本  
---|---|---  
V1.0| PostgreSQL| 9.2.3、9.4.7、9.5.0、9.5.2、9.6.0  
V1.0.3| PostgreSQL| 9.2.3、9.4.7、9.5.0、9.5.2、9.6.0、13.0  
FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除 postgresql 相关驱动  

  

用户如需使用相关数据连接（postgresql、华为DWS等），必须确保已通过驱动管理手动上传相关驱动。
请下载最新驱动：[Postgresql驱动](<https://jdbc.postgresql.org/>) ，并将其上传至 FineBI 中，如何上传详情可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html?source=4>) 2.1 节
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
  

## 3\. 配置外接数据库
### 3.1 安装插件
点击下载插件：[PostgreSQL外置数据库](<https://market.fanruan.com/plugin/909bce9a-542f-487e-9a99-c531e22f55d0>)
插件安装方法请参照：[插件管理](<https://help.fanruan.com/finebi6.0/doc-view-459.html> "插件管理")[](<http://help.finereport.com/doc-view-2220.html>)
### 3.2 外接数据库配置入口
管理员登录数据决策系统，点击「管理系统>系统管理>常规>外接数据库」，如下图所示：
![](/core/style/lod.png)
### 3.3 配置外接数据库
进入到外接数据库配置界面后，选择数据库类型，输入实际数据库相应的信息即可。如下图所示：
![](/core/style/lod.png)
#### 3.3.1 设置项
各设置项说明如下表所示：
设置项| 说明  
---|---  
数据库类型| 选择 postgresql  
驱动| 无需修改，会自动配置  
数据库名称| 第二章新建的数据库名称禁止与其他工程共用数据库，建议新建数据库数据库名称只允许包含数字、字母、下划线和「.」  
用户名/主机/密码/端口| 根据本地数据库实际情况填写主机名称只允许包含数字、字母、下划线、「-」和「.」用户需要具备 create、delete、alter、update、select、insert、index 权限  
模式| 仅支持下拉选择模式正确填写完上面几项设置后，点击模式下拉框中的「点击连接数据库」，系统将自动连接该数据库并读取模式，选择即可（尽量选择和数据库用户的名字相同的模式）![](/core/style/lod.png)  
注1：若提示数据库连接失败，请检查上面几项设置。注2：模式名称不支持大写，若新建模式，请使用小写  
#### 3.3.2 迁移数据至要启用的数据库
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
[![](/core/style/back.png)上一篇：配置DB2外接数据库](<index.php?doc-view-1252.html>)
[下一篇：外接数据库配置常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-529.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
