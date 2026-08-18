---
title: 更新Excel
doc_id: 331
url: https://help.fanruan.com/finebi/doc-view-331.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:27
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本新增内容7.0-1.2 应用场景用户需要对 Excel 进行更新的时候，可以使用「更新 Excel」功能。1.3 功能介绍支持「追加数据」与「替换数据」的操作。追

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 更新Excel
[__](<doc-edit-331.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[36](<edition-list-331.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-07-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 新增内容  
---|---  
7.0  
| -  
### 1.2 应用场景
用户需要对 Excel 进行更新的时候，可以使用「更新 Excel」功能。  

### 1.3 功能介绍
支持「追加数据」与「替换数据」的操作。
  * 追加数据：是指在原先上传的 Excel 数据表基础上追加增量数据。
  * 替换数据：是指上传新的 Excel ，替换掉原先上传的数据。


注1：在对 Excel 数据集中的字段类型进行修改时，无论是在表编辑界面，还是更新 Excel 界面，均以最后一次修改的类型生效。
注2：Excel 数据集不支持实时更新。
## 2\. 操作步骤
1）进入「数据目录」，选择你要更新的 Excel 数据集，点击「更新excel」按钮，如下图所示：
注：有编辑权限的 Excel数据集才会有「更新 Excel」按钮。
Excel 下载：[店铺.xlsx](<doc-download-/finebi6.X/uploads/file/20220916/店铺.xlsx> "下载资料")
![](https://help.fanruan.com/core/style/lod.png)
2）进入到 Excel 更新页面，可以看到有两种更新方式：「追加数据」和「替换数据」。
![](https://help.fanruan.com/core/style/lod.png)
### 2.1 追加数据
追加数据即将上传的 Excel 数据作为新增数据，添加到原数据后面。追加数据不会影响之前的原数据。
1）选择要追加的 Excel 文件，点击打开，如下图所示：
Excel 下载：[店铺-华东区.xlsx](<doc-download-/finebi5.1/uploads/file/20220506/店铺-华东区.xlsx> "下载资料")
![](https://help.fanruan.com/core/style/lod.png)
2）用户需要勾选自己需要的 sheet 页。若 Excel 文件就只有一个 sheet ，直接上传就可以。点击「确定」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）追加数据成功后，页面提示「Excel 追加数据成功」，并可以在最后看到追加的华东的数据。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
**追加数据的上传逻辑**
**情况**| **上传方式**  
---|---  
追加表中有新字段（新字段与原表所有的字段名称都不相同）| 忽略新字段，不追加数据到原表中  
  
追加表中缺少字段（原表中有该字段，但追加表中没有字段名称与之相同的进行匹配）  
| 在上传以后的追加数据的那部分，原表该字段对应的值为空值  
追加表中的字段类型和原表的字段类型不同| 根据字段类型转换为原表的类型  
追加表中有重复字段| 按照字段出现的先后顺序进行对应  
### 2.2 替换数据
重新上传是指将数据替换为新上传的 Excel 数据。
1）点击「更新Excel>替换数据」，选择要替换数据的 Excel 文件，如下图所示：
**![](https://help.fanruan.com/core/style/lod.png)**  

2）用户选择自己需要上传的 sheet 页，点击「确定」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）上传成功后， FineBI 提示「Excel 上传成功」，成功将数据替换为「华东」地区的数据，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
**替换数据的上传逻辑**
**情况**| **上传方式**  
---|---  
替换表中有新字段（新字段就是与原表所有的字段名称都不相同的字段）| 增加该字段  
替换表中缺少字段（原表中有的字段，替换表中没有字段名与之一致的字段）  
| 上传成功后，字段值都为 null  
替换表中的字段类型和原表的字段类型不同| 根据字段类型转换规则转换为当前 Excel 的类型  
替换表中有重复字段| 按照字段的出现的先后顺序进行对应，即重新上传不改变原字段名顺序  
## 3\. Excel 数据集更新说明
### 3.1 会触发 Excel 更新的操作
进行一些操作会触发Excel数据集的更新，如下所示：
操作| 更新内容| 关联  
---|---|---  
上传 Excel 数据集，成功保存该数据集后| 立即更新数据集本身| 无关联  
修改一个已经成功更新过的的 Excel 数据集的字段类型| 立即更新数据集本身| 更新存在的关联  
重新上传一个Excel数据集，成功保存该数据集后| 立即更新数据集本身| 更新存在的关联  
追加上传一个Excel数据集，成功保存该数据集后| 立即更新数据集本身| 更新存在的关联  
注1：在业务包更新时，业务包下的 Excel 数据集不会同时更新。
注2：全局更新时，某特定 Excel 数据集所在的某特定业务包配置为跟随全局更新而更新，Excel 数据集不跟随更新。
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：基础表单表更新](<index.php?doc-view-90.html>)
[下一篇：自助数据集单表更新 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1498.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
