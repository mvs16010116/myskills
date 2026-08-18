---
title: WeLink定时推送消息
doc_id: 2069
url: https://help.fanruan.com/finebi6.X/doc-view-2069.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:12:33
---

> 1. 概述1.1 版本FineBI 版本WeLink&nbsp;管理插件版本功能变动6.0V11.0.68-6.0.4&nbsp;V11.0.74定时调度支持推送「图片消息」，无需再通过链接跳转查看1.

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# WeLink定时推送消息
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Alicehyy](<user-space-504714.html>)_
* 历史版本：[2](<edition-list-2069.html>)
* 最近更新：[Alicehyy](<user-space-504714.html>) 于 2022-12-06 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| WeLink 管理插件版本| 功能变动  
---|---|---  
6.0| V11.0.68| -  
6.0.4|  V11.0.74| 定时调度支持推送「图片消息」，无需再通过链接跳转查看  
### 1.2 功能简介
服务器端消息推送到个人，用户可以及时了解数据情况，例如产品库存，销售进度，工资明细，迟到考勤等
服务器消息推送到群，可以让众人共同监督数据情况，可以及时在群内@相关负责人，及时推送让大家讨论。
### 1.3 功能描述
通过配置 WeLink 管理插件和定时调度任务，可及时推送消息至个人和 WeLink 群。
## 2\. WeLink 定时推送消息
### 2.1 配置 WeLink 集成
详情参见：[WeLink集成](<https://help.fanruan.com/finebi6.0/doc-view-1797.html>) 。
### 2.2 设置定时调度任务
定时调度任务的设置步骤请参考：[](<https://help.fanruan.com/finereport/doc-view-1387.html>)[定时调度客户端通知-APP通知](<https://help.fanruan.com/finereport/doc-view-1387.html>) 。
在「定时调度>文件处理」步骤中，勾选「客户端通知> WeLink 通知」，并选择对应应用名称即可。如下图所示：
![2021-10-20_18-35-19.png](/core/style/lod.png)
示例的「客户端通知」设置，选择「WeLink 通知」，消息类型选择「链接消息」。输入主题内容。
注：推送消息类型支持：链接消息（仅支持自定义链接）、图文消息，V11.0.74 及之后版本还支持图片消息。详情请参考：[第三方集成推送支持的消息类型](<https://help.fanruan.com/finebi6.0/doc-view-1186.html>) 。
详情如下图所示：
  

![](/core/style/lod.png)
### 2.3 效果查看
WeLink 在通知中心可查看到消息，如下图所示：  

![Screenshot_20211020_185300_com.huawei.welink\(1\).jpg](/core/style/lod.png)
## 3\. WeLink 定时推送群消息
### 3.1 配置 WeLink 集成
详情参见：[WeLink集成](<https://help.fanruan.com/finereport/doc-view-4351.html>)
### 3.2 新建 WeLink 群
在 [WeLink集成](<https://help.fanruan.com/finereport/doc-view-4351.html>) 中，在点击「WeLink 管理>应用快捷配置>新建 WeLink 群」，可实现推送消息到群，群成员除群主外还要至少两人。
  

![1634713284511903.png](/core/style/lod.png)
### 3.3 设置定时调度任务
在「定时调度>文件处理」步骤中，勾选「客户端通知>Welink通知」，选择创建群的应用，勾选需要推送消息的群即可，如下图所示：
1）定时调度任务的设置步骤请参考：[](<https://help.fanruan.com/finereport/doc-view-1387.html>)[定时调度客户端通知-APP通知](<https://help.fanruan.com/finereport/doc-view-1387.html>) 。
2）推送消息类型支持：链接消息（仅支持自定义链接）、图文消息，V11.0.74 及之后版本还支持图片消息。详情请参考：[第三方集成推送支持的消息类型](<https://help.fanruan.com/finebi6.0/doc-view-1186.html>) 。
注1：WeLink推送不支持推送「文件消息」到用户，此消息类型将转为「链接消息」进行发送。
注2：WeLink 推送到群的「图片消息」，只能在云空间打开。
注3：若勾选 WeLink 群后，未选择群聊名称，则无法推送群消息。
注4：接收人中，默认用户组为必选项。如果用户不在群聊但在默认用户组中，仍将单独收到消息。
![2021-10-21_13-39-17.png](/core/style/lod.png)
## 4\. 注意事项
不同的「客户端通知>消息类型」设置，可能会影响单点登录的效果。  

### 4.1 链接消息
链接消息仅支持自定义链接。
自定义链接可以填入 三种类型的链接，如下：
1）模板相对路径
如：decision/view/report?viewlet=GettingStarted.cpt
不开启「[模板认证](<https://help.fanruan.com/finebi6.0/doc-view-403.html>)」的情况下不需要手动输入账号密码，可直接预览模板；开启后，需手动输入账号密码进入。
2）模板预览链接
如：http://secure.finedevelop.com:55082/webroot/decision/view/report?viewlet=GettingStarted.cpt
不开启「[模板认证](<https://help.fanruan.com/finebi6.0/doc-view-403.html>)」的情况下不需要手动输入账号密码，可直接预览模板；开启后，需手动输入账号密码进入。
3）WeLink 管理生成的链接
详情参见：[WeLink集成](<https://help.fanruan.com/finebi6.0/doc-view-1797.html>) 2.5.2 生成 WeLink 链接 。
支持单点登录。
### 4.2 图文消息
  * 自定义链接  



支持单点登录，单点登录情况同 4.1 节链接消息。
注：WeLink群消息推送不支持图文消息，此消息类型将转为链接消息进行发送。
  * **定时结果链接**


支持单点登录。  

注：WeLink群消息推送不支持图文消息，此消息类型将转为链接消息进行发送。
### 4.3 文件消息
WeLink 推送不支持推送文件消息到个人，支持推送文件消息到群。
如果推送到群的文件打不开或者打开空白，需要使用 wps 或者其他工具打开。
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](/core/style/back.png)上一篇：WeLink集成](<index.php?doc-view-1797.html>)
[下一篇：已有群消息推送 ![](/core/style/forward.png) ](<index.php?doc-view-2316.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
