---
title: 平台日志 LogDB 数据库
doc_id: 706
url: https://help.fanruan.com/finebi6.X/doc-view-706.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:20
---

> 对于运维平台部署的工程，如在部署时勾选了ElasticSearch组件，ElasticSearch会替换swift（logdb）作为日志存储。如在工程「管理系统&gt;系统管理&gt;常规」界面看到「E

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 平台日志 LogDB 数据库
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[27](<edition-list-706.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-07-15 
[](<javascript:;>) [](<javascript:>)
对于运维平台部署的工程，如在部署时勾选了ElasticSearch组件，ElasticSearch会替换swift（logdb）作为日志存储。
如在工程「管理系统>系统管理>常规」界面看到「ElasticSearch连接配置」，说明已启用ElasticSearch作为日志存储。
请勿参考本文连接工程日志库，如需连工程日志服务，请联系帆软技术支持获取帮助。技术支持联系方式：「[服务](<https://service.fanruan.com/>)>在线支持」
![](/core/style/lod.png)
  

## 1\. 概述
### 1.1 版本
FineBI 版本  
---  
6.0  
### 1.2 应用场景
为了加强对 FineBI 工程的管理，随时监控其运行状态，可在平台中开启日志记录，如下图所示：
注：系统日志级别的设置仅影响系统日志的输出，不影响操作日志。两种日志的区别请参见：[日志简介](<https://help.fanruan.com/finebi6.0/doc-view-599.html>) 。
![](/core/style/lod.png)
### 1.3 功能简介
LogDB 是 FineBI 日志监控开启之后，用于保存日志的内置数据库，那么 FineBI 日志都包含哪些内容呢？
本文将简单介绍 LogDB 中各个数据表的含义以及字段的含义。
数据库 LogDB 中表的实际应用可以参考：[LogDB 的实际应用场景](<https://help.fanruan.com/finebi6.0/doc-view-799.html>)
## 2\. 连接 LogDB 数据库
### 2.1 新建数据连接
1）管理员登录数据决策系统，点击「管理系统>数据连接>数据连接管理>新建数据连接」，如下图所示：
![](/core/style/lod.png)
2）数据连接方式选择「其他>其他JDBC」，如下图所示：
![](/core/style/lod.png)
3）如下图配置好数据连接信息，点击「保存」即可。
配置项| 内容| 备注  
---|---|---  
数据连接名称| LogDB| -  
驱动| com.fr.swift.jdbc.Driver| 手动输入驱动器名称  
数据连接 URL| jdbc:swift:emb://default| Mac、Windows、Linux 通用  
![](/core/style/lod.png)
### 2.2 查询 LogDB 数据表
注：使用 LogDB 数据表时，不支持 [实时数据](<https://help.fanruan.com/finebi6.0/doc-view-85.html>) 。  

1）管理员登录数据决策系统，点击「管理系统>数据连接>服务器数据集>创建数据集>SQL 数据集」，如下图所示：
![](/core/style/lod.png)
2）输入数据库查询语句，点击「预览」按钮即可查询 LogDB 中的数据表。如下图所示：
![](/core/style/lod.png)
### 2.3 LogDB 数据表和字段
Logdb 数据库中各个数据表和表字段的含义，请参见：[LogDB 表结构](<https://help.fanruan.com/finebi6.0/doc-view-1134.html>)
## 3\. 查询语法
本章将简单介绍LogDB支持的查询语法，本文未列举的语法，不确保可用。
### 3.1 明细查询
SQL 语句示例：
1）select * from fine_record_execute
2）select tname, displayName, consume from fine_record_execute
### 3.2 group by 查询
GROUP BY 查询，有 SUM,COUNT, MAX, MIN, AVG 这五种聚合方式。
如果SQL语句中不写聚合方式，会默认使用 COUNT 。
SQL 语句示例：
1）select sum(consume) from fine_record_execute group by tname, displayName
2）select consume from fine_record_execute group by tname, displayName
等同于：select COUNT(consume) from fine_record_execute group by tname, displayName
3）select min(consume), max(consume) from fine_record_execute group by tname, displayName
### 3.3 where 过滤条件
简单的 WHERE 过滤条件，支持 AND， OR, =，<>，>，>=， <，<=， in， isnull 
SQL 语句示例：
1）select * from fine_record_execute where consume > 10
2）select sum(consume) from fine_record_execute where consume > 10 and consume < 100 group by tname, displayName
3）select consume from fine_record_execute where tname = `doc/Advanced/Chart/GraphSwitching/多图表实现统一切换.frm`
4）select sum(consume) from fine_record_execute where tname in (`doc/Advanced/Chart/GraphSwitching/多图表实现统一切换.frm`, `doc/Advanced/Chart/Combination/柱形-面积组合图.cpt`) group by tname, displayName
### 3.4 todate() 将时间戳转换为普通的日期类型
todate() 结果的日期格式为：2018-12-18 10:15:26
SQL 语句示例：
1)  select todate(time) from fine_record_execute
2) select * from fine_record_execute where todate(time)<'2018-12-18 10:15:26' and todate(time)>'2018-12-17 10:15:26'
### 3.5 like 模糊查询
只支持前后‘%’的用法  

注1：支持使用 like 进行模糊查询，不支持 not like 用法 。
注2：目前只支持 '%'，暂不支持通配符 ‘_’，需要更新 2019-06-14 以后的 JAR。
SQL 语句示例：
1）select * from fine_record_execute where tname like '%demo%'
## 4\. 注意事项
### 4.1 LogDB 中添加表后更新失败
**问题描述：**  

在 LogDB 数据库中添加表后，更新失败。平台报错：更新失败，请联系管理员查看报错信息。如下图所示：  

![3.png](/core/style/lod.png)
**原因分析：**
1）编辑过的 [基础表](<https://help.fanruan.com/finebi6.0/doc-view-829.html#3>) 更新会嵌套，但目前 swift 不支持嵌套。所以，FineBI 目前暂不支持本节「问题描述」中的操作。
2）LogDB不支持增量更新，logdb本身就是内部数据，不建议外部连接，如果要使用抽数查看，可以使用全量更新。
### 4.2 browser 字段说明
LogDB 数据库fine_record_execute表中 browser 字段一般记录客户端访问报表所用的浏览器版本，例如：CHROME/83.0.，当 browser 字段值如下所示时：
{'Browser':'webkit','Version':'537.36','Agent':'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/81.0.4044.138 safari/537.36','BoxModel':true,'terminal':'null'}
记录的是浏览器请求头user agent（用户代理字符串）的值，user agent相当于浏览器的唯一标识。
### 4.3 一个模板编号对应多个模板名称
**问题描述：**  

LogDB 数据库fine_record_execute表中，一个 reportId 对应多个 tname ，如下图所示：
![12.png](/core/style/lod.png)
**原因分析：**
仪表板被多次重命名，每次重命名后都对仪表板进行访问/导出/打印操作，所以 fine_record_execute 表中一个模板编号会对应多个模板名称。
### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：填报修改fine_conf_entity](<index.php?doc-view-2157.html>)
[下一篇：LogDB 表结构 ![](/core/style/forward.png) ](<index.php?doc-view-1134.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
