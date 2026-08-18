---
title: INFORMIX数据连接
doc_id: 99
url: https://help.fanruan.com/finebi/doc-view-99.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:45
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-6.0.9适配直连数据1.2 应用场景本文将介绍如何连接 Infromix 数据源。2. 准备工作2.1 版本和驱动下载驱动包，并将其上传至 Fi

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# INFORMIX数据连接
[__](<doc-edit-99.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[22](<edition-list-99.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0  
| -  
  
6.0.9| 适配直连数据  
  
### 1.2 应用场景
本文将介绍如何连接 Infromix 数据源。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动包，并将其上传至 FineBI 中，如何上传详情可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html?source=4>)
支持的| 驱动下载   
---|---  
V11.7、V11.5  
| [ifxjdbc_informix.jar](<doc-download-/finebi5.1/uploads/file/20211209/ifxjdbc_informix.jar> "下载资料")  
2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 INFORMIX 数据源，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）输入 2.2 节的连接信息，驱动由于是内置的，选择「默认即可」
模式需要连接数据库后才可以选择，所以需要先点击「点击连接数据库」后，再选择「模式」，如下图所示：
「数据库名称」的输入格式为 数据库名称:INFORMIXSERVER=服务器名
![](https://help.fanruan.com/core/style/lod.png)
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：达梦DM数据连接](<index.php?doc-view-1712.html>)
[下一篇：Apache Phoenix数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-294.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
