---
title: PUT、DELETE请求转成POST插件
doc_id: 1262
url: https://help.fanruan.com/finebi6.X/doc-view-1262.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:37
---

> 1. 概述1.1 版本BI 服务器版本插件版本功能变动6.XV1.1-1.2 问题描述平台中的请求很多都是 PUT、DELETE 请求。但是部分用户环境禁用了 PUT、DELETE请求，导致平台一些请求

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# PUT、DELETE请求转成POST插件
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[3](<edition-list-1262.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
BI 服务器版本| 插件版本| 功能变动  
---|---|---  
6.X| V1.1| -  
### 1.2 问题描述
平台中的请求很多都是 PUT、DELETE 请求。
但是部分用户环境禁用了 PUT、DELETE请求，导致平台一些请求不正常。
在「控制台>网络」中可以看到这些请求都飘红报错了，如下图所示：
![1571883568130295.png](/core/style/lod.png)
## 2\. 解决方案
用户可通过安装「PUT、DELETE请求转成POST」插件，将 PUT、DELETE 请求转成 POST 请求。
### 2.1 安装插件
点击下载插件：[PUT、DELETE请求转成POST 插件](<https://market.fanruan.com/plugin/592306d9-928e-46f7-a76c-e7a0a398cac6>)
安装插件方法参照 [插件管理](<https://help.fanruan.com/finebi6.0/doc-view-459.html> "插件管理")。[](<https://help.fanruan.com/finereport/doc-view-2220.html>)
### 2.2 重启服务器
无需重启服务器，插件生效。
无论 PUT、DELETE 请求是否被禁用，都会强制转换为 POST 请求。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：FineBI外网地址](<index.php?doc-view-1336.html>)
[下一篇：temp文件夹占用空间过大 ![](/core/style/forward.png) ](<index.php?doc-view-589.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
