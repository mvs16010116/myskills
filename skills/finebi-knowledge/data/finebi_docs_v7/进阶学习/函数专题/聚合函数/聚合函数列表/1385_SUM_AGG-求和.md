---
title: SUM_AGG-求和
doc_id: 1385
url: https://help.fanruan.com/finebi/doc-view-1385.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:07
version: "7.X"
---

> 1. 概述1.1 函数简介SUM_AGG 为对指定维度（拖入分析栏）数据进行汇总求和，且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。语法SUM_AGG(array)根据当前分析维度，返回指标

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# SUM_AGG-求和
[__](<doc-edit-1385.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[12](<edition-list-1385.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2024-07-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 函数简介
SUM_AGG 为对指定维度（拖入分析栏）数据进行汇总求和，且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。
语法  
| SUM_AGG(array)| 根据当前分析维度，返回指标字段的汇总求和值，生成结果为一数据列，行数与当前分析维度行数一致  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果  
### 1.2 注意事项
1）仅能在组件「添加计算字段」时使用聚合函数，不可在自助数据集「新增公式列」时使用。  

2）如组件中使用了包含 SUM_AGG 函数的字段，请勿修改合计行的「合计方式」，否则可能导致合计值不符合预期。
## 2\. 使用聚合函数求平均
若用户横轴维度字段为「日」时，纵轴的计算字段 SUM_AGG(销量) 返回的值为每日的汇总销量。
若用户横轴维度字段为「月」时，SUM_AGG(销量)返回的值为每月的汇总销量。
例如，用户通过分组表已经获得 2011-2017 年每年的合同金额与购买数量，想要求得每年的「平均金额」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
1）新增计算字段「聚合函数求平均」，输入公式：SUM_AGG(合同金额)/SUM_AGG(购买数量)，操作方式如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
2）将「聚合求平均」拖拽到指标栏，效果如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
公式说明：
由于当前的分析维度为合同签约时间(年)，则公式意义如下所示：
公式| 说明  
---|---  
SUM_AGG(合同金额)| 返回值是每年的合同金额汇总值  
SUM_AGG(购买数量)| 返回值为每年的购买数量汇总值  
SUM_AGG(合同金额)/SUM_AGG(购买数量)| 每年的平均金额例如：2013年平均金额=3887220/412013 年全年的合同金额为 3887220 ，购买数量为 41   
## 3\. 使用非聚合函数求平均
### 3.1 公式原理对比
由于当前的分析维度为合同签约时间(年)，以 2013 年合同的平均金额为例，公式意义如下表所示：
公式| 计算顺序  
---|---  
合同金额/购买数量| 先对 2013 年「每单合同」依据公式合同金额/购买数量求出「每单合同的平均值」，再对 2013 年所有合同的平均值进行了「求和汇总」  
SUM_AGG(合同金额)/SUM_AGG(购买数量)| 先对 2013 年的合同金额汇总，2013 年购买数量汇总，再使用 2013 年合同金额汇总值除 2013 年购买数量汇总值，得到 2013 年的合同的平均值  
  
### 3.2 示例
为了帮助用户更好的理解聚合函数，在同样的场景下不使用聚合函数与本文第三章进行对比。
1）新增计算字段「非聚合求平均值」，直接使用公式合同金额/购买数量，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）将「非聚合函数求平均」拖拽到指标栏，得出的结果如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
很显然，不使用聚合函数得出的结果是对明细数据做除法后进行求和汇总。
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：聚合函数概述](<index.php?doc-view-4.html>)
[下一篇：MAX_AGG-最大值 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1390.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
