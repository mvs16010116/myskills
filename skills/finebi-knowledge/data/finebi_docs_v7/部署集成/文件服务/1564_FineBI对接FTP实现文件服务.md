---
title: FineBI对接FTP实现文件服务
doc_id: 1564
url: https://help.fanruan.com/finebi/doc-view-1564.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:40
version: "7.X"
---

> 1. 概述FTP（File Transfer Protocol）是一种用于在计算机网络之间传输文件的标准协议，被大多数操作系统和 FTP 客户端支持，方便用户进行文件传输。在帆软集群项目中，文件服务器用

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI对接FTP实现文件服务
[__](<doc-edit-1564.html>)
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
* 历史版本：[10](<edition-list-1564.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-02-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FTP（File Transfer Protocol）是一种用于在计算机网络之间传输文件的标准协议，被大多数操作系统和 FTP 客户端支持，方便用户进行文件传输。
在帆软集群项目中，文件服务器用于存储和共享集群中所需的文件和数据资源，以确保每个节点都可以访问并使用它们。
本文主要讲解帆软集群项目如何对接vsftpd（一个广泛使用的FTP服务器），作为集群文件服务：
  * 用户可**自行准备一个 vsftpd**，并进行参数调优
  * 在部署新项目/项目部署好后，可将项目与该文件服务器对接


注：FTP传输的数据和命令都是明文的，容易被窃听和篡改。推荐使用更安全的 SFTP 协议 ，详情请参见：[集群项目对接SFTP](<https://help.fanruan.com/finebi7.0/doc-view-1567.html>)
## 2\. 安装FTP
用户需要**自行准备并部署 vsftpd** 。
帆软不提供相关资料和指导，仅对必要内容进行指明，请自行查阅相关官网获取其他帮助。
**如运维能力不足，推荐使用运维平台部署新项目时，在「文件服务」中勾选「部署MinIO」即可，无需手动部署和调优。**
### 2.1 建议的服务器配置
配置类型| 最低配置| 推荐配置  
---|---|---  
服务器数量| 所准备的服务器，仅用于部署该集群项目的负载均衡、状态服务、文件服务、配置库组件| 所准备的服务器，仅用于部署文件服务  
物理内存| 8G| 16G  
CPU| 2.5GHz以上8核16线程| 2.5GHz以上16核32线程  
可用磁盘空间| 500G~1T其中根目录可用磁盘不可小于40G后续请根据使用情况扩展| 1T~2T其中根目录可用磁盘不可小于80G后续请根据使用情况扩展  
网络要求| 1）文件服务和应用工程、其他组件建议在同一网段，避免网络波动等问题2）文件服务和应用工程、其他组件如处于公网环境，带宽需在10M以上3）文件服务和应用工程、其他组件之间需要网络畅通，互相端口可访问  
### 2.2 安装 vsftpd
本节以 **CentOS 可联网系统** 为例演示，内网及其他系统请自行查阅相关官网获取其他帮助。
建议使用超级管理员用户（root）完成。
  
| 步骤| 语句  
---|---|---  
1| 安装 vsftpd 服务，并自动确认安装过程中的提示| sudo yum install vsftpd -y  
2| 立即启动 vsftpd 服务| sudo systemctl start vsftpd  
3| 配置 vsftpd 服务在系统启动时自动启动| sudo systemctl enable vsftpd  
### 2.3 配置 vsftpd 用户和存储目录
本文以ftp用户「**ftpuser** 」、ftp存储目录「**/home/ftpuser** 」为例演示，请根据服务器情况自行调整语句。
建议使用超级管理员用户（root）完成。
  
| 步骤| 语句  
---|---|---  
1| 创建用户ftpuser，并指定该用户主目录为/home/ftpuser| sudo useradd -m -d /home/ftpuser ftpuser  
2| 为用户ftpuser设置密码，输入两次密码完成设置| sudo passwd ftpuser  
3| 设置目录/home/ftpuser的所有者为用户ftpuser| sudo chown ftpuser:ftpuser /home/ftpuser  
4| 确保用户ftpuser对目录/home/ftpuser有读写执行权限| sudo chmod 777 /home/ftpuser注：如果考虑安全性，可以只给 755 权限，但是下文拷贝 WEB-INF 文件时务必使用 ftp 用户，否则会因为文件归属问题导致不能写入  
5| 确保用户ftpuser可用| 请确保用户未被列入禁止访问列表1）检查 /etc/vsftpd/ftpusers 文件这个文件列出了被禁止访问 FTP 服务器的用户如果用户在这个文件中，删除相应的行即可  
2）检查 /etc/vsftpd/user_list 文件这个文件列出了被禁止访问的用户确保用户不在这个文件中  
### 2.4 修改 vsftpd 配置文件
1）编辑配置文件：sudo nano /etc/vsftpd.conf
2）建议对以下配置项进行修改，修改完成后保存并退出编辑器。
3）重启 vsftpd 服务以使配置修改生效：sudo systemctl restart vsftpd
  
| 配置|   
| 修改建议  
---|---|---|---  
1| 用户相关| # 禁止匿名用户登录，匿名用户一般不允许上传文件，配置十分复杂，建议禁用**anonymous_enable=NO** # 允许本地用户登录，本地用户可以使用他们的系统账户登录到 FTP 服务器，并访问他们的主目录或其他被授权的目录**local_enable=YES**  
# 允许本地用户进行写操作，（如上传文件、创建目录等），作为集群的文件服务器，请务必开启该权限**write_enable=YES**  
# 将本地用户限制在其主目录中，防止他们访问系统的其他部分。这是一个安全措施，通常建议启用（非强制）**chroot_local_user=YES**  
# 允许可写的 chroot 环境，如果启用了 chroot_local_user，并且用户的主目录是可写的，需要将此选项设置为 YES 以避免 vsftpd 拒绝启动**allow_writeable_chroot=YES**  
2| 日志相关| # 启用传输日志记录，vsftpd将记录所有的文件传输操作，包括上传和下载，帮助管理员监控和审计 FTP 活动**xferlog_enable=YES** # 指定传输日志文件的路径（示例使用/var/log/vsftpd.log），请确保指定的路径存在，并且对 vsftpd 进程具有写权限，以便能够正确记录日志**xferlog_file=/var/log/vsftpd.log**  
3| 工作模式(二选一）| 介绍  
| FTP 有两种工作模式：主动模式和被动模式。请按需选择
  * **被动模式：** FTP服务器需要开放21端口和额外端口供客户端进行数据传输，但传输速度更优秀，**推荐使用被动模式**
  * **主动模式：** FTP服务器只需要开放20和21端口

  
选择被动模式| # 允许数据传输时使用PASV被动模式**pasv_enable=YES** # 指定被动模式端口范围（示例使用50000~50100端口），请根据预期的并发连接数预留足够大的端口范围，请避免使用系统保留端口（1024以下）和常见服务端口。如全部设置为0，代表随机取用不限制# 指定被动模式使用的最小端口号**pasv_min_port=50000** # 指定被动模式使用的最大端口号**pasv_max_port=50100**  
选择主动模式| # 在 vsftpd 配置文件中，没有专门的配置项是专门用于启用主动模式的，因为主动模式是默认行为，只需要检查一些可能影响主动模式的配置项# 允许 FTP 服务器在主动模式下从端口 20 发起数据连接，禁用将随机选择高端口发起数据连接，可能会因防火墙配置导致失败**connect_from_port_20=YES**  
4  
| 其他  
| # 禁用反向 DNS 查找，反向 DNS 查找可能会导致连接延迟，特别是在 DNS 解析速度较慢或失败的情况下**reverse_lookup_enable=NO**  
### 2.5 开放防火墙端口
1）根据2.4节选择的ftp工作模式，开放对应的防火墙端口  

2）开放防火墙端口后，需要更新防火墙规则以生效：sudo firewall-cmd --reload
  
|   
  
---|---  
**必须开放21端口**|  原因：以便客户端能够连接到服务器并发送 FTP 命令和接收响应，包括登录、目录导航、文件操作命令等。sudo firewall-cmd --permanent --add-port=21/tcp  
**主动模式** ：必须额外开放**20** 端口| 原因：以便服务器能够向客户端发起数据连接，以便服务器能够向客户端发起数据连接sudo firewall-cmd --permanent --add-port=20/tcp  
**被动模式** ：必须额外开放**被动模式端口范围**|  （如2.4节配置示例中，使用50000~50100端口）原因：被动模式下，服务器使用指定的高端口范围进行数据连接，必须开放这些端口以允许数据传输sudo firewall-cmd --permanent --add-port=50000-50100/tcp  
### 2.6 配置SELinux（选做）
SELinux 是 Linux 内核中的一个安全模块，通过强制访问控制机制来严格限制程序和用户对系统资源的访问。
在 SELinux 开启的情况下，可能会限制 FTP 服务器对文件系统和网络资源的访问，导致 FTP 服务器无法正常工作。
**如果在完成了上文的权限分配和 ftp 配置操作后，尝试登录 ftp 仍然失败或无权限操作文件，建议关闭 SELinux 或调整 SELinux 配置 。**
#### **方案一：关闭SELinux**
  
|   
  
---|---  
查看SELinux状态| **命令：**
  * **getenforce**

**返回值：**
  * Enforcing：强制模式，所有违反SELinux策略的操作都会被阻止
  * Permissive：宽容模式，违反SELinux策略的操作不会被阻止，但会被记录在日志中
  * Disabled：SELinux被禁用，系统不再使用SELinux的安全策略

如返回值为**Enforcing** ，则需要手动关闭SELinux  
关闭SELinux| **1）临时关闭SELinx**
  * 命令：**sudo setenforce 0**

将SELinux从强制模式切换到宽容模式，无需重启服务器立刻生效，但服务器重启后又会恢复到强制模式**2） 永久关闭SELinux（可选，需重启Linux服务器生效）**
  * 编辑配置文件：**sudo vi /etc/selinux/config**
  * 修改 SELinux 状态：**SELINUX=disabled**

将SELinux禁用，重启服务器后更改方可生效  
#### **方案二：配置SELinux以支持FTP**
  

  
|  配置| 命令  
---|---|---  
1  
| 允许 FTP 服务器访问用户主目录| sudo setsebool -P ftp_home_dir 1  
2| 允许 FTP 服务器使用指定的被动模式端口范围| 其中的端口范围，为2.4节指定的被动模式端口范围，请按需修改sudo semanage port -a -t ftp_data_port_t -p tcp 50000-50100  
3| 允许 FTP 服务器写入文件| sudo setsebool -P allow_ftpd_full_access 1  
4| 允许 FTP 服务器使用网络| sudo setsebool -P ftpd_connect_all_unreserved 1  
## 3\. 准备工程文件
### 3.1 创建工程文件存储目录
2.3节已经创建了ftp用户「**ftpuser** 」、ftp存储目录「**/home/ftpuser** 」。
用户需要在该文件夹中，创建子目录，用于存储工程文件和工程备份文件。
步骤  
|   
  
---|---  
ftp创建工程文件存储目录| 在NAS共享文件夹（示例为**/home/ftpuser** ）中，创建一个子文件夹（推荐命名为WEB-INF），用于存储工程文件本文示例****/home/ftpuser** /WEB-INF**  
ftp创建工程备份文件存储目录| 备份还原文件存储路径默认为../backup即在工程文件存储目录同级，生成backup文件夹，用于存储平台备份本文示例为****/home/ftpuser** /backup**  
### 3.2 上传文件到存储目录（按需选做）
如需在**部署新项目** 时接入FTP作为文件服务，**请勿执行** 本步骤！
对于已部署好的工程，如需接入/替换集群文件服务，需要先将工程文件上传到FTP存储目录中。
  * 如当前工程已配置文件服务，请将原文件服务器工程存储目录下的所有文件，拷贝到FTP准备的工程存储目录。请注意原文件服务器类型是否支持后端拷贝等传输细节（例如minio等S3类型，必须前端下载文件再上传）  

  * 如当前工程未配置文件服务，首次接入文件服务，请将工程某个节点下的以下文件夹拷贝到FTP


本文以上节的ftp存储目录「**/home/ftpuser** 」为例演示，请根据服务器情况自行调整。
  
| 步骤| 说明  
---|---|---  
1| **拷贝工程文件**|  将原工程**/webroot/WEB-INF** 目录下的**assets、dpworks、reportlets、resources、schedule、treasures** 文件夹，拷贝到ftp的**/home/ftpuser/WEB-INF** 目录下  
2| **拷贝工程备份文件**|  将原工程**/webroot/WEB-INF/ backup**目录下的内容，拷贝到ftp的**/home/ftpuser/ backup**目录下  
附：文件说明
原工程文件  
| 文件夹内容说明  
---|---  
/webroot/WEB-INF/assets| 存放着以下内容：工程Excel原始文件信息FineReport模板备份文件驱动管理上传的驱动通用的共享持久化目录  
/webroot/WEB-INF/dpworks| FineDataLink任务相关的配置文件如不存在该文件夹，说明工程没有使用FDL相关功能，可忽略  
/webroot/WEB-INF/reportlets| FineReport模板存放目录  
/webroot/WEB-INF/resources| 存放工程相关的资源配置文件  
/webroot/WEB-INF/schedule| 定时调度生成的文件  
/webroot/WEB-INF/treasures| 云端运维生成的数据包  
/webroot/backup| 工程历史备份文件  
## 4\. 准备FTP信息
信息  
| 说明  
---|---  
编码| Linux 系统默认：**UTF-8** Windows 系统默认：**GBK**  
主机  
| vsftpd 服务所在服务器 IP  
端口| 默认为 **21** 端口用于客户端发起命令连接 FTP 服务器  
用户名| 2.3 节准备的 FTP 用户，示例为**ftpuser** 所准备的用户需要有存储目录的读写执行权限  
密码| 2.3 节准备的 FTP 用户的密码如集群与该文件服务已连接，文件服务密码出现变更后，请在集群配置中进行修改并确认连接成功  
传输模式| 即 2.4 节选择的 FTP 工作模式：**主动/被动** 如集群与该文件服务已连接，FTP 主被动模式出现变更后，请在集群配置中进行修改并确认连接成功  
路径| 3.1节创建的工程文件存储目录本示例为：/home/ftpuser/WEB-INF/1）注意是**工程文件存储路径** ，而非用户目录路径2）Linux系统中部署的FTP服务，路径必须是**以斜杠/开头的 绝对路径**，非斜杠开头会被识别为用户相对路径。3）Windows系统中部署的FTP服务，可填写相对路径/WEB-INF  
## 5\. 集群接入文件服务
支持在以下情况下接入 FTP 作为集群文件服务，请根据情况自行选择，任选其一即可。
### 5.1 部署新集群时接入
在「[部署新项目-项目设置](<https://help.fanruan.com/fineops/doc-view-59.html>)」时，可接入自备的 FTP 作为集群文件服务。
此情况下，请确保准备的工程存储目录文件夹中内容为空，不存在任何数据，否则无法成功对接。
1）文件服务选择「对接已有文件服务」。
![](https://help.fanruan.com/core/style/lod.png)  

2）在「文件服务」信息填写处：
  * 协议：FTP  

  * 编码、主机、端口、用户名、密码、传输模式、路径：填写第四章准备的FTP信息


3）点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 5.2 运维平台集群管理接入
项目部署成功后，在运维平台的「集群管理」中，可为项目接入自备的 FTP 作为文件服务。
**使用前提：请务必参考3.2节，将当前工程文件上传到准备好的FTP存储目录中。**
1）管理员登录运维平台，选中指定项目。
2）点击「维护>集群管理」，对「文件服务器」进行配置。
![](https://help.fanruan.com/core/style/lod.png)  

3）输入相关信息
  * 协议：FTP  

  * 编码、主机、端口、用户名、密码、传输模式、路径：填写第四章准备的FTP信息


4）点击「保存」，提示「连接成功」，即代表可正常对接。
![](https://help.fanruan.com/core/style/lod.png)
### 5.3 管理系统集群管理接入
在帆软应用的「管理系统>集群管理」中，可为项目接入自备的FTP作为文件服务。
**使用前提：请务必参考3.2节，将当前工程文件上传到准备好的FTP存储目录中。**
1）管理员登录帆软应用，点击「管理系统>智能运维>集群配置」。
2）在开启了状态服务器的前提下，在文件一致设置中选择「文件服务器共享」。
3）点击「编辑」填写相关信息，点击「测试连接」，提示「测试连接成功」，即代表可正常对接。
  * 协议：FTP  

  * 编码、主机、端口、用户名、密码、传输模式、路径：填写第三章准备的FTP信息


![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI对接MinIO实现文件服务](<index.php?doc-view-2021.html>)
[下一篇：FineBI对接HDFS实现文件服务 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1234.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
