---
title: token读取失败导致登录异常
doc_id: 2295
url: https://help.fanruan.com/finebi/doc-view-2295.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:04
version: "7.X"
---

> 1. 概述1.1 版本说明FineBI服务器版本功能变动6.0-1.2 问题描述登录时提示：登录信息已失效，错误代码：21300019，如下图所示：1.3 原因分析工程环境设置 HttpOnly 、域名

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# token读取失败导致登录异常
[__](<doc-edit-2295.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[1](<edition-list-2295.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本说明
FineBI服务器版本  
| 功能变动  
---|---  
6.0| -  
### 1.2 问题描述
登录时提示：登录信息已失效，错误代码：21300019，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 1.3 原因分析
工程环境设置 HttpOnly 、域名等情况后，阻止了前台从 cookie 里读取 token，从而无法写入到 header 里。
进行如跨域登录、后台单点等登录操作，导致后台读取 token进行身份验证失败。
## 2\. 解决方案
超级管理员可将 FineDB 的 fine_conf_entity 表中 ServerConfig.tokenFromCookie 参数值修改为 true，并重启服务器。
注：修改 FineDB 数据库表字段值的方法请参考 [FineDB 常用表字段修改](<https://help.fanruan.com/finebi7.0/doc-view-1235.html>)
参数及对应的值说明如下表所示：
参数名  
| 参数值  
---|---  
ServerConfig.tokenFromCookie| 参数值需为布尔型，默认为 false
  * false：后台校验 token 时不可从 cookie 中取
  * true：后台校验 token 时可从 cookie 中取

  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：单点登录常见问题](<index.php?doc-view-1278.html>)
[下一篇：集群参数配置 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1192.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
