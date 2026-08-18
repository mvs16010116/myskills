---
title: Linux系统编码修改
doc_id: 27
url: https://help.fanruan.com/finebi6.X/doc-view-27.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:57
---

> 1、描述在 Linux 服务器中系统的编码默认设置成的是&nbsp;en_US.UTF-8&nbsp;，而FineBI中中文编码默认是&nbsp;zh_cn.UTF-8&nbsp;的编码，因此会存在在

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux系统编码修改
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[6](<edition-list-27.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-05-27 
[](<javascript:;>) [](<javascript:>)
## 1、描述
在 Linux 服务器中系统的编码默认设置成的是 en_US.UTF-8 ，而FineBI中中文编码默认是 zh_cn.UTF-8 的编码，因此会存在在 BI 应用中导出 Excel 出现乱码的情况，因此要将 Linux 系统的编码改成 zh_CN.UTF-8 。修改方法包括全局修改和局部修改。
## 2、全局修改
全局修改即为对整个系统都有效的修改方式，使整个系统都适应于该系统编码。该方法是在系统配置文件中添加编码方式将默认的方式覆盖掉。执行的命令如下：
[code]
    vi /etc/profile  
    
[/code]
打开文件后在最后一行加入如下命令：
[code]
    export LC_ALL="zh_CN.UTF-8"  export LANG="zh_CN.UTF-8"  
    
[/code]
保存退出后，执行文件生效命令：
[code]
    source /etc/profile  
    
[/code]
修改完成。  

## 3、局部修改
有时 Linux 系统中编码并不能统一使用，而是只针对某用户下才使用该编码，即当使用 FineBI 的时候，在该系统用户下才能使用该编码。因此编辑配置文件时需要在该用户下编辑。
如给用户 wind 进行该编码设置，执下如下命令：
[code]
    vi /home/wind/.bash_profile  
    
[/code]
在最后一行输入：
### 
[code]
    export LC_ALL="zh_CN.UTF-8" export LANG="zh_CN.UTF-8"  
    
[/code]
### 再执行 source 命令即可：
[code]
    source /home/wind/.bash_profile  
    
[/code]
注：./bash_profile 是每个用户都可使用该文件输入专用于自己使用的 shell 信息。  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux中BI进程异常关闭](<index.php?doc-view-380.html>)
[下一篇：修改 Linux 最大进程数 ![](/core/style/forward.png) ](<index.php?doc-view-691.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
