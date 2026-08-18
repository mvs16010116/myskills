---
title: 跳转到 FineReport 模板
doc_id: 1228
url: https://help.fanruan.com/finebi/doc-view-1228.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:20:46
version: "7.X"
---

> 1. 概述1.1 应用场景FineBI 支持点击组件后，跳转到 FineReport 的模板。如下图所示：1.2 功能介绍跳转到报表模板可实现传递参数或不传递参数。若目标报表模板中原本就没有参数的话，则

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 跳转到 FineReport 模板
[__](<doc-edit-1228.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[28](<edition-list-1228.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-10-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
FineBI 支持点击组件后，跳转到 FineReport 的模板。如下图所示：  

![37.gif](https://help.fanruan.com/core/style/lod.png)
### 1.2 功能介绍
跳转到报表模板可实现传递参数或不传递参数。若目标报表模板中原本就没有参数的话，则无法实现跳转传参功能。
## 2\. 跳转不传递参数
### 2.1 获取报表模板链接
有两种方式，本文使用第二种做示例。
  * 第一种：直接获取报表模板的预览链接。


从 FineBI 组件跳转到报表模板时，可能需要重新登录 FineReport 账号。
  * 第二种：将报表模板放置到 FineBI 工程中，再获取预览链接的相对路径。


需要 FineBI 中连接了此报表模板使用的数据库和数据表，否则会预览失败。使用此种方式的优点是，模板内置到了 FineBI 中，跳转到报表模板后不需要登录 FineReport 就能查看。
1）下载 cpt 模板：[自动查询.cpt](<doc-download-/finebi5.1/uploads/file/20210824/自动查询.cpt> "下载资料")
2）将下载的 cpt 模板放置到\webapps\webroot\WEB-INF\reportlets下，如下图所示：
![26.png](https://help.fanruan.com/core/style/lod.png)
3）将 「自动查询.cpt」 添加到 FineBI 目录中，如下图所示：
![1663671498559272.png](https://help.fanruan.com/core/style/lod.png)
![28.png](https://help.fanruan.com/core/style/lod.png)
4）在 FineBI 中预览该模板，并复制预览链接。如下图所示：
![30.png](https://help.fanruan.com/core/style/lod.png)
### 2.2 设置跳转
1）找到 FineBI 内置的仪表板「多角度销售分析」，如下图所示：
![1656577131936091.png](https://help.fanruan.com/core/style/lod.png)
2）对该仪表板内的「哪个区域销量最好」组件设置跳转，如下图所示：
![32.png](https://help.fanruan.com/core/style/lod.png)
3）设置跳转到报表模板的预览链接即可。如下图所示：
![33.png](https://help.fanruan.com/core/style/lod.png)
若目标报表模板放置在 FineBI 中，预览路径最好填写成相对路径。  

  * 即从 webroot 开始，删除前面的端口和 IP 信息，例如：/webroot/decision/v10/entry/access/889c14a8-f11e-462a-b46b-c021f8564f8f?preview=true
  * 对于操作过 [Tomcat 下通过 IP 直接访问数据决策系统](<https://help.fanruan.com/finebi7.0/doc-view-903.html>) 的 BI 工程，填写预览时需要从 decision 文件夹开始写路径，例如：
/decision/v10/entry/access/889c14a8-f11e-462a-b46b-c021f8564f8f?preview=true


若目标报表模板未放置在 FineBI 中，直接填写完整的预览路径即可。  

设置跳转后模板打开位置参见：[如何设置跳转窗口](<https://help.fanruan.com/finebi7.0/doc-view-1595.html#7>)
### 2.3 效果查看
点击「哪个区域销量最好」组件的非空白区域，即可跳转到报表模板「自动查询」。如下图所示：
可以看到点击「华北」跳转到 cpt 模板后，并没有实现传参。如何实现传参可参见本文第三节。
![36.gif](https://help.fanruan.com/core/style/lod.png)
## 3\. 跳转传递参数
报表模板「自动查询」中含有参数 city（报表如何设置参数可参见： [模板参数说明](<https://help.fanruan.com/finereport/doc-view-157.html>) ）
### 3.1 操作步骤
在本文第 2 节示例的基础上，我们更改下「哪个区域销量最好」组件的跳转设置，在原先的链接后面增加 &参数=字段值。
所以在本示例中，添加后缀为 &city=所属小区，如下图所示：
![35.png](https://help.fanruan.com/core/style/lod.png)
设置跳转后模板打开位置参见：[如何设置跳转窗口](<https://help.fanruan.com/finebi7.0/doc-view-1595.html#7>)
### 3.2 效果查看
点击「华北」跳转后，报表 cpt 模板的参数接收到了「华北」值，自动填充到它的文本控件中，点击「查询」即可查看到华北的数据。
![37.gif](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [制作仪表板](<category-view-99>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：跳转到网页链接](<index.php?doc-view-1596.html>)
[下一篇：FineBI跳转和Web组件传参增强 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2436.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
