---
title: Worker引擎读写分离配置
doc_id: 2279
url: https://help.fanruan.com/finebi/doc-view-2279.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:05
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本功能变更7.0-1.2 问题描述正式业务系统，往往白天工作时间进行业务查询，夜晚下班时间进行数据更新。1）白天，若进行数据更新，不能占用查询的资源。2）晚上，

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Worker引擎读写分离配置
[__](<doc-edit-2279.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[6](<edition-list-2279.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
| 功能变更  
---|---  
7.0| -  
### 1.2 问题描述
正式业务系统，往往白天工作时间进行业务查询，夜晚下班时间进行数据更新。
1）白天，若进行数据更新，不能占用查询的资源。
2）晚上，若有用户进行查询，不能占用更新的资源。
3）随着系统的使用时间变长，数据更新会越来越慢，需要通过清理冗余资源。
### 1.3 方案说明
帆软提供计算引擎worker节点读写分离方案。
  * 读：worker节点为查询节点，主要承担查询转发功能
  * 写：worker节点为更新节点，主要承担数据抽取更新任务

  
|   
  
---|---  
高性能时段（白天）| **查询节点：只查询，不更****新****更新节点：只更新，不查询** 如果更新节点数量为0，那么查询节点承担更新任务  
高性能时段（夜晚）| 所有worker节点都作为更新节点**既更新又查询，优先更新**  
## 2\. 开启读写分离
### 2.1 准备worker节点名称
管理员登录FineBI系统，点击「管理系统>系统管理>引擎集群管理」，可以查看到各个worker节点的名称。
请记录下作为更新节点的worker节点名称。
![](https://help.fanruan.com/core/style/lod.png)
### 2.2 配置worker节点属性
在finedb的fine_conf_entity表中，添加读写分离参数
  * 参数名：SystemOptimizationConfig.readWriteSeparationV2
  * 参数值：填写上一步准备的worker节点名称，如需填写多个worker节点名称，用英文逗号间隔。例如：worker1,worker2,worker3


填写的这些worker节点将作为更新节点，其他未填写的worker节点作为查询节点
如不配置该参数，或参数值为空，即代表不开启读写分离
### 2.3 配置高性能时段
在finedb的fine_conf_entity表中，添加高性能时段参数
  * 参数名：DistributedOptimizationConfig.spiderConfig.spider_high_performance_resource_time
  * 参数值：XX:XX-XX:XX


必须配置该参数，否则读写分离无法成功开启。默认值21:00:00-09:00:00
参数值格式必须完全符合要求，例如九点，必须写作09:00，而非9:00
### 2.4 重启bi-web组件
配置读写分离后，需要重启 bi-web 组件生效。
1）管理员登录运维平台，选中指定项目。点击「维护>组件管理」。
2）找到FineBI应用节点，点击「重启」，并等待 bi-web 状态至 healthy 。
![](https://help.fanruan.com/core/style/lod.png)
### 2.5 确认读写分离配置成功
管理员登录FineBI系统，点击「管理系统>系统管理>引擎集群管理」
worker节点的「readOrWrite」状态从OFF变更为了WRITE/READ，即代表读写分离配置成功。
![](https://help.fanruan.com/core/style/lod.png)
  

  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：集群参数配置](<index.php?doc-view-1192.html>)
[下一篇：使用ipv6进行集群内部通信 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1578.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
