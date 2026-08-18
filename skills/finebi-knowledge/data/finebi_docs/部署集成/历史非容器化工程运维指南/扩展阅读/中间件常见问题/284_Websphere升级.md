---
title: Websphere升级
doc_id: 284
url: https://help.fanruan.com/finebi6.X/doc-view-284.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:48
---

> 1、描述因为 FineBI 内置 Spider 引擎不支持 JDK 1.6，且 WebSphere 版本仅支持&nbsp;8.5.5.13、JDK1.8，因此我们需要将 WebSphere 选择升级到&

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Websphere升级
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[8](<edition-list-284.html>)
* 最近更新：[Kevin-s](<user-space-197867.html>) 于 2020-10-23 
[](<javascript:;>) [](<javascript:>)
## 1、描述
因为 FineBI 内置 Spider 引擎不支持 JDK 1.6，且 WebSphere 版本仅支持 8.5.5.13、JDK1.8，因此我们需要将 WebSphere 选择升级到 8.5.5.13。
## 2、检查当前 WebSphere 环境
登录到 was 控制台查看当前 WebSphere 版本，可以看到当前版本为 8.5.5.0。如下图：
![461.png](/core/style/lod.png)
该 WebSphere 版本为 8.5.5.0，因此需要升级。
## 3、升级步骤
### 3.1下载 was 升级包和 JDK 包
  1. 下载 8.5.5.13 或更高版本的升级包，下载地址为：<https://www.ibm.com/support/pages/recommended-updates-websphere-application-server#ver85_0>
百度云下载链接：[https://pan.baidu.com/s/1JQYnpGD7DmbzQ---cPHZSw ](<https://pan.baidu.com/s/1JQYnpGD7DmbzQ---cPHZSw>) 密码: tg0f 
![376.png](/core/style/lod.png)  

  2. 下载后上传至服务器，将 was 更新的三个介质包放在同一目录下解压，was 更新包解压后的结果如下图：
![](/core/style/lod.png)  

  3. 将 SDK 压缩包放在另一目录下解压，SDK 解压后的结果如下图：
![](/core/style/lod.png)  



### 3.2 升级 was
使用 IM（installation management）来升级 was。
  1. 首先在 /opt/IBM/InstallationManager/eclipse目录下执行 ./launcher 启动安装控制管理台；
出现如下图界面，点击左上角的File<Preferences...，添加 was 更新包的介质存储库位置，如下图：
![312.png](/core/style/lod.png)  

  2. 选择前面解压 was 更新包的解压路径下的 repository.config 文件，如/opt/was/wasnd/repository.config，如下图：
![](/core/style/lod.png)  

  3. 点击 ok，如下图：
![](/core/style/lod.png)  

  4. 选择Update，后面步骤按需选择，或者默认，如下图：
![](/core/style/lod.png)  

  5. 更新完成后界面如图，点击finish完成更新，如下图：
![](/core/style/lod.png)  

  6. 在路径 /opt/IBM/WebSphere/AppServer/bin下执行命令****./versionInfo.sh 查看当前版本，显示已经更新到了 8.5.5.16 版本，如下图：
![](/core/style/lod.png)  

  7. 启动应用程序，登录 was 控制台查看版本，为更新后的 8.5.5.16，如下图：
![341.png](/core/style/lod.png)  



### 3.3 安装 SDK1.8
  1. 在 /opt/IBM/InstallationManager/eclipse 目录下，执行 ./launcher 启动安装控制管理台，
出现如下图界面，点击左上角的 File<Preferences...来添加 SDK 的介质存储库位置，如下图；
![312.png](/core/style/lod.png)  

  2. 选择前面 SDK 解压路径下的 repository.config 文件，如/opt/was/update/repository.config，点击 ok，如下图：
![](/core/style/lod.png)  

  3. 选择install，如下图：
![](/core/style/lod.png)  

  4. 选择名称后面带有Optional 的选项，点击 Next，如下图：
![](/core/style/lod.png)  

  5. 后面步骤默认即可，到最后点击install安装，等待安装完成，点击finish，至此 SDK 安装完成，如下图：
![](/core/style/lod.png)  

  6. 升级验证
在 /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin目录下执行managesdk.sh -listAvailable ，则会显示有1.8_64的名称，至此安装成功，如下图：
![89-.png](/core/style/lod.png)  



### 3.4 配置 was 使用 SDK1.8
  1. 在终端配置
执行以下命令：
[code][root@localhost ~]# cd /opt/IBM/WebSphere/AppServer/bin  
         [root@localhost bin]# ./managesdk.sh -listAvailable   
                 CWSDK1003I: Available SDKs :  
                 CWSDK1005I: SDK name: 1.8_64_bundled  
                 CWSDK1005I: SDK name: 1.8_64  
                 CWSDK1001I: Successfully performed the requested managesdk task.  
         [root@localhost bin]# ./managesdk.sh -getNewProfileDefault   
                 CWSDK1007I: New profile creation SDK name: 1.8_64_bundled  
                 CWSDK1001I: Successfully performed the requested managesdk task.  
         [root@localhost bin]# ./managesdk.sh -setNewProfileDefault -sdkName 1.8_64  
                 CWSDK1022I: New profile creation will now use SDK name 1.8_64.  
                 CWSDK1001I: Successfully performed the requested managesdk task.  
         [root@localhost bin]# ./managesdk.sh -enableProfileAll -sdkName 1.8_64     
                 CWSDK1017I: Profile AppSrv01 now enabled to use SDK 1.8_64.  
                 CWSDK1001I: Successfully performed the requested managesdk task.  
         [root@localhost bin]# 
[/code]
  2. 启动应用程序，登录 was 控制台，选择 server1，如下图：
![](/core/style/lod.png)  

  3. 选择 Java SDK 选项，如下图:
![33.png](/core/style/lod.png)  

  4. 勾选 1.8_64 用作缺省值，如下图：
![26.png](/core/style/lod.png)  

  5. 点击保存到主配置，如下图：
![555.png](/core/style/lod.png)  

  6. 此时，缺省值处显示为 true，至此，完成，如下图：
![356.png](/core/style/lod.png)  



  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Weblogic部署相关问题](<index.php?doc-view-48.html>)
[下一篇：Websphere升级最新的SDK ![](/core/style/forward.png) ](<index.php?doc-view-285.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
