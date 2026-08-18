---
title: 阿里云MaxCompute数据连接
doc_id: 1127
url: https://help.fanruan.com/finebi/doc-view-1127.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:49
version: "7.X"
---

> 1. 概述1.1 版本&nbsp;FineBI 版本功能变动7.0-1.2 简介MaxCompute（之前称为 ODPS），是阿里巴巴通用计算平台提供的一种快速、完全托管的 GB/TB/PB 级数据仓库

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 阿里云MaxCompute数据连接
[__](<doc-edit-1127.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[38](<edition-list-1127.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-10-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
7.0| -  
  
### 1.2 简介
MaxCompute（之前称为 ODPS），是阿里巴巴通用计算平台提供的一种快速、完全托管的 GB/TB/PB 级数据仓库解决方案，现在已更名为 MaxCompute，MaxCompute 向用户提供了完善的数据导入方案以及多种经典的分布式计算模型，能够更快速的解决用户海量数据计算问题，有效降低企业成本，并保障数据安全。
本文介绍如何连接 MaxCompute 数据库。
## 2\. 准备工作
### 2.1 版本和驱动
1）下载驱动；
2）下载日志jar压缩包并解压；
3）将数据库驱动和日志jar文件，同时上传至FineBI。如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi/doc-view-1540.html>) 2.1 节。
配置  
| 说明  
---|---  
数据库版本| V3.2.7 以上  
驱动| com.aliyun.odps.jdbc.OdpsDriver  
URL| jdbc:odps:<maxcompute_endpoint>?project=<maxcompute_project_name>  
URL 解释：[JDBC参考使用说明](<https://help.aliyun.com/document_detail/161246.html?spm=a2c4g.11186623.6.1039.713e64e4J1G6nk>)
  * **< maxcompute_endpoint>**：MaxCompute 服务所在区域的 Endpoint。例如，华东1（杭州）区域的外网Endpoint为http://service.cn-hangzhou.maxcompute.aliyun.com/api；
  * **< maxcompute_project_name>**：MaxCompute项目空间名称。

  
数据库驱动  
| [odps-jdbc-3.2.8-jar-with-dependencies.jar](<doc-download-/finebi/uploads/file/20251023/odps-jdbc-3.2.8-jar-with-dependencies.jar> "下载资料")  
日志JAR| [日志jar.zip](<doc-download-/finebi/uploads/file/20251023/日志jar.zip> "下载资料")  
2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * **< maxcompute_endpoint>**：MaxCompute 服务所在区域的 Endpoint
  * **< maxcompute_project_name>**：MaxCompute项目空间名称  

  * 数据库的用户名和密码；
  * 需要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 MaxCompute 图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，然后输入 2.2 节的连接信息。
点击「点击连接数据库」连接成功后，便可以选择模式，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注1：用户可以选择性修改高级设置，详细请参见 [配置数据连接](<https://help.fanruan.com/finebi7.0/doc-view-94.html>) 第 4 节
4）测试连接成功后，点击「保存」保存该数据连接。
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表到 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
## 5\. MaxCompute使用说明
### 5.1 官方文档
MaxCompute官方文档：[MaxCompute阿里云官方文档](<https://help.aliyun.com/product/27797.html>)
DataWorks 官方文档：[DataWorks阿里云官方文档](<https://help.aliyun.com/product/72772.html?spm=a2c4g.11186623.6.540.9a445808H9pB8P>)
用户可以使用 DataWorks 对 MaxCompute 进行可视化管理。
### 5.2 快速查询（MCQA）
MaxCompute 的快速查询功能：
  * 可以对中、小数据量查询作业进行加速优化，将执行时间为分钟级的查询作业缩减至秒级，同时完全兼容原 MaxCompute 的查询功能。
  * MCQA 支持将主流BI工具或SQL客户端连接至 MaxCompute 项目，开展即席查询（Ad Hoc）或商业智能（BI）分析。
  * MCQA 使用独立的资源池，不占用配额组，可以自动识别查询作业，缓解排队压力，优化使用体验。


**如何在 FineBI 中启用计算查询（MCQA）**
在 2.1 节的 URL 后面增加&interactiveMode=true
注：若使用加速参数，数据量超过100w限制时，需要加参数 autoSelectLimit=1000000000。
详细请参见：[加速查询使用说明](<https://help.aliyun.com/document_detail/180702.html?spm=a2c4g.11186623.6.792.614d1538mdKYaG>)
### 5.3 表有分区时 FineBI 如何取数
在 MaxCompute 中，如果一张表添加了分区，就不能在 FineBI 中直接通过添加「数据库表」来进行取数，而是使用「SQL数据集」。
例如，MaxCompute 中有一张表「test」，有两个分区「A、B」。添加「SQL数据集」，输入语句：select * from test where fenqu = A 进行取数。
![image.png](https://help.fanruan.com/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：阿里云AnalyticDB数据连接](<index.php?doc-view-291.html>)
[下一篇：APACHE KYLIN数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-95.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
