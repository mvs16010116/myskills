---
title: 阿里云Hologres数据连接
doc_id: 1347
url: https://help.fanruan.com/finebi/doc-view-1347.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:07
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-7.0.11「连接池设置」中新增「初始化SQL」设置项，可配置初始化 SQL 语句1.2 功能简介Hologres是阿里巴巴自主研发的一款交互式分

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 阿里云Hologres数据连接
[__](<doc-edit-1347.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[21](<edition-list-1347.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2026-07-02 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
7.0.11| 「连接池设置」中新增「初始化SQL」设置项，可配置初始化 SQL 语句  
### 1.2 功能简介
Hologres是阿里巴巴自主研发的一款交互式分析产品，兼容 PostgreSQL 11协议，与大数据生态无缝连接，支持高并发和低延时地分析处理PB级数据。
Hologres致力于低成本和高性能地大规模计算型存储和强大的查询能力，为您提供海量数据的实时数据仓库解决方案和实时交互式查询服务。
## 2\. 连接前准备
### 2.1 数据库版本与驱动
驱动下载| 驱动  
---|---  
请根据数据库版本从 [官网](<https://central.sonatype.com/artifact/org.postgresql/postgresql/versions>) 下载对应插件| org.postgresql.Driver  
数据连接 URL 格式：jdbc:postgresql://instance-id-region-endpoint-internal.hologres.aliyuncs.com:port/dbname
### 2.2 准备工作
1）下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html>) 2.1 节。驱动上传界面如下图所示，上传成功后点击保存。
![](https://help.fanruan.com/core/style/lod.png)
2）在连接数据库之前，请收集以下信息：  

  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接步骤
1）管理员BI，选择「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，在「全部」选项下选择「Hologres」，如下图所示：
注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接控制](<https://help.fanruan.com/finebi7.0/doc-view-488.html>)
![](https://help.fanruan.com/core/style/lod.png)
2）选择「Hologres」数据库，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）按照前面提供的配置信息，输入数据库的对应信息，可选择填入高级设置信息（相关介绍可参考[配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html>)），如下图所示：
7.0.11 及之后版本，「连接池设置」中新增「初始化SQL」设置项，可配置初始化 SQL 语句；详情请参见：[配置数据连接入门](<https://help.fanruan.com/finebi/doc-view-94.html>)
![1625193484831516.png](https://help.fanruan.com/core/style/lod.png)
4）点击测试连接，或者在模式下点击连接数据库，若测试连接成功则表示成功连接上数据库，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI 
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：[直连]Kyligence企业版数据连接](<index.php?doc-view-1169.html>)
[下一篇：JSON 数据集插件 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-489.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
