---
title: TOTAL-汇总
doc_id: 1215
url: https://help.fanruan.com/finebi6.X/doc-view-1215.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:56
---

> 1. 概念语法total(x_agg(array), range, agg)根据横纵轴或行列维度添加的字段对指标进行跨行汇总的计算。参数1x_agg(array)第一个参数为用户计算的指标，该指标必须为

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# TOTAL-汇总
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1215.html>)
* 最近更新：[Ellie23](<user-space-1308124.html>) 于 2022-11-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法  
| total(x_agg(array), range, agg)| 根据横纵轴或行列维度添加的字段对指标进行跨行汇总的计算。  
---|---|---  
参数1| x_agg(array)| 第一个参数为用户计算的指标，该指标必须为聚合函数或聚合指标。  
参数2| range| 第二个参数range为用户设置计算的范围，0为对所有行进行汇总，1为对组内所有行进行汇总。  
参数3| agg| 第三个参数agg为汇总的计算规则，"sum"为求和；"avg"为求平均，"max"为求最大值，"min"为求最小值  
## 2\. 注意事项
第三个参数支持SUM、AVG、MAX、MIN，不区分大小写。
## 3\. 示例
### 3.1 计算组内汇总值
计算「每年」不同合同类型的合同金额的汇总值,公式为：TOTAL(SUM_AGG(合同金额),1)。
例如对2013年合同金额进行组内汇总值计算，如下图所示：
![](/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi6.0/doc-view-2.html>)
### 3.2 计算组内占比
继续进行「组内占比」计算，计算同一年内不同合同类型的合同金额的占比：SUM_AGG(合同金额)/TOTAL(SUM_AGG(合同金额),1,"sum")，如下图所示：
![](/core/style/lod.png)
公式说明：
公式| 说明  
---|---  
SUM_AGG(合同金额)| 按照「年份」和「合同类型」进行组内汇总的合同金额  
TOTAL(SUM_AGG(合同金额),1,"sum")| 计算同一年所有合同类型的合同金额汇总值  
SUM_AGG(合同金额)/TOTAL(SUM_AGG(合同金额),1,"sum")| 每年每个合同类型的合同金额 / 当年内所有合同类型的合同金额汇总值  
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi6.0/doc-view-2.html>)
### 3.3 计算组内累计占比
计算「组内累计占比」， 输入公式：ACC_SUM(SUM_AGG(合同金额),1)/TOTAL(SUM_AGG(合同金额),1,"sum")，如下图所示：
![](/core/style/lod.png)
公式说明：
公式  
| 说明  
---|---  
ACC_SUM(SUM_AGG(合同金额),1)| 计算同一年内不同合同类型的合同金额累计值  
TOTAL(SUM_AGG(合同金额),1,"sum")| 计算同一年的合同金额汇总值  
ACC_SUM(SUM_AGG(合同金额),1)/TOTAL(SUM_AGG(合同金额),1,"sum")| 累计值/汇总值  
## 4\. 拓展阅读
1）[所有值（快速计算）](<https://help.fanruan.com/finebi6.0/doc-view-1679.html>)
2）数据集计算
若在数据集中计算所有合同金额汇总值，可新增汇总列对所有合同金额求和，如下图所示：
![](/core/style/lod.png)
该处数据由于是对明细数据进行的计算，因此不会因为维度变化而改变结果，结果如下所示：
![](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：SAME_PERIOD-同期](<index.php?doc-view-1212.html>)
[下一篇：数据清洗整合运算概述 ![](/core/style/forward.png) ](<index.php?doc-view-1318.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
