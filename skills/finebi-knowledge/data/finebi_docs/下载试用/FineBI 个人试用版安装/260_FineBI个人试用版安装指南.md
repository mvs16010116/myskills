---
title: FineBI个人试用版安装指南
doc_id: 260
url: https://help.fanruan.com/finebi6.X/doc-view-260.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:28
---

> 1. 概述1.1 版本FineBI服务器版本功能变更6.0-1.2 应用场景更多方案对比项请参考：FineBI企业部署版、个人本地版、在线试用版介绍分类说明超链个人用户试用面向对象：面向准合作客户或个人

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI个人试用版安装指南
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[126](<edition-list-260.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
6.0| -  
  
### 1.2 应用场景
更多方案对比项请参考：[FineBI企业部署版、个人本地版、在线试用版介绍](<https://bbs.fanruan.com/thread-149119-1-1.html>)
分类  
| 说明| 超链  
---|---|---  
个人用户试用| 面向对象：面向**准合作客户或个人用户** 安装环境要求：**免安装** 快速体验功能说明：
  * 支持在线分享和协作
  * 公共数据、数据连接等企业级功能需请申请团队版试用（周期1个月）

|  [FineBI 在线分析平台](<https://pcdemo.finebi.com/webroot/decision/?online_bi_from=0402>)  
IT人员选型测试| 面向对象： [IT人员](<https://help.fanruan.com/finebi6.X/doc-view-777.html?source=4#>) 产品选型测试，可选择本地/个人电脑安装满足采购产品前的调研与简单功能测试需求| 本文仅面向 **FineBI 6.0.X 版本**  
企业正式部署| 企业正式使用或需要模拟企业正式使用场景（比如产品培训推广、性能测试等）需要在服务器中部署企业版FineBI| [FineBI企业版部署指南](<https://help.fanruan.com/finebi6.X/doc-view-2108.html>)  
### 1.3 安装流程
![未命名文件.png](/core/style/lod.png)
  

### 1.4 注意事项
1）本文仅面向 **FineBI 6.0.X 版本** 的用户进行本地个人试用版安装指导。
2）本地安装个人试用版时，安装路径**不可包含中文** ，否则会启动失败。如：D:\FR\FineBI6 。
3）本地/个人电脑安装的FineBI，**不支持分享与协作** ，即做好的分析看板无法分享出去。
4）在同一台本地电脑，无法同时运行**多个FineBI。**
5）由于个人电脑内存、磁盘空间有限，本地/个人电脑安装的FineBI，大数据量情况下可能存在**卡顿** 问题。
6）安装常见问题请参见： [FineBI 安装常见问题](<https://help.fanruan.com/finebi6.0/doc-view-637.html>)
## 2\. Windows系统安装试用版FineBI
本文安装包仅适合试用。企业正式工程请勿参考本文安装，请参考文档部署：[FineBI企业版部署指南](<https://help.fanruan.com/finebi6.X/doc-view-2108.html>)
### 2.1 准备环境
配置| 要求  
---|---  
系统| Windows7 或更高版本仅支持64位  
CPU| Intel Core i3-4代 或更快的处理器  
内存| 4G及以上  
磁盘| 准备安装目录，目录路径**不可包含中文** ，否则会启动失败  
目录所在磁盘剩余可用2G以上  
  
### 2.2 下载FineBI安装包
访问 [FineBI下载页面](<https://www.finebi.com/product/download>)，在「个人本地试用及其他版本下载>历史版本」中，点击下载「Win 64版」到本地。
![](/core/style/lod.png)
### 2.3 安装FineBI
  
|   
|   
  
---|---|---  
1| 启动安装包  
| 1）选中下载的.exe安装包，右击，选择「以管理员身份运行」  
2）自动加载安装向导，请耐心等待安装向导加载完毕![](/core/style/lod.png)  
2| 进入安装| 出现安装助手界面，点击「下一步」![](/core/style/lod.png)  
3| 签订许可协议| 请耐心阅读许可协议如确定接受协议继续安装，请选择「我接受协议」，并点击「下一步」![](/core/style/lod.png)  
4| 选择安装目录| 请点击浏览，选择 FineBI 安装目录，完成后点击「下一步」注1：安装目录路径**不可包含中文** ，否则会启动失败。注2：FineBI 不建议安装在系统盘。![](/core/style/lod.png)  
5| 设置最大内存| 请输入FineBI可占用的最大 JVM内存，完成后点击「下一步」
  * 默认值为 2048M，也就是 2G
  * 支持设置 2048 及以上值，单位M
  * 最大 JVM 内存不能超过本机最大内存

![](/core/style/lod.png)  
6| 设置开始菜单文件夹| 请按需选择，完成后点击「下一步」![](/core/style/lod.png)  
7| 选择附加工作| 请按需选择，完成后点击「下一步」「生成安全密钥文件」说明请参考：[生成安全密钥文件按钮说明](<https://help.fanruan.com/finebi6.0/doc-view-996.html>)![](/core/style/lod.png)  
8| 自动执行安装| 请耐心等待安装完成![](/core/style/lod.png)  
9| 选择是否自动运行| 如果勾选「运行FineBI」，点击「完成」后，FineBI 会自动启动并弹出系统初始设置页面如果不勾选「运行FineBI」，点击「完成」后，FineBI 不会自动启动![](/core/style/lod.png)  
  

### 2.4 启动FineBI
1）启动 FineBI 有两种方式：
  * 方法一：通过点击桌面上的快捷图片
  * 方法二：点击安装目录下%FineBI%/bin/finebi.exe文件启动


![](/core/style/lod.png)
2）个人试用版FineBI中，内置了 Tomcat 的服务器环境，点击此文件即弹出加载页面，随后出现 Tomcat 打开 BI 服务器。
![](/core/style/lod.png)
3）当 Tomcat 服务器开启以后，会自动弹出浏览器地址：http://localhost:37799/webroot/decision打开BI平台进入初始化设置，如下图所示：
后续设置操作请参见：[初始化设置](<https://help.fanruan.com/finebi6.0/doc-view-262.html>)
注1：http://localhost:37799/webroot/decision为默认访问地址，可根据实际情况调整。 
注2：此处数据决策系统访问地址，在外网访问时，需将 localhost 换成服务器 IP 访问；若外网访问不了，可借助第三方工具：例如花生壳、fcn、frp 等实现内网穿透。 
注3：如需输入激活码，获取方法：登录：[FineBI官网](<https://www.fanruan.com/finebi>)，点击「免费试用」，输入相关信息即可获取激活码
![](/core/style/lod.png)
## 3\. Linux系统安装试用版FineBI
Linux 系统是常用的服务器系统，用户使用 FineBI 经常会采用 Linux 服务器安装，下文介绍 Linux 的安装方式。
本文安装包仅适合试用。企业正式工程请勿参考本文安装，请参考文档部署：[FineBI企业版部署指南](<https://help.fanruan.com/finebi6.X/doc-view-2108.html>)
### 3.1 准备环境
配置| 要求  
---|---  
系统| Centos、RedHat 等常见 Linux 版本系统  
CPU| Intel Core i3-4代 或更快的处理器  
内存| 4G及以上  
磁盘| 准备安装目录，目录路径**不可包含中文** ，否则会启动失败  
目录所在磁盘剩余可用2G以上  
  
JDK| JDK 1.8 且小版本需在 JDK8u102 以上32位：Oracle64位：Oracle、IBM J9  
### 3.2 下载上传FineBI安装包
1）访问 [FineBI下载页面](<https://www.finebi.com/product/download>)，在「个人本地试用及其他版本下载>历史版本」中，点击下载「Linux版本」。
![](/core/style/lod.png)
2）将安装包 Linux_unix_FineBI6_1-CN.sh 上传至 Linux 服务器中。如下图所示：
![2022-09-05_18-26-17.png](/core/style/lod.png)
3）使用终端设备连接 Linux 服务器，执行命令赋予安装包文件权限。
[code]
    chmod 777 linux_unix_FineBI6_1-CN.sh
[/code]
注：如果不先执行权限命令，安装时会报错：-bash: ./linux_unix_FineBI6_0-CN.sh: Permission denied。 
### 3.3 安装FineBI
1）执行安装命令，如下图所示：
[code]
    ./linux_unix_FineBI6_1-CN.sh
[/code]
![2022-09-07_10-33-41.png](/core/style/lod.png)
2）选择回车键进行安装，出现许可协议，继续按提示敲击回车键出现是否接受协议，输入1，按回车键，如下图所示：
![2022-09-07_10-20-54.png](/core/style/lod.png)
3）选择要安装的目录，可按该形式写出要安装的目录路径，此处默认用缺省值，直接选择回车键，如下图所示：
注：安装目录路径**不可包含中文** ，否则会启动失败。请输入完整绝对路径。
![2022-09-07_10-35-11.png](/core/style/lod.png)
4）设置BI系统使用的最大内存，直接写入数值即可，其单位是M ，此处使用缺省值，直接选择回车键，如下图所示：
注：此处若为64位操作系统，JVM内存最小设置为2048，即2G，否则FineBI无法正常运行。
![2022-09-07_10-36-24.png](/core/style/lod.png)
5）提示是否创建快捷连接，一般放置在服务器上的并不需要，输入 n，按回车即可。
同样桌面快捷方式一般也不需要，同样输入 n，按回车键，然后选择是否生成安全密钥文件，选择后文件即解压进行安装，如下图所示：
注：「生成安全密钥文件」按钮的介绍请参见：[生成安全密钥文件按钮说明](<https://help.fanruan.com/finebi6.0/doc-view-996.html>)
![2022-09-07_10-37-58.png](/core/style/lod.png)
6）完成安装后，提示是否运行，可以输入 y 按回车运行 FineBI，如下图所示：
![2022-09-07_10-40-13.png](/core/style/lod.png)
### 3.4 启动FineBI
详情参见：[Linux中启动FineBI](<https://help.fanruan.com/finebi6.X/doc-view-24.html>)
启动成功后，可以在浏览器中输入地址：http://IP:37799/webroot/decision访问，其中 IP 为对应安装服务器的 IP 。
若外网访问不了，可借助第三方工具：例如花生壳、fcn、frp 等实现内网穿透。后续操作请参见：[初始化设置](<https://help.fanruan.com/finebi6.0/doc-view-262.html>)
注1：http://localhost:37799/webroot/decision为默认访问地址，可根据实际情况调整。 
注2：如需输入激活码，获取方法：登录：[FineBI官网](<https://www.fanruan.com/finebi>)，点击「免费试用」，输入相关信息即可获取激活码
## 4\. Mac
本文安装包仅适合试用。企业正式工程请勿参考本文安装，请参考文档部署：[FineBI企业版部署指南](<https://help.fanruan.com/finebi6.X/doc-view-2108.html>)
### 4.1 准备环境
配置| 要求  
---|---  
系统| MacOS10 或更高版本（64位）  
CPU| Intel Core i3-4代 或更快的处理器  
内存| 4G及以上  
磁盘| 准备安装目录，目录路径**不可包含中文** ，否则会启动失败  
目录所在磁盘剩余可用2G以上  
  
### 4.2 下载FineBI安装包
访问 [FineBI下载页面](<https://www.finebi.com/product/download>)，在「个人本地试用及其他版本下载>历史版本」中，点击下载「MacOS版」到本地。
![](/core/style/lod.png)
### 4.3 安装FineBI
Mac 系统下安装与 Windows 类似，双击 FineBI 安装文件，会加载安装向导，安装向导加载完后，会弹出对话框，随后按照 Windows 的 2.4 节操作流程即可。
启动FineBI安装文件时，需要选择「仍要打开」。运行 FineBI 安装程序。如下图所示：  

![企业微信截图_986cc1ad-ace9-40e1-b2d0-0e2f146322fc.png](/core/style/lod.png)
### 4.4 启动FineBI
MAC 系统启动 FineBI 包含两种方式
第一种：直接在程序栏找到安装的 finebi 程序，双击图标启动，如下图所示：
![1662521501522921.png](/core/style/lod.png)
第二种：进入FineBI安装目录，通过点击%FineBI%/bin/finebi4shell启动。如下图所示：
![222](/core/style/lod.png)  

启动成功后，就可以在浏览器中输入地址：http://IP:37799/webroot/decision访问，其中 IP 为对应安装服务器的IP。
若外网访问不了，可借助第三方工具：例如花生壳、fcn、frp 等实现内网穿透。后续操作请参见：[初始化设置](<https://help.fanruan.com/finebi6.0/doc-view-262.html>)
注：http://localhost:37799/webroot/decision为默认访问地址，可根据实际情况调整。
## 5\. 下一步操作
帮助文档| 说明  
---|---  
[初始化设置](<https://help.fanruan.com/finebi6.0/doc-view-262.html>)| 第一次安装 FineBI 后，进行初始化操作  
[FineBI界面介绍](<https://help.fanruan.com/finebi6.0/doc-view-263.html>)| 了解 FineBI 操作界面  
[新手入门指南](<https://help.fanruan.com/finebi6.0/doc-view-1316.html>)| 快速上手 FineBI  
[管理员操作概述](<https://help.fanruan.com/finebi6.0/doc-view-777.html>)| 管理员配置 FineBI 管理系统  
## 6\. 完整性校验
为了方便用户校验，确保FineBI安装包在下载和传输过程中没有被篡改，自 FineBI6.1.2 版本起，提供完整性校验方式。
### 6.1 获取方式
官网默认只提供最新版本的文件哈希。可以通过访问 [安装包校验信息](<https://official-download.oss-cn-shanghai.aliyuncs.com/finebi/6.1/stable/exe/spider/FineAll_Verify.json>) 查看。
![](/core/style/lod.png)
### 6.2 校验方式
将软件下载到本地，使用系统自带工具计算单个文件的校验和。
注：file 需要替换成本地具体的文件路径，如果路径中包含空格，需要使用双引号“” 将路径包含在内。
校验方式  
| Windows| Mac| Linux  
---|---|---|---  
SHA-256| certUtil -hashfile file SHA256| shasum -a 256 file| sha256sum file  
MD5| certUtil -hashfile file MD5| md5 file| md5sum file  
### 6.3 示例
以 Windows 为例，示例软件包 windows-x64_FineBI6_1-CN.exe
官方提供的 SHA256 值为 bdf6a854ec5615fc9086a38751276f9ed988178b67e85590cfa46abf2cc7d699
本地计算结果如下图所示，与官方提供的校验值一致，文件无篡改。
![](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：FineBI 使用入口](<index.php?doc-view-2486.html>)
[下一篇：FineBI初始化设置 ![](/core/style/forward.png) ](<index.php?doc-view-262.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
