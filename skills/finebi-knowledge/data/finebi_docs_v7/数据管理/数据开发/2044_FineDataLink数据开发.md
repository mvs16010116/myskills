---
title: FineDataLink数据开发
doc_id: 2044
url: https://help.fanruan.com/finebi/doc-view-2044.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:27:01
version: "7.X"
---

> 1. 什么是数据开发「数据开发」是&nbsp;FineDataLink&nbsp;产品中的一个功能点，可通过 SQL 和可视化的方式，完成 ETL 任务的开发和步骤编排。FineBI 支持对接 Fine

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineDataLink数据开发
[__](<doc-edit-2044.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[22](<edition-list-2044.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2025-09-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 什么是数据开发
「数据开发」是 [FineDataLink](<https://help.fanruan.com/finedatalink/doc-view-2.html?source=0&from=BI01>) 产品中的一个功能点，可通过 SQL 和可视化的方式，完成 ETL 任务的开发和步骤编排。
![40.png](https://help.fanruan.com/core/style/lod.png)
FineBI 支持对接 FineDataLink 数据开发模块，具备 ELT、ETL 双核数据开发引擎，灵活满足不同数据处理场景，IT 人员可使用该功能将处理好的高质量数据同步至 FineBI，以供业务人员自助分析。
![1686122996768848.png](https://help.fanruan.com/core/style/lod.png)
## 2\. 数据开发介绍
![10.png](https://help.fanruan.com/core/style/lod.png)
### 2.1 支持的数据源
数据开发支持多种数据源，可以将多种来源数据进行数据处理和集成。
支持数据读取和数据写入的数据库请参见：[FineDataLink支持的数据源](<https://help.fanruan.com/finedatalink/doc-view-39.html?source=0&from=BI01>) 第三章内容。
![1687258278288089.png](https://help.fanruan.com/core/style/lod.png)
### 2.2 任务管理
数据开发中通过「定时任务」存放设计好的业务流程。
通过「文件夹」对定时任务进行管理。
![1686122238256656.png](https://help.fanruan.com/core/style/lod.png)
### 2.3 任务开发
![1687258311301977.png](https://help.fanruan.com/core/style/lod.png)
#### 2.3.1 价值场景示例
**1）实现跨数据源批量[同步数据](<https://help.fanruan.com/finedatalink/doc-view-183.html?source=0&from=BI01>)**
![1687258456702485.png](https://help.fanruan.com/core/style/lod.png)
**2）提供多种数据转换算子，灵活处理数据。**
下图中的算子介绍请参见本文 2.3.2 节内容。
![1687258479697809.png](https://help.fanruan.com/core/style/lod.png)
****3）支持JSON解析，一键解析半结构化数据。****
****![1687258506728312.png](https://help.fanruan.com/core/style/lod.png)****
****4）支持Spark SQL，覆盖更多数据转换场景。****
****![72.png](https://help.fanruan.com/core/style/lod.png)****
****5）循环容器，支持对数据遍历循环。****
****![73.png](https://help.fanruan.com/core/style/lod.png)****
****6）对接企微，实现数据找人。****
****![74.png](https://help.fanruan.com/core/style/lod.png)****
****7）支持 SQL 脚本，对数据库进行增删改。****
****![75.png](https://help.fanruan.com/core/style/lod.png)****
****8）支持调用 shell 脚本，对接外部的独立数据处理过程。****
****![76.png](https://help.fanruan.com/core/style/lod.png)****
#### 2.3.2 节点介绍
任务开发界面如下图所示：  

![46.png](https://help.fanruan.com/core/style/lod.png)
节点介绍如下表所示：  

分类| 节点| 说明  
---|---|---  
通用| [数据同步](<https://help.fanruan.com/finedatalink/doc-view-7.html?source=0&from=BI01>)| 
  * 适用于较大数据量的同步场景，当单表数据量超过 1kw 时，推荐使用数据同步
  * 适用于没有复杂处理逻辑的数据同步场景

  
[数据转换](<https://help.fanruan.com/finedatalink/doc-view-10.html?source=0&from=BI01>)| 当数据需要利用 FDL 完成复杂场景处理时，推荐使用数据转换  
脚本| SQL 脚本| 通过写 SQL 的形式，完成对表和数据的处理，例如：创建、更新、删除、读取、关联、汇总等操作  
[shell脚本](<https://help.fanruan.com/finedatalink/doc-view-117.html?source=0&from=BI01>)| 支持通过执行 Shell 脚本，对接外部的独立数据处理过程例如 SVN 更新、文件运维清理、调用 Kettle 任务、调用 Python 计算任务、调用 Spark 计算任务、执行数据库备份还原等  
流程| [参数赋值](<https://help.fanruan.com/finedatalink/doc-view-18.html?source=0&from=BI01>)| 参数赋值节点通过数据来源将需要赋值的数据取出，并为参数赋值将获取到的数据输出为参数，下游节点可以利用公式使用参数值  
[条件分支](<https://help.fanruan.com/finedatalink/doc-view-19.html?source=0&from=BI01>)  
| 基于配置的执行条件，判断是否运行下游节点  
[调用任务](<https://help.fanruan.com/finedatalink/doc-view-21.html?source=0&from=BI01>)| 调用平台内其他定时任务，完成跨任务的调度执行  
[循环容器](<https://help.fanruan.com/finedatalink/doc-view-67.html?source=0&from=BI01>)| 在容器内对节点执行遍历循环、条件循环，满足节点循环执行的场景  
[消息通知](<https://help.fanruan.com/finedatalink/doc-view-32.html?source=0&from=BI01>)| 自定义通知内容，通知指定渠道的用户通知渠道：邮件/短信/企业微信应用推送/企业微信群机器人/钉钉应用推送/钉钉群机器人通知内容：可自定义  
[虚拟节点](<https://help.fanruan.com/finedatalink/doc-view-20.html?source=0&from=BI01>)| 空操作，无实际意义，常用于多分支到多分支场景的实现  
其他| [备注说明](<https://help.fanruan.com/finedatalink/doc-view-69.html?source=0&from=BI01>)| 可帮助用户为任务、节点增加备注  
其中，「数据转换」节点提供输入、输出、转换等类型的算子，可实现复杂的数据处理。如下图所示：
![47.png](https://help.fanruan.com/core/style/lod.png)
「数据转换」中的算子介绍如下表所示：  

分类| 算子| 说明  
---|---|---  
数据输入| DB表输入  
| 读取关系型数据库表中的数据  
[API输入](<https://help.fanruan.com/finedatalink/doc-view-90.html?source=0&from=BI01>)| 从 API 中读取数据，支持 RESTful API 和 WebService API  
[文件输入](<https://help.fanruan.com/finedatalink/doc-view-203.html?source=0&from=BI01>)| 从 FineDataLink 服务器本地和 FTP/SFTP 服务器上读取 Excel、CSV、Txt 文件数据  
[简道云输入](<https://help.fanruan.com/finedatalink/doc-view-61.html?source=0&from=BI01>)| 读取简道云表单中的数据  
[MongoDB输入](<https://help.fanruan.com/finedatalink/doc-view-72.html?source=0&from=BI01>)| 读取 MongoDB 中指定集合的数据  
[SAP RFC输入](<https://help.fanruan.com/finedatalink/doc-view-139.html?source=0&from=BI01>)| 支持通过 RFC 接口调用 SAP 系统内已经开发好的函数，并将数据取出  
数据集输入| 支持读取文件数据集（Excel、TXT、XML、CSV）、树数据集、存储过程、程序数据集、内置数据集、关联数据集。其中存储过程、程序数据集、内置数据集、关联数据集仅在FineReport设计器可定义  
数据输出| [DB表输出](<https://help.fanruan.com/finedatalink/doc-view-229.html?source=0&from=BI01>)  
| 将数据输出到关系型数据库表  
[参数输出](<https://help.fanruan.com/finedatalink/doc-view-190.html?source=0&from=BI01>)| 将取到的数据输出为参数，供下游节点使用  
[API输出](<https://help.fanruan.com/finedatalink/doc-view-285.html?source=0&from=BI01>)| 将数据输出到API  
[简道云输出](<https://help.fanruan.com/finedatalink/doc-view-234.html?source=0&from=BI01>)| 将数据输出到简道云表单  
连接| [数据关联](<https://help.fanruan.com/finedatalink/doc-view-35.html?source=0&from=BI01>)| 用户两张数据表在不同的数据库中，希望能够将两张不同来源库的表进行关联生成新表。连接方式如下：
  * 左连接（LEFT JOIN）：左合并  

  * 右连接（RIGHT JOIN）：右合并
  * 内连接（INNER JOIN）：取交集
  * 全外连接（FULL OUTER JOIN）：取并集

  
[数据比对](<https://help.fanruan.com/finedatalink/doc-view-12.html?source=0&from=BI01>)| 将 2 个输入的数据进行比较，筛选出新增、删除、相同、更新的数据  
转换| [列转行](<https://help.fanruan.com/finedatalink/doc-view-11.html?source=0&from=BI01>)  
| 实现数据表行列结构的改变，列转行  
[行转列](<https://help.fanruan.com/finedatalink/doc-view-197.html?source=0&from=BI01>)| 实现数据表行列结构的改变，行转列  
[JSON解析](<https://help.fanruan.com/finedatalink/doc-view-13.html?source=0&from=BI01>)| 解析 JSON 结构的数据，输出行列格式的数据  
[XML解析](<https://help.fanruan.com/finedatalink/doc-view-123.html?source=0&from=BI01>)| 将 XML 格式数据解析为行列格式数据  
[字段设置](<https://help.fanruan.com/finedatalink/doc-view-40.html?source=0&from=BI01>)| 可实现数据流字段的选择、重命名、数据类型转换操作  
[新增计算列](<https://help.fanruan.com/finedatalink/doc-view-286.html?source=0&from=BI01>)| 在不影响原有字段的情况下，可利用原有字段通过引用或计算获得一个新的字段  
[数据过滤](<https://help.fanruan.com/finedatalink/doc-view-237.html?source=0&from=BI01>)| 过滤符合条件的数据记录  
[JSON生成](<https://help.fanruan.com/finedatalink/doc-view-230.html?source=0&from=BI01>)| 选择字段，将表单数据，转换为生成多个 JSON 对象，用户可以在其中配置多层 JSON 嵌套  
实验室  
| [Spark SQL](<https://help.fanruan.com/finedatalink/doc-view-3.html?source=0&from=BI01>)| Spark SQL 基于内置的 Spark 计算引擎，满足用户查询数据、处理数据的需求，支持使用参数、函数  
其他| [备注说明](<https://help.fanruan.com/finedatalink/doc-view-69.html?source=0&from=BI01>)  
| 可帮助用户为任务、节点增加备注  
### 2.4 任务调度
提供了定时调度功能，可以定期自动运行定时任务，以保证数据能够及时更新。
  * 开始时间：设置任务开始执行时间
  * 执行频率：任务执行频率
  * 结束时间：设置任务结束执行时间
  * 结果通知：对调度任务运行后的执行结果，如果执行失败会进行通知


详细介绍请参见：[定时任务调度配置](<https://help.fanruan.com/finedatalink/doc-view-22.html?source=0&from=BI01>)  

![1686121968246602.png](https://help.fanruan.com/core/style/lod.png)
### 2.5 任务运维
任务支持灵活调度、运行状态实时监控，便捷的操作将会释放运维人员巨大的工作量。
  * 运行记录：可以通过筛选和搜索的方式查看任务运行状态、运行耗时以及任务运行的历史日志。
  * 任务管理：查看任务调度配置情况。  

  * 资源控制：限制「数据平台」占用的内存和带宽，控制数据开发所占用的内存资源。


详细介绍请参见：[定时任务运维](<https://help.fanruan.com/finedatalink/doc-view-23.html?source=0&from=BI01>)  

![49.png](https://help.fanruan.com/core/style/lod.png)
## 3\. 如何体验 FineDataLink
Demo体验：[FineDataLink数据平台](<https://demo.finedatalink.com/>)
FineDataLink了解试用：[FineDataLink 了解试用](<https://t6ixa9nyl6.jiandaoyun.com/f/6152dbd4a57b9b0008992c6a?ext=bihelp>)
## 4\. 帆软产品组合应用
简介  
| 参考文档  
---|---  
主要介绍业务系统数据经过FDL处理落库后，FineBI 调用该数据进行自助分析的全流程，通过 FDL+BI 的组合方案解决自助数据集冗余杂乱、更新时间长、维护困难的问题| [FDL和FineBI组合应用示例](<https://help.fanruan.com/finedatalink/doc-view-77.html?source=0&from=BI01>)  
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：表信息继承和命名规则](<index.php?doc-view-798.html>)
[下一篇：指标中心简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2646.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
