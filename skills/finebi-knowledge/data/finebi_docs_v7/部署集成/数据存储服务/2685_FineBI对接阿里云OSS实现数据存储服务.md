---
title: FineBI对接阿里云OSS实现数据存储服务
doc_id: 2685
url: https://help.fanruan.com/finebi/doc-view-2685.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:33
version: "7.X"
---

> 1. 概述1.1 版本运维平台版本功能变更V2.18.0-V2.23.0支持自定义存储桶文件夹路径，连接信息加密存储V2.28.0新增配置项：Region、ChunkedEncodingV2.32.01

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接阿里云OSS实现数据存储服务
[__](<doc-edit-2685.html>)
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
* 历史版本：[3](<edition-list-2685.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-01 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
运维平台版本  
| 功能变更  
---|---  
V2.18.0| -  
V2.23.0| 支持自定义存储桶文件夹路径，连接信息加密存储  
V2.28.0| 新增配置项：Region、ChunkedEncoding  
V2.32.0| 1）存储路径为必填项2）存储路径下不得存在任何文件  
### 1.2 应用场景
对于FineBI项目，支持自备一个S3组件，用来存储FineBI中抽取的基础表和自助数据集数据。
帆软推荐用户自备支持 S3 协议的云存储文件系统作为数据存储组件。
支持的云存储文件系统包括：阿里云OSS、华为云OBS 、亚马逊云S3。其他自行搭建的 S3 平台不确保支持。
### 1.3 功能简介
本文主要讲解FineBI项目与**阿里云对象存储OSS** 的对接：
  * **用户需要自行 购买并准备阿里云对象存储OSS**。****
  * 在部署新项目/项目部署好后，可将FineBI项目与该云存储系统对接，实现数据存储服务


## 2\. 准备阿里云OSS
用户需要自行购买并准备阿里云对象存储OSS**。**
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅阿里云官网获取其他帮助。请参见：[阿里云对象存储OSS](<https://help.aliyun.com/zh/oss/?spm=a2c4g.11174283.0.0.2a9c646clbWL2W>)
注：对于集群文件服务和FineBI数据存储服务，不建议混用同一个对象存储，请至少准备2个完全独立的Bucket。
  
|   
|   
  
---|---|---  
1| 购买| 自行购买阿里云对象存储OSS  
2| 创建RAM用户和AccessKey| 1）登录阿里云[RAM 访问控制](<https://ram.console.aliyun.com/users>)2）创建RAM用户点击「身份管理>用户」，点击「创建用户」务必勾选「OpenAPI 调用访问」，以生成AccessKeyID和AccessKeySecret![](https://help.fanruan.com/core/style/lod.png)3）复制AccessKey信息创建成功后，请务必记录下AccessKeyID和AccessKeySecret，下文需要用到后续无法再次查询到对应Secret，只能重新新建![](https://help.fanruan.com/core/style/lod.png)4）分配权限  
勾选该用户，点击「添加权限」为用户分配AliyunOSSFullAccess：管理对象存储服务（OSS）权限![](https://help.fanruan.com/core/style/lod.png)  
3| 创建存储空间Bucket  
| 1）登录阿里云[对象存储OSS控制台](<https://oss.console.aliyun.com/bucket>)2）创建Bucket（存储空间）示例bucket：bi-oss-test注1：桶名称长度至少 3 个字符。注2：为确保系统稳定性，建议集群文件服务与 FineBI 数据存储服务使用完全独立的存储空间，分别配置两个独立的 Bucket 。![](https://help.fanruan.com/core/style/lod.png)2）新建文件夹点击进入Bucket，在「文件管理>文件列表」中新建目录，用于存储FineBI中抽取的基础表和自助数据集数据，请确保其中不存在任何冗余数据或无关文件示例文件夹：fanruan![](https://help.fanruan.com/core/style/lod.png)  
## 3\. 准备阿里云OSS信息
配置项  
| 说明  
---|---  
协议| S3  
BucketEndpointRegion| **配置项说明：** Bucket：存储空间，用于存储对象的容器Endpoint：OSS对外服务的访问域名Region：OBS的数据中心所在物理位置**获取方式：**  
1）登录阿里云[对象存储OSS控制台](<https://oss.console.aliyun.com/bucket>)2）点击「Bucket列表」，点击工程文件所在Bucket3）点击「概览」，即可查看到相关信息**![](https://help.fanruan.com/core/style/lod.png)**  
AccessKey SecretKey| **配置项说明：** AccessKey是阿里云提供给用户的永久访问凭据
  * AccessKey：用于标识用户，即上文创建RAM用户时记录下的AccessKeyId
  * SecretKey：是一个用于验证你拥有该AccessKey ID的密码，即上文创建RAM用户时记录下的AccessKeySecret

**获取方式：**  
推荐新建RAM用户并配置 AccessKey（上文创建RAM用户时已记录相关信息）如果遗失这个 AccessKey，只能创建新的来替代，如何创建：[创建AccessKey](<https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair?spm=a2c4g.11186623.0.0.2e4baf15tVX9j6>)  
PathStyleAccess| 访问OSS存储桶时，URL的路径结构，**一般情况下无需配置**
  * false：默认值，虚拟主机样式，存储桶名称为主机名的一部分，这种方式是阿里云OSS的推荐访问方式，通常用于生产环境中
  * true：路径样式，存储桶名称为路径的一部分，如项目对接OSS时，出现证书或unknownhost相关报错，可调整为true

  
signerOverride| 允许用户指定请求签名的算法或版本，**一般情况下无需配 置**如项目对接OSS时，出现证书或unknownhost相关报错，可调整为S3SignerType  
路径| 桶内的目录地址，即存储FineBI中抽取的基础表和自助数据集数据的目录完整地址本示例为**fanruan/** 注1：请确保该路径下不存在任何冗余数据或无关文件注2：「路径」必须以「/」结尾，开头不能加「/」注3：「路径」不能是相对路径  
ChunkedEncoding| 是否采用分块传输编码，动态传输未知长度的数据流，**一般情况下默认开启，无需配置** 允许服务器在未提前知道数据总量时，按需分块发送数据，适用于实时流式传输或大文件上传场景  
## 4\. 项目接入数据存储
支持在以下情况下接入阿里云对象存储 OSS 作为 FineBI 数据存储服务，请根据情况自行选择，任选其一即可。
### 4.1 部署新项目时接入
#### 4.1.1 接入数据存储服务
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的阿里云对象存储 OSS 作为FineBI数据存储服务。
1）数据存储服务选择「对接已有数据存储服务」
**![](https://help.fanruan.com/core/style/lod.png)**
2）在「数据存储服务」信息填写处第三章准备的阿里云对象存储 OSS 信息
3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
#### 4.1.2 注意事项
建议在项目部署成功后，对数据存储组件的性能进行检测。性能检测不通过不影响对接，但建议进行优化，以确保FineBI工程运行的稳定性。
  * 管理员登录运维平台，选中指定项目。点击「维护>集群管理>数据存储服务>已配置」。
  * 点击「存储性能检测」，根据提示优化所准备的数据存储服务的性能。


![](https://help.fanruan.com/core/style/lod.png)
### 4.2 部署成功后切换
项目部署成功后，在运维平台的「集群管理」中，可为项目接入自备的阿里云对象存储 OSS 作为 FineBI 数据存储服务。
#### 4.2.1 更换须知
在进行数据存储服务更换前，请务必充分了解并确认接受以下影响：
**1）服务更换后，已抽取的历史数据将无法继续使用，需由管理员执行全局更新操作以重新获取数据。**
**2）对于原采用增量更新的数据，若源数据已不存在，则全局更新后将无法恢复相关数据。**
#### 4.2.2 备份和删除表的元数据
bi-engine-master组件，负责存储表的元数据（即表的结构、数据类型、分区信息等描述性信息，而不是实际的数据内容）
在切换数据存储服务前，需要清理master中历史的元数据路径信息，以确保切换后新配置可用。  

**1）查看元数据信息存储路径**  

管理员登录运维平台，选中指定项目。点击「维护>集群管理>数据存储服务>已配置」。
根据提示找到表的元数据信息存储路径，示例为/home/bi61/fanruan240727164101/bi-engine-master/polars/rocks_data
**![](https://help.fanruan.com/core/style/lod.png)**
**2）备份 元数据信息**
请前往bi-engine-master组件所在服务器，找到元数据信息存储路径，对rocks_data文件夹进行手动异地备份。
**3）删除 元数据信息**
请在备份成功后，对rocks_data文件夹进行删除。
![](https://help.fanruan.com/core/style/lod.png)
#### 4.2.3 重启FineBI应用节点
删除表的元数据后，需要重启 bi-web 组件生效。
1）管理员登录运维平台，选中指定项目。点击「维护>组件管理」。
2）找到FineBI应用节点，点击「重启」，并等待 bi-web 状态至 healthy 。
![](https://help.fanruan.com/core/style/lod.png)
#### 4.2.4 切换数据存储服务
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「数据存储服务」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
3）在「数据存储服务」信息填写处第三章准备的阿里云对象存储 OSS 信息
4）点击「存储性能检测」，根据提示优化所准备的数据存储服务的性能。
（性能检测不通过不影响对接，但建议进行优化，以确保FineBI工程运行的稳定性）
5）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
#### 4.2.5 再次重启FineBI应用节点
数据存储服务切换成功后，会自动重启master和worker组件，需要再次手动重启 bi-web 组件生效。
1）管理员登录运维平台，选中指定项目。点击「维护>组件管理」。
2）找到FineBI应用节点，点击「重启」，并等待 bi-web 状态至 healthy 。
![](https://help.fanruan.com/core/style/lod.png)  

#### 4.2.6 重新全局抽取数据
bi-web 组件重启成功后，请管理员登录FineBI，点击「公共数据>全局更新」。
执行「立即全局更新」，即可抽取最新数据，并存放到新的数据存储服务中。
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接华为云OBS实现数据存储服务](<index.php?doc-view-2684.html>)
[下一篇：FineBI对接单机Redis实现状态服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1561.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
