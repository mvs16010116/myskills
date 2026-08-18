---
title: FineBI企业版部署指南
doc_id: 2108
url: https://help.fanruan.com/finebi/doc-view-2108.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:08
version: "7.X"
---

> 1. 概述1.1 版本FineBI服务器版本7.01.2 功能简介服务器部署一直都是比较繁重的运维操作。企业版FineBI使用容器化部署方案，降低部署带来的较高成本。本文以最简洁清晰的步骤拆解，带大家了

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI企业版部署指南
[__](<doc-edit-2108.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[33](<edition-list-2108.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI服务器版本  
  
---  
7.0  
### 1.2 功能简介
服务器部署一直都是比较繁重的运维操作。
企业版FineBI使用容器化部署方案，降低部署带来的较高成本。
本文以最简洁清晰的步骤拆解，带大家了解部署运维平台和帆软应用的流程，以及用户可使用运维平台进行的运维操作。
**部署流程简介：通过finekey工具部署运维平台，通过运维平台部署/对接运维项目**
## 2\. 部署指南
  * FineBI企业版仅支持运维平台部署，降低因部署不合理带来的工程性能和宕机风险等。
  * FineBI架构详解：[FineBI产品架构一览](<https://help.fanruan.com/fineops/doc-view-132.html>)[](<https://help.fanruan.com/fineops/doc-view-132.html>)

分类  
| 说明  
---|---  
个人用户使用| 帆软提供「[帆软在线数据分析平台](<https://pcdemo.finebi.com/webroot/decision/?online_bi_from=0402>)」
  * 面向**个人用户** 使用：免安装快速体验，支持在线分享和协作
  * 面向**企业选型** 测试：支持开通团队版账号，体验 FineBI 完整的功能，以满足采购前对产品进行深入调研和功能测试的需求。支持连接数据库、权限管理、用户管理、公共数据等

  
企业部署FineBI正式工程| 企业版FineBI，仅支持使用运维平台部署**1）服务器资源充足** 若服务器资源充足，可提供足量全新服务器用于部署FineBI请参考：[快速部署FineBI](<https://help.fanruan.com/fineops/doc-view-54.html>)**2）服务器资源有限** 若服务器资源有限，可能会存在端口占用等情况服务器配置要求请参考：[确认FineBI项目服务器配置](<https://help.fanruan.com/fineops/doc-view-134.html>)工程部署步骤请参考：[部署FineBI](<https://help.fanruan.com/fineops/doc-view-59.html>)  
企业部署FineBI测试工程  
| 对于企业正式工程，在实际部署前，往往需要部署测试工程，以验收相关功能为了方便企业测试，帆软支持在资源有限的体验环境下部署测试版FineBI详情请参见：[了解运维项目测试版与正式版](<https://help.fanruan.com/fineops/doc-view-171.html>)  
FineBI6.1升级7.0| 企业版FineBI6.1升级7.0，由帆软升级团队协助完成请填写表单申请：[升级风险评估](<https://t6ixa9nyl6.jiandaoyun.com/f/620320767c4dd90007f816c7>)帆软升级团队评估后，会主动联系你  
## 3\. 运维指南
仅列出部分常用操作，更多运维功能，请参考：[运维平台](<https://help.fanruan.com/fineops/>)  

  
| 分类  
| 指导文档  
---|---|---  
常用操作| 工程注册| [注册新项目](<https://help.fanruan.com/fineops/doc-view-108.html>)  
最适合容器化工程的注册方式，前端界面化配置  
工程升级| [外网升级运维项目](<https://help.fanruan.com/fineops/doc-view-53.html>)[内网升级运维项目](<https://help.fanruan.com/fineops/doc-view-55.html>)通过前端替换镜像完成升级，无需手动更换jar  
工程备份还原| [备份项目](<https://help.fanruan.com/fineops/doc-view-37.html>)[还原项目](<https://help.fanruan.com/fineops/doc-view-142.html>)  
支持异地备份，支持完整工程备份，支持自动备份  
工程启停| [组件管理](<https://help.fanruan.com/fineops/doc-view-44.html>)一键启停，无需进入服务器后台操作
  * 如需重启**worker/bi-web** 组件：可**直接重启**
  * 如需重启**master** 组件：请**停止全部master和worker** 组件，**启动master** 组件至running状态三分钟（等待healthy），**再启动全部worker** 组件

  
工程迁移| [迁移项目](<https://help.fanruan.com/fineops/doc-view-147.html>)支持工具/手动，将原生部署工程迁移到运维平台部署的工程  
上传文件| [文件管理](<https://help.fanruan.com/fineops/doc-view-39.html>)  

  * 将模板、Excel文件上传到文件服务器。
  * 单机切换集群时，需要将单机工程文件上传到集群文件服务器上。
  * 将定时调度结果下载到本地，将工程模板文件下载备份。
  * 对于复杂目录结构，根据文件名称快速搜索查找。

  
工程配置| 修改工程配置| [更改项目组件配置](<https://help.fanruan.com/fineops/doc-view-52.html>)界面化修改工程内存、线程、等参数  
配置HTTPS证书| [为运维项目开启SSL](<https://help.fanruan.com/fineops/doc-view-104.html>)无需后台上传证书，无需手动修改配置文件，前端快速配置  
短域名/IP访问工程| [使用IP/域名访问项目](<https://help.fanruan.com/fineops/doc-view-138.html>)前端配置，实现通过 IP 或者域名访问工程  
工程扩容| 集群原有组件扩容| [集群项目扩容组件数量](<https://help.fanruan.com/fineops/doc-view-81.html>)随着业务用量增加，原有集群配置不足以支撑使用，需要添加业务节点或计算worker的数量，例如从两节点集群扩容为三节点集群基于安全性考虑，希望对原有单节点内网关进行扩容，变成双节点内网关，确保高可用  
工程监控  
| 定期巡检工程  
| [系统巡检](<https://help.fanruan.com/fineops/doc-view-8.html>)对应用进行定期健康巡检，确保应用所在的环境及应用内配置合理，以保证应用的正常运行  
获取工程日志| [日志管理](<https://help.fanruan.com/fineops/doc-view-13.html>)  
支持前端按时间、按类型下载日志  
工程状态监测| [项目监控](<https://help.fanruan.com/fineops/doc-view-12.html>)  
通过运维平台的「项目监控」功能，快速查看哪些配置飘红有隐患在业务用户感知之前，解决这些应用平台的隐患  
工程异常告警| [告警简介](<https://help.fanruan.com/fineops/doc-view-124.html>)  
通过运维平台的「告警」功能，即可设置告警规则和告警方式运维平台检测到触发告警规则（例如某节点负载过高）时，直接发送邮件提醒管理员  
组件管理| 配置外接库配置集群组件| [集群管理](<https://help.fanruan.com/fineops/doc-view-157.html>)支持对配置库、状态服务、文件服务、日志存储进行配置  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI_Cli 介绍及使用](<index.php?doc-view-2776.html>)
[下一篇：FineBI项目组件运维指南 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-436.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
