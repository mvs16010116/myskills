---
title: Windows系统配置使用SFTP
doc_id: 1563
url: https://help.fanruan.com/finebi6.X/doc-view-1563.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:54
---

> 1.&nbsp;概述&nbsp;SFTP 服务器，在 Linux 和 Mac 系统中是自带的。Windows 系统中需要安装 freeSSHd 进行实现。2. 下载 freeSSHd点击&nbsp;链接

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统配置使用SFTP
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[1](<edition-list-1563.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-08-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
SFTP 服务器，在 Linux 和 Mac 系统中是自带的。Windows 系统中需要安装 freeSSHd 进行实现。
## 2\. 下载 freeSSHd
点击 [链接](<http://www.freesshd.com/?ctt=download>) ，下载 freeSSHd 。如下图所示：
![10.png](/core/style/lod.png)
## 3\. 安装 freeSSHd
1）双击下载的freeSSHd.exe，点击「Next」，如下图所示：
![1595917186288082.png](/core/style/lod.png)
2）根据实际情况选择 SFTP 服务器安装路径，点击「Next」。如下图所示：
![1595917316194615.png](/core/style/lod.png)
3）点击「Next」，如下图所示：
![1595917372985781.png](/core/style/lod.png)
4）点击「Next」，如下图所示：
![1595917426179591.png](/core/style/lod.png)
5）点击「Next」，如下图所示：
![1595917538489623.png](/core/style/lod.png)
6）点击「Next」，如下图所示：
![1595919031483262.png](/core/style/lod.png)
7）点击「Next」，如下图所示：
![1595917696212259.png](/core/style/lod.png)
8）提示：需要安装私有密钥，点击「是」。如下图所示：
![1595917781121266.png](/core/style/lod.png)
10）提示：是否把 freeSSHd 作为一个服务安装到服务中，点击「否」。如下图所示：
![1595917914716642.png](/core/style/lod.png)
11）点击「Finish」，如下图所示：
![1595917954936122.png](/core/style/lod.png)
## 4\. 配置 freeSSHd
### 4.1 添加用户
添加用户，设置用户名和密码，勾选「SFTP」，如下图所示：  

![21.png](/core/style/lod.png)
### 4.2 设置 IP、端口号
点击「SSH」，设置 SFTP 服务器的 IP 和端口号。如下图所示：  

![1595918830525094.png](/core/style/lod.png)
### 4.3 设置登录授权选项
点击「Authentication」，设置项如下图所示：  

注：Public key authentication 指通过公钥登录。
![1595919155801157.png](/core/style/lod.png)
### 4.4 设置 SFTP 服务器根目录
设置 SFTP 服务器根目录。如下图所示：  

![1595919367680267.png](/core/style/lod.png)
### 4.5 启动服务器 Server Status
如下图所示：  

![1595919481271452.png](/core/style/lod.png)
## 5\. 测试 SFTP 服务器是否配置成功
cmd 命令行输入sftp 用户名@IP，输入密码。如下图所示：
![1595920848233267.png](/core/style/lod.png)
**问题描述：**
cmd 命令行输入sftp 用户名@IP后，可能会出现下图所示错误：
**![1595921887743403.png](/core/style/lod.png)**
**解决方案：**
删除上图所示红框路径下的.ssh文件夹，如下图所示：
![1595921906413240.png](/core/style/lod.png)
## 6\. 平台配置文件服务器
注：开启集群完整步骤请参见：[Linux 系统部署集群](<https://help.fanruan.com/finereport/doc-view-2643.html>)、[Linux系统自动化部署集群](<https://help.fanruan.com/finereport/doc-view-2948.html>)、[Windows 系统部署集群](<https://help.fanruan.com/finereport/doc-view-2818.html>)
1）拷贝工程里的 WEB-INF 文件夹，并粘贴到本文 4.4 节设置的 SFTP 根目录下。如下图所示：
![4.png](/core/style/lod.png)
2） 平台配置文件服务器时，ftp 路径填写/WEB-INF。如下图所示：
![6.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统配置FTP服务](<index.php?doc-view-1562.html>)
[下一篇：Windows系统搭建Web集群 ![](/core/style/forward.png) ](<index.php?doc-view-1571.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
