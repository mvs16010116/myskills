---
title: Linux最大打开文件数
doc_id: 28
url: https://help.fanruan.com/finebi6.X/doc-view-28.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:59
---

> 1. 概述1.1 问题描述Linux 服务器中部署帆软应用时，出现报错打开的文件过多或者too many open files，如下图所示：1.2 原因分析Linux 系统本身默认系统应用最大打开的文件

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux最大打开文件数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[20](<edition-list-28.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-11-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 问题描述
Linux 服务器中部署帆软应用时，出现报错打开的文件过多或者too many open files，如下图所示：
![37.png](/core/style/lod.png)
### 1.2 原因分析
Linux 系统本身默认系统应用最大打开的文件数为 1024，BI 执行时会读取保存在本地的数据，有些情况 BI 打开的文件数会超过这个限制，因此需要手动改掉linux系统的最大打开文件数。该修改在不同情况下会涉及到3个关键值。 
## 2\. 参数说明
### 2.1 参数介绍
参数  
| 说明| 默认值  
---|---|---  
nofile| 单个进程的最大打开文件数| 1024  
nr_open| 单个进程可分配的最大文件数| 1024*1024=1048576  
file-max| 系统内核一共可以打开的最大值| 185745  
### 2.2 修改策略
一般情况下，nofile 的值不允许超过 nr_open 和 file-max 的值。因此在修改 nofile 时要考虑是否超过以上两个值的情况：
  * 当要修改的「nofile」值未超过「nr_open」和「file-max」两个值时，直接修改「nofile」值即可。
  * 当要修改的「nofile」值超过「nr_open」和「file-max」两个值时，不仅要修改「nofile」的值，还要修改「nr_open」和「file-max」的值满足「大于nofile」值。


### 2.3 查看参数大小
基于修改策略，请在执行下文的修改操作前，先查看各个参数的大小。
参数  
| 查询语句  
---|---  
nofile| ulimit -n  
nr_open| cat /proc/sys/fs/nr_open  
file-max| cat /proc/sys/fs/file-max  
![](/core/style/lod.png)
## 3\. 修改 nofile 值
当要修改的「nofile」值（最大打开文件数）未超过「nr_open」和「file-max」两个值时，直接修改「nofile」值即可。
### 3.1 临时生效
1）使用终端工具连接服务器，执行命令：ulimit -n 128000
2）该修改只会影响当前shell会话。如果你打开一个新的终端窗口，nofile 限制将恢复为系统设置值。
![7.png](/core/style/lod.png)
### 3.2 永久生效
参考3.1节步骤后，直接执行 reboot 重启 Linux 服务器，即可永久生效；
若不想重启 linux 服务器，可参考本节完整步骤（但需要重启 FineBI 工程）。
1）使用vi /etc/security/limits.conf编辑 limits.conf 文件，修改 nofile 值（其中 128000 即为修改的 nofile 值），如下所示：
[code]
    vi /etc/security/limits.conf  #进入文件编辑界面
    * soft nofile 128000 #确保有该行内容
    * hard nofile 128000  #确保有该行内容
[/code]
注：有的系统需把「*」替换为具体用户名才生效，例如root soft nofile 128000
![13.png](/core/style/lod.png)
2）编辑/etc/pam.d/login文件，确保有下面内容，如下图所示：
[code]
    session required pam_limits.so
[/code]
![10.png](/core/style/lod.png)
3）配置完成后，终端用户重新登录，并重启Tomcat工程，配置方可生效。如下图所示：
![1622787438237364.png](/core/style/lod.png)
## 4\. nr_open 和 file-max 值
### 4.1 临时生效
[code]
    echo 1200000 > /proc/sys/fs/nr_open  
    echo 200000 > /proc/sys/fs/file-max  
    
[/code]
### 4.2 永久生效：需重启服务器
当要修改的最大打开文件数超过 nr_open 和 file-max 时，就需要改动该值，将该值提高。其修改方式如下：
在文件/proc/sys/fs/nr_open  
中加入如下代码：（1200000 为修改的参数值）
[code]
    fs.nr_open=1200000
[/code]
在文件 /proc/sys/fs/file-max 中插入如下代码：
[code]
    fs.file-max=200000
[/code]
保存并执行 reboot 重启服务器。
注：Linux的内核参数 nr_open 只有在内核版本是 2.6.25 之后的版本才可设置。查看内核版本使用命令“uname -a”。
然后再修改 nofile 值 ，请参见 3.2 节。
### 4.3 永久生效：无需重启服务器
在/etc/sysctl.conf中设置fs.nr_open= 1200000 fs.file-max=200000，然后执行sysctl -p，使配置生效。如下所示：
![15.png](/core/style/lod.png)
### 4.4 效果查看
通过cat /proc/pid/limits查看单进程最大打开文件数，如下图所示：
![1612427271613637.png](/core/style/lod.png)
## 5\. 注意事项
### 5.1 nofile修改不生效
**问题描述**
参考文档第三章修改nofile值不生效，仍为之前的值。
**原因及解决方案**
检查/etc/profile文件中，是否存在 ulimit -n xxx相关语句，删除即可
### 5.2 普通用户修改未生效
**问题描述**  

参考本文 4.3 节无需重启服务器的步骤后，普通用户修改未生效，使用 ssh 连接 Linux 报错：ulimit: open files: cannot modify limit: Operation not permitted
**原因分析**
该问题发生在 openssh 升级之后，且只有 ssh 登录才发生此问题，与 ssh 有关。
**解决方案**
1）修改sshd_config文件，将#UseLogin no修改为UseLogin yes，如下所示：
[code]
    vi  /etc/ssh/sshd_config
[/code]
![1622787539250143.png](/core/style/lod.png)  

2）使用service sshd restart重启 ssh 服务。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：修改 Linux 最大进程数](<index.php?doc-view-691.html>)
[下一篇：磁盘扩容 ![](/core/style/forward.png) ](<index.php?doc-view-1370.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
