---
title: TeraData数据连接
doc_id: 310
url: https://help.fanruan.com/finebi/doc-view-310.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:04
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本号功能变动6.0-1.2 应用场景本章我们将介绍如何在 FineBI 中连接 TeraData 数据库。2. 准备工作2.1 版本与驱动下载驱动，并将其上传至 F

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# TeraData数据连接
[__](<doc-edit-310.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[34](<edition-list-310.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本号  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本章我们将介绍如何在 FineBI 中连接 TeraData 数据库。
## 2\. 准备工作
### 2.1 版本与驱动
下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>) 2.1 节。
支持的数据库版本| 选择驱动| 驱动下载  
---|---|---  
抽取版本支持：V16.1、V14.0直连版本支持：V15| com.teradata.jdbc.TeraDriver| [tdgssconfig.jar](<doc-download-/uploads/file/20200713/tdgssconfig.jar> "下载资料")[terajdbc4.jar](<doc-download-/uploads/file/20200713/terajdbc4.jar> "下载资料")  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的主机 IP；
  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：
注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 Tera Data 的图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动切换为自定义，选择 2.1 节上传的驱动，然后输入 2.2 节收集的连接信息。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
URL说明：  
URL 后增加参数 TMODE=ANSI,CHARSET=UTF8，可解决中文乱码、中文过滤不出来等问题。  
4）点击「点击连接数据库」，成功后便可选择需要使用的模式（若不选择则默认使用第一个），最后保存该数据连接，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
## 5\. 注意事项
teradata 表的字段名不能为 value，驱动执行sql select id,value from table 这种会报错，误认为了关键字。(加上""可以执行 sql )
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：SPARK数据连接](<index.php?doc-view-308.html>)
[下一篇：星环Transwarp Inceptor数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-311.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
