---
title: FineDB 数据库简介
doc_id: 1080
url: https://help.fanruan.com/finebi6.X/doc-view-1080.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:03
---

> 1. 概述FineBI&nbsp;系统中除平台属性配置以外的所有信息，包括目录树设置、模板定时任务信息等，均存储于 FineDB 数据库。FineBI 支持使用内置 FineDB 数据库或启用外接 Fi

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineDB 数据库简介
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[9](<edition-list-1080.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2024-03-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineBI 系统中除平台属性配置以外的所有信息，包括目录树设置、模板定时任务信息等，均存储于 FineDB 数据库。
FineBI 支持使用内置 FineDB 数据库或启用外接 FineDB 数据库。
## 2\. 内置数据库
FineBI 工程内置了一个 HSQL 数据库，作为 FineDB 数据库。  

### 2.1 存放位置
FineDB 数据库保存在%BI_Home%\webapps\webroot\WEB-INF\embed文件夹下。如下图所示：
![](/core/style/lod.png)
### 2.2 数据库表内容
FineDB 数据库存储了 FineBI 系统中除平台属性配置以外的所有信息，包括目录树设置、模板定时任务信息等。
FineDB 数据库表内容请参见：[FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>)
### 2.3 数据库文件
文件名| 是否必要| 存放内容  
---|---|---  
db.properties| 必要| 存放 HSQL 数据库的属性  
db.script| 必要| 保存表及数据  
db.lck| 可无| 表示数据库处于打开状态  
db.log| 可无| 文件包含当前数据库的变更  
db.lobs| 可无| 保存某些类型的数据  
db.tmp| 可无| 临时文件目录  
注：全新安装的 FineBI ，仅存在 db.properties、db.script 等必有文件。
若数据库被使用，且表及数据修改了某些属性，其他文件会自动生成。
### 2.4 FineDB 数据连接
注：「内置 FineDB 数据库」为HSQL数据库，使用时会建立内存数据库，数据量大时会占用大量内存。
因此非必要请勿在 FineBI 工程中创建「内置 FineDB 数据库」的数据连接。
用户可在 BI 平台中连接内置 FineDB 数据库。
1）管理员进入 FineBI 系统，点击「管理系统>数据连接>数据连接管理>新建数据连接」，如下图所示：
![](/core/style/lod.png)
2）点击「其他」，选择「其他JDBC」，如下图所示：
![](/core/style/lod.png)
3）填写数据库连接信息，并点击模式下拉框中的「点击连接数据库」按钮，选择「PUBLIC」，如下图所示：
value| 值  
---|---  
数据连接名称| FineDB （用户可自定义）  
驱动器| 输入com.fr.third.org.hsqldb.jdbcDriver  
URL| 输入jdbc:hsqldb:file://${ENV_HOME}/embed/finedb/db注：Windows／Linux／Mac 通用  
用户名| 输入sa  
密码| 无需输入  
模式| 选择PUBLIC  
![](/core/style/lod.png)
3）点击「测试连接」，提示连接成功，如下图所示：
![](/core/style/lod.png)
4）点击右上角「保存」按钮即可。
注：服务器添加 FineDB 数据连接后，务必控制 [数据连接的权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html>)，否则存在被越权访问并修改配置数据库的风险。
## 3\. 外接数据库
HSQL 数据库不能多线程访问，集群环境、数据量较大可能会导致 HSQL 数据库不稳定的情况。因此在企业正式工程中，推荐配置外接数据库。
外接数据库支持的类型和使用方式，请参见：[配置外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-437.html>)  

注1：如需调用外接数据库内的数据进行分析，请根据数据库类型选择合适的数据连接方式。[](<https://help.fanruan.com/finereport/doc-view-2586.html>)
注2：服务器添加 FineDB 数据连接后，务必控制[ 数据连接的权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html>)，否则存在被越权访问并修改配置数据库的风险。   

## 4\. FineDB 表
**1）表结构简介**
FineDB 数据库表内容请参见：[FineDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-819.html>)
**2）表字段修改**
部分配置项无前台修改设置，需要修改 FineDB 数据库表字段来调整配置。
FineDB 数据库中部分字段可通过插件进行修改，详情请参见：[FineDB 常用表字段修改](<https://help.fanruan.com/finereport/doc-view-2471.html>)
禁止直接修改 FineDB 数据库文件，禁止通过第三方软件连接/修改 FineDB 数据库。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：用户中心插件使用说明](<index.php?doc-view-1988.html>)
[下一篇：配置外接数据库 ![](/core/style/forward.png) ](<index.php?doc-view-437.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
