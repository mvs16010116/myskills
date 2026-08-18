---
title: [直连]仪表板URL直接添加参数条件传参
doc_id: 86
url: https://help.fanruan.com/finebi6.X/doc-view-86.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:02:18
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 问题描述在集成环境下，用户想要在打开门店相关仪表板 URL 的时候，直接添加相关参数，如http://xxxxxxxx?店性质=管理店过滤

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# [直连]仪表板URL直接添加参数条件传参
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[42](<edition-list-86.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-06-17 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0| -  
### 1.2 问题描述
在集成环境下，用户想要在打开门店相关仪表板 URL 的时候，直接添加相关参数，如http://xxxxxxxx?店性质=管理店过滤出店性质为「管理店」的数据。
### 1.3 实现思路
  * 在 SQL数据集中添加参数；
  * 在前端仪表板中直接增加参数条件，实现数据过滤功能。


若需要通过过滤组件传递参数，详情参见：[过滤组件作为参数参与计算](<https://help.fanruan.com/finebi6.0/doc-view-974.html>)、[](<https://help.fanruan.com/finebi6.0/doc-view-1228.html#3>)[跳转到仪表板(网页链接)](<https://help.fanruan.com/finebi6.0/doc-view-1594.html>)。
## 2\. 传递一个参数
### 2.1 添加 SQL 数据集
1）若同时拥有「直连数据」和「抽取数据」功能，则需要在数据列表中切换为「直连数据」，然后选择「公共数据」，点击进入分组下业务包，点击「添加数据集>添加 SQL 数据集」，如下图所示：
![21.png](/core/style/lod.png)
2）输入 SQL 语句：select * from new_dian where 店性质 in ('${店性质}')。${店性质}就是设置的参数变量，点击「刷新」，设置参数的默认值为「自有店」，设置参数类型为文本类型，点击「预览」，并确定保存数据集，如下图所示：
![43.png](/core/style/lod.png)
### 2.2 制作分组表
制作一个组件，图表类型选择「分组表」后，拖入字段，如下图所示：
![44.png](/core/style/lod.png)
### 2.3 传递参数
链接类型| 传递一个值写法| 传递多个值写法  
---|---|---  
公共链接| ?参数名称=参数值| ?参数名称=参数值1','参数值2  
预览链接| ?参数名称=参数值| ?参数名称=参数值1','参数值2  
#### 2.3.1 公共链接传递参数
若要实现在 URL 中的参数传递过滤，首先需要获取该仪表板的 URL 。进入仪表板节点，对新建的仪表板选择「创建公共链接」，开启公共链接并「复制链接」，如下图所示：
![45.png](/core/style/lod.png)
比如获取的链接为：http://localhost:37799/webroot/decision/link/njps  

在最后添加「?店性质=管理店」：http://localhost:37799/webroot/decision/link/njps?店性质=管理店
在地址栏输入添加参数后的 URL，可以看到通过 URL 中的参数传递，实现「管理店」的过滤。
![46.png](/core/style/lod.png)
注：若浏览器不支持中文参数，即该参数传递过滤不生效，就需要把 json 类型的 url 参数值先进行编码 encodeURIComponent()。比如 edge 浏览器。 
#### 2.3.2 预览链接传递参数
获取仪表板预览链接，详情请参见：[获取仪表板预览链接](<https://help.fanruan.com/finebi6.X/doc-view-164.html#0294798c1ecf8622>)。仪表板预览的 URL 加上「?参数名称=参数值」，也可以进行参数的传递。
例如，在预览的 URL 后加入「?店性质=管理店」，可以看到下方的分组表中过滤出了管理店的数据，实现参数的传递功能，如下图所示：
![48.png](/core/style/lod.png)
## 3\. 传递多个参数
在有多个参数的时候，URL 同样可以通过添加参数来实现多个条件过滤的效果。
### 3.1 添加有多个参数的 SQL 数据集
添加 SQL 数据集，输入带包含多个参数的 SQL 语句：select * from NEW_DIAN where 店性质 in ('${店性质}' ) and 店风格 in ('${店风格}' )
点击「刷新」，设置默认值为「时尚馆」和「自有店」，并保存数据集，如下图所示：
![49.png](/core/style/lod.png)
### 3.2 创建仪表板
使用该数据表的字段创建组件，包含「店性质」、「店风格」、「记录数」字段，组件中显示字段值均为参数默认值。如下图所示：
![50.png](/core/style/lod.png)
### 3.3 传递参数
参考 2.3 节获取该仪表板的链接，在获取的 URL 之后加上多个参数及值：?参数名称1=参数值1&参数名称2=参数值2添加参数后仪表板可以直接过滤出对应的参数值，如下图所示：
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [制作仪表板](<category-view-99>)
[![](/core/style/back.png)上一篇：[直连]参数为空选择所有值](<index.php?doc-view-397.html>)
[下一篇：[直连]跳转传递参数 ![](/core/style/forward.png) ](<index.php?doc-view-729.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
