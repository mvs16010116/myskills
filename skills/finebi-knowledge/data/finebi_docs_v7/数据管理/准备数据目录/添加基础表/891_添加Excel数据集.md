---
title: 添加Excel数据集
doc_id: 891
url: https://help.fanruan.com/finebi/doc-view-891.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:25
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动7.0-1.2 应用场景本文介绍如何将 Excel 添加到「数据目录」1.3 功能简介支持批量上传 Excel 文件。若需对上传的 Excel 数据进行更

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 添加Excel数据集
[__](<doc-edit-891.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[45](<edition-list-891.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-06-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
7.0| -  
  
### 1.2 应用场景
本文介绍如何将 Excel 添加到「数据目录」
### 1.3 功能简介
支持批量上传 Excel 文件。若需对上传的 Excel 数据进行更新，可参见：[更新Excel](<https://help.fanruan.com/finebi7.0/doc-view-331.html>) 。
## 2\. 上传前确认工作
### 2.1 确认支持上传文件类型
FineBI 可上传的表类型为 csv、xls、xlsx 三种格式，支持的字段类型详情参见： [导入Excel支持的字段类型](<https://help.fanruan.com/finebi7.0/doc-view-628.html>) 。
注1：支持上传 2003 和 2007 版本且后缀为 xls、xlsx 的 Excel 文件，不支持上传保存类型为 Excel 5.0/95 的后缀为 xls 的 Excel 文件。
注2：不支持上传加密 Excel 文件。
### 2.2 关闭文件上传校验
在上传 csv 格式文件前，需要进入「管理系统>安全管理>安全防护 」中，关闭「文件上传校验」，才能上传成功。
### 2.3 Excel 首行不能有合并单元格
上传前需要确认，添加的 Excel 首行不能有合并单元格，否则会上传失败，如下图所示：
![1592359824984918.png](https://help.fanruan.com/core/style/lod.png)
### 2.4 确认是否有函数计算的内容
上传的 Excel 数据集中不能有 Excel 函数计算的内容，例如：vlookup，sumifs 函数等。
## 3\. 操作步骤
下载示例 Excel ：[示例.zip](<doc-download-/finebi6.X/uploads/file/20220624/示例.zip> "下载资料")
### 3.1 上传 Excel
进入「公共数据」，选择一个有管理权限的文件夹（可参见：[公共数据管理权限](<https://help.fanruan.com/finebi7.0/doc-view-249.html>)）。点击「新建数据集>Excel数据集」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
选择你要上传的 Excel 。用户可以使用ctrl键、shift键或鼠标框选选择多张表，如下图所示：
注：最多选择 100 个 Excel 文件，且每个 Excel 中 sheet 页不能超过 255 张。
![](https://help.fanruan.com/core/style/lod.png)
3） Excel 内的 sheet 页会自动展开，勾选要用的 Excel 表点击「确定」。如下图所示：
注：最多在左侧勾选 100 张表，否则添加失败。
注： FineBI 在读取 Excel 文件时会自动跳过空 sheet 页。
![](https://help.fanruan.com/core/style/lod.png)
表名默认为「sheet 名」，用户可以手动修改表名。
4）若选中的表中，有「字段名、字段类型和字段顺序完全一致」的表，系统就会出现提示：存在数据表中字段一致，是否合并成一张表。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  * 点击「不合并」：正常上传示例中的三张表；
  * 点击「合并」：字段一致的「上海」和「北京」两张表将进行上下合并，合并到一张表中。如下图所示：


![](https://help.fanruan.com/core/style/lod.png)
## 4\. 注意事项
### 4.1 上传数据量限制
单个 Excel 文件不能超过256个sheet，如超过可进行多次追加上传。
### 4.2 上传时字段类型识别规则
#### 4.2.1 抽数版本识别规则
1）优先识别添加字段是否为数字格式（ 0 开头的数字不被识别为数字）。
2）其次识别添加字段是否为日期格式 。
3）最后识别添加字段是否为文本格式（超过 15 位的数值默认为文本格式）。
若添加后表的字段类型与添加前不一致，手动修改所需字段类型即可。当添加的 Excel 数据集中有字段值为小数类型（如 double、float 等浮点类型）的值时，使用 [分组表](<https://help.fanruan.com/finebi7.0/doc-view-121.html?source=4>) 或者 [交叉表](<https://help.fanruan.com/finebi7.0/doc-view-122.html?source=4>) 进行汇总计算时可能无法精确显示出小数位。
#### 4.2.2 直连版本识别规则
去除空值后，取前 100 行进行字段类型预判：前 100 行有三种字段类型取数量大于 1/3 的作为识别类型，有两种字段类型取数量大于1/2的作为识别类型。若数量相同，则按照「文本>日期>数值>空」规则进行判断。
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：添加SQL数据集](<index.php?doc-view-890.html>)
[下一篇：数据更新概述 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-93.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
