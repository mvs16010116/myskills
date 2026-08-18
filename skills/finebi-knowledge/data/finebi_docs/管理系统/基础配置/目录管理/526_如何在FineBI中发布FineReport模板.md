---
title: 如何在FineBI中发布FineReport模板
doc_id: 526
url: https://help.fanruan.com/finebi6.X/doc-view-526.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:08:16
---

> 1. 概述1.1 版本BI 服务器版本功能变更6.0-1.2 问题描述FineBI工程未集成FineReport工程的情况下，如何挂载/使用FineReport模板呢？1.3 解决思路有两种使用场景：1

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 如何在FineBI中发布FineReport模板
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[15](<edition-list-526.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-01-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
BI 服务器版本  
| 功能变更  
---|---  
6.0| -  
### 1.2 问题描述
FineBI工程未集成FineReport工程的情况下，如何挂载/使用FineReport模板呢？  

### 1.3 解决思路
有两种使用场景：
1）将FineReport模板挂载到FineBI工程目录中展示。
2）将FineReport模板通过仪表板的 Web 组件链接展示。
注：若FineBI工程和FineReport工程互通，也可在FineBI工程目录直接挂载FineReport模板的超链，本文不赘述此情况。
## 2\. 示例一：挂载到目录中
本章示例：在FineBI系统目录中，展示FineReport模板「段落明细表」。
### 2.1 上传FineReport模板
将FineReport模板「段落明细表」拷贝到%FineBI%\webapps\webroot\WEB-INF\reportlets目录下，如下图所示：
![](/core/style/lod.png)
### 2.2 设置数据连接
在FineBI系统中，需要新增一个数据连接，和FineReport模板「段落明细表」用到的数据连接完全一致，命名也必须完全相同。
管理员登录FineBI系统，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，新建一个和「段落明细表」用到的数据连接完全一致的数据连接。
![](/core/style/lod.png)
### 2.3 新增目录
管理员登录FineBI系统，点击「管理系统>目录管理」，选择想要挂出的对应目录后，点击「添加模板」，如下图所示：
![](/core/style/lod.png)
进入模板设置界面，此时页面即显示当前工程中的所有 FineReport 模板，选择FineReport模板「段落明细表」，点击「下一步」。  

设置挂出模板的名称、描述、类型等，点击「确定」，FineReport模板「段落明细表」即发布成功。如下图所示：  

注：如模板预览类型为填报，FineBI工程必须购买了「数据录入」功能点，否则无法进行填报。详情请参见：[注册管理](<https://help.fanruan.com/finebi6.0/doc-view-177.html>) 。
![](/core/style/lod.png)
### 2.4 效果预览
打开目录，刷新，左侧目录树中显示刚刚添加的FineReport模板「段落明细表」，如下图所示：
![](/core/style/lod.png)
## 3\. 示例二：在组件中引用
本章示例：在FineBI的Web组件中，展示FineReport模板「段落明细表」。
### 3.1 上传FineReport模板
将FineReport模板「段落明细表」拷贝到%FineBI%\webapps\webroot\WEB-INF\reportlets目录下，如下图所示：
![](/core/style/lod.png)
  

### 3.2 设置数据连接
在FineBI系统中，需要新增一个数据连接，和FineReport模板「段落明细表」用到的数据连接完全一致，命名也必须完全相同。
管理员登录FineBI系统，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，新建一个和「段落明细表」用到的数据连接完全一致的数据连接。
![](/core/style/lod.png)
### 3.3 新建仪表板
用户登录FineBI系统，点击「我的分析」，点击「新建分析主题」。如下图所示：
![](/core/style/lod.png)
无需选择数据，直接点击「取消」。添加一个「仪表板」，选择「其他>Web组件」，将其拖入仪表板中，如下图所示：
![](/core/style/lod.png)
为该 Web 组件添加超链接，对应 FineReport 模版的链接为：/webroot/decision/view/report?viewlet=xxxxx.cpt
xxxxx.cpt 对应为该模板保存在 reportlets 文件夹中的 cpt 文件名称。
比如 FineReport模板 cpt 文件为「段落明细表.cpt」，则该模板的链接就是/webroot/decision/view/report?viewlet=段落明细表.cpt。如下图所示：  

![](/core/style/lod.png)
  * 若 cpt 文件位于 reportlets 下一级文件夹，例如模板段落明细表位于..\webapps\webroot\WEB-INF\reportlets\test，则链接形式为/webroot/decision/view/report?viewlet=test/段落明细表.cpt
  * 若添加填报报表，则需在链接添加后缀&op=write。例如供应商信息查询为填报报表，则链接形式为/webroot/decision/view/report?viewlet=供应商信息查询.cpt&op=write
  * 若需要添加的报表A中添加了超链接，且链接至另一报表B，如下图所示，供应商信息查询报表中添加了超链接，链接模板为折线图模板，且地址位于..\reportlets\demo\chart


则在FineBI 中添加时，不仅需要将供应商信息查询报表拷贝至..\webapps\webroot\WEB-INF\reportlets\目录下，还需要将超链接的折线图模板拷贝至对应的..\reportlets\demo\chart目录下，这样供应商信息查询模板在添加成功后，才能成功超链接跳转。
![1.png](/core/style/lod.png)
### 3.4 效果预览
保存仪表板，预览即可在该仪表板的Web组件中查看到FineReport模板「段落明细表」，如下图所示：
![](/core/style/lod.png)
## 4\. 注意事项
若模板不存放在当前FineBI工程中，而是在其他工程中。
当前工程以目录超链/Web组件超链调用其他工程的模板时，必须要关闭模板所在工程的「管理系统>安全管理>安全防护>Security Headers」的「点击劫持攻击防护」。
详情请参见：[安全防护](<https://help.fanruan.com/finebi6.0/doc-view-781.html>)  

![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：管理目录](<index.php?doc-view-246.html>)
[下一篇：用户管理 ![](/core/style/forward.png) ](<index.php?doc-view-170.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
