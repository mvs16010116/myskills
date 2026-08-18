---
title: FineBI对接阿里云OSS实现文件服务
doc_id: 1270
url: https://help.fanruan.com/finebi/doc-view-1270.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:38
version: "7.X"
---

> 1. 概述1.1 应用场景手动搭建本地 HDFS 文件系统，对于用户的运维能力要求过高，但用户又希望使用高可用的文件服务器。通过安装「S3 资源仓库」插件，帆软集群可对接支持 S3 协议的云存储文件系统

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接阿里云OSS实现文件服务
[__](<doc-edit-1270.html>)
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[10](<edition-list-1270.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-05-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
手动搭建本地 HDFS 文件系统，对于用户的运维能力要求过高，但用户又希望使用高可用的文件服务器。
通过安装「S3 资源仓库」插件，帆软集群可对接支持 S3 协议的云存储文件系统作为文件服务器。
支持的云存储文件系统包括：阿里云OSS、华为云OBS 、亚马逊云S3。其他自行搭建的 S3 平台不确保支持。
### 1.2 功能简介
本文主要讲解帆软集群与**阿里云对象存储OSS** 的对接：
  * **用户需要自行 购买并准备阿里云对象存储OSS**。****
  * 在部署新项目/项目部署好后，可将项目与该云存储系统对接


## 2\. 帆软应用安装插件（选做）
**对于全新部署项目时，接入阿里云 OSS 作为文件存储，请忽略此章节。**
对于已部署好的工程，如需接入/替换集群文件服务，需要确保工程已安装「S3资源仓库」插件。
点击下载插件：[S3资源仓库插件](<https://market.fanruan.com/plugin/cdb472a9-64ef-4a9d-bbca-baa3cac103c4>)
插件安装方法请参见：[插件管理](<https://help.fanruan.com/finebi/doc-view-459.html>)
## 3\. 准备阿里云OSS
用户需要自行购买并准备阿里云对象存储OSS**。**
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅阿里云官网获取其他帮助。请参见：[阿里云对象存储OSS](<https://help.aliyun.com/zh/oss/?spm=a2c4g.11174283.0.0.2a9c646clbWL2W>)
**如运维能力不足，推荐使用运维平台部署新项目时，**在「文件服务」中勾选「部署MinIO」即可** ，无需手动部署和调优。**
  
|   
|   
  
---|---|---  
1| 购买| 自行购买阿里云对象存储OSS  
2| 创建RAM用户和AccessKey| 1）登录阿里云[RAM 访问控制](<https://ram.console.aliyun.com/users>)2）创建RAM用户点击「身份管理>用户」，点击「创建用户」务必勾选「OpenAPI 调用访问」，以生成AccessKeyId和AccessKeySecret![](https://help.fanruan.com/core/style/lod.png)3）复制AccessKey信息创建成功后，请务必记录下AccessKeyId和AccessKeySecret，下文需要用到后续无法再次查询到对应Secret，只能重新新建![](https://help.fanruan.com/core/style/lod.png)4）分配权限  
勾选该用户，点击「添加权限」为用户分配AliyunOSSFullAccess：管理对象存储服务（OSS）权限![](https://help.fanruan.com/core/style/lod.png)  
3| 创建存储空间和文件目录| 1）登录阿里云[对象存储OSS控制台](<https://oss.console.aliyun.com/bucket>)2）创建Bucket（存储空间）![](https://help.fanruan.com/core/style/lod.png)3）点击进入Bucket，在「文件管理>文件列表」中新建目录用于存储工程文件和工程备份文件示例目录：fanruan![](https://help.fanruan.com/core/style/lod.png)4）点击进入上一节创建的目录，新建两个子目录子目录1：推荐命名为WEB-INF，用于存储工程文件子目录2：必须命名为backup，用于存储工程备份文件![](https://help.fanruan.com/core/style/lod.png)  
## 4\. 上传文件到阿里云OSS（选做）
**对于全新部署项目时，接入阿里云 OSS 作为文件存储，请忽略此章节。**
**对于已部署好的工程，如需接入/替换集群文件服务，需要先将工程文件上传到阿里云OSS存储目录中。**
  * 如当前工程已配置文件服务，请将原文件服务器工程存储目录下的所有文件，拷贝到阿里云OSS准备的工程存储目录。请注意原文件服务器类型是否支持后端拷贝等传输细节（例如minio等S3类型，必须前端下载文件再上传）  

  * 如当前工程未配置文件服务，首次接入文件服务，请将工程某个节点下的以下文件夹拷贝到阿里云OSS存储目录中

阿里云文件夹| 工程文件  
| 文件夹内容说明  
---|---|---  
工程存储目录（一般为WEB-INF）| /webroot/WEB-INF/assets| 存放着以下内容：工程Excel原始文件信息FineReport模板备份文件驱动管理上传的驱动通用的共享持久化目录  
/webroot/WEB-INF/dpworks| FineDataLink任务相关的配置文件如不存在该文件夹，说明工程没有使用FDL相关功能，可忽略  
/webroot/WEB-INF/reportlets| FineReport模板存放目录  
/webroot/WEB-INF/resources| 存放工程相关的资源配置文件  
/webroot/WEB-INF/schedule| 定时调度生成的文件  
/webroot/WEB-INF/treasures| 云端运维生成的数据包  
backup| /webroot/backup| 工程历史备份文件  
## 5\. 准备阿里云OSS信息
配置项  
| 说明  
---|---  
协议| S3  
BucketEndpointRegion| **配置项说明：** Bucket：存储空间，用于存储对象的容器Endpoint：OSS对外服务的访问域名Region：OSS的数据中心所在物理位置。**注意不包含前缀的Bucket，例如示例的Region最终值为：oss-cn-shanghai.aliyuncs.com****获取方式：**  
1）登录阿里云[对象存储OSS控制台](<https://oss.console.aliyun.com/bucket>)2）点击「Bucket列表」，点击工程文件所在Bucket3）点击「概览」，即可查看到相关信息![](https://help.fanruan.com/core/style/lod.png)  
AccessKeyIdAccessKeySecret| **配置项说明：** AccessKey是阿里云提供给用户的永久访问凭据
  * AccessKeyId：用于标识用户
  * AccessKeySecret：是一个用于验证你拥有该AccessKey ID的密码

**获取方式：**  
推荐新建RAM用户并配置AccessKey（上文创建RAM用户时已记录相关信息）如果遗失这个 AccessKey，只能创建新的来替代，如何创建：[创建AccessKey](<https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair?spm=a2c4g.11186623.0.0.2e4baf15tVX9j6>)  
路径| 文件服务的根目录名称，即存储工程文件的目录完整地址本示例为**fanruan/WEB-INF/** 注1：「路径」必须以「/」结尾，开头不能加「/」。注2：「路径」不能是相对路径。  
PathStyleAccess| 访问OSS存储桶时，URL的路径结构，**一般情况下无需配置**  

  * false：默认值，虚拟主机样式，存储桶名称为主机名的一部分，这种方式是阿里云OSS的推荐访问方式，通常用于生产环境中
  * true：路径样式，存储桶名称为路径的一部分，如集群对接OSS时，出现证书或unknownhost相关报错，可调整为true

  
signerOverride| 允许用户指定请求签名的算法或版本，**一般情况下无需配 置**如集群对接OSS时，出现证书或unknownhost相关报错，可调整为S3SignerType  
## 6\. 集群接入文件服务
支持在以下情况下接入阿里云对象存储 OSS 作为集群文件服务，请根据情况自行选择，任选其一即可。
### 6.1 部署新集群时接入
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的阿里云对象存储 OSS 作为集群文件服务。
此情况下，请确保运维平台版本在**V2.24.0** 及以上。
此情况下，请确保准备的工程存储目录文件夹中内容为空，不存在任何数据，否则可能无法成功对接。
1）文件服务选择「对接已有文件服务」。
![](https://help.fanruan.com/core/style/lod.png)
2）在「文件服务」信息填写处
  * 协议：S3
  * 输入第五章准备的相关信息****


3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 6.2 运维平台集群管理接入
项目部署成功后，在运维平台的「集群管理」中，可为项目接入阿里云对象存储 OSS 作为文件服务。
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「文件服务器」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
3）输入第五章准备的相关信息
4）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 6.3 管理系统集群管理接入
在帆软应用的「管理系统>集群管理」中，可为项目接入阿里云对象存储 OSS 作为文件服务。
1）管理员登录帆软应用，点击「管理系统>智能运维>集群配置」。
2）在开启了状态服务器的前提下，在文件一致设置中选择「文件服务器共享」。
3）点击「编辑」填写第五章准备的相关信息。
4）点击「测试连接并保存」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接NAS实现文件服务](<index.php?doc-view-1580.html>)
[下一篇：FineBI对接华为云OBS实现文件服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2676.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
