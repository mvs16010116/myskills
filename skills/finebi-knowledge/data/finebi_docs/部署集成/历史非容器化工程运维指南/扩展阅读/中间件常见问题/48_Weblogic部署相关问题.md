---
title: Weblogic部署相关问题
doc_id: 48
url: https://help.fanruan.com/finebi6.X/doc-view-48.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:47
---

> 1. 概述在 WebLogic 部署过程中可能存在各种问题导致最终无法使用，本文介绍这些问题及对应的解决方法。注：在文档中提及的 FineReport 目录及文件找到 FineBI 对应的即可。2. 示

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Weblogic部署相关问题
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[9](<edition-list-48.html>)
* 最近更新：[Wendy123456](<user-space-240644.html>) 于 2021-09-06 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
在 WebLogic 部署过程中可能存在各种问题导致最终无法使用，本文介绍这些问题及对应的解决方法。
注：在文档中提及的 FineReport 目录及文件找到 FineBI 对应的即可。
## 2\. 示例
### 2.1 当前部分数据计算结果为空
**问题描述**  

抽数数据中，在普通业务包里新建的自助数据集，预览都显示：当前部分数据计算结果为空，在「我的自助数据集」里建的业务包，预览正常。实时数据中，预览也正常。
报错代码中包含语句：caused by:java.lang.ExceptionInInitializerError，如下图所示：
![1630895518289166.jpg](/core/style/lod.png)
**解决方案**
下载文件：[weblogic.xml](<doc-download-/finebi5.1/uploads/file/20210906/weblogic.xml> "下载资料")
将下载的 weblogic.xml 文件，放到 Weblogic 的 webapp 所在的目录下（和 web.xml 同一层级），重启工程。
## 3\. 索引
[WebLogic 部署问题](<http://help.finereport.com/doc-view-780.html>)
[WebLogic 端口号和内存修改](<http://help.finereport.com/doc-view-779.html>)
[WebLogic 服务器 war 包部署](<http://help.finereport.com/doc-view-1934.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Tomcat部署相关问题](<index.php?doc-view-47.html>)
[下一篇：Websphere升级 ![](/core/style/forward.png) ](<index.php?doc-view-284.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
