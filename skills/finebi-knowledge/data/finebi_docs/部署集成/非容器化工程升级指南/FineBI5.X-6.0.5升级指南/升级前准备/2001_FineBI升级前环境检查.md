---
title: FineBI升级前环境检查
doc_id: 2001
url: https://help.fanruan.com/finebi6.X/doc-view-2001.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:56
---

> 1. 概述1.1 版本FineBI版本FR和BI升级检测工具功能变动6.04.1-1.2 功能简介升级 FineBI6.0 之前，需要先对 5.1 的 BI 工程进行升级检测，保证用户尽可能规避已知的升

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI升级前环境检查
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[5](<edition-list-2001.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-11-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI版本  
| FR和BI升级检测工具| 功能变动  
---|---|---  
6.0| 4.1| -  
### 1.2 功能简介
升级 FineBI6.0 之前，需要先对 5.1 的 BI 工程进行升级检测，保证用户尽可能规避已知的升级风险。
检测需要通过安装插件「FR和BI升级检测」工具实现。
## 2\. 操作步骤
### 2.1 安装插件
在「管理系统>插件管理」安装插件「FR和BI升级检测」。安装插件方法参照 [插件管理](<https://help.fanruan.com/finebi6.0/doc-view-459.html> "插件管理")
安装成功后，在左侧导航栏出现「升级检测」。如下图所示：
注1：安装前请确保安装最新版升级工具，而非老版本升级工具插件，否则检测内容可能不完备。
注2：不建议适用IE浏览器，安装插件可能不显示入口。
![2022-09-07_15-30-25.png](/core/style/lod.png)
### 2.2 升级注意事项
1）进入「升级检测」界面，阅读升级注意事项，**按照要求对 BI 工程进行**[**系统备份**](<https://help.fanruan.com/finebi6.0/doc-view-400.html>)**** 。
2）完成后点击「已经阅读完上述注意事项」进行「下一步」。如下图所示：  

![2022-09-07_15-35-57.png](/core/style/lod.png)
出现提示，点击「确定」。如下图所示：  

![2022-09-07_15-48-09.png](/core/style/lod.png)
**备份步骤说明：**
进入「管理系统>智能运维>备份还原」，在「平台配置、报表模板、BI模板、jar 包、插件」 Tab 栏下分别点击「手动备份」，详情信息见：[备份还原](<https://help.fanruan.com/finebi6.0/doc-view-400.html>)  

  * 若「管理系统>智能运维>备份还原」页面提示为当前环境为内置库不支持备份还原功能。手动将%FineBI%/webroot/WEB-INF下的dashboards、embed、lib、plugins、reportlets、resource文件夹拷贝到%FineBI%/webroot/backup目录下


### 2.3 系统升级检测
系统检测需要一定的时间，请耐心等待。
1）完成检测后，界面上只显示阻塞和警告风险。点击「导出」查看全部风险。如下图所示：
注：阻塞项不解决无法进行升级。
![2022-09-07_16-23-11.png](/core/style/lod.png)
2）根据提示修复风险后，重新进行风险检测。详情参考：[升级风险项及修复方案列表](<https://help.fanruan.com/finebi6.0/doc-view-2004.html>)
3）无风险项后，则点击「下一步」。（点击下一步会进行一些脏数据的删除，隐患配置修改等操作）
### 2.4 完成检测
检测完成后，可填写「升级风险评估书」并提交，申请技术支持协助升级。
  * 升级风险评估书填写说明：[升级风险评估表填写说明](<https://help.fanruan.com/finebi6.X/doc-view-2147.html>) 。
  * 升级风险评估书链接如下：[升级风险评估书](<https://t6ixa9nyl6.jiandaoyun.com/f/620320767c4dd90007f816c7?ext=%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3>) 。


![2022-09-07_16-33-29.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineBI升级前业务检查](<index.php?doc-view-2016.html>)
[下一篇：FineBI升级前环境检查风险项修复方案 ![](/core/style/forward.png) ](<index.php?doc-view-2004.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
