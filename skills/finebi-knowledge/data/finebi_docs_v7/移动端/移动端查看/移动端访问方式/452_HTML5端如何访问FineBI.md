---
title: HTML5端如何访问FineBI
doc_id: 452
url: https://help.fanruan.com/finebi/doc-view-452.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:10
version: "7.X"
---

> 1.&nbsp;概述1.1 版本FineBI 版本功能变更6.0-1.2&nbsp;应用场景本文介绍在 HTML5&nbsp;端查看 FineBI 的方法，使用移动浏览器访问仪表板或工程。2. 操作方法

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# HTML5端如何访问FineBI
[__](<doc-edit-452.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[30](<edition-list-452.html>)
* 最近更新：[Fairy.Zhang](<user-space-2357884.html>) 于 2024-12-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变更  
---|---  
6.0| -  
### 1.2 应用场景
本文介绍在 HTML5 端查看 FineBI 的方法，使用移动浏览器访问仪表板或工程。
## 2\. 操作方法
### 2.1 安装插件
HTML5 端访问 FineBI，依赖两个插件：
点击下载插件：[HTML5移动端展现](<https://market.fanruan.com/plugin/8bc0fc35-8403-4fbf-afe5-526bb2452932>)、[BI6.0移动端布局编辑界面H5](<https://market.fanruan.com/plugin/41162e14-d7e3-4d36-a1a4-8b21c8bb98e8>)
安装插件方法参照：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html> "插件管理")
![](https://help.fanruan.com/core/style/lod.png)  

### 2.2 移动端访问
注：移动端访问相应链接时，应保证移动端与 PC 端处于同一网络环境下。
**移动端可直接使用 PC 端链接访问对应页面。**
  

移动端访问时各链接格式如下表所示：
预览方式| 分类| 场景| 链接格式  
---|---|---|---  
HTML5  
| 平台  
| 登录页面| http://ip:端口号/webroot/decision/login  
目录页面| http://ip:端口号/webroot/decision#/directory  
单张仪表板| 预览链接  
| 获取到 [仪表板预览](<https://help.fanruan.com/finebi7.0/doc-view-159.html>) 链接直接移动端访问即可http://ip:端口号/webroot/decision/v5/design/report/此处放置仪表板ID/view  
公共链接| 获取到[公共链接](<https://help.fanruan.com/finebi7.0/doc-view-164.html>)直接移动端访问即可  
给出一些示例：
**1）登录页面**
PC端FineBI的链接为：http://localhost:37799/webroot/decision
移动端访问时链接需修改为：http://172.16.2.134:37799/webroot/decision
![Screenshot_20220930_134656_com.tencent.wework.jpg](https://help.fanruan.com/core/style/lod.png)
**2）目录页面**
PC端FineBI的目录链接为：http://localhost:37799/webroot/decision#/directory
移动端访问时需修改为：http://172.16.2.134:37799/webroot/decision#/directory
注：访问目录页面时，第一次进入需要先登录，如果缓存中有 Token ，可以直接进入目录页面。 
![Screenshot_20220930_134920_com.tencent.wework.jpg](https://help.fanruan.com/core/style/lod.png)
**3）访问单张仪表板**
移动端也可以直接通过链接访问单张仪表板，PC端获取仪表板链接的方式分别为「预览链接」和「公共链接 」。
两种方式获取的链接均需要修改为指定格式才能在移动端访问。
  * 预览链接


在 PC 端预览仪表板时，可以在浏览器的地址栏直接获取该仪表板的预览链接，例如：
http://localhost:37799/webroot/decision#/analysis/own/subject/e5c58a91c26143299551ba73d856242f/report/c2594718581f493f951f055b0f3122f6  
注：末尾的 c2594718581f493f951f055b0f3122f6 是仪表板的ID，写移动端链接要用到。
![Snag_4d2db469.png](https://help.fanruan.com/core/style/lod.png)
移动端访问时链接如下修改，链接中附带了仪表板ID：
http://192.168.43.102:37799/webroot/decision/v5/design/report/c2594718581f493f951f055b0f3122f6/view
  * 公共链接


仪表板可通过生成公共链接的方式分享给他人查看，如下图所示：
![Snag_4d47c245.png](https://help.fanruan.com/core/style/lod.png)
示例：
PC端生成的公共链接为：http://localhost:37799/webroot/decision/link/pUHK
移动端访问时链接修改下IP：http://192.168.43.102:37799/webroot/decision/link/pUHK
## 3\. URL特殊参数
H5 端访问访问仪表板或工程时，URL 后面可以加参数实现一些特殊效果，参数写法和作用如下：
参数  
| 作用  
---|---  
?force_web=true| 强制 PC 布局  
?fine_digital_signature=数字签名密钥| 添加数字签名密钥  
## 4\. 注意事项
### 4.1 仪表板下方出现左向箭头
H5 预览时，模板下方出现左向箭头，这个是浏览器窗口过宽，识别成了横屏展示效果。
解决方案就是改变浏览器的窗口大小。
![1608688335752161.png](https://help.fanruan.com/core/style/lod.png)
### 4.2 仪表板无法查看提示该模板已被删除
**报错详情：**
在电脑端做的仪表板，手机端无法查看，显示「该模板已被删除」。
**解决方案：**
没有注册 lic 。关于注册步骤，详情请参考：[本地机器信息认证](<https://help.fanruan.com/finebi7.0/doc-view-188.html>) 。
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：移动端功能点说明](<index.php?doc-view-552.html>)
[下一篇：App端如何访问FineBI ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-346.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
