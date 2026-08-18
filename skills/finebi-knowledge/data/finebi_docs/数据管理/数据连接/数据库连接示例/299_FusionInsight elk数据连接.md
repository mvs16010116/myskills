---
title: FusionInsight elk数据连接
doc_id: 299
url: https://help.fanruan.com/finebi6.X/doc-view-299.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:21
---

> 1. 概述1.1 版本FineBI&nbsp;功能变动6.0-1.2 应用场景本文将介绍 FineBI 如何连接 FusionInsight elk 数据库。注：该数据库不支持使用直连属性的数据表2.

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FusionInsight elk数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[17](<edition-list-299.html>)
* 最近更新：[帆软用户aEcMI0N7Gz](<user-space-3206309.html>) 于 2025-06-04 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI   
| 功能变动  
---|---  
6.0  
| -  
  
### 1.2 应用场景
本文将介绍 FineBI 如何连接 FusionInsight elk 数据库。
注：该数据库不支持使用直连属性的数据表
## 2\. 连接前准备
### 2.1 数据库版本和驱动
支持的数据库版本  
| 驱动包下载| 驱动  
---|---|---  
V100R002C80| [postgresql](<https://helpfile.obs.cn-east-3.myhuaweicloud.com/%E9%A9%B1%E5%8A%A8/postgresql-42.1.4.jar>)| org.postgresql.Driver  
### 2.2 收集连接信息
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.X/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：  

  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 若是用户名密码认证，需要收集用户名和密码；若是 Kerberos 认证，需要收集客户端 principal 和 keytab 密钥路径；


## 3\. 具体连接步骤
1）登录 FineBI ，选择「管理系统>数据连接」，点击「新建数据连接」。如下图所示：
![](/core/style/lod.png)
2）选择「所有」，找到 FusionInsight elk 数据库，如下图所示：
![](/core/style/lod.png)
3）输入 2.2 节收集的连接信息，如下图所示：
Kerberos 认证方式详情可参见：[数据连接 kerberos 认证](<https://help.fanruan.com/finebi6.0/doc-view-282.html>)
![](/core/style/lod.png)
4）点击「点击连接数据库」，可以测试是否连接成功。连接成功后，用户可以选择需要的数据库模式，并点击保存。如下图所示：
![](/core/style/lod.png)
## 4\. 添加数据库的表到 FineBI 
有两种方式可以将 FusionInsight elk 数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：TiDB数据连接](<index.php?doc-view-1640.html>)
[下一篇：Doris数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-1688.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
