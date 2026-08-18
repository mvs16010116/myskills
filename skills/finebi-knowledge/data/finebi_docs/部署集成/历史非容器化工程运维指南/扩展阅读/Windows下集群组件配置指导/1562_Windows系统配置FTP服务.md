---
title: Windows系统配置FTP服务
doc_id: 1562
url: https://help.fanruan.com/finebi6.X/doc-view-1562.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:53
---

> 1.&nbsp;概述1.1&nbsp;应用场景定时任务完成后，希望把生成的附件上传到其他服务器的 FTP 上面，需要提前准备已配置的 FTP 服务器。配置开启集群 若选择文件服务器共享，协议选择 FTP

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统配置FTP服务
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[4](<edition-list-1562.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-11-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
  * 定时任务完成后，希望把生成的附件上传到其他服务器的 FTP 上面，需要提前准备已配置的 FTP 服务器。
  * [配置开启集群](<https://help.fanruan.com/finebi6.0/doc-view-436.html>) 若选择文件服务器共享，协议选择 FTP 时，需要提前准备已配置的 FTP 服务器。


### 1.2 功能简介
FTP 是 File Transfer Protocol（文件传输协议）的英文简称，而中文简称为「文传协议」，用于 Internet 上控制文件的双向传输。
本文描述的配置流程以 Windows Server 2012 Standard 服务器为例，若使用其他版本的 Windows Server 操作系统，配置方法类似。
注：建议使用更安全的协议 SFTP，详情请参见：[Windows系统配置使用SFTP](<https://help.fanruan.com/finebi6.X/doc-view-1563.html>)
## 2\. 操作步骤 
[](<https://kms.fineres.com/pages/viewpage.action?pageId=168009413>)
### 2.1 配置FTP服务器
1）从启动栏打开服务器管理器，选择添加角色和功能
![1559045954413292.png](/core/style/lod.png)  

2）点击进入「服务器选择」界面，选择服务器，然后点击「下一步」
![1559045984581445.png](/core/style/lod.png)
3）勾选 Web 服务器(IIS)后，弹窗进行确认，点击「添加功能」
![1559046014930365.png](/core/style/lod.png)
4）然后点击两次「下一步」，进入「角色服务」界面，勾选「FTP 服务」
![1559046053122888.png](/core/style/lod.png)
5）点击「下一步」，进行确认安装
![1559046075561819.png](/core/style/lod.png)
6）开始安装
![1559046098518882.png](/core/style/lod.png)
### 2.2 添加FTP站点
1）从服务器管理器的工具菜单栏，打开「IIS 管理器」
![1559046128573748.png](/core/style/lod.png)
2）选择网站选项，点击右侧的 添加 FTP 站点  

![1559046145275802.png](/core/style/lod.png)
3）填写 FTP 站点名称和物理路径，物理路径即 FTP 上传下载文件的保存目录（可以在任意盘新建，名称自定义）  

![1559046169601585.png](/core/style/lod.png)
4）绑定和 SSL 设置：勾选自动启动 FTP 站点，选择「无 SSL」
**![1559046193293746.png](/core/style/lod.png)**
5）按照下图，选择身份验证和授权、权限
![1559046276694310.png](/core/style/lod.png)
### 2.3 新建用户和测试FTP
1）打开计算机管理，在本地用户和组—用户中，右键新建用户
![1559046330474864.png](/core/style/lod.png)
2）给新用户配置用户名、密码，建议勾选「密码永不过期」
![1559046353344670.png](/core/style/lod.png)
注意：密码建议英文字母大小写+数字，当密码过于简单时无法创建，本文档FAQ中提供有解决办法。  

3）创建完毕：  

![1559046377870663.png](/core/style/lod.png)
4） 拷贝工程里的 WEB-INF 文件夹，并粘贴到设置的物理路径下  

5） 将浏览器地址栏访问 ftp://ip，这步需要用户名和密码登录 FTP
![1559046509326665.png](/core/style/lod.png)
![1559046509369652.png](/core/style/lod.png)
至此，我们在 Windows Server 上成功搭建了文件服务器。  

## 3\. 平台配置文件服务器
1） Windows Server 编码默认为 GBK，在平台配置文件服务器时要选择对应的编码。
2） 平台配置文件服务器时，ftp 路径填写 /WEB-INF
![1628564964501237.png](/core/style/lod.png)
注1：按照文档部署的 FTP 服务，Linux 系统填写绝对路径，如用户名为 ftpuser ，那么路径为 /home/ftpuser/WEB-INF，Windows 系统填写相对路径 /WEB-INF 即可。
注2：配置集群更多步骤请参见：[配置集群](<https://help.fanruan.com/finebi6.0/doc-view-436.html>)
## 4\. 常见问题
1）新建 FTP 时可能提示密码不符合复杂度要求。如下图所示：
![1559046666839893.png](/core/style/lod.png)
可以在命令行输入gpedit.msc，「计算机配置 -> Windows 设置 -> 安全设置 -> 账户策略 -> 密码策略」，在右边列表，可以根据自己需求进行修改。
![1559046675693930.png](/core/style/lod.png)
2） 访问 ftp://ip 时报错
在浏览器访问 ftp://ip 时，报错：200 Switching to ASCII mode.227 Entering Passive Mode (0,0,0,0,227,175)
解决方案：打开「网络和共享中心>Internet选项>高级」，将使用被动FTP（用于防火墙和DSL调制解调器的兼容）选项去掉即可。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统安装配置单机Redis](<index.php?doc-view-1557.html>)
[下一篇：Windows系统配置使用SFTP ![](/core/style/forward.png) ](<index.php?doc-view-1563.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
