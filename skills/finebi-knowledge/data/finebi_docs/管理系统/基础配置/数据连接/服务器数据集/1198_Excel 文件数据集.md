---
title: Excel 文件数据集
doc_id: 1198
url: https://help.fanruan.com/finebi6.X/doc-view-1198.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:09:22
---

> 1.概述1.1 版本FineBI 版本JAR 包5.1.92021-01-061.2 功能简介Excel 数据集，就是指数据源是一系列的 Excel 文件。管理员可以将这些文件作为数据来源，用 Fine

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Excel 文件数据集
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[4](<edition-list-1198.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2023-04-10 
[](<javascript:;>) [](<javascript:>)
## 1.概述
### 1.1 版本
FineBI 版本| JAR 包  
---|---  
5.1.9| 2021-01-06  
### 1.2 功能简介
Excel 数据集，就是指数据源是一系列的 Excel 文件。
管理员可以将这些文件作为数据来源，用 FineBI 来呈现这些数据，并做相应的数据分析。  

## 2\. 添加权限
超级管理员默认可从数据决策系统添加服务器数据集。普通用户如需添加，需要超管授予权限。
超级管理员登录数据决策系统，点击「管理系统>权限管理>全局设置」，打开「分级授权」和「数据连接控制」，点击「保存」。如下图所示：
![](/core/style/lod.png)
超级管理员登录数据决策系统，点击「管理系统>权限管理>权限配置」，选择权限载体「部门/角色/用户」，选择具体项，打开「管理系统>数据连接>查看权限」。如下图所示：
![](/core/style/lod.png)
## 3\. 调用 Excel 文件
服务器数据集支持两种 Excel 文件格式：xls和xlsx
服务器数据集支持三种方法调用 Excel 文件，用户可根据自身情况进行选择。
1）服务器文件：Excel 文件存储在 BI 工程的%BI_HOME%\webroot\WEB-INF\reportlets目录下。
2）本地文件：Excel 文件存储在用户电脑上，调用后自动存储至 BI 工程的%BI_HOME%\webroot\WEB-INF\reportlets\excel目录下。
3）远程 URL 文件：Excel 文件存储在某个服务器端，调用该文件的访问 URL 即可。
### 3.1 服务器文件
将准备好的 Excel 文件上传至 BI 工程的%BI_HOME%\webroot\WEB-INF\reportlets目录下。如下图所示：
![image.png](/core/style/lod.png)
拥有权限的用户登录 BI 工程，点击「管理系统>数据连接>服务器数据集」，选择「创建数据集>文件数据集」，如下图所示：
![image.png](/core/style/lod.png)
1）设置数据集名称，名称不可为空，不可与已有数据集重复。
2）选择文件类型为 Excel。
3）文件来源选择「服务器文件」，选择 reportlets 目录下的 Excel 文件。
![image.png](/core/style/lod.png)
### 3.2 本地文件
拥有权限的用户登录 BI 工程，点击「管理系统>数据连接>服务器数据集」，选择「创建数据集>文件数据集」，如下图所示：
![](/core/style/lod.png)
1）设置数据集名称，名称不可为空，不可与已有数据集重复。
2）选择文件类型为 Excel。
3）文件来源选择「本地文件」，选择本地电脑准备好的 Excel 文件。上传成功后跳出提示框：Excel 上传成功！
![image.png](/core/style/lod.png)
已上传的文件自动存储至 BI 工程的%BI_HOME%\webroot\WEB-INF\reportlets\excel目录下。如下图所示：
注：若该目录下存在同名文件，则无法成功上传。
![image.png](/core/style/lod.png)
### 3.3 远程 URL 文件
将 Excel 文件存储在某个服务器下，获得该文件的访问 URL。
注：请确保 BI 工程可成功访问该文件，否则将调用失败。
拥有权限的用户登录 BI 工程，点击「管理系统>数据连接>服务器数据集」，选择「创建数据集>文件数据集」，如下图所示：
![](/core/style/lod.png)
1）设置数据集名称，名称不可为空，不可与已有数据集重复。
2）选择文件类型为 Excel。
3）文件来源选择「URL」，输入 URL 地址，点击「测试连接」。连接成功后跳出提示框：连接成功！
注：URL地址中若包含中文，必须先进行 [URL转码](<https://tool.oschina.net/encode?type=4>) ，在平台填写转码后的路径，方可正常访问。
![image.png](/core/style/lod.png)
## 4\. 数据集设置
1）用户可自定义设置数据集函数。
2）用户可选择调用的 Excel 文件第一行是否包含标题。
点击保存，即保存服务器数据集。
![image.png](/core/style/lod.png)
## 5\. 注意事项
### 5.1 本地文件上传失败
**问题描述：**
本地文件上传失败，提示：XXX文件已经存在，但此时系统「服务器数据集>文件数据集」中未使用该文件。如下图所示：
![](/core/style/lod.png)
**原因分析：**
用户曾经使用本地文件的方法调用过同名文件。
本地文件在调用后会自动存储至 BI 工程，并且在「管理系统>服务器数据集」页面中删除该文件数据集时，不会删除 BI 工程下的该文件。
因此，再次上传时，会因为同名文件的存在而导致上传失败。
**解决方案：**
前往 BI 工程%BI_HOME%\webroot\WEB-INF\reportlets\excel文件夹下找到原同名文件，删除/重命名原同名文件后，重新上传文件即可。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：文本 文件数据集](<index.php?doc-view-1197.html>)
[下一篇：XML 文件数据集 ![](/core/style/forward.png) ](<index.php?doc-view-1199.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
