---
title: PERIOD_ANLS-上期末
doc_id: 1210
url: https://help.fanruan.com/finebi6.X/doc-view-1210.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:53
---

> 1. 概念语法period_anls(x_agg(array), datepart)根据横纵轴或行列维度添加的日期字段进行上期末的计算。参数1x_agg(array)第一个参数为用于计算的指标，该指标必

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# PERIOD_ANLS-上期末
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[11](<edition-list-1210.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-12-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法  
| period_anls(x_agg(array), datepart)| 根据横纵轴或行列维度添加的日期字段进行上期末的计算。  
---|---|---  
参数1| x_agg(array)| 第一个参数为用于计算的指标，该指标必须为聚合函数或聚合指标。  
参数2| datepart| 第二个参数用于配置计算的上期末为上年期末或者上月期末。横纵轴拖拽的字段不满足函数的计算要求时，该指标会标红。  
## 2\. 注意事项
支持在[设置日期分组和格式](<https://help.fanruan.com/finebi6.0/doc-view-1654.html>)为：使用年季度、年月日、年月、年周数时使用。
注1：横纵轴拖拽的字段不满足函数的计算要求时，该指标会标红。
注2：参数仅支持Y、M、W，不区分大小写。不支持按季度计算。
## 3\. 示例
示例数据：[合同事实表.xlsx](<doc-download-/finebi6.X/uploads/file/20230821/合同事实表.xlsx> "下载资料")
希望实现展示「上年期末」数值和「上月期末」数值。
### 3.1 计算上年期末金额
1）计算「上年」期末金额，需要将日期字段「合同签约时间」的分组改为年月，如下图所示：
![](/core/style/lod.png)
2）新增 [计算字段](<https://help.fanruan.com/finebi6.0/doc-view-118.htmlsrc=> "1609837801896176.png")，命名为「期末」字段，输入公式：period_anls(SUM_AGG(合同金额), "Y")，如下图所示：
![](/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi6.0/doc-view-2.html>)
3）将计算字段「期末」拖入指标栏，因此 2014 年对应的期末数据为 2013-12 的合同金额，如下图所示：
![](/core/style/lod.png)
### 3.2 计算上月期末金额
1）计算「上月」期末金额，需要将日期字段「合同签约时间」的分组改为年月日，如下图所示：
![](/core/style/lod.png)
2）新增 [计算字段](<https://help.fanruan.com/finebi6.0/doc-view-118.htmlsrc=> "1609837801896176.png")，命名为「上月期末」字段，输入公式为：period_anls(SUM_AGG(合同金额), "M")，如下图所示：
![](/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi6.0/doc-view-2.html>)
3）将计算字段「期末」拖入指标栏，因此 2014-07 对应的期末数据为 2014-06-30 的合同金额，如下图所示：
![](/core/style/lod.png)
## 4\. 拓展阅读
[同比/环比（快速计算）](<https://help.fanruan.com/finebi6.0/doc-view-131.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：ACC_SUM-累计](<index.php?doc-view-1214.html>)
[下一篇：PREVIOUS_PERIOD-环期 ![](/core/style/forward.png) ](<index.php?doc-view-1213.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
