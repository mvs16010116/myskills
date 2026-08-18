---
title: 添加Excel数据
doc_id: 1903
url: https://help.fanruan.com/finebi6.X/doc-view-1903.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:58:06
---

> 1. 概述1.1 应用场景&nbsp;FineBI 支持用户使用本地 Excel 表分析。1.2 功能简介在「我的分析&gt;分析主题&gt;数据」下可以添加「本地Excel文件」。1.3 准备工作1.

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 添加Excel数据
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[16](<edition-list-1903.html>)
* 最近更新：[Marlon.Zhao](<user-space-2679419.html>) 于 2024-06-04 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
FineBI 支持用户使用本地 Excel 表分析。
### 1.2 功能简介
在「我的分析>分析主题>数据」下可以添加「本地Excel文件」。
### 1.3 准备工作
#### 1.3.1 确认支持上传文件类型  

FineBI 可上传的表类型为 csv、xls、xlsx 三种格式，支持的字段类型详情参见： [导入Excel支持的字段类型](<https://help.fanruan.com/finebi6.0/doc-view-628.html>) 。
注1：支持上传 2003 和 2007 版本且后缀为 xls、xlsx 的 Excel 文件，不支持上传保存类型为 Excel 5.0/95 的后缀为 xls 的 Excel 文件。
注2：不支持上传加密 Excel 文件。
#### 1.3.2 关闭文件上传校验
在上传 csv 格式文件前，需要进入「管理系统>安全管理>安全防护 」中，关闭「文件上传校验」，才能上传成功。
#### 1.3.3 Excel 首行不能有合并单元格
上传前需要确认，添加的 Excel 首行不能有合并单元格，否则会上传失败。
#### 1.3.4 确认是否有函数计算的内容
上传的 Excel 中不能有 Excel 函数计算的内容，例如：vlookup，sumifs 函数等。
#### 1.3.5 确认文件名称是否符合规范
文件名不能包含？*："<>\/，不能空格开头。
#### 1.3.6 数据量限制
分析主题中，最多添加 100 张数据表。
## 2\. 操作步骤
### 2.1 添加Excel数据
1）点击创建 [分析主题](<https://help.fanruan.com/finebi6.0/doc-view-1888.html>) 。进入添加数据界面。点击「本地Excel文件」。点击或拖拽都可上传Excel，点击「上传数据」。如下图所示：
![](/core/style/lod.png)
### 2.2 选择Excel表
1）点「上传数据」选择本地文件中的 Excel 表，点击打开。如下图所示：  

![](/core/style/lod.png)
2）选择要添加的表，可以编辑表名。完成后点击「确定」。成功上传。如下图所示：
![](/core/style/lod.png)
### 2.3 数据预览并保存更新
完成后进入数据编辑界面，点击保存更新主题数据。如下图所示：  

![](/core/style/lod.png)
点击右上角「预览」，预览数据。如下图所示：  

![](/core/style/lod.png)
### 2.4 更新数据
在数据编辑界面，点击「更新Excel」，如下图所示： 
![](/core/style/lod.png)
用户可以进行「追加数据」和「替换数据」，操作步骤及规则可参见 [更新Excel](<https://help.fanruan.com/finebi6.0/doc-view-331.html>) 。如下图所示：  

![](/core/style/lod.png)
  

## 3\. 批量上传数据
用户支持选择多张Excel表上传。可以使用ctrl键、shift键或鼠标框选选择多张表。
选择多表后，可选择多 sheet 页数据上传。一个 Excel 文件中的多 sheet 页数据，会变成多张表上传到 FineBI 中。如下图所示：
![23.png](/core/style/lod.png)
## 4\. 数据合并
所有表的字段类型调整好后，即可以点击「确定」。
若选中的表中，有「字段名、字段类型和字段顺序完全一致」的表，系统就会出现提示：存在数据表中字段一致，是否合并成一张表。
详情请参见：[添加Excel数据集](<https://help.fanruan.com/finebi6.0/doc-view-891.html>) 第 3.1 节
### 附件列表 
  
下载次数：：0
    
**主题：** [添加并编辑数据](<category-view-94>)
[![](/core/style/back.png)上一篇：添加当前工程上的数据](<index.php?doc-view-1902.html>)
[下一篇：编辑数据概述 ![](/core/style/forward.png) ](<index.php?doc-view-506.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
