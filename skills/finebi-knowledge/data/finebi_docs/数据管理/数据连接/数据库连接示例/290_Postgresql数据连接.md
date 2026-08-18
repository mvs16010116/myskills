---
title: Postgresql数据连接
doc_id: 290
url: https://help.fanruan.com/finebi6.X/doc-view-290.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:17
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-6.0.18FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除&nbsp;postgresql

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Postgresql数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[20](<edition-list-290.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-05-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
6.0.18| FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除 postgresql 相关驱动用户如需使用相关数据连接（postgresql、华为DWS等），必须确保已通过驱动管理手动上传相关驱动  
### 1.2 应用场景
本文将介绍如何连接 PostgreSQL 数据库。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动包，并将其上传至 FineBI 中，如何上传详情可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html?source=4>) 2.1 节
支持的数据库版本  
| 驱动包下载  
---|---  
postgresql_9.2.3；9.4.7；9.5.0；9.5.2；9.6.0；12| [Postgresql驱动](<https://jdbc.postgresql.org/>) 请下载最新驱动  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，选择「PostgreSQL」，如下图所示：
注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限控制](<https://help.fanruan.com/finereport/doc-view-2457.html>)
![1.png](/core/style/lod.png)
2）输入 2.2 节的连接信息。驱动选择「自定义」，并勾选 2.1 节上传的驱动。
模式需要连接数据库后才可以选择，所以需要先点击「点击连接数据库」后，再选择「模式」，如下图所示：
![20.png](/core/style/lod.png)
3）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![5.png](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：Amazon Redshift数据连接](<index.php?doc-view-292.html>)
[下一篇：Gbase 8A数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-295.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
