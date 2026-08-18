---
title: MinIO资源仓库插件
doc_id: 2021
url: https://help.fanruan.com/finebi6.X/doc-view-2021.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:45
---

> 1.&nbsp;概述1.1 版本FineBI服务器版本6.01.2&nbsp;应用场景MinIO 是一款高性能、分布式的对象存储系统，用户希望使用MinIO作为文件服务器。1.3&nbsp;功能简介用户

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# MinIO资源仓库插件
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[2](<edition-list-2021.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-11-29 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
---  
6.0  
### 1.2 应用场景
MinIO 是一款高性能、分布式的对象存储系统，用户希望使用MinIO作为文件服务器。
### 1.3 功能简介
用户可通过安装「MinIO资源仓库」插件，使用MinIO存储系统作为文件服务器。
## 2\. 操作步骤
### 2.1 安装插件
点击下载插件：[MinIO资源仓库插件](<https://market.fanruan.com/plugin/7e74a2a2-e265-4e6c-addb-281f94053d32>)
插件安装方法请参见：[插件管理](<https://help.fanruan.com/finebi6.0/doc-view-459.html>)
### 2.2 集群环境准备
在配置 MinIO 文件服务器之前请准备集群环境，具体可参见： [集群环境准备](<https://help.fanruan.com/finereport/doc-view-2642.html>)
### 2.3 配置文件服务器
1）将主节点工程的%BI_HOME%\webapps\webroot\WEB-INF文件夹拷贝到文件服务器中，拷贝后 WEB-INF 所在文件夹需要赋予权限，Linux 系统中为 777 权限。  

2）管理员进入FineBI系统，点击「管理系统>智能运维>集群配置>文件服务共享」，如下图所示：
![](/core/style/lod.png)
选择MinIO协议时，界面如下图所示：
![](/core/style/lod.png)
各设置项介绍如下表所示：
设置项| 说明  
---|---  
Endpoint| MinIO地址，形如http://ip:port  
AccessKeyId| MinIO账号  
AccessKeySecret| MinIO密码  
Bucket| MinIO文件桶名称  
路径| MinIO文件夹地址  
### 2.4 测试连接并保存
点击「测试连接并保存」，提示连接成功，如下图所示：
![](/core/style/lod.png)  

注：配置集群的后续步骤请参见：[配置开启集群](<https://help.fanruan.com/finereport/doc-view-2443.html#5>)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：集群项目对接SFTP](<index.php?doc-view-1567.html>)
[下一篇：HDFS资源仓库插件 ![](/core/style/forward.png) ](<index.php?doc-view-1234.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
