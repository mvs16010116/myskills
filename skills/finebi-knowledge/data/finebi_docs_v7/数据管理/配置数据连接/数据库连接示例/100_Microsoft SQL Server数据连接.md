---
title: Microsoft SQL Server数据连接
doc_id: 100
url: https://help.fanruan.com/finebi/doc-view-100.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:47
version: "7.X"
---

> 1.&nbsp;概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 Microsoft SQL Server 数据库。2. 准备工作2.1 版本和驱动下载对应的驱动包，

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Microsoft SQL Server数据连接
[__](<doc-edit-100.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[30](<edition-list-100.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0  
| -  
  
### 1.2 应用场景
本文将介绍如何连接 Microsoft SQL Server 数据库。
## 2\. 准备工作
### 2.1 版本和驱动
下载对应的驱动包，如何上传驱动包可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html?source=4>)  

支持的数据库版本| 驱动包下载   
---|---  
SQL Server 2000  
|  [sqljdbc.zip](<doc-download-/uploads/file/20200413/sqljdbc.zip> "下载资料")  
  
SQL Server 2005SQL Server 2008SQL Server 2012SQL Server 2014SQL Server 2016|  已内置无需下载  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）选择「Microsoft SQL Server」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）输入 2.2 节的连接信息，驱动由于是内置的，选择「默认即可」。
模式需要连接数据库后才可以选择，所以需要先点击「点击连接数据库」后，再选择「模式」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注1：用户若是想要连接非默认实例，可以更改「数据连接URL」，有两种方式：
  * jdbc:sqlserver://ip;instanceName=实例名;databaseName=数据库名
  * jdbc:sqlserver://ip\实例名;databaseName=数据库名


注2：连接多模式的数据库时使用 SQL 语句需要带上模式名前缀进行搜索，例如 SELECT * FROM [dbo].[asdfg]
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
## 5\. 注意事项
### 5.1 常见问题
若数据库查询速度慢可参考文档：[SQL Server查询速度较慢](<https://help.fanruan.com/finereport/doc-view-300.html>)
数据库报错可参考文档：[SQL Server 数据连接常见错误解决方案](<https://help.fanruan.com/finereport/doc-view-306.html>)
对于特殊场景的参考文档：[SQLSERVER多实例名情况建立数据链接](<https://help.fanruan.com/finereport/doc-view-2880.html>)
### 5.2 decimal 数据类型注意点
若在数据库中，字段类型为的 decimal，保留一位小数且小数为 0 时，在 FineBI 中预览时会直接显示成整数。  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：ClickHouse 数据连接](<index.php?doc-view-1102.html>)
[下一篇：阿里云AnalyticDB数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-291.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
