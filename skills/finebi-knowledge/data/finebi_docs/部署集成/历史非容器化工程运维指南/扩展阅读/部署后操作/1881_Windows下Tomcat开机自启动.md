---
title: Windows下Tomcat开机自启动
doc_id: 1881
url: https://help.fanruan.com/finebi6.X/doc-view-1881.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:38
---

> 1. 概述本文介绍 Windows 系统安装 Tomcat 后，设置开机自启动的方法。注1：Linux 系统安装 Tomcat 后，设置开机自启动的方法请参见：Linux下Tomcat开机自启动注2：用

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows下Tomcat开机自启动
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[5](<edition-list-1881.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-05-26 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍 Windows 系统安装 Tomcat 后，设置开机自启动的方法。
注1：Linux 系统安装 Tomcat 后，设置开机自启动的方法请参见：[Linux下Tomcat开机自启动](<https://help.fanruan.com/finebi6.0/doc-view-1878.html>)
注2：用户请自行百度 Tomcat 解压版与安装版区别，根据实际情况选择方案。
## 2\. Tomcat 为解压版
本章示例环境为 Windows 10+Tomcat 9.0.38+JDK1.8.0_152 。
### 2.1 方案一
该方法是将 Tomcat 启动程序添加到开始菜单的开机启动文件夹中，实现开机时自启动。
1）使用快捷键 Win+R，在运行对话框中输入shell:startup，打开开始菜单的开机启动文件夹。如下图所示：
![1641886689459167.png](/core/style/lod.png)
2）进入%TOMCAT_HOME%/bin目录，为startup.bat文件生成快捷方式，将生成的快捷方式拖入到开机启动文件夹中。如下图所示：
![1641886833727411.png](/core/style/lod.png)
### 2.2 方案二
该方法将 Web 应用服务器启动程序注册为系统服务，系统开机后，服务器就会自动启动，并且在前台也不会有运行窗口。
注：该方法仅支持启动，若需要停止 Tomcat 服务，可在 %TOMCAT_HOME%/bin 目录下启动 shutdown.bat （Windows 系统）。
#### 2.2.1 工具准备
点击下载工具包：[工具包.rar](<doc-download-/uploads/file/20191217/工具包.rar> "下载资料")，下载完成后解压缩，将解压得到的两个文件放到到某个路径下，示例是将其放到D:\bb\工具包目录下。
![4.png](/core/style/lod.png)
#### 2.2.2 注册服务
使用 instsrv.exe 将 srvany.exe 注册为系统服务，有关 instsrv.exe 工具的使用方法，下面给出简单介绍。
instsrv.exe 这个工具会将 Win32 程序注册为系统服务，其命令用法如下：
  * instsrv [服务名] [srvany 的绝对路径]：新增一个系统服务
  * instsrv [服务名] REMOVE：删除一个系统服务


使用快捷键 Win+R，以管理员身份运行 cmd，打开命令提示符窗口，使用 cd 命令进入 instsrv.exe 所在目录，输入命令instsrv FRServer D:\bb\工具包\srvany.exe，并回车。如下图所示：
注：命令中的路径需根据实际情况修改。
![1641888068515717.png](/core/style/lod.png)
#### 2.2.3 服务添加启动程序
在D:\bb\工具包目录下新建一个 FR.bat 文件，用来启动 Tomcat 服务器。文件内容如下：
[code]
    E: cd "E:\apache-tomcat-9.0.38\bin" start startup.bat  
    
[/code]
![1641888348173767.png](/core/style/lod.png)
使用快捷键 Win+R，在运行对话框中输入 regedit ，打开注册表编辑器窗口，进入HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FRServer目录下。
1）选中 FRServer ，右击「新建>项」，名为Parameters
2）选中 Parameters ，右击「新建>字符串值」，名为Application
3）双击 Application ，数值数据为‪D:\bb\工具包\FR.bat
![8.png](/core/style/lod.png)
#### 2.2.4 启动服务
在「服务」中，找到我们注册好的系统服务 FRServer，可以看到该服务的启动类型为自动，也就是说开机后该服务自启，如下图选中并启动该服务即可。
![9.png](/core/style/lod.png)
## 3\. Tomcat 为安装版
本章示例环境为 Windows 11+Tomcat 8+JDK1.8（需提前配置 JAVA_HOME 环境变量）。
### 3.1 配置步骤
**1）验证 Tomcat 基础运行状态**
启动 Tomcat：双击%Tomcat_HOME%/bin/startup.bat，观察控制台是否无报错。
访问测试：浏览器打开http://localhost:8080，应看到 Tomcat 默认页。若失败，请检查端口冲突（如 8080 被占用）。
**2）注册为 Windows 服务（如未自动注册）**
Tomcat 的 EXE 安装版，通常会将其注册为系统服务，如未注册，可参考本节注册系统服务。
  * 进入%Tomcat_HOME%/bin目录下，找到 service.bat 批处理文件
  * 按住「Win+R」进入 cmd 命令提示符窗口，将 service.bat 文件拖动到窗口中
  * 输入一个空格，然后输入install tomcat并回车，即可将该 Tomcat 注册为系统服务


注1：如报错「 JAVA_HOME not defined 」，请检查 JDK 环境变量。
注2：如服务名冲突，请将命令中的tomcat改用唯一名称（如 Tomcat9-YourApp）。
![1641892290810507.png](/core/style/lod.png)
**3）设置服务启动类型为自动**
按住「Win+R」，输入 services.msc，回车，进入「服务」界面
找到 Tomcat 服务，服务名称通常为 Apache Tomcat [版本号] 或类似名称（如 Tomcat8）
右键点击「服务>属性」，将启动类型改为「自动」，点击「应用>确定」即可。
![2.png](/core/style/lod.png)
### 3.2 删除服务
若想删除本文 3.1 节的服务，进入%Tomcat_HOME%\bin目录下，找到service.bat批处理文件，然后打开 cmd 命令提示符窗口，将service.bat文件拖动到窗口中，空一格输入remove tomcat并回车。如下图所示：
![1641956536288334.png](/core/style/lod.png)
## 4\. 注意事项
### 4.1 500 报错
**问题描述**  

使用本文第 3 节的方法来设置服务器开机自启动时，如果在访问报表工程时遇到下图所示 500 报错的问题。  

![1576578577842905.png](/core/style/lod.png)
**解决方案**
参考：[Tomcat 为安装版本](<https://help.fanruan.com/finereport/doc-view-1021.html#5>)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Redis单机开机自启动](<index.php?doc-view-1880.html>)
[下一篇：Nginx 开机自启动脚本 ![](/core/style/forward.png) ](<index.php?doc-view-1877.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
