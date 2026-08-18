---
title: FineChatBI 使用权限配置
doc_id: 2590
url: https://help.fanruan.com/finebi/doc-view-2590.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:31
version: "7.X"
---

> 1. 概述1.1 版本FineChatBI 版本功能变动V3.24.0删除智能问答用户，在管理系统中配置智能问答的使用权限V3.26.0支持查看用户对有权限的指标维度进行提问V3.33.0补充找报表相关

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineChatBI 使用权限配置
[__](<doc-edit-2590.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[24](<edition-list-2590.html>)
* 最近更新：[Aria.Han](<user-space-2499654.html>) 于 2026-03-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
#### 1.1 版本
FineChatBI 版本| 功能变动  
---|---  
V3.24.0  
| 删除智能问答用户，在管理系统中配置智能问答的使用权限  
V3.26.0| 支持查看用户对有权限的指标维度进行提问  
  
V3.33.0| 补充找报表相关权限  
  
V4.0| 
  * 支持独立配置问数据、找报表的使用权限

注：找报表功能尚在内测中，可联系技术支持开通。  

  * 权限体系适配指标维度

  
V4.3| 支持锁定分析主题问数  
  
### 1.2 应用场景
若用户想使用 FineChatBI 进行数据分析，那么他需要什么权限呢？管理员应该怎么给他分配权限呢？
本章将以销售部员工 echo 开通问答 BI 权限为例，讲述权限配置路径。若是给某个部门或角色开通权限，同样可以参考本文，只需要变更权限载体即可。
## 2\. 配置使用权限
1）在「管理系统>权限管理」中，开启分级授权，如下图所示：
![22.gif](https://help.fanruan.com/core/style/lod.png)
2）在管理系统中，先为 echo 开启「智能问答」权限，然后可对「问数据」或「找报表（beta）」的使用权限进行单独控制。
开启后界面即出现功能入口图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 3\. 配置用户的提问范围
用户仅可对以下两种数据进行提问：  

  * 有权限的预加载数据（由管理员配置）
  * 拥有有编辑权限的分析主题


### 3.1 配置预加载数据的提问权限
在完成预加载配置之后（详情请参见：[预加载配置](<https://help.fanruan.com/finebi/doc-view-2575.html>)），管理员需要为相关用户配置预加载数据的使用权限。
#### 3.1.1 预加载分析主题权限配置  

例如，希望 echo 可以对「连锁经营分析」这个预加载数据进行提问。
1）管理员进入「权限管理>普通权限配置>用户最终权限>智能问答」，为指定用户 echo 授予预加载主题「连锁经营分析」的使用权限。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）若预加载主题源自数据目录，在授予其使用权限后，还需额外开启该主题对应的数据源，方可正常使用。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
#### 3.1.2 预加载指标维度
例如，希望 echo 可以对「问答test」这个预加载数据进行提问。
进入「权限管理>普通权限配置>用户最终权限>数据目录&指标中心」，为 echo 开启「问答test」的使用权限。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 分析主题的编辑权限
设计用户还可以对有编辑权限的分析主题进行提问，以下两种情况设计用户可以拥有分析主题的编辑权限：  

  * 自己创建的分析主题。
  * 其他用户将自己的分析主题协作给他，允许他进行编辑，详情请参见：[协作](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)。


## 4\. 智能问答配置的使用权限
超管可通过管理系统的「权限管理」模块，授予其他用户「智能问答配置」的使用权限，使他们能够执行同义词配置、推荐问题设置、近似问题配置、预加载配置以及主题编辑权限配置等。
例如：给 echo 分配「智能问答配置」的使用权限。
1）进入权限「全局设置」，打开「分级授权」。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）先给 echo 开启「智能问答配置」权限，即可对下面的功能单独进行权限控制。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
配置项  
| 次管权限  
---|---  
管理员监管  
| 
  * 支持查看数据使用权限范围内的问数记录
  * 支持查看目录查看权限范围内的仪表板提问记录  


  
预加载配置| 
  * 支持修改自动刷新频率  

  * 支持添加有使用权限的分析主题
  * 支持添加拥有「目录查看权限」的仪表板
  * 不支持修改预加载分析主题/仪表板的数量限制
  * 不支持对其他用户添加的分析主题/仪表板进行修改、删除、刷新缓存

  
标签| 支持增加、删除、修改标签。删除规则：
  * 数据标签：可删除所有已存在的分析主题
  * 语义标签：只可删除有目录查看权限且被添加到预加载的仪表板

  
同义词配置| 
  * 支持对有管理权限的预加载分析主题，增加、删除、修改同义词
  * 支持对有目录查看权限的预加载仪表板，增加、删除、修改同义词  


  
## 5\. 提供锁定分析主题的问数界面
在完成权限配置后，管理员可以通过 URL 给用户提供特定分析主题的问答界面，实现方式如下：
http://ip:port/webroot/decision/ai/conversation/resource/web/html?**subjectId=主题id** &**pureChat=true**
subjectId ：强制指定对话主题；pureChat=true：开启纯净模式。
此界面将自动屏蔽主题切换、历史记录、侧边栏及新建对话等入口，用户仅能在指定分析主题内提问。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
主题 ID 获取：选择目标主题，复制 subject 后的字符串，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-763>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：集成指南下架说明](<index.php?doc-view-2757.html>)
[下一篇：FineChatBI 授权权限配置 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2651.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
