---
title: FineBI个人试用版安装常见问题
doc_id: 637
url: https://help.fanruan.com/finebi6.X/doc-view-637.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:32
---

> 1. 安装必知必会1.1 安装有哪几种方式？FineBI 安装有两种方式：安装方式适用场景说明本机安装个人试用推荐直接使用&nbsp;FineBI 6.0 在线分析平台&nbsp;，无需下载安装，即可试

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI个人试用版安装常见问题
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[22](<edition-list-637.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-02-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 安装必知必会
### 1.1 安装有哪几种方式？
FineBI 安装有两种方式：
安装方式| 适用场景| 说明  
---|---|---  
本机安装| **个人试用****推荐直接使用****[FineBI 6.0 在线分析平台](<https://pcdemo.finebi.com/webroot/decision/>) ，无需下载安装，即可试用数据分析功能**本机安装一般适用于 IT 用户对FineBI试用操作阶段，工程一般不共享给其他员工。| 直接下载与操作系统匹配的 FineBI 安装包，按照 [FineBI 安装与启动](<https://help.fanruan.com/finebi6.0/doc-view-260.html>)文档步骤执行操作  
  
服务器安装| **企业正式工程****企业测试工程** 当企业有多个用户需要使用一个 BI 工程时，将 BI 安装在服务器上，管理员启动 BI ，其他员工即可在浏览器中通过输入安装地址访问 BI （例如http://ip:端口号/webroot/decision），但若关闭 BI 工程，那其他用户将无法通过访问 IP 地址，登录 BI 。因此，将 BI 部署在服务器上，能让 BI 保持 24 小时的开放状态，用户即可随时通过 IP 地址访问 BI ，从而实现系统平台的作用，达到企业整体工作的业务活动需求。|   
  
使用 Web 服务器部署，FineBI 支持的Web服务器有 [Tomcat](<https://help.fanruan.com/finebi6.0/doc-view-45.html>) 、[WebLogic](<https://help.fanruan.com/finebi6.0/doc-view-46.html>) 、[JBoss](<https://help.fanruan.com/finebi6.0/doc-view-49.html>)（Wildfly） 、[WebSphere](<https://help.fanruan.com/finebi6.0/doc-view-50.html>) ，需要先部署好 Web 服务器再进行 FineBI 的部署，Web 容器部署具有更高的安全性和可扩展性。  
### 1.2 本机安装的 FineBI 能不能与其他电脑的 FineBI 互相同步？
不能。
虽然启动 FineBI 工程后，登录和数据分析等操作在浏览器内实现，但是FineBI的计算、更新等等核心操作都在服务器内进行。因此， FineBI 本地试用版用户在工程内上传的数据和分析仅存储在个人电脑内，无法在多台电脑实现同步。
### 1.3 FineBI 的公共链接分享不出去，如何将分析成功分享给其他人？
安装 FineBI 本地版的用户，建议使用 [在线版FineBI](<https://pcdemo.finebi.com/webroot/decision/>) 体验功能。
如果需要再本地实现公共链接分享，需要修改链接并受到环境限制，详情见 [分享公共链接第 5 节](<https://help.fanruan.com/finebi6.X/doc-view-164.html#529ec47f05779198>)。
### 1.4 直接下载的安装包是不是已经集成了Tomcat和jdk？
[FineBI 官网](<https://www.finebi.com/product/download>) 提供的安装包包含 Windows、Mac、Linux 版本，均已集成了 Tomcat 和 jdk1.8。
若直接安装下载的安装包版本，则不需要再单独部署 jdk 。
### 1.5 如何让用户访问到 BI？ 如何验证用户的电脑跟服务器能通信？
通过访问 BI 的安装地址登录 BI 。获取安装地址后，在浏览器输入，跳转访问 BI 登录界面。若能进入登录界面即用户的电脑和服务器能顺利通信。
### 1.6 如何获取纯净的工程？
在下载 FineBI 后，如何获得一个无目录、无仪表板以及无内置数据的纯净的工程，有以下三步：
**1）删除目录**
超管登录FineBI系统，点击「管理系统>目录管理」，在目录列表中选择「批量删除」，将所有挂出在目录的仪表板全部删除，如下图所示：
![](/core/style/lod.png)
**2）取消发布数据**  

超管登录FineBI系统，点击「管理系统>公共数据管理」，点击「立即公共数据检测」，点击「全部选择>取消发布」。如下图所示：
![](/core/style/lod.png)
**3）删除主题**
超管登录FineBI系统，点击「我的分析」/「用户的分析」，选中文件夹并删除，如下图所示：
![](/core/style/lod.png)
**4）删除公共数据**
超管登录FineBI系统，点击「公共数据>全部数据」，勾选任意文件夹，点击「全选>删除」 ，删除内置的公共数据，如下所示：
![](/core/style/lod.png)  

## 2\. Windows安装
### 2.1 FineBI能不安装在默认的安装目录下吗？
可以的，在安装过程中的选择安装目录步骤，直接修改安装目录即可。
### 2.1 FineBI安装在了C盘，想将其迁移到D盘应该如何操作？
在 D 盘重新安装一个相同版本的 FineBI，然后将 C 盘 FIneBI 安装目录下的 ../webapps/webroot文件夹拷贝至相同位置替换原先的文件夹，迁移后需要重新更新数据。
## 3\. Linux安装
### 3.1 Linux安装包上传服务器就能直接安装吗？
Linux安装包上传到服务器上后，需要先给安装包赋执行的权限，在当前登录的用户有执行权限以后，才能执行后续的安装操作。安装目录的大小最好满足自身数据量支撑的大小，因为数据存放路径默认就在 FineBI 的工程路径下。
### 3.2 Linux环境安装必须要有图形化界面才行吗？
无论是在 [FineBI 官网](<https://www.finebi.com/>)下载的 Linux 安装版本，还是部署在 Web 服务器中，均不要求 Linux 操作系统必须有图形化界面，命令字符界面也可以安装。安装成功后一般可以正常使用，只有用到图表导出时需要调用图形化。
### 3.3 Linux中查看FineBI安装路径的命令是什么？
Linux 系统中可直接使用 ps -ef | grep finebi，可查找出系统已经启动的 FineBi 进程，进程信息描述中包含 FineBi 安装的路径。
## 4\. Mac安装
### 4.1 Mac下载安装出现安全提示
**问题描述：**  

在官网下载 Mac安装时，有时候会遇到的安全提示「无法打开“FineBI 安装程序”，因为Apple无法检查其是否包含恶意软件」。如下图所示：
![](/core/style/lod.png)
**原因分析：**
FineBI 没有上架 App store 。
**解决方案：**
在「安全性与隐私设置」中，允许从以下位置下载 APP ，选择「App Store和被认可的开发者」。
若仍显示「已阻止使用“FineBI安装程序”，因为来自身份不明的开发者」，点击「仍要打开」。
如下图所示：
![](/core/style/lod.png)
设置完成后，即可再次尝试打开，如下图所示：  

![](/core/style/lod.png)
### 4.2 Mac部署FineBI卡在许可协议步骤
**问题描述：**
Mac部署FineBI时，卡在许可协议步骤，且伴随服务器负载过高的现象。
![](/core/style/lod.png)
![](/core/style/lod.png)
**原因分析：**
软件冲突导致读取协议内容卡住，根据服务器性能具体表现为卡死或者等待时间过长的现象。
**解决方案：**
以下软件均有存在冲突的嫌疑，建议逐一关闭后再次尝试安装，待安装成功后再重启对应软件。
1）语法纠正软件Grammarly Desktop
2）窗口管理工具rectangle
3）分屏软件magent
### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：FineBI个人试用版启动常见问题](<index.php?doc-view-811.html>)
[下一篇：FineBI个人试用版安装与升级FAQ ![](/core/style/forward.png) ](<index.php?doc-view-985.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
