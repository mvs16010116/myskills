---
title: FineBI初始化设置
doc_id: 262
url: https://help.fanruan.com/finebi6.X/doc-view-262.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:29
---

> 应用场景当 FineBI 在&nbsp;安装并启动&nbsp;后，会自动跳出 FineBI 数据决策系统平台网页。本章介绍首次访问 FineBI 和再次登录的步骤。功能简介完成初始化后，FineBI 可

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI初始化设置
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[41](<edition-list-262.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-23 
[](<javascript:;>) [](<javascript:>)
## 应用场景
当 FineBI 在 [安装并启动](<https://help.fanruan.com/finebi6.0/doc-view-260.html>) 后，会自动跳出 FineBI 数据决策系统平台网页。本章介绍首次访问 FineBI 和再次登录的步骤。
## 功能简介
完成初始化后，FineBI 可进行一系列的数据准备、数据加工、可视化分析等操作。
## 首次访问决策系统
在本地安装启动 FineBI 服务器以后，输入地址：http://localhost:37799/webroot/decision 访问 FineBI，进入引导页面，分为两个步骤：账号设置和数据库设置，如下图所示：
![1.png](/core/style/lod.png)  

### 账号设置
账号设置：配置系统管理员的用户名和密码，管理员负责统筹整个系统，包含用户、数据、权限、系统信息等。
系统管理员也就是 FineBI 系统中的最大权限用户，介绍详情参见：[管理员修改密码/忘记密码](<https://help.fanruan.com/finebi6.0/doc-view-1299.html>) 修改密码。
### 数据库选择
点击「下一步」进入数据库选择。如下图所示：
数据库中存放 FineBI 所有使用信息（不包括平台属性配置），如目录树设置、模板定时任务信息等。
![2022-09-05_15-49-11.gif](/core/style/lod.png)
#### 内置数据库
内置数据库适用于个人本地试用，点击「直接登录」，可直接登录系统使用。
#### 外接数据库
外接数据库适用于企业正式使用，点击「配置数据库」，为工程配置外接数据库。  

关于外接数据库的配置，请参考 [配置外接数据库](<https://help.fanruan.com/finebi6.0/doc-view-437.html>) 。
## 再次登录
启动 FineBI ，访问http://localhost:37799/webroot/decision，再次进入登录页面，输入正确用户名和密码登录。如下图所示：
注：若需要修改 BI 访问端口，可参考：[Tomcat 下通过 IP 直接访问数据决策系统](<https://help.fanruan.com/finebi6.0/doc-view-903.html>)。
![2022-09-05_15-53-11.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：FineBI个人试用版安装指南](<index.php?doc-view-260.html>)
[下一篇：FineBI个人试用版端口开放列表 ![](/core/style/forward.png) ](<index.php?doc-view-359.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
