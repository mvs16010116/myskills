---
title: FineBI跳转和Web组件传参增强
doc_id: 2436
url: https://help.fanruan.com/finebi/doc-view-2436.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:20:47
version: "7.X"
---

> 1. 概述1.1 版本&nbsp;FineBI 版本插件版本功能变动7.0V1.0.1-1.2 应用场景使用本插件后：web 组件无需再通过链接方式添加 FineReport 模板，可以直接添加目录中已

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI跳转和Web组件传参增强
[__](<doc-edit-2436.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[5](<edition-list-2436.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-10-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 插件版本| 功能变动  
---|---|---  
7.0  
| V1.0.1  
| -  
  
### 1.2 应用场景
使用本插件后：
  * web 组件无需再通过链接方式添加 FineReport 模板，可以直接添加目录中已挂载的 FineReport 模板。
  * 普通组件可联动 web 组件中的 FineReport 模板
  * FineBI 仪表板可直接跳转到已挂载到目录的 FineReport 模板


![](https://help.fanruan.com/core/style/lod.png)
## 2\. 插件安装
点击下载插件：[finebi跳转和web组件传参增强](<https://market.fanruan.com/plugin/bbbddd96-ed3b-4e43-a578-2fb64d51b1a3>)
FineBI 插件安装方法参照：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html>)
## 3\. 操作步骤
### 3.1 挂载 FineReport 模板到目录
使用插件实现 FineReport 模板的web组件挂载、联动、跳转的前提，是需要将 FineReport 的模板挂载到目录。  

1）下载 cpt 模板：[自动查询.cpt](<doc-download-/finebi6.X/uploads/file/20240708/自动查询.cpt> "下载资料")
2）将下载的 cpt 模板放置到webroot\WEB-INF\reportlets下，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)  

3）将 「自动查询.cpt」 添加到 FineBI 目录中，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 web组件挂载 FineReport 模板
在 Web 组件中直接选择挂载后的 FineReport 模板「自动查询」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
效果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.3 联动 FineReport 模板
使用 web 组件挂载 FineReport 模板后，可实现组件与 FineReport 模板的联动。
报表模板「自动查询」中含有参数 city（报表如何设置参数可参见： [模板参数说明](<https://help.fanruan.com/finereport/doc-view-157.html>) ）
更改下 Web组件的被联动设置，配置组件字段和web组件字段。如下图所示：
  * 组件字段：设置组件要传递哪个字段值，这里我们选择「所属小区」
  * web组件字段：填写参数名


即点击「所属小区」字段对参数「city」传值
![](https://help.fanruan.com/core/style/lod.png)  
效果如下图所示：
![23.gif](https://help.fanruan.com/core/style/lod.png)
### 3.4 跳转到 FineReport 模板
下载示例数据：[门店销售数据统计.xlsx](<doc-download-/finebi6.X/uploads/file/20240611/门店销售数据统计.xlsx> "下载资料")
1）使用「所属小区、销售额」制作组件和仪表板，对该组件添加跳转，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
#### 3.4.1 普通跳转
设置跳转到的报表模板「自动查询」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
设置跳转后模板打开位置参见：[如何设置跳转窗口](<https://help.fanruan.com/finebi7.0/doc-view-1595.html#7>)
点击组件的非空白区域，即可跳转到报表模板「自动查询」。如下图所示：
可以看到点击「华中」跳转到 cpt 模板后，并没有实现传参。如何实现传参可参见本文第三节。
![](https://help.fanruan.com/core/style/lod.png)
#### 3.4.2 跳转传递参数
报表模板「自动查询」中含有参数 city（报表如何设置参数可参见： [模板参数说明](<https://help.fanruan.com/finereport/doc-view-157.html>) ）
在本文第 3.1 节示例的基础上，我们更改下组件的跳转设置，配置源字段和目标字段。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
点击所属小区的「华中」跳转后，报表 cpt 模板的参数接收到了「华中」值，自动填充到它的文本控件中，点击「查询」即可查看到华中的数据。
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [制作可视化组件](<category-view-569>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：跳转到 FineReport 模板](<index.php?doc-view-1228.html>)
[下一篇：钻取简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1630.html>)


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
