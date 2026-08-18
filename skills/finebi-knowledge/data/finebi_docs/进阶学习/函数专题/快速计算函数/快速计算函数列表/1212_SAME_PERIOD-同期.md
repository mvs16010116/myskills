---
title: SAME_PERIOD-同期
doc_id: 1212
url: https://help.fanruan.com/finebi6.X/doc-view-1212.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:55
---

> 1. 概念语法same_period(x_agg(array), datepart)根据横纵轴或行列维度添加的日期字段进行同期值的计算。参数1x_agg(array)第一个参数为用于计算的指标，该指标必

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# SAME_PERIOD-同期
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[13](<edition-list-1212.html>)
* 最近更新：[Ellie23](<user-space-1308124.html>) 于 2022-11-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法  
| same_period(x_agg(array), datepart)| 根据横纵轴或行列维度添加的日期字段进行同期值的计算。  
---|---|---  
参数1| x_agg(array)| 第一个参数为用于计算的指标，该指标必须为聚合函数或聚合指标。  
参数2| datepart| 第二个参数用于配置计算同期时计算某日的年同期或者某日的月同期。横纵轴拖拽的字段不满足函数的计算要求时，该指标会标红。  
注1：参数支持Y、M、W，不区分大小写。
## 2\. 注意事项
支持在[设置日期分组和格式](<https://help.fanruan.com/finebi6.0/doc-view-1654.html>)为：使用年季度、年月日、年月、年周数时使用。
## 3\. 示例
same_period(sum_agg(amount),"Y") 用户横纵轴拖拽销售日期（年月日分组），则该指标计算结果为，根据年月日对销量进行分组汇总，然后计算出该日数据上年同日的销量；如果参数 2 为“M”，则计算结果为该日销量上月同日的销量。
示例数据：「销售DEMO>合同事实表」  

例如计算 2014 年 7 月同期值，即展示 2013 年 7 月的合同金额。
### 3.1 计算月同期金额
计算月同期金额，需要将日期字段「合同签约时间」的分组改为年月，如下图所示：
![](/core/style/lod.png)
新增 [计算字段](<https://help.fanruan.com/finebi6.0/doc-view-118.html>)，命名为「同期」字段，输入公式：SAME_PERIOD(SUM_AGG(合同金额),"Y")，如下图所示：
![](/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi6.0/doc-view-2.html>)
### 3.2 效果查看
将计算字段拖入指标栏即可，因此 2014 年 7 月同期值会展示 2013 年 7月的合同金额，如下图所示：
![](/core/style/lod.png)
## 4\. 拓展阅读
[同比/环比（快速计算）](<https://help.fanruan.com/finebi6.0/doc-view-131.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：RANK_ANLS-排名](<index.php?doc-view-1216.html>)
[下一篇：TOTAL-汇总 ![](/core/style/forward.png) ](<index.php?doc-view-1215.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
