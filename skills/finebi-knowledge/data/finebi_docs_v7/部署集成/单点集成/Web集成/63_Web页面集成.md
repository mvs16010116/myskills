---
title: Web页面集成
doc_id: 63
url: https://help.fanruan.com/finebi/doc-view-63.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:46
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本功能变更6.0-1.2 功能简介FineBI 通过各种样式如表格、图表等来呈现数据，进行统计分析。这些数据表格或图表，用户在开发系统的时候也可以自己编程来实现

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Web页面集成
[__](<doc-edit-63.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[31](<edition-list-63.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-16 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
6.0| -  
### 1.2 功能简介
FineBI 通过各种样式如表格、图表等来呈现数据，进行统计分析。这些数据表格或图表，用户在开发系统的时候也可以自己编程来实现，但是工作量大，维护难。
因此用户往往选用现成的软件开发，最后将制作好的 FineBI 模板嵌入到自己的系统中，以节省项目开发周期。
用户开发的系统基本上趋于 B/S 架构的浏览器/服务器模式，因此需要将制作好的模板嵌入到系统的某一个页面中，作为页面的一部分。
本章节将详细介绍 Web 页面集成方法。
## 2\. 索引
帮助文档仅提供官方接口，提供给具备自主产品集成能力的用户使用。技术支持不负责接口示例的维护和使用问题解答。
接口调试注意事项请参见：[Web页面集成常见问题](<https://help.fanruan.com/finebi7.0/doc-view-1035.html>)
### 2.1 数据接口
注：直连接口，可在接口URL中，加一个direct即可。
例如添加分组：
  * 抽取接口：/v5/api/group/add
  * 直连接口：/v5/api/direct/group/add

分类  
| 用途| 数据接口  
---|---|---  
[数据更新](<https://help.fanruan.com/finebi7.0/doc-view-2041.html>)| 触发全局更新| /v5/api/conf/update/generate  
触发单表/文件夹更新| /v5/api/conf/update/pack/table  
触发批量更新| /v5/api/conf/update/batch  
获取此次更新实例的信息| /v5/api/conf/update/instance/{taskInstanceId}  
[数据表](<https://help.fanruan.com/finebi7.0/doc-view-2056.html>)| 添加数据集-DB表/SQL表| /v5/api/table/add  
编辑保存数据集-DB表/SQL表| /v5/api/table/update  
修改数据集转义名| /v5/api/tables/{tableName}/rename  
删除数据集| /v5/api/pack/delete  
获取数据集| /v5/api/table/{tableName}/get  
获取我的分析下直连数据的查询SQL| /v5/api/analysis/table/execute/sql/{tableName}  
获取数据集数据| /v5/api/tables/fields/page  
获取数据集分页数据| /v5/api/tables/data/page  
[公共数据文件夹](<https://help.fanruan.com/finebi7.0/doc-view-2059.html>)| 添加文件夹| /v5/api/pack/{groupId}/add  
重命名文件夹| /v5/api/pack/{packId}/rename  
删除文件夹| /v5/api/pack/delete  
获取文件夹信息| /v5/api/conf/packs/{packId}/structure  
获取业务包中的表信息| /v5/api/conf/packs/{packId}  
获取公共数据根文件夹信息| /v5/api/conf/groups  
### 2.2 仪表板接口
分类| 用途| 接口  
---|---|---  
[仪表板编辑](<https://help.fanruan.com/finebi7.0/doc-view-2060.html>)  
| 新建仪表板| /v5/api/platform/dashboard/reports  
删除仪表板| /v5/api/platform/dashboard/report  
重命名仪表板| /v5/api/platform/dashboard/rename  
仪表板另存为| /v5/api/platform/dashboard/saveas  
创建公共链接| /v5/api/platform/dashboard/{reportId}/create  
[仪表板查看](<https://help.fanruan.com/finebi7.0/doc-view-2061.html>)| 仪表板导出Excel| /v5/api/dashboard/report/export/excel  
仪表板导出PDF| /v5/api/dashboard/report/export/pdf  
仪表板导出图片| /v5/api/dashboard/report/export/png  
[仪表板分享](<https://help.fanruan.com/finebi7.0/doc-view-2063.html>)| 分享仪表板给其他用户| /v5/api/dashboard/share/user/result  
取消分享| /v5/api/dashboard/share/user/rejection/result  
分享给我的所有仪表板| /v5/api/dashboard/share  
仪表板分享给哪些用户| /v5/api/dashboard/share/user  
[仪表板信息](<https://help.fanruan.com/finebi7.0/doc-view-2064.html>)| 获取用户信息和用户创建的仪表板| /v5/api/dashboard/user/info  
获取发布管理节点下的仪表板信息| /v5/api/dashboard/search  
获取某个主题下的仪表板列表| /v5/api/platform/dashboard/list  
获取仪表板信息| /v5/api/platform/dashboard/reports/info  
获取仪表板中所有组件的信息| /v5/api/dashboard/report/consanguinity  
### 2.3 集成接口
分类| 用途| 接口  
---|---|---  
[页面集成接口](<https://help.fanruan.com/finebi7.0/doc-view-2066.html>)| 仪表板编辑页面| /v5/design/report/{reportId}/edit  
仪表板预览页面| /v5/design/report/{reportId}/view  
公共数据页面| /v5/api/conf/page  
公共数据表预览页面| /v5/api/conf/page#config/{tableName}  
我的分析页面| /v5/api/page/analysis  
我的分析数据编辑页面| /v5/conf/analysis/page  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：开放平台业务场景示例](<index.php?doc-view-2166.html>)
[下一篇：Web页面集成常见问题 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1035.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
