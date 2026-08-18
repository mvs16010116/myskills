---
title: Linux中BI进程异常关闭
doc_id: 380
url: https://help.fanruan.com/finebi6.X/doc-view-380.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:57
---

> 1、问题描述在 Linux 中使用 FineBI，系统使用过程中 FineBI 的进程异常关闭，查看 BI 的日志并没有任何的异常信息。2、问题原因及解决方案2.1 可能原因针对上述的现象，问题原因可能

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux中BI进程异常关闭
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[6](<edition-list-380.html>)
* 最近更新：[Scyalcire](<user-space-217892.html>) 于 2020-10-29 
[](<javascript:;>) [](<javascript:>)
## 1、问题描述
在 Linux 中使用 FineBI，系统使用过程中 FineBI 的进程异常关闭，查看 BI 的日志并没有任何的异常信息。
## 2、问题原因及解决方案
### 2.1 可能原因
针对上述的现象，问题原因可能为 FineBI 的进程是被系统 Kill 掉的，可去检查 Linux 系统日志/var/log/messages，查看进程被异常关闭的时间点日志。
若该时间点存在对应 Kill 掉 FineBI 进程的日志，说明 FineBI 进程是被系统 Kill 掉的。
### 2.2 解决方案
Linux 系统 Kill 掉 FineBI 的进程，可能是由于自身的 OOM KILLER 机制造成的，查看自身 Linux 系统的/etc/sysctl.conf文件（内核参数配置），若其中的vm.overcommit_memory=2，即表示系统不允许 overcommit 操作。
该 OOM KILLER 机制会在 linux 内存紧张的时候，依次 Kill 内存占用较高的进程，并在/var/log/message中进行记录，里面会记录一些如 pid，process name，cpu mask，trace 等信息，通过监控可以发现类似问题。
针对此类问题，我们可以调整系统的 vm.overcommit_memory 内核参数值，将其设置 0/1，分别表示：
  * 0 – Heuristic overcommit handling. 这是缺省值，它允许 overcommit，但过于明目张胆的 overcommit 会被拒绝，比如 malloc 一次性申请的内存大小就超过了系统总内存。Heuristic 的意思是“试探式的”，内核利用某种算法（对该算法的详细解释请看文末）猜测你的内存申请是否合理，它认为不合理就会拒绝 overcommit。
  * 1 – Always overcommit. 允许 overcommit，对内存申请来者不拒。


根据需要调整内核参数值，或者增加系统的内存来解决。调整内核参数值后需要输入命令 sysctl -p，使配置文件生效。
[code]
    sysctl -p  
    
[/code]
详细原理可参考 [理解LINUX的MEMORY OVERCOMMIT](<http://linuxperf.com/?p=102>)。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux常见问题](<index.php?doc-view-25.html>)
[下一篇：Linux系统编码修改 ![](/core/style/forward.png) ](<index.php?doc-view-27.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
