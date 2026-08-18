---
title: FineBI个人试用版启动常见问题
doc_id: 811
url: https://help.fanruan.com/finebi6.X/doc-view-811.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:31
---

> 1. 概述1.1 版本FineBI服务器版本6.01.1 问题描述本文简单介绍，FineBI工程启动失败的原因和解决方案。1.2 替代方案普通用户个人使用，推荐直接使用：FineBI 在线分析平台&nb

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI个人试用版启动常见问题
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[14](<edition-list-811.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
  
---  
6.0  
### 1.1 问题描述
本文简单介绍，FineBI工程启动失败的原因和解决方案。
### 1.2 替代方案
普通用户个人使用，推荐直接使用：[FineBI 在线分析平台](<https://pcdemo.finebi.com/webroot/decision/?online_bi_from=0402>) ，免安装快速体验，支持在线分享。
## 2\. 磁盘剩余可用空间不足
### 2.1 Windows/Linux磁盘剩余空间不足
**问题描述：**  

FineBI启动失败，在%FineBI%/logs下打开fanruan.log日志，存在报错在关键词：
  * java.io.IOException: 设备上没有空间
  * 磁盘剩余空间不足


**原因分析：**
待安装目录，磁盘剩余可用空间不足。
**解决方案：**
1）联系运维，对服务器磁盘空间进行扩容。
2）清理磁盘
使用df -h命令检查当前各分区磁盘占用大小，如下图所示：
![](/core/style/lod.png)
使用命令du -sh *查看当前目录下每个文件夹大小，如下图所示：
![](/core/style/lod.png)
将不需要的文件清理即可。
### 2.2 Mac电脑内存不足导致无法访问
**问题描述：**
启动FineBI，进程还在，但无法访问工程，提示「找不到主机」。
**原因分析：**
部署在个人Mac电脑时，内存默认分配为1.2g。若电脑总内存过小，或其他软件占用了大量内存，导致剩余可用内存过小，则会出现该问题。
**解决方案：**
1）建议更换一个服务器部署，提升硬件配置。
2）如需继续在该设备启动工程，建议在启动FineBI时，关闭其他无用进程，保证充足的可用内存。
## 3\. 权限不足
### 3.1 未使用管理员权限启动BI
Windows系统，推荐使用管理员身份运行FineBI。如下图所示：  

![](/core/style/lod.png)
### 3.2 文件权限不足
**问题描述：**  

FineBI启动失败，在%FineBI%/logs下打开fanruan.log日志，存在报错在关键词：
  * permission denied
  * Database is not initialized


**原因分析：**
启动工程的用户权限不足
**解决方案：**
请检查下用户读写权限，可使用命令chmod -R 777，给对应文件夹配置权限。
### 3.3 临时目录创建失败
**问题描述：**  

FineBI启动失败，在%FineBI%/logs下打开fanruan.log日志，存在报错在关键词：
  * Failed to create local dir in /home/ap/bin/ROOT/temp/spark


**原因分析：**
启动工程的用户权限不足，导致spark临时目录创建失败
**解决方案：**
请检查下用户读写权限，可使用命令chmod -R 777，给临时目录对应路径配置权限。
## 4\. 安装包问题
### 4.1 内部文件错误
**问题描述：**
FineBI启动失败，报错提示为An internal ereor occurred(error code:34)
![](/core/style/lod.png)
**原因分析：**
下载的安装包不完整。
**解决方案：**
重新下载安装包安装。
### 4.2 解压缩失败导致闪退
**问题描述：**  

Windows系统，安装包部署后出现闪退的情况，日志停在start unzip file:D:\app\FineBI5.1\\...\assist\update\update.zip
**原因分析：**
启动卡在解压缩插件文件的步骤 ，关键词start unzip
**解决方案：**
手动把插件的压缩文件解压缩之后放到plugins文件夹里，即可启动成功
## 5\. 进程异常
工程启动异常或失败时，需要依次检查以下进程问题。
### 5.1 FineBI重复启动两个线程
1）输入命令 ps -ef|grep java ，查看当前路径下的BI 启动了多少线程，如下图所示：
![1588220199305329.png](/core/style/lod.png)
2）若有多个线程则全部结束，输入 kill -9 进程号，如下图所示：
![1588224754844662.png](/core/style/lod.png)
### 5.2 FineBI端口被占用
**问题描述：**  

部署后闪退/前端无法访问，日志里有关键词Address already in use
**原因分析：**
端口号端口号只能被一个进程占用。FineBI启动所需的端口目前被其他进程占用中。
**解决方案：**
1）使用lsof -i:端口号 命令检查当前端口是否被占用，若如下图所示，则表示端口未被占用：
![1588219468834145.png](/core/style/lod.png)
注：若报错-bash: lsof-i:xx: command not found，则需要输入命令 yum install lsof ，才能使用 lsof 命令。
若如下图所示，则表示进程 ID 为 8152 的 java 应用占用 80 端口：
![1588224939231636.png](/core/style/lod.png)
2）端口号只能被一个进程占用，若当前端口号已经被占用，则需要将 BI 服务器的端口号调整为未被占用的端口号。
详情参见：[Tomcat 端口配置](<https://help.fanruan.com/finereport/doc-view-770.html>) 、[如何修改FineBI端口号](<https://help.fanruan.com/finebi6.0/doc-view-326.html>) 。
### 5.3 webapps目录下存在多个工程/没有工程
进入 BI 安装目录，查看 %FineBI%\webapps 目录下是否有多个webroot文件或没有文件。
若没有，需要将安装的 webroot 文件放置在 webapps 下，如下图所示：
注：备份文件都以压缩文件夹形式存放，或者把备份文件拷贝到非工程所在目录，确保 Web 容器里只有一个名为webroot的工程。
![1588225747220501.png](/core/style/lod.png)
### 5.4 db.lck 文件报错
Windows 使用其他工具打开 FineDB 数据库并且未关闭，检查是否有其他软件连接 FineDB 内置数据库，如果有，需要关闭工程并重启 BI 。
## 6\. hostname问题
### 6.1 UnknownHostException
**问题描述：**  

FineBI启动失败，界面报错61300110Spider计算引擎服务初始化异常
查看%FineBI%/logs日志，报错为UnknownHostException
**解决方案：**
登录安装服务器，查看hosts文件（Linux为/etc/hosts，Windows通常在C盘下），添加该服务器IP和对应hostname。
### 6.2 获取hostname失败
**问题描述：**
FineBI访问失败，前端提示「获取hostname失败，请检查服务器hostname是否正常或重新配置hostname」
![](/core/style/lod.png)
**原因分析：**
服务器hosts文件中，没正确配置好映射关系
**解决方案：**
根据hostname命令返回的值，配置到/etc/hosts文件中，配置127.0.0.1 具体的hostname
## 7\. 其他问题
### 7.1 安装FineBI后，没有配置管理员用户名密码界面？
该问题需要排查下是否之前安装过 FineBI ，此处使用了之前安装过的路径重新安装。
若安装过，需将之前安装的版本完全卸载干净再重新安装。
### 7.2 tools.jar异常
**问题描述：**
Mac环境下，FineBI部署到tomcat中，启动工程时报错「tools.jar异常」
![](/core/style/lod.png)
**原因分析：**
tomcat部署，使用的tools.jar必须和环境变量中配置的jdk相一致。
**解决方案：**
1）设置好正确的JAVA环境路径。
2）更换tools.jar。
### 7.3 注册码异常
若启动 FineBI 输入注册码弹窗提示异常，可进入 C:\Users\用户\\.FineBI60目录下打开的FineBIEnv.xml文件，如下图所示：
![](/core/style/lod.png)
更换已有的激活码，如下图所示：
![](/core/style/lod.png)
激活码获取方法：登录：[FineBI官网](<https://www.fanruan.com/finebi>)，点击「免费试用」，输入相关信息即可获取激活码。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：生成安全密钥文件按钮说明](<index.php?doc-view-996.html>)
[下一篇：FineBI个人试用版安装常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-637.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
