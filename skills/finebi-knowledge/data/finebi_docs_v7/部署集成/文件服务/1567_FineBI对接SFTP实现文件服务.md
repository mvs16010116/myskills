---
title: FineBI对接SFTP实现文件服务
doc_id: 1567
url: https://help.fanruan.com/finebi/doc-view-1567.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:36
version: "7.X"
---

> 1. 概述SFTP是一种通过SSH协议进行加密的文件传输协议，部署简单，是Linux系统自带的，相对于FTP而言更加安全和稳定。在帆软集群项目中，文件服务器用于存储和共享集群中所需的文件和数据资源，以确

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接SFTP实现文件服务
[__](<doc-edit-1567.html>)
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
* 历史版本：[14](<edition-list-1567.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-02-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
SFTP是一种通过SSH协议进行加密的文件传输协议，部署简单，是Linux系统自带的，相对于FTP而言更加安全和稳定。
在帆软集群项目中，文件服务器用于存储和共享集群中所需的文件和数据资源，以确保每个节点都可以访问并使用它们。
本文主要讲解帆软集群项目如何对接SFTP，作为集群文件服务：
  * 用户可**自行准备一个SFTP** ，并进行参数调优
  * 在部署新项目/项目部署好后，可将项目与该文件服务器对接


## 2\. 准备文件服务器
用户需要自行准备并部署SFTP。
帆软不提供相关资料和指导，仅对必要内容进行指明，请查阅相关官网获取其他帮助。
**如运维能力不足，推荐使用运维平台部署新项目时，在「文件服务」中勾选「部署MinIO」即可，无需手动部署和调优。**
### 2.1 服务器配置
配置类型| 最低配置| 推荐配置  
---|---|---  
服务器数量| 所准备的服务器，仅用于部署该集群项目的负载均衡、状态服务、文件服务、配置库组件| 所准备的服务器，仅用于部署文件服务  
物理内存| 8G| 16G  
CPU| 2.5GHz以上8核16线程| 2.5GHz以上16核32线程  
可用磁盘空间| 500G~1T其中根目录可用磁盘不可小于40G后续请根据使用情况扩展| 1T~2T其中根目录可用磁盘不可小于80G后续请根据使用情况扩展  
网络要求| 1）文件服务和应用工程、其他组件建议在同一网段，避免网络波动等问题2）文件服务和应用工程、其他组件如处于公网环境，带宽需在10M以上3）文件服务和应用工程、其他组件之间需要网络畅通，互相端口可访问  
### 2.2 确认安装SSH服务
SFTP 使用 SSH 协议进行文件传输，因此需要在 Linux 服务器上安装和配置 SSH 服务器。
  * 大多数 Linux 发行版已经预装了 OpenSSH，只需要确认其安装和运行状态。
  * 本节以CentOS 7系统为例，介绍如何在 Linux 系统中检查和安装 OpenSSH 服务。
  * 具体步骤可能因操作系统版本和配置差异而有所不同。帆软不提供相关资料和指导，请自行百度。


1）打开终端或命令行界面，以root用户身份登录。
2）运行以下命令以判断是否安装**4.8p1 以上版本的** OpenSSH 服务：
yum -q list openssh-server
  * 如果未找到相关的 OpenSSH 输出，并显示类似于"command not found"等错误消息，则表示系统尚未安装 OpenSSH 服务。
  * 如果看到与 OpenSSH 相关的输出行，说明系统中已安装了OpenSSH客户端。请确保 OpenSSH 服务版本大于 4.8p1，如果版本过低，需要更新。


![](https://help.fanruan.com/core/style/lod.png)
3）运行以下命令以更新系统软件包列表：
sudo yum update
![](https://help.fanruan.com/core/style/lod.png)
4）运行以下命令以安装OpenSSH服务：
sudo yum install openssh-server
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 修改并发和会话数限制
由于使用SFTP时，可能会出现高并发状况，因此需要提前根据预期负载情况来优化服务器的并发和会话数限制。
否则在高并发状态下，SFTP连接会出现报错：connection is closed by foreign host
**参数介绍：**
参数  
| 说明  
---|---  
MaxStartups| 用于限制 SSH 服务器允许的最大并发连接数和连接速率限制，即同时连接到服务器的客户端数量的上限参数值的格式为 a:b:c
  * a：表示最大并发连接数
  * b：表示在a个连接数后进行启动速率限制的时间窗口（以分钟为单位）
  * c：表示在限制期间允许的最大增量连接数

默认值MaxStartups 10:30:100，表示最大并发连接数为10，限制为30分钟内的连接速率，并允许每30分钟增加100个连接。  
MaxSessions| 用于限制一个用户可以同时建立的 SSH 会话数参数值的格式是一个整数，表示允许的最大会话数默认值MaxSessions 10，表示每个用户最多可以同时打开 10 个 SSH 会话  
**修改方法：**  

1）打开终端或命令行界面。以root用户身份登录。
2）使用文本编辑器（如vi或nano），打开/etc/ssh/sshd_config文件。
3）在文件中找到包含MaxStartups和MaxSessions的行。
默认情况下，这两行是注释状态（使用#开头），取消注释行。或者如果不存在，请在文件的末尾添加以下行并保存：
MaxStartups 1000:30:1200
MaxSessions 1000
![](https://help.fanruan.com/core/style/lod.png)
4）重新加载SSH服务的配置以应用更改。可以使用以下命令重新加载OpenSSH服务：
sudo systemctl reload sshd
### 2.4 确认启动SFTP服务
确保SFTP服务启动的情况下，再进行集群对接操作。
1）打开终端或命令行界面。以root用户身份登录。
2）运行以下命令以检查SSH服务器的状态：
service sshd status
  * 如果Active状态为running，说明 SFTP 已启动。
  * 如果Active状态不是running，说明SFTP未启动。


3）运行以下命令以启动SSH服务器：
service sshd start
![](https://help.fanruan.com/core/style/lod.png)
### 2.5 防火墙开放SSH端口
如果 Linux 服务器上启用了防火墙（如 iptables 或 firewalld），请确保开放 SSH（默认端口 22）端口，以允许 SFTP 的正常运行。
**1）确认SSH端口**
执行语句，确认SSH使用的端口号，一般默认为22端口
sudo netstat -tlnp | grep ssh
**2）防火墙开放SSH端口**
  * 开放端口：firewall-cmd --zone=public --add-port=22/tcp --permanent。返回值为「success」，说明已放行22端口
  * 更新防火墙规则：firewall-cmd --reload。返回值为「success」，说明已更新规则
  * 再次检查端口是否放行：firewall-cmd --zone=public --query-port=22/tcp。返回值为「yes」，说明已放行22端口


## 3\. 准备文件路径
### 3.1 创建SFTP用户
默认情况下，OpenSSH服务器使用系统上的用户进行身份验证。推荐直接使用root用户，也可创建一个专门用于SFTP的用户。
本节示例创建一个用户名为fanruan的用户，并为其设置密码和文件夹权限。
**1）新建用户** （将"fanruan"替换为你要创建的用户名）
sudo adduser fanruan  

**2）为用户设置密码** （将"fanruan"替换为你要创建的用户名，并按照提示设置密码）
sudo passwd fanruan
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 创建存储目录
用户需要准备一个目录，用于存储工程文件和工程备份文件。并确保上文的SFTP用户有该目录的读写执行权限。
步骤  
|   
  
---|---  
创建父目录| 创建一个文件夹，用于存储工程文件和工程备份文件本文示例/home/fanruanmkdir /home/fanruan  
创建工程文件存储目录| 在父目录中，创建一个文件夹（推荐命名为WEB-INF），用于存储工程文件本文示例/home/fanruan/WEB-INFmkdir /home/fanruan/WEB-INF/  
创建工程备份文件存储目录| **无需手动创建** 备份还原文件存储路径默认为../backup即在工程文件存储目录同级，自动生成backup文件夹，用于存储平台备份  
设置父目录所有者| **设置父目录的所有者为上文的fanruan用户** （将"fanruan"和"/home/fanruan"替换为你的用户名称和文件夹路径）chown -R fanruan /home/fanruan  
设置父目录权限| **请确保所有者有父目录的****读写执行权限** （将"/home/fanruan"替换为你的文件夹路径）chmod -R 755 /home/fanruan  
### 3.3 上传文件到存储目录（按需选做）
如需在**部署新项目** 时接入SFTP作为文件服务，**请勿执行** 本步骤！
对于已部署好的工程，如需接入/替换集群文件服务，需要先将工程文件上传到SFTP存储目录中。
  * 如当前工程已配置文件服务，请将原文件服务器工程存储目录下的所有文件，拷贝到SFTP准备的工程存储目录。请注意原文件服务器类型是否支持后端拷贝等传输细节（例如minio等S3类型，必须前端下载文件再上传）  

  * 如当前工程未配置文件服务，首次接入文件服务，请将工程某个节点下的以下文件夹拷贝到SFTP

SFTP父目录下文件夹| 工程文件  
| 文件夹内容说明  
---|---|---  
工程存储目录（一般为WEB-INF）| /webroot/WEB-INF/assets| 存放着以下内容：工程Excel原始文件信息FineReport模板备份文件驱动管理上传的驱动通用的共享持久化目录  
/webroot/WEB-INF/dpworks| FineDataLink任务相关的配置文件如不存在该文件夹，说明工程没有使用FDL相关功能，可忽略  
/webroot/WEB-INF/reportlets| FineReport模板存放目录  
/webroot/WEB-INF/resources| 存放工程相关的资源配置文件  
/webroot/WEB-INF/schedule| 定时调度生成的文件  
/webroot/WEB-INF/treasures| 云端运维生成的数据包  
backup| /webroot/backup| 工程历史备份文件  
## 4\. 准备SFTP信息
信息  
| 说明  
---|---  
主机  
| SFTP所在服务器IP  
端口| SSH服务占用端口，默认为22  
用户名| 3.1节准备的SFTP用户，优先推荐root所准备的用户需要有存储目录的读写执行权限  
密码| SFTP用户的密码，支持使用密钥如集群与该文件服务已连接，文件服务密码出现变更，请在集群配置中进行修改并确认连接成功  
路径| 3.2节创建的工程文件存储目录本示例为：/home/fanruan/WEB-INF/1）注意是**工程文件存储路径** ，而非父目录路径2）路径必须是**以斜杠/开头的 绝对路径**，非斜杠开头会被识别为用户相对路径  
  
## 5\. 集群接入文件服务
支持在以下情况下接入 SFTP 作为集群文件服务，请根据情况自行选择，任选其一即可。
### 5.1 部署新集群时接入
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的SFTP作为集群文件服务。
此情况下，请确保准备的工程存储目录文件夹中内容为空，不存在任何数据，否则无法成功对接。
1）文件服务选择「对接已有文件服务」。
![](https://help.fanruan.com/core/style/lod.png)
2）在「文件服务」信息填写处：
  * 协议：SFTP  

  * 编码：一般默认选择UTF-8，防止中文乱码
  * 主机、端口、用户名、密码：填写第4章准备的SFTP信息
  * 路径：填写第四章准备的，以**/** 开头的工程文件存储目录


3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 5.2 运维平台集群管理接入
项目部署成功后，在运维平台的「集群管理」中，可为项目接入自备的SFTP作为文件服务。
**使用前提：请务必参考3.3节，将当前工程文件上传到准备好的SFTP存储目录中。**
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「文件服务器」进行配置。
![](https://help.fanruan.com/core/style/lod.png)
3）输入相关信息
  * 协议：SFTP  

  * 编码：一般默认选择UTF-8，防止中文乱码
  * 主机、端口、用户名、密码：填写第4章准备的SFTP信息
  * 路径：填写第四章准备的，以**/** 开头的工程文件存储目录


4）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)  

### 5.3 管理系统集群管理接入
在帆软应用的「管理系统>集群管理」中，可为项目接入自备的SFTP作为文件服务。
**使用前提：请务必参考3.3节，将当前工程文件上传到准备好的SFTP存储目录中。**
1）管理员登录帆软应用，点击「管理系统>智能运维>集群配置」。
2）在开启了状态服务器的前提下，在文件一致设置中选择「文件服务器共享」。
3）点击「编辑」填写相关信息，点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
  * 协议：SFTP  

  * 编码：一般默认选择UTF-8，防止中文乱码
  * 主机、端口、用户名、密码：填写第4章准备的SFTP信息
  * 路径：填写第四章准备的，以**/** 开头的工程文件存储目录


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接腾讯云Redis实现状态服务](<index.php?doc-view-1136.html>)
[下一篇：FineBI对接NAS实现文件服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1580.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
