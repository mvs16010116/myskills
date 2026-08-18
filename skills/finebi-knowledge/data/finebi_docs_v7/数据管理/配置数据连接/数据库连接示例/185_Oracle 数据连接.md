---
title: Oracle 数据连接
doc_id: 185
url: https://help.fanruan.com/finebi/doc-view-185.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:52
version: "7.X"
---

> 1.&nbsp;概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 Oracle 数据库。2. 准备工作2.1 版本和驱动&nbsp;支持的数据库版本驱动包下载Orac

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Oracle 数据连接
[__](<doc-edit-185.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[67](<edition-list-185.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何连接 Oracle 数据库。  

## 2\. 准备工作
### 2.1 版本和驱动
支持的数据库版本| 驱动包下载  
---|---  
Oracle 11.1Oracle 11.2 / 11g-R2Oracle 12.1 / 12c-R1Oracle 12.2 / 12c-R2Oracle 13 及以上Oracle 19c| 已内置，无需下载  
  
Oracle 9.2.0 / 9iOracle 10.1Oracle 10.2 / 10g-R2| [ojdbc14.jar](<doc-download-/finebi5.1/uploads/file/20220105/ojdbc14.jar> "下载资料")上传驱动包的具体步骤可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>)  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 Oracle 数据库，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）输入 2.2 节的连接信息。若驱动是内置的，选择「默认」；若驱动是自己上传的，可以选择「自定义」，勾选自己要的驱动。
模式需要连接数据库后才可以选择，所以需要先点击「点击连接数据库」后，再选择「模式」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注：连接多模式的数据库时使用 SQL 语句需要带上模式名前缀进行搜索，例如 SELECT * FROM "ABBY"."FR_S_UEP"
驱动、数据库名称、URL 的介绍如下表所示：
驱动| DatabaseName  
| URL  
---|---|---  
oracle.jdbc.driver.OracleDriver | sid_name| jdbc:oracle:thin:@ip:port:sid_name  
service_name| jdbc:oracle:thin:@//ip:port/service_name 或者jdbc:oracle:thin:@ip:port/service_name  
TNSName注：Oracle 安装路径下需要有 tnsnames.ora 文件| jdbc:oracle:thin:@TNSName  
TNSName 说明如下：
jdbc:oracle:thin:@TNSName URL 中，TNSName 的值为tnsnames.ora文件中 ORCL 的值，如下图所示：
![1613723315446537.png](https://help.fanruan.com/core/style/lod.png)
完整的 URL 为：jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST =(ADDRESS=(PROTOCOL=TCP)(HOST =localhost)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
[](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)
## 5\. 注意事项
  * **在 Oracle 9i 版本中，精度为 0 的字段值会被识别成文本而不是数值「该字段值用** column.getSize()**计算得到的是 38 ，所以会被识别成文本属性」；其他版本的 Oracle 未有此现象出现。**
  * BI 平台 Oracle 连接池的连接在一段时间没有使用会自动释放。之所以在查看连接池时有之前的连接，是因为后面用户连接时又重新启用了连接，所以不会因为连接一直得不到释放而造成问题。
  * 若 Oracle 中的字段名包含特殊值（例如：date#$%?/2"），可能会导致自助数据集选字段的时候出现如下图报错。这时需要用户更换使用驱动 ojdbc14 来连接数据库，操作方式可参见本文 2.1 节。


![46.png](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：DERBY数据连接](<index.php?doc-view-96.html>)
[下一篇：Amazon Redshift数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-292.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
