---
title: FineBI和FineReport的区别
doc_id: 279
url: https://help.fanruan.com/finebi6.X/doc-view-279.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:22
---

> 1. 概述FineBI 和 FineReport 是帆软软件旗下的两款数据分析工具。两款产品各有区别及各自的优势所在。本文介绍两款产品的异同点及兼容性。2. 产品区别FineBI 和 FineRepor

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI和FineReport的区别
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[29](<edition-list-279.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-09-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineBI 和 FineReport 是帆软软件旗下的两款数据分析工具。两款产品各有区别及各自的优势所在。本文介绍两款产品的异同点及兼容性。
## 2\. 产品区别
FineBI 和 FineReport 作为两种分析工具，最终的结果可以放在一个信息门户上「数据决策系统、移动门户」。
![222](/core/style/lod.png)  

主要区别如下表和图所示：
  

**类型**| **FineBI**| **FineReport**  
---|---|---  
数据引擎| 提供 [实时数据](<https://help.fanruan.com/finebi6.0/doc-view-85.html>) 与抽取数据两种方式的 Spider 计算引擎，用户可以根据数据量、实时性要求、使用频次等自由选择| 直连数据库，性能方面需要数据库的支撑  
支持范围| 提供自助式的 OLAP 多维数据分析模式| 支持灵活定制各种中国式复杂报表  
面向对象| 主要面向业务人员，业务人员可以自己设计仪表板进行分析，自主分析得出结果，辅助企业业务决策| 主要面向信息人员，由信息人员完成业务部分的需求，完成的报表由底层员工和领导使用可以用来出固定格式的周报、月报、适合作为正式汇报材料  
使用目的| 关注长期的战略决策，更着重于商业趋势和业务单元的联系而非具体的数据和精确度本身| 着重于短期的运作支持  
## 3\. 产品联系
1）FineReport 中的所有数据源都可以通过 [服务器数据集](<https://help.fanruan.com/finebi6.0/doc-view-253.html>) 在 FineBI 中进行读取和使用。
2）FineReport 制作的所有报表页面都可以挂载在 FineBI 中进行查看和使用。详情参见：[如何在 FineBI 中发布 FineReport 模板](<https://help.fanruan.com/finebi6.0/doc-view-526.html>) 。
3）FineBI 和 FineReport 产品支持融合部署，所有功能都可以整合在同一个工程中进行使用「推荐 FineReport 整合到 FineBI 」，详情参见：[FineReport 集成到 FineBI](<https://help.fanruan.com/finebi6.0/doc-view-67.html>) ，版本兼容请参考：[FineBI与FineReport版本适配说明](<https://help.fanruan.com/finebi6.X/doc-view-1061.html>) ，同时移动端也可以共用一个数据分析 App 。
## 4\. 详细功能对比
### 4.1 业务数据整合处理能力
FineReport：能跨系统直连数据库，通过 SQL 创建数据集取数制作报表，方便快捷。如下图所示： 
![](/core/style/lod.png)  

FineBI：自助查询服务平台，可直接对接数据库的实时数据或抽取数据到本地，通过业务包来管理获取的数据。如下图所示： 
![1605346811146555.png](/core/style/lod.png)
### 4.2 大数据处理能力
FineReport：报表的数据直接通过 SQL 快速查询，满足绝大多数展示取数需求。
FineBI：灵活支撑不同数据量级的分析，对于处理千万级、上亿级的数据效率值很高。
### 4.3 制作表格/图表的方式
FineReport：C/S 设计器设计开发报表模板，用户可任意制作所需要的展示效果。
比如可以制作一些中国式的复杂报表，如下图所示：  

![](/core/style/lod.png)
FineBI：纯 B/S 端自定义拖拽分析报表，业务人员可根据报表需求自行拖拽生成各类分析图表，自主分析得出结果，辅助企业业务决策。如下图所示： 
![1605346905901463.png](/core/style/lod.png)
### 4.4 Dashboard 管理驾驶舱支持决策
FineReport：通过图表联动等功能实现固定式分析报表，多图形随意切换，能通过图形多角度给用户提供清晰的数据走势，展示功能强大；
FineBI：Dashboard 称为管理驾驶舱，主要是把公司领导关心的指标，维度等放在一个页面展示，通过 FineBI 的汇总、OLAP、过滤等操作，可以很快地将关键指标展示出来，供企业领导决策分析做数据支撑。
### 4.5 移动端的服务支持响应
FineReport：支持在手机上查看各种报表模板，也可以进行问题数据的注释、批注、分享、邮件发送、识别手机号码等操作；
FineBI：支持在移动设备上查看分析数据，同样可以进行注释、批注、分享等操作。
## 5\. 总结
  
| ****FineReport****| ****FineBI****  
---|---|---  
工具类型| 报表工具：报表是企业信息化必不可少统计分析工具，主要实现一些企业固定的月报、季报、关键数据的统计分析| 商业智能工具：侧重于数据分析，改变之前传统做表的方式，交互性更好，性能更加强大  
目的| 旨在统计或者告诉决策者：过去发生了什么，什么正在发生| 旨在将企业中现有的数据转化为知识，帮助企业做出明智的业务经营决策  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [产品简介](<category-view-626>)
[![](/core/style/back.png)上一篇：FineBI架构介绍](<index.php?doc-view-2443.html>)
[下一篇：FineBI、FineDataLink产品组合应用 ![](/core/style/forward.png) ](<index.php?doc-view-2216.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
