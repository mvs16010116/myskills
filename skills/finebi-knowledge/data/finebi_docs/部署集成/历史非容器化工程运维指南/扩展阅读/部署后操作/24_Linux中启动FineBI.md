---
title: Linux中启动FineBI
doc_id: 24
url: https://help.fanruan.com/finebi6.X/doc-view-24.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:39
---

> 1. 概述在 Linux 服务器上，安装成功后的 FineBI 需要进行进程管理，比如启动、设置开机自启动、关闭等操作。2. 启动 FineBI2.1 进入目录例如 FineBI 安装在 opt 目录下

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux中启动FineBI
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[28](<edition-list-24.html>)
* 最近更新：[HeroZ](<user-space-1842712.html>) 于 2023-03-01 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
在 Linux 服务器上，安装成功后的 FineBI 需要进行进程管理，比如启动、设置开机自启动、关闭等操作。
## 2\. 启动 FineBI
### 2.1 进入目录
例如 FineBI 安装在 opt 目录下，需要进入到%FineBI%bin 目录中，如下所示：
[code]
    cd /opt/FineBI/bin  
    
[/code]
### 2.2 启动工程
直接执行启动命令，如下所示：
[code]
    nohup ./finebi &  
    
[/code]
操作结果如下图所示：  

![19.png](/core/style/lod.png)
  * & ：在后台运行，该命令让进程实现在后台运行。
  * nohup ：不挂断地运行命令。该命令可以在退出账号/关闭终端之后继续运行相应的进程。


将 nohup 和 & 结合使用，就可以实现使命令永久地在后台执行的功能。
### 2.3 启动成功
执行命令后如下图，即为启动成功。
![63.png](/core/style/lod.png)
如果需要修改内存，需要在finebi.vmoptions文件中修改，详情参见：[Linux 中修改 JVM 内存](<https://help.fanruan.com/finebi6.0/doc-view-56.html#5>)
注：启动和内存设置文件都在安装一级目录下。
## 3\. 开机自启动 FineBI
在 Linux 服务器中，通常会把常用的应用设置为开机自动启动，这样方便于当重启服务器时，不需要再进行应用启动的繁杂操作，同时可减少因为服务器的重启而遗漏应用的启动。
Linux 服务器开机自启动的原理：Linux 服务器中一切都是文件，开机应用启动也是读取文件。因此只要在服务器启动时要读取的配置文件中写入该应用的启动命令即可，该配置文件使用的是 rc.local 文件。
### 3.1 修改配置文件
1）找到rc.local文件进行编辑，其路径固定在 /etc 下，可以直接执行编辑命令，如下所示：
[code]
    vi /etc/rc.local  
    
[/code]
2）在该编辑界面下，按 i 键进入insert状态。在文件最后一行输入 FineBI 的启动命令，由于当前不在 FineBI 的目录路径，因此启动命令要加上文件绝对路径，启动命令为（路径需改为对应FineBI安装路径）：
[code]
    nohup /opt/FineBI/bin/finebi &  
    
[/code]
如下图所示：  

![222](/core/style/lod.png)  

3）编辑后，按ESC键退出insert界面，输入 :wq ，保存文件并退出。
注：若配置之后无法生效，可执行 chmod +x /etc/rc.d/rc.local 使得配置文件生效，因为在 CentOS7 等 Linux 操作系统中 rc.local 文件已经逐渐被弃用权限。 
### 3.2 重启服务器
执行重启 Linux 系统命令 reboot ，重新登录后，使用如下命令查看进程：
[code]
    ps -ef | grep finebi  
    
[/code]
若看到 FineBI 进程，则说明 Linux 系统重启后， FineBI 自动启动成功，如下图所示：
![54.png](/core/style/lod.png)
注：若按照 2.2.1 节方式配置文件后无法生效，无法实现开机自启动，可执行 chmod +x /etc/rc.d/rc.local ，给配置文件添加执行权限。因为在 CentOS7 等 Linux 操作系统中/etc/rc.d/rc.local没有执行权限。
## 4\. 关闭 FineBI
Linux 系统中，FineBI 没有 Windows 系统中对应的后台界面来关闭程序，因此，需要通过杀进程来关闭服务。
1）使用如下命令查看 FineBI 进程对应的 PID ，如下所示：
[code]
    ps -ef | grep finebi  
    
[/code]
2）kill 掉此 PID 进程，例如 FineBI 对应进程 PID 为 4626 ，则执行如下命令：
[code]
    kill -9 4626  
    
[/code]
注：以上两个步骤可以使用一个命令完成，即ps -ef | grep finebi | grep -v 'grep' | awk '{print $2}' | xargs -I {} kill -9 {}
## 5\. 注意事项
当非 root 用户启动时，可能会因权限问题导致日志、spark 的临时 tmp 路径等异常。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Nginx 开机自启动脚本](<index.php?doc-view-1877.html>)
[下一篇：关闭或重启FineBI工程 ![](/core/style/forward.png) ](<index.php?doc-view-1322.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
