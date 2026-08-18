---
title: 新SAP BW数据集插件
doc_id: 256
url: https://help.fanruan.com/finebi/doc-view-256.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:09
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本新SAP BW数据集插件版本6.0V1.5.301.2 功能简介本文将介绍如何在 FineBI 中添加 SAP BW 类型的&nbsp;服务器数据集&nbsp

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 新SAP BW数据集插件
[__](<doc-edit-256.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[18](<edition-list-256.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-10-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本| 新SAP BW数据集插件版本  
---|---  
6.0| V1.5.30  
### 1.2 功能简介
本文将介绍如何在 FineBI 中添加 SAP BW 类型的 [服务器数据集](<https://help.fanruan.com/finebi7.0/doc-view-253.html>) ，用于进行数据分析。
### 1.3 实现原理
通过 [FineReport 设计器远程连接 FineBI 工程](<https://help.fanruan.com/finebi7.0/doc-view-931.html>)，在 FineReport 设计器中添加 SAP BW 服务器数据集后，FineBI 工程中即可出现该服务器数据集。
## 2\. 准备工作
### 2.1 开启服务
1）首先确认 SAP BW 服务器已经开启了 XMLA 服务，才能在外部软件中使用 XMLA 连接。
客户端进入 SAP 系统，按照如下路径进入：「TCODE:SICF >default_host> sap>bw」，如下图所示:
![222](https://help.fanruan.com/core/style/lod.png)
2）右击「bw」，选择「Deactivate service」，点击「确认」；再次右击「bw」选择「Activate service」，点击「确认」，确保所有的服务都已经开启。
![222](https://help.fanruan.com/core/style/lod.png)  

### 2.2 安装插件
FineBI 与 FineReport 中都需要安装「新 SAP BW 数据集插件」，且两者安装的插件版本需保持一致。
#### 2.2.1 FineBI  

点击下载安装插件：[新 SAP BW 数据集插件](<https://market.fanruan.com/plugin/645>)   

插件安装方法请参考：[服务器插件管理](<https://help.fanruan.com/finereport/doc-view-2220.html>)
#### 2.2.2 FineReport
点击下载安装插件：[新 SAP BW 数据集插件](<https://market.fanruan.com/plugin/645>)   

设计器插件安装方法请参照 [设计器插件管理](<https://help.fanruan.com/finereport/doc-view-2198.html>)
服务器安装插件方法请参照 [服务器插件管理](<https://help.fanruan.com/finereport/doc-view-2220.html>)
注1：更新重装插件后如果出现连接报错，可以重启工程解决。
注2：SAP BW 插件需要授权。
注3：暂不支持 [服务器部署包](<https://help.fanruan.com/finereport10.0/doc-view-2804.html>) 下使用新 SAP BW 数据集插件。
注4：不支持 jdk5 及低于此版本的 jdk
### 2.3 导入文件
与 SAP 系统进行连接，需要导入 SAP 接口包和本地库，并确保运行的 JVM 能够找到接口包和本地库。
1）下载对应版本并解压文件夹，获得sapjco3相关接口包和本地库文件。
2）登录服务器，找到/webapps/webroot/WEB-INF/plugins目录下的SAP插件文件夹。
3）将文件上传到SAP插件文件夹中即可
4）如需远程设计，请选择本地电脑环境对应的文件，上传到本地设计器%FR_HOME%\webapps\webroot\WEB-INF\plugins和%FR_HOME%\plugins两个目录下的SAP插件文件夹中
5）重启工程后生效。
服务器类型| SAP 文件包  
---|---  
Linux32| [sapjco3_linux_32bit.rar](<doc-download-/finebi/uploads/file/20251023/sapjco3_linux_32bit.rar> "下载资料")  
Linux64| [sapjco3_linux_64bit.rar](<doc-download-/finebi/uploads/file/20251023/sapjco3_linux_64bit.rar> "下载资料")  
Windows32| [sapjco3_windows_32bit.rar](<doc-download-/finebi/uploads/file/20251023/sapjco3_windows_32bit.rar> "下载资料")  
Windows64| [sapjco3_windows_64bit.rar](<doc-download-/finebi/uploads/file/20251023/sapjco3_windows_64bit.rar> "下载资料")  
Mac| [libsapjco3.rar](<doc-download-/finebi/uploads/file/20251023/libsapjco3.rar> "下载资料")  
其他服务器/架构  
| 不同服务器架构需对应 SAP 驱动，版本众多。其他架构请访问SAP官网获取：[SAP官网驱动下载地址](<https://support.sap.com/en/product/connectors/jco.html> "下列链接") ![](https://help.fanruan.com/core/style/lod.png)  
注1：Windows Server 2003 和 Windows XP 的系统在连接 SAP 时，需要下载安装 Microsoft Visual C++ 2005 SP1。
注2：如果同时安装了 SAP 和 SAP BW 插件，可能会存在冲突导致有某一种数据集预览报错的问题。
注3：如果数据连接失败，可以尝试将 sapjco3.dll 文件放置在系统 jre 的 bin 目录下，例如：%JAVA_HOME%\jre\bin
注4：如果仍连接不了，看报错信息，例如验证 SAPJCO 失败，缺少依赖包 libstdc++.so「SAPJCO2 才需要，而 SAPJCO3 不需」，则需要安装共享库。
注5：MAC OS系统，需要在vmoptions.txt文件中写入-Djava.library.path=/放置驱动文件的路径
打开设计器%FineReport%/bin，右击「designer」，选择「显示包内容」，打开 vmoptions.txt 文件，如下图所示：
在文件中写入：-Djava.library.path=/Applications/FineReport10.0/lib（放置驱动文件的路径）
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 操作步骤
### 3.1 建立远程连接
首先需要将设计器远程连接至 FineBI 服务器。此处详情请参见：[远程连接 FineReport 设计器](<https://help.fanruan.com/finebi7.0/doc-view-931.html>)
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 FineReport中添加服务器数据集
FineReport 提供三种 SAP BW 类型的数据连接方式和对应的数据集，如下表所示：
数据连接| 服务器数据集  
---|---  
SAP BW Cube| SAPBW Cube 数据集  
SAP BW Query| SAPBW Query 数据集  
SAP BW BICS| SAPBW BICS 数据集  
请根据需求新建 SAP BW 数据连接及对应的数据集。操作步骤如下：
1）参考 [新 SAP BW 数据集插件](<https://help.fanruan.com/finereport/doc-view-1466.html>) 文档新建所需类型的 SAP BW 数据连接。
注1：使用 JCO 方式连接 SAP BW Query 时，需按照 [新 SAP BW 数据集插件](<https://help.fanruan.com/finereport/doc-view-1466.html>) 文档的 2.3 节内容在 FineBI 工程路径（将提供的 FineReport 路径替换为相同的 FineBI 路径即可）下导入相关文件。
注2：使用 SAP BW BICS 连接时，需按照 [新 SAP BW 数据集插件](<https://help.fanruan.com/finereport/doc-view-1466.html>) 文档的 2.3、2.4 节内容在 FineBI 工程路径（将提供的 FineReport 路径替换为相同的 FineBI 路径即可）下导入相关文件。
2）数据连接建立完成后，选择「服务器>服务器数据集」，进入服务器数据集配置界面，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）点击「+」按钮，选择并添加 SAP BW 类型的服务器数据集，详细配置步骤请参考 [新SAPBW数据集插件](<https://help.fanruan.com/finereport/doc-view-1466.html>) 文档中的 3.2、4.4 和 5.2 节。
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 FineBI 中添加服务器数据集
1）管理员登录 FineBI 系统，点击「数据目录」，选择任意文件夹，点击「新建数据集>数据库表」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）在服务器数据集下，可以看到刚刚在设计器中添加的 SAP BW 服务器数据集，选中表并点击「确定」添加到文件夹中即可使用。如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
## 3\. 注意事项
**问题描述：**
FineBI 和 FineReport 均安装了新 SAP BW 数据集插件，并通过 [FineReport 设计器远程连接 FineBI 工程](<https://help.fanruan.com/finebi7.0/doc-view-931.html>) ，但添加服务器数据集的时候不显示 SAP BW 数据集。
**解决方案：**  

FineBI 工程的报表模块 JAR 包版本要跟设计器的 JAR 包版本保持一致，查看 FineBI 工程报表模块 JAR 包版本方法如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：JSON 数据集插件](<index.php?doc-view-489.html>)
[下一篇：Mongodb数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-417.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
