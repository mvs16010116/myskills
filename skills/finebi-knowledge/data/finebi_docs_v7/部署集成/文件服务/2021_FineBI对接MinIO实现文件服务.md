---
title: FineBI对接MinIO实现文件服务
doc_id: 2021
url: https://help.fanruan.com/finebi/doc-view-2021.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:39
version: "7.X"
---

> 1. 概述MinIO是一个灵活而强大的对象存储服务器，旨在提供高性能、可扩展和易于部署的分布式存储系统。在帆软集群项目中，文件服务器用于存储和共享集群中所需的文件和数据资源，以确保每个节点都可以访问并使

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接MinIO实现文件服务
[__](<doc-edit-2021.html>)
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
* 历史版本：[4](<edition-list-2021.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
MinIO是一个灵活而强大的对象存储服务器，旨在提供高性能、可扩展和易于部署的分布式存储系统。
在帆软集群项目中，文件服务器用于存储和共享集群中所需的文件和数据资源，以确保每个节点都可以访问并使用它们。  

本文主要讲解帆软集群项目如何对接MinIO，作为集群文件服务：
  * 用户可**自行准备一个MinIO** ，并进行参数调优
  * 在项目部署好后，可将项目与该文件服务器对接


![icon](https://help.fanruan.com/core/style/lod.png)提示:
MinIO使用的是S3协议，有着独特的文件存储逻辑。
请勿直接使用FileZilla等FTP工具连接MinIO，进行文件的上传/下载。
请通过浏览器访问MinIO服务器的地址，然后使用提供的Web界面进行文件的上传和下载。
详情请参见：[MinIO文件服务器简介](<https://help.fanruan.com/fineops/doc-view-110.html>)  

## 2\. 准备文件服务器
用户需要自行准备并部署MinIO。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅相关官网获取其他帮助。
**如运维能力不足，推荐使用运维平台部署新项目时，在「文件服务」中勾选「部署MinIO」即可，无需手动部署和调优。**
### 2.1 服务器配置
配置类型| 最低配置| 推荐配置  
---|---|---  
服务器数量| 所准备的服务器，仅用于部署该集群项目的负载均衡、状态服务、文件服务、配置库组件| 所准备的服务器，仅用于部署文件服务  
物理内存| 8G| 16G  
CPU| 2.5GHz以上8核16线程| 2.5GHz以上16核32线程  
磁盘类型| -| 磁盘类型**推荐** 是**XFS**  
可用磁盘空间| 500G~1T其中根目录可用磁盘不可小于40G后续请根据使用情况扩展| 1T~2T其中根目录可用磁盘不可小于80G后续请根据使用情况扩展  
网络要求| 1）文件服务和应用工程、其他组件建议在同一网段，避免网络波动等问题2）文件服务和应用工程、其他组件如处于公网环境，带宽需在10M以上3）文件服务和应用工程、其他组件之间需要网络畅通，互相端口可访问  
### 2.2 部署MinIO及准备MinIO信息
用户需要自行准备并部署MinIO。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅相关官网获取其他帮助。
本文基于[MinIO官方部署指南](<https://www.minio.org.cn/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-single-drive.html#>)，对必要对接信息的获取进行指明。
信息  
| 说明  
---|---  
Endpoint| MinIO API 访问地址，
  * 格式：http://IP:port 或 https://IP:port
  * IP：MinIO 所在服务器的 IP 或域名  

  * port：MinIO 的 API 端口，默认为 9000 。

如自定义 API 端口，一般是在 /etc/default/minio 创建的环境变量文件中，设置的 MINIO_OPTS 的 --address 值（注意不是 --console-address 值，--console-address 是控制台端口）![](https://help.fanruan.com/core/style/lod.png)  
AccessKeyId| MinIO管理员名称即在/etc/default/minio创建的环境变量文件中，设置的MINIO_ROOT_USER的值![](https://help.fanruan.com/core/style/lod.png)  
  
AccessKeySecret| MinIO管理员密码即在/etc/default/minio创建的环境变量文件中，设置的MINIO_ROOT_PASSWORD的值![](https://help.fanruan.com/core/style/lod.png)  
  
## 3\. 准备文件存储路径
用户需要准备一个目录，用于存储工程文件和工程备份文件。并确保上文的MinIO管理员有该目录的读写执行权限。
### 3.1 登录MinIO控制台
用户需要通过浏览器访问 MinIO 服务器的地址，然后使用提供的 Web 界面进行文件的上传和下载。
**1）在浏览器窗口访问 MinIO 的 Console 控制台**
地址形如：http://IP:port 或 https://IP:port
  * IP：MinIO 所在服务器的 IP 或域名  

  * port：MinIO 的控制台端口，默认为 9001 。


如自定义控制台端口，一般是在 /etc/default/minio 创建的环境变量文件中，设置的 MINIO_OPTS 的 --console-address 值（注意不是 --address 值，--address 是 API 端口）
![](https://help.fanruan.com/core/style/lod.png)
**2）输入管理员账号密码**
账号密码为 2.2 节获取的 MinIO 管理员账号和密码。
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 新建Bucket存储桶
MinIO 对象存储使用 Bucket 来组织对象。 Bucket 存储桶类似于文件系统中的顶级驱动器、文件夹或目录。
1）在 MinIO 控制台，点击左侧导航栏的「Buckets」，点击「Create Bucket」按钮。
2）输入桶名称，示例为「fanruan」，点击「Create Bucket」完成创建。
注1：用户可通过左侧导航栏的「Identity」为管理员分配桶权限，本文不做演示。
请确保 2.2 节准备的 MinIO 管理员有该桶的增删读写权限即可。
注2：为确保系统稳定性
  * 优先建议该 MinIO 完全用于单个项目的集群文件服务，完全不做他用。
  * 请至少确保该 Bucket 存储桶仅用于单个项目的集群文件服务。
  * 请至少确保集群文件服务与 FineBI 数据存储服务使用完全独立的存储空间，分别配置两个独立的 Bucket 。


注3：请勿为该 Bucket 开启「版本控制」功能，否则工程与 MinIO 对接将失败。
版本控制功能一旦开启，即使随后关闭也会影响对接，必须删除该 Bucket 并重新创建。
![](https://help.fanruan.com/core/style/lod.png)
### 3.3 新建文件存储路径
Bucket 存储桶创建完毕后，用户需要在桶内准备好存储工程文件的路径。
1）在 MinIO 控制台，点击左侧导航栏的「Object Browser」，点击上一节创建的 Bucket 存储桶「fanruan」。
2）点击「Create new path」，在该桶内创建一个目录，用于存储工程文件和工程备份文件
示例目录：webroot
![](https://help.fanruan.com/core/style/lod.png)
3）点击进入上一节创建的目录，新建两个子目录
子目录1：推荐命名为WEB-INF，用于存储工程文件
子目录2：必须命名为backup，用于存储工程备份文件
![](https://help.fanruan.com/core/style/lod.png)
### 3.4 上传文件到MinIO
**对于已部署好的工程，如需接入/替换集群文件服务，需要先将工程文件上传到**MinIO 工程** 存储目录中。**
请将原文件服务器工程存储目录下的所有文件，拷贝到 MinIO 准备的工程存储目录（示例为fanruan存储桶内的/webroot/WEB-INF）。
请注意原文件服务器类型是否支持后端拷贝等传输细节（例如minio等S3类型，必须前端下载文件再上传）
MinIO文件夹| 工程文件  
| 文件夹内容说明  
---|---|---  
工程存储目录（一般为WEB-INF，示例为fanruan存储桶内的/webroot/WEB-INF）| /webroot/WEB-INF/assets| 存放着以下内容：工程Excel原始文件信息FineReport模板备份文件驱动管理上传的驱动通用的共享持久化目录  
/webroot/WEB-INF/dpworks| FineDataLink任务相关的配置文件如不存在该文件夹，说明工程没有使用FDL相关功能，可忽略  
/webroot/WEB-INF/reportlets| FineReport模板存放目录  
/webroot/WEB-INF/resources| 存放工程相关的资源配置文件  
/webroot/WEB-INF/schedule| 定时调度生成的文件  
/webroot/WEB-INF/treasures| 云端运维生成的数据包  
backup| /webroot/backup| 工程历史备份文件  
### 3.5 准备MinIO对接信息
基于上文3.1~3.4节，对必要对接信息的获取进行指明。
信息  
| 说明  
---|---  
Bucket| 3.2节新建的存储桶的名称示例为：fanruan  
路径| 文件服务的根目录名称，即3.3节新建的存储工程文件的目录完整地址本示例为**webroot/WEB-INF/  
** 注1：「路径」必须以「/」结尾，开头不能加「/」。注2：「路径」不能是相对路径。  
## 4\. 使用前提
**1）请务必参考 3.4 节，将当前工程文件上传到准备好的 MinIO 对象存储的工程文件存储目录中。  
**
**2）确认是否需要安装「共享外部目录」插件**
帆软集群与 MinIO的对接，依赖「MinIO资源仓库」插件，该插件默认已安装。
管理员登录帆软应用，点击「管理系统>插件管理>我的插件」，可查看是否正常启用「MinIO资源仓库」插件。如已卸载，需要重新安装。
  * 点击下载插件：[MinIO资源仓库插件](<https://market.fanruan.com/plugin/7e74a2a2-e265-4e6c-addb-281f94053d32>)
  * 插件安装方法请参见：[插件管理](<https://help.fanruan.com/finebi/doc-view-459.html>)


## 5\. 集群接入文件服务
支持在以下情况下接入 MinIO 对象存储作为集群文件服务，请根据情况自行选择，任选其一即可。
### 5.1 运维平台集群管理接入
项目部署成功后，在运维平台的「集群管理」中，可为项目接入 MinIO 对象存储作为文件服务。
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「文件服务器」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
3）协议选择 MinIO ，输入 2.2 节和 3.5 节准备的相关信息
4）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 5.2 管理系统集群配置接入
在帆软应用的「管理系统>智能运维>集群配置」中，可为项目接入 MinIO 对象存储作为文件服务。
1）管理员登录帆软应用，点击「管理系统>智能运维>集群配置」。
2）在开启了状态服务器的前提下，在文件一致设置中选择「文件服务器共享」。
3）点击「编辑」，协议选择 MinIO ，输入 2.2 节和 3.5 节准备的相关信息
4）点击「测试连接并保存」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接华为云OBS实现文件服务](<index.php?doc-view-2676.html>)
[下一篇：FineBI对接FTP实现文件服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1564.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
