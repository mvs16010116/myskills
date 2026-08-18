---
title: 可监控SQL执行的druid线程池
doc_id: 2698
url: https://help.fanruan.com/finebi/doc-view-2698.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:15
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本插件版本7.0V2.61.2 功能简介安装「可监控SQL执行的druid线程池」插件后，在管理系统下新增「SQL执行监控」节点。用户可在该节点页面中实现以下功

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 可监控SQL执行的druid线程池
[__](<doc-edit-2698.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[3](<edition-list-2698.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-10-23 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本| 插件版本  
---|---  
7.0| V2.6  
### 1.2 功能简介
安装「可监控SQL执行的druid线程池」插件后，在管理系统下新增「SQL执行监控」节点。
用户可在该节点页面中实现以下功能：
1）查看 SQL 的执行的详细数据，包括 SQL语句、模板与执行次数、数据连接名等；  

2）支持用户在该页面中查询、导出、重置 SQL 执行记录。
## 2\. 示例
### 2.1 安装插件
点击下载插件：[可监控SQL执行的druid线程池](<https://market.fanruan.com/plugin/7015e7f8-6465-4a84-b3c8-36b445ab0165>)
插件安装方法请参见：[插件管理](<https://help.fanruan.com/finebi/doc-view-459.html>)
### 2.2 开启SQL执行监控
插件安装完成后，管理员登录FineBI系统，可以查看到在管理系统下已经新增「SQL执行监控」节点。
![](https://help.fanruan.com/core/style/lod.png)
SQL 执行监控默认为未开启状态。
1）点击「开启」按钮
弹出提示信息「当前操作会中断所有JDBC连接」。
原因：如果有正在访问的数据连接（如预览模板取数等），会导致已有的数据库连接无法被监控，因此需要全部断开再开启。
2）点击「确定」按钮
自动断开全部的数据连接，SQL执行监控开启成功。
系统开始记录所有新的 JDBC 连接和 SQL 执行信息。
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 查看SQL执行记录
开启 SQL 执行监控后，所有执行过的 SQL 语句均会在「SQL执行监控」页面内留下记录。
点击「刷新」按钮后，即可查看到更新的的 SQL 执行记录。
「SQL执行监控」页面内会提供一张报表供用户查看具体信息。如下图所示：
  * 编号：为不同的 SQL 语句生成编号；
  * SQL：执行的 SQL 语句；
  * 模板与执行次数：在同一数据连接下，记录报表会根据 SQL 语句分组，记录一条 SQL 语句在不同模板中的使用与执行次数；
  * 时间相关信息包括：执行总时间、平均时间、最长执行时间、最大执行时间开始时间、游标时间、平均游标时间；
  * 执行次数：对每条 SQL 语句的执行次数组内求和；
  * 行数相关信息包括：获取行数、平均行数、最大行数；
  * 数据连接名：SQL 语句执行时访问的数据连接。


![](https://help.fanruan.com/core/style/lod.png)
### 2.4 查询SQL执行记录
用户可以选择某个数据连接，并设置查询条件。点击「查询」，可以取出该查询条件下的 SQL 执行信息，如下图所示：
注：执行过 SQL 的数据连接才会出现在「选择数据连接」的下拉复选框中。
![](https://help.fanruan.com/core/style/lod.png)
### 2.5 导出SQL执行记录
SQL 执行记录不支持存储，用户可以通过页面工具栏中的按钮导出记录，导出方式包括：打印、导出、邮件等。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 2.6 重置SQL执行记录
点击「重置」按钮，选择「确定」后，系统会清除该页面上的 SQL 执行记录，开始记录所有新的 JDBC 连接和 SQL 执行信息。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 2.7 关闭SQL执行监控
点击「关闭」按钮，弹出提示信息「确定退出?」，点击「确定」，即可关闭 SQL 执行监控。
退出监控后，再次开启监控，在页面上不会保存上次的监控记录，开始记录所有新的 JDBC 连接和 SQL 执行信息。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：DB2数据连接常见问题](<index.php?doc-view-2120.html>)
[下一篇：更换表的数据库来源 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-810.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
