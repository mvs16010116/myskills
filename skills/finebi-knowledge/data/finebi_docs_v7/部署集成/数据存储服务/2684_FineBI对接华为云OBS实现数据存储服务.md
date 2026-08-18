---
title: FineBI对接华为云OBS实现数据存储服务
doc_id: 2684
url: https://help.fanruan.com/finebi/doc-view-2684.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:32
version: "7.X"
---

> 1. 概述1.1 版本运维平台版本功能变更V2.18.0-V2.23.0支持自定义存储桶文件夹路径，连接信息加密存储V2.28.0新增配置项：Region、ChunkedEncodingV2.32.01

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接华为云OBS实现数据存储服务
[__](<doc-edit-2684.html>)
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
* 历史版本：[3](<edition-list-2684.html>)
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
本文主要讲解FineBI项目与****华为云对象存储OBS**** 的对接：
  * **用户需要自行 购买并准备**华为云对象存储OBS****。****
  * 在部署新项目/项目部署好后，可将FineBI项目与该云存储系统对接，实现数据存储服务


## 2\. 准备华为云OBS
用户需要自行购买并准备华为云对象存储OBS。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅华为云官网获取其他帮助。请参见：[华为云对象存储OBS](<https://support.huaweicloud.com/obs/index.html>)
注：对于集群文件服务和FineBI数据存储服务，不建议混用同一个对象存储，请至少准备2个完全独立的桶。
  
|   
|   
  
---|---|---  
1| 创建华为云超管| 如已有华为云企业超管账号，可忽略本步骤**1）注册华为账号** 请参考华为云文档完成：[注册华为账号并开通华为云](<https://support.huaweicloud.com/usermanual-account/account_id_001.html>)**2）实名认证** 请参考华为云文档完成：[个人账号如何完成实名认证](<https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0077914254.html>) 或 [企业账号如何完成实名认证](<https://support.huaweicloud.com/usermanual-account/zh-cn_topic_0077914253.html>)**3）为华为账号充值** 请确保你的华为账号有足够的余额，才能正常使用OBS等相关资源请参考华为云文档完成：[账户充值](<https://support.huaweicloud.com/usermanual-billing/bills-topic_30000002.html>)  
2| 创建华为云IAM用户和访问密钥| 华为云企业超管账号下，一般有企业内的多种资源超管可以创建一个IAM用户，用于分配对应OBS权限，和帆软集群对接**1）创建IAM用户** 管理员登录[IAM控制台](<https://console.huaweicloud.com/iam/?locale=zh-cn#/iam/users>)，选择「用户>创建用户」，设置IAM用户名请务必勾选「访问密钥」凭证，以生成AccessKeyId和AccessKeySecret请参考华为云文档完成：[创建IAM用户](<https://support.huaweicloud.com/usermanual-iam/iam_02_0001.html>)**![](https://help.fanruan.com/core/style/lod.png)****2）保存访问密钥文件** 创建成功后，请务必妥善保管生成的访问密钥文件credentials.csv，其中包含该IAM用户的Access Key Id和Secret Access Key，下文需要用到请参考华为云文档完成：[管理IAM用户访问密钥](<https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html>)![](https://help.fanruan.com/core/style/lod.png)**3） 分配权限**请为该用户或用户所在的用户组，分配OBS Administrator权限：对象存储服务管理员权限请参考华为云文档完成：[创建用户组并授权](<https://support.huaweicloud.com/usermanual-iam/iam_03_0001.html>)![](https://help.fanruan.com/core/style/lod.png)  
3| 创建桶和文件目录| 1）创建桶登录华为云OBS控制台，[创建桶](<https://console.huaweicloud.com/console/?locale=zh-cn#/obs/create>)请参考华为云文档完成：[创建桶](<https://support.huaweicloud.com/usermanual-obs/zh-cn_topic_0045829088.html>)示例桶名称：bi-oss-test注1：桶名称长度至少 3 个字符。注2：为确保系统稳定性，建议集群文件服务与 FineBI 数据存储服务使用完全独立的存储空间，分别配置两个独立的桶。![](https://help.fanruan.com/core/style/lod.png)2）新建文件夹点击进入创建好的桶，在「对象」中新建文件夹，用于存储FineBI中抽取的基础表和自助数据集数据，请确保其中不存在任何冗余数据或无关文件请参考华为云文档完成：[新建文件夹](<https://support.huaweicloud.com/usermanual-obs/obs_03_0316.html>)示例文件夹：fanruan![](https://help.fanruan.com/core/style/lod.png)  
  
## 3\. 准备华为云OBS信息
配置项  
| 说明  
---|---  
协议| S3  
BucketEndpointRegion| **配置项说明：** Bucket：桶，用于存储对象的容器Endpoint：OBS对外服务的访问域名Region：OBS的数据中心所在物理位置**获取方式：**  
1）登录华为云对象存储OBS[管理控制台](<https://console.huaweicloud.com/console/?locale=zh-cn#/obs/manager/buckets>)2）点击桶列表，桶名称即为Bucket3）点击桶，进入「概览」界面，在域名信息中，可以看到Endpoint和Region![](https://help.fanruan.com/core/style/lod.png)  
AccessKeySecretKey| **配置项说明：** AccessKey是华为云提供给用户的永久访问凭据
  * AccessKey：用于标识用户
  * SecretKey：是一个用于验证你拥有该AccessKey的密码

**获取方式：**  
推荐新建IAM用户并创建访问密钥，即上文创建IAM用户时生成的访问密钥文件credentials.csv其中包含该IAM用户的Access Key Id（即帆软所需的AccessKey）和Secret Access Key（帆软所需的SecretKey）如果遗失这个 AccessKey，请参考华为云文档重新创建：[管理IAM用户访问密钥](<https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html>)  
PathStyleAccess| 访问OBS存储桶时，URL的路径结构，**一般情况下无需配置**  

  * false：默认值，虚拟主机样式，存储桶名称为主机名的一部分，这种方式是华为云OBS的推荐访问方式，通常用于生产环境中
  * true：路径样式，存储桶名称为路径的一部分，如集群对接OBS时，出现证书或unknownhost相关报错，可调整为true

  
signerOverride| 允许用户指定请求签名的算法或版本，**一般情况下无需配 置**如集群对接OBS时，出现证书或unknownhost相关报错，可调整为S3SignerType  
路径| 桶内的目录地址，即存储FineBI中抽取的基础表和自助数据集数据的目录完整地址本示例为**fanruan/** 注1：请确保该路径下不存在任何冗余数据或无关文件注2：「路径」必须以「/」结尾，开头不能加「/」注3：「路径」不能是相对路径  
ChunkedEncoding| 是否采用分块传输编码，动态传输未知长度的数据流，**一般情况下默认开启，无需配置** 允许服务器在未提前知道数据总量时，按需分块发送数据，适用于实时流式传输或大文件上传场景  
## 4\. 项目接入数据存储
支持在以下情况下接入华为云对象存储OBS作为 FineBI 数据存储服务，请根据情况自行选择，任选其一即可。
### 4.1 部署新项目时接入
#### 4.1.1 接入数据存储服务
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的华为云对象存储OBS作为FineBI数据存储服务。
1）数据存储服务选择「对接已有数据存储服务」
![](https://help.fanruan.com/core/style/lod.png)
2）在「数据存储服务」信息填写处第三章准备的华为云对象存储OBS信息
3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
**![](https://help.fanruan.com/core/style/lod.png)**
#### 4.1.2 注意事项
建议在项目部署成功后，对数据存储组件的性能进行检测。性能检测不通过不影响对接，但建议进行优化，以确保FineBI工程运行的稳定性。
  * 管理员登录运维平台，选中指定项目。点击「维护>集群管理>数据存储服务>已配置」。
  * 点击「存储性能检测」，根据提示优化所准备的数据存储服务的性能。


![](https://help.fanruan.com/core/style/lod.png)
### 4.2 部署成功后切换
项目部署成功后，在运维平台的「集群管理」中，可为项目接入自备的华为云对象存储OBS作为 FineBI 数据存储服务。
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
![](https://help.fanruan.com/core/style/lod.png)
**2）备份元数据信息**
请前往bi-engine-master组件所在服务器，找到元数据信息存储路径，对rocks_data文件夹进行手动异地备份。
**3）删除元数据信息**
请在备份成功后，对rocks_data文件夹进行删除。
![](https://help.fanruan.com/core/style/lod.png)
#### 4.2.3 重启FineBI应用节点
删除表的元数据后，需要重启 bi-web 组件生效。
1）管理员登录运维平台，选中指定项目。点击「维护>组件管理」。
2）找到FineBI应用节点，点击「重启」，并等待 bi-web 状态至 healthy 。
**![](https://help.fanruan.com/core/style/lod.png)**
#### 4.2.4 切换数据存储服务
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「数据存储服务」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
3）在「数据存储服务」信息填写处第三章准备的华为云对象存储OBS信息
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
**![](https://help.fanruan.com/core/style/lod.png)**
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：日志库表结构](<index.php?doc-view-1134.html>)
[下一篇：FineBI对接阿里云OSS实现数据存储服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2685.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
