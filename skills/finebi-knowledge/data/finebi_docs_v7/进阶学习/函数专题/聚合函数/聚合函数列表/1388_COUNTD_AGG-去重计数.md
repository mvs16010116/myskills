---
title: COUNTD_AGG-去重计数
doc_id: 1388
url: https://help.fanruan.com/finebi/doc-view-1388.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:11
version: "7.X"
---

> 1. 概述COUNTD_AGG() 为对指定维度（拖入分析栏）数据进行去重计数（非空），且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。语法COUNTD_AGG(array)根据当前分析维度，

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# COUNTD_AGG-去重计数
[__](<doc-edit-1388.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[7](<edition-list-1388.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-14 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
COUNTD_AGG() 为对指定维度（拖入分析栏）数据进行去重计数（非空），且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。
语法  
| COUNTD_AGG(array)| 根据当前分析维度，返回某字段的去重计数，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
实时数据支持使用一个任意类型的参数。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段 COUNTD_AGG(销量) 返回的值为每日的销量的去重个数。
当用户横轴为维度字段'月'时，COUNTD_AGG(销量)返回的值为每月的销量的去重个数。
例如使用「合同信息」，希望统计不同合同类型的的客户数，有两种实现方案。
### 方法一：
使用 COUNTD_AGG 函数，创建计算字段「客户数」，输入公式：COUNTD_AGG(客户ID)，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
将数据拖入分析栏，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 方法二：
使用维度转指标，将「客户ID」转成指标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：COUNT_AGG-计数](<index.php?doc-view-1386.html>)
[下一篇：VAR_AGG-方差 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1392.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
