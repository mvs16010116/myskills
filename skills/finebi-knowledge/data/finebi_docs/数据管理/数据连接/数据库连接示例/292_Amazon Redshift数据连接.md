---
title: Amazon Redshift数据连接
doc_id: 292
url: https://help.fanruan.com/finebi6.X/doc-view-292.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:17
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何在 FineBI 中连接 Amazon Redshift 数据库。2. 准备工作2.1 版本和驱动下载驱动，并将其上

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Amazon Redshift数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[14](<edition-list-292.html>)
* 最近更新：[帆软用户aEcMI0N7Gz](<user-space-3206309.html>) 于 2025-06-04 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何在 FineBI 中连接 Amazon Redshift 数据库。  

## 2\. 准备工作
### 2.1 版本和驱动
下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html>) 2.1 节。
驱动包下载| 选择驱动  
---|---  
[RedshiftJDBC41.jar](<doc-download-/uploads/file/20200713/RedshiftJDBC41.jar> "下载资料")| com.amazon.redshift.jdbc4.Driver 或com.amazon.redshift.jdbc41.Driver  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的终端地址和端口号；
  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi6.0/doc-view-488.html?source=4>)
![](/core/style/lod.png)
2）找到 Amazon Redshift 图标，如下图所示：
![](/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。
![](/core/style/lod.png)
注：用户可以选择性修改高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi6.0/doc-view-94.html>) 4.3 节
4）点击「点击连接数据库」，成功后便可选择需要使用的模式（若不选择则默认使用第一个），最后保存该数据连接，如下图所示：
![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
## 5\. 注意事项
**问题现象：  
**
发现 DB 里面少了部分数据表。
**原因说明：  
**
简单来说，数据库表可以分 2 类：  
1）标准的 Table/View：这类表 FineBI 可以直接通过 DB 表取到；  
2）External Table：这类表 FineBI 无法通过 DB 表取到，但是可以通过 SQL 表来取（直接写 SQL 取）。
DB 里缺少的这些表大概率是 External Table（不是标准的 Table/View），然后 FineBI 的 DB 表只对应标准的 Tabel/View ，所以DB里会少表。
****解决方案** ：**
可以通过 SQL 表来取数据表（直接写 SQL 取）。
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Oracle 数据连接](<index.php?doc-view-185.html>)
[下一篇：Postgresql数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-290.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
