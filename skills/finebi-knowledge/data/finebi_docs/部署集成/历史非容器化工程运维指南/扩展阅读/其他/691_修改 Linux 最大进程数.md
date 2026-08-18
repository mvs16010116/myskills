---
title: 修改 Linux 最大进程数
doc_id: 691
url: https://help.fanruan.com/finebi6.X/doc-view-691.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:58
---

> 1. 描述&nbsp;Linux 系统中可以设置关于资源的使用限制，比如：进程数量，文件句柄数，连接数等等。在使用 Linux 系统时，若切换 root 用户为普通用户，可能出现&nbsp;Resour

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 修改 Linux 最大进程数
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[6](<edition-list-691.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-05-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 描述
Linux 系统中可以设置关于资源的使用限制，比如：进程数量，文件句柄数，连接数等等。  
在使用 Linux 系统时，若切换 root 用户为普通用户，可能出现 Resource temporarily unavailable 报错，这是由于当前用户的进程数超出限制。因此需要手动修改 Linux 系统的最大进程数。
## 2\. 关键值
nproc：表示 max number of processes，是操作系统级别对每个用户创建的进程数的限制。
nofile：表示 max number of open file descriptors，每个进程可以打开的文件数的限制。
hard/soft：soft 是一个警告值，而 hard 则是一个真正意义的阀值，超过就会报错。
## 3\. 修改方法
### 3.1 查看当前用户打开的最大进程数
1）在 Linux 终端执行命令 ulimit -a
查看 max user processes ：即系统限制某用户下最多可以运行多少进程或线程。如下图所示：
![1576054140646976.png](/core/style/lod.png)
2）也可在 Linux 终端执行命令 ulimit -u。
### 3.2 使用 root 用户登录。
#### 方法一：
进入 /etc/security/limits.conf 文件下，增加如下代码，并保存：
[code]
    roxy soft nproc 10240  
    roxy hard nproc 10240  
    roxy soft nofile 10240  
    roxy hard nofile 10240
[/code]
注：roxy 为需要修改线程数的用户名，10240 为设置的进程数和文件数限制，可根据需要修改。
#### 方法二：
1）进入 /etc/security/limits.conf 文件下，增加如下代码，并保存：
[code]
    * soft nproc 10240    
    * hard nproc 10240
[/code]
注：* 表示对所有用户都生效。
2）进入 /etc/security/limits.d/xx-nproc.conf 文件下，增加如下代码，并保存：
[code]
    * soft nproc 10240  
    
[/code]
注：1. 10240 为设置的进程数和文件数限制，可根据需要修改。
注：2. cemtos6 需修改的文件路径为 /etc/security/limits.d/90-nproc.conf ，CentOS7 需修改的文件路径为 /etc/security/limits.d/20-nproc.conf 。
### 3.3 再次登录超过线程限制的用户
在终端执行 ulimit -a，即可查看修改后系统限制某用户下最多可以运行多少进程或线程。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux系统编码修改](<index.php?doc-view-27.html>)
[下一篇：Linux最大打开文件数 ![](/core/style/forward.png) ](<index.php?doc-view-28.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
