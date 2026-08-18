---
title: 填报修改fine_conf_entity
doc_id: 2157
url: https://help.fanruan.com/finebi/doc-view-2157.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:27
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本7.01.2 应用场景平台中的大部分的配置项都存储在 FineDB 中的 FINE_CONF_ENTITY 表中。部分配置项未提供前台配置界面，或无法通过&n

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 填报修改fine_conf_entity
[__](<doc-edit-2157.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Suki陈](<user-space-1778923.html>)_
* 历史版本：[4](<edition-list-2157.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-11 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
---  
7.0  
### 1.2 应用场景
平台中的大部分的配置项都存储在 FineDB 中的 FINE_CONF_ENTITY 表中。
部分配置项未提供前台配置界面，或无法通过 [fine_conf_entity可视化配置](<https://help.fanruan.com/finebi7.0/doc-view-1235.html>) 进行修改，只能通过修改 FINE_CONF_ENTITY 表的方式进行更改。
注1：修改 FineDB 文件，有可能造成不可修复的 BUG，因此非必要请勿修改 FineDB 文件。
注2：请优先使用前台配置界面或 [fine_conf_entity可视化配置](<https://help.fanruan.com/finebi7.0/doc-view-1235.html>) 方式修改配置项。
注3：FINE_CONF_ENTITY 表中部分配置项的值固定，不支持修改，即使成功进行了填报修改，也会按照原固定逻辑生效。
### 1.3 功能简介
本文通过一个简单的示例来介绍如何通过填报的方式修改 FINE_CONF_ENTITY 的表字段。
示例：
修改 FineDB 中 FINE_CONF_ENTITY 表中的「CustomConfig.printWidget」字段，将字段值改为「true」。
步骤：  

1）备份平台配置。
2）连接 FineDB 数据库，用于获取需要修改的 FINE_CONF_ENTITY 表。
3）将提供的「finedb字段修改」模板挂载到平台目录中，用于填报修改 FINE_CONF_ENTITY 的表字段。
4）修改表字段，并提交入库到 FineDB 中。  

5）重启工程。
## 2\. 备份平台配置
请在修改 FINE_CONF_ENTITY 的表字段前，通过手动或自动的方式备份平台配置项，备份方式请参考：[备份还原](<https://help.fanruan.com/finebi7.0/doc-view-400.html#f4941a4230376b35>) 。  

以手动备份平台配置为例，管理员登录 FineBI 系统，在「管理系统>智能运维>备份还原>平台配置」中选中手动备份。
默认备份路径为：../backup，备份文件储存在工程的 %FineBI%/webapps/webroot/backup文件夹下，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 新建数据连接
管理员登录 FineBI 系统，点击「管理系统>系统管理>常规」。点击即可查看外接数据库的信息。
![](https://help.fanruan.com/core/style/lod.png)
新建一个数据连接，数据连接名称为 FineDB ，数据库相关配置信息可根据上文获取，新建数据连接步骤请参考：[FineDB 数据连接](<https://help.fanruan.com/finebi7.0/doc-view-1080.html#7cd2bc34f5e92c31>) 。
注：数据连接名称不可修改，否则下面的模板可能无法使用。
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 目录挂载模板
1）点击下载模板：[finedb字段修改.cpt](<doc-download-/finebi6.X/uploads/file/20230328/finedb字段修改.cpt> "下载资料")
2）将模板保存至工程的%FineBI%\webapps\webroot\WEB-INF\reportlets文件夹下。
![](https://help.fanruan.com/core/style/lod.png)
3）点击「管理系统>目录管理」，添加该模板，类型选择「填报」，展示终端无需勾选（勾选可能会导致其他非管理用户看到）。
「填报预览」指在 Web 端预览用来填报数据的模板，一般在只需要录入修改数据的时候使用，也可用来查看数据。
![](https://help.fanruan.com/core/style/lod.png)
## 5\. 填报修改字段
1）在「管理系统>目录管理」中，预览该模板，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）在参数栏中输入需要修改的字段，点击「查询」。本文以「CustomConfig.printWidget」字段为例，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）将「CustomConfig.printWidget」字段值由「false」修改为「true」。
点击「提交」，弹窗提示「成功」后，修改后的数据已经入库 FineDB。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注：若 fine_conf_entity 表中不存在配置项，在填报页面中新增记录，输入参数和相应参数值即可，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

## 6\. 重启工程
填报提交成功后，重启工程，配置生效。
重启步骤请参见：[关闭或重启FineBI工程](<https://help.fanruan.com/finebi7.0/doc-view-1322.html>) 。
## 7\. 注意事项
### 7.1 还原平台配置
若用户在修改字段值后未出现预期效果，想要还原平台配置，可登录数据决策系统对本文第二节的备份文件进行还原，详情请参考：[还原](<https://help.fanruan.com/finebi7.0/doc-view-400.html#68c7c868fdf07dde>) 。
### 7.2 修改后无法登录FineBI系统
如果出现在修改 FINE_CONF_ENTITY 表字段前能够正常登录 FineBI 系统，修改后无法登录的情况，可参考以下步骤重置平台配置：  

注：如果用户在修改表字段前无法登录 FineBI 系统，使用以下步骤重置平台配置无效。
1）根据第二节设置的备份路径，找到备份文件，进行平台配置的还原。
在%FineBI%/webapps/webroot/backup/config/manual下，根据文件夹的名字（备份时间），找到备份的内容，将备份的 config.zip 解压得到的 finedb，替换%FineBI%/webapps/webroot/WEB-INF/embed下的 finedb 文件。
2）重启工程。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：fine_conf_entity可视化配置](<index.php?doc-view-1235.html>)
[下一篇：修改外接配置库账号密码 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1332.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
