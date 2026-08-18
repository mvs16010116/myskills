---
title: IFERROR-处理异常值
doc_id: 2324
url: https://help.fanruan.com/finebi6.X/doc-view-2324.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:51
---

> 1. 版本FineBI 版本功能变动6.0.16-2. 概述IFERROR 函数用于识别和处理异常值。语法IFERROR(value1,value2)判断 value1 是否是异常值，如果是则返回 va

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# IFERROR-处理异常值
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[3](<edition-list-2324.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2024-01-03 
[](<javascript:;>) [](<javascript:>)
## 1\. 版本
FineBI 版本  
| 功能变动  
---|---  
6.0.16| -  
  
## 2\. 概述
IFERROR 函数用于识别和处理异常值。
语法| IFERROR(value1,value2)判断 value1 是否是异常值，如果是则返回 value2，如果不是则返回 value1。  
---|---  
参数1| value1| “value1”可以是任何表达式，判断其是否为异常值。异常值定义：正无穷(∞)、负无穷(-∞)、NAN值(任何与无穷值计算获得的结果) ，不包括空值  
参数2| value2| “value2”需要和“value1”是一种字段类型  
## 3\. 示例
示例数据：[IFERROR.xlsx](<doc-download-/finebi6.X/uploads/file/20240103/IFERROR.xlsx> "下载资料")
有一份机器温度的采集数据。由于故障，有两台机器今天没有数据。这就导致求环比增长率时，出现了异常值。
1）在主题中使用 [新增列](<https://help.fanruan.com/finebi6.0/doc-view-509.html>) ，计算环比增长率：1-昨天温度/今天温度，看今天的温度相对于昨天有怎样的变化。
在下图中，J16 今天没有温度数据，导致计算获得的环比增长率为-∞。异常值对于后期计算非常不友好，所以我们需要对异常值进行处理。
![](/core/style/lod.png)
2）添加 [新增列](<https://help.fanruan.com/finebi6.0/doc-view-509.html>) ，并命名为「异常值处理」，输入下图公式。  

若「环比增长率」为异常值，返回“0”，否则返回「环比增长率」
![](/core/style/lod.png)
3）计算结果如下图所示：  

![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：NVL](<index.php?doc-view-1479.html>)
[下一篇：快速计算函数概述 ![](/core/style/forward.png) ](<index.php?doc-view-1499.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
