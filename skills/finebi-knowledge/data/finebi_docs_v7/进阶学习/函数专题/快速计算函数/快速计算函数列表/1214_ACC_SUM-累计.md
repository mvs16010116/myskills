---
title: ACC_SUM-累计
doc_id: 1214
url: https://help.fanruan.com/finebi/doc-view-1214.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:56
version: "7.X"
---

> 1. 概念语法ACC_SUM(x_agg(array),range)根据横纵轴或行列维度添加的字段对指标进行跨行累计的计算。参数1x_agg(array)第一个参数为用户计算的指标，该指标必须为&nbs

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# ACC_SUM-累计
[__](<doc-edit-1214.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1214.html>)
* 最近更新：[Ellie23](<user-space-1308124.html>) 于 2024-03-16 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法  
| ACC_SUM(x_agg(array),range)| 根据横纵轴或行列维度添加的字段对指标进行跨行累计的计算。  
---|---|---  
参数1| x_agg(array)| 第一个参数为用户计算的指标，该指标必须为 [聚合函数](<https://help.fanruan.com/finebi7.0/doc-view-4.html>) 或聚合指标。  
参数2| range| 第二个参数range为用户设置计算的范围0 为对所有行进行累计1 为对组内所有行进行累计。  
## 2.注意事项
  

## 3\. 示例
示例数据：[股票买卖数据.xlsx](<doc-download-/finebi5.1/uploads/file/20210106/股票买卖数据.xlsx> "下载资料")
### 3.1 计算每月累计剩余数
已知每日的买入和卖出股票数，需要统计每月剩余股票数。
1）将「日期」拖入维度栏，并设置为年月格式，将「买入」和「卖出」拖入指标栏，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）添加计算字段，命名为「累计剩余股票数」，输入公式：ACC_SUM(SUM_AGG(买入-卖出),0)，点击「确定」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
公式说明：
公式  
| 说明  
---|---  
SUM_AGG(买入-卖出)| 对每日买入-卖出差按照年月维度求和汇总  
ACC_SUM(SUM_AGG(买入-卖出),0)| 以月为单位，对每日的买入卖出差所有值进行从上到下累加  
3）可以看到 2016-01 的累计值=-469+2562=2093，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi7.0/doc-view-2.html>)
### 3.2 效果查看
统计每月累计剩余股票数，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 拓展阅读
[累计值（快速计算）](<https://help.fanruan.com/finebi7.0/doc-view-1680.html>)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：快速计算函数概述](<index.php?doc-view-1499.html>)
[下一篇：PERIOD_ANLS-上期末 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1210.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
