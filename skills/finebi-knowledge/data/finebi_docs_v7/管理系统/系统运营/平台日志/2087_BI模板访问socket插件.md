---
title: BI模板访问socket插件
doc_id: 2087
url: https://help.fanruan.com/finebi/doc-view-2087.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:29:53
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本插件版本6.0V1.0.111.2 功能简介安装「BI模板访问socket」插件后，在不开启 Websocket&nbsp;的情况下，系统能够通过该插件正常记

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# BI模板访问socket插件
[__](<doc-edit-2087.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Suki陈](<user-space-1778923.html>)_
* 历史版本：[2](<edition-list-2087.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2022-12-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 插件版本  
---|---  
6.0| V1.0.11  
### 1.2 功能简介
安装「BI模板访问socket」插件后，在不开启 Websocket 的情况下，系统能够通过该插件正常记录用户的模板访问操作。
用户可以在「模板访问明细」中查看、查询、导出具体的访问记录。
## 2\. 示例
### 2.1 安装插件
插件下载请点击：[BI模板访问socket插件](<https://market.fanruan.com/plugin/90534010-a485-4729-a396-3bd5355ea7d4>)
安装插件请参见：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html>)
### 2.2 插件使用
插件安装完成后，系统即可在不开启 Websocket 的情况下，正常记录用户的模板访问操作。  

管理员登录 FineBI 系统，点击「管理系统>智能运维>平台日志>访问统计」，在「模板访问明细」中可以查看到具体的用户访问记录。
「模板访问明细」中的记录项包括：被访问资源（哪个目录下面的报表被访问）、操作用户（登录用户名）、操作 IP、操作时间、操作类型（什么方式访问的 BI 如：BI 查看、BI 编辑、EXCEL 导出等）。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 支持操作类型
「BI模板访问socket」插件支持记录以下类型的模板操作。如下表所示：  
注：模板访问明细可以正常记录使用导出插件进行的导出操作。  

数字  
| 类型  
| 具体场景| 显示内容  
---|---|---|---  
101| 查看 BI 模板| 预览仪表板访问「目录」上挂出的模板访问「目录」上分享的模板|   
-  
102| 编辑 BI 模板| 编辑仪表板| -  
103| 分享 BI 模板| 分享 BI 模板  
| 被分享人：XXXX  
104| 创建 BI 公共链接| 创建 BI 公共链接| -  
105| 查看BI 公共链接| 访问 BI 公共链接| -  
106| 全局导出 PDF| 编辑、预览仪表板时全局导出为 PDF「目录」上挂载的模板全局导出为 PDF「目录」上分享的模板全局导出为 PDF| -  
  
107| 全局导出 Excel| 编辑、预览仪表板时全局导出为 Excel「目录」上挂载的模板全局导出为 Excel「目录」上分享的模板全局导出为 Excel| 导出单元格：XXXX  
108| 组件导出 Excel| 编辑、预览仪表板时单独导出组件为 Excel「目录」上挂载的模板单独导出组件为 Excel「目录」上分享的模板单独导出组件为 Excel| 导出单元格：XXXX  
203| 分享自助数据集| 分享自助数据集| 被分享人：XXXX 类型：XXX  
204| 关闭分享自助数据集| 关闭分享自助数据集| 被分享人：XXXX  
205| 关闭分享 BI 模板| 关闭分享 BI 模板| 被分享人：XXXX  
  
  
### 2.4 不支持操作类型
「BI模板访问socket」插件不支持记录以下类型的模板操作：  

1）BI 模板另存为
  * 预览、编辑仪表板时的另存为主题操作
  * 「目录」上挂载的模板另存为主题操作
  * 「目录」上分享的模板另存为主题操作


2）关闭浏览器 Tab 页
  * 关闭仪表板编辑或者预览界面
  * 关闭公共链接界面


3）编辑自助数据集
4）关闭 BI 公共链接
### 2.5 模板访问明细查询
管理员可选择某个时间段，默认为「前一日」到「当日」，点击「查询」，即可查询该时间段下的明细，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
管理员可勾选「高级查询条件」，选择需要查询的内容，再点击查询，即可查询出特定设置条件下的明细，如下图所示：
注：支持筛选操作用户为空的日志，支持筛选模板名称为空的模板。
![](https://help.fanruan.com/core/style/lod.png)
### 2.6 模板访问明细导出
查询后，管理员可导出日志文件，如下图所示：
点击「导出为log」按钮可导出 .txt 格式，点击「导出为excel」可导出 .xls 格式。  

注：最多只可导出1W条日志数据。
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：错误代码汇总](<index.php?doc-view-530.html>)
[下一篇：数据集更新情况 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2168.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
