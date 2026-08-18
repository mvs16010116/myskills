---
title: VAR_AGG-方差
doc_id: 1392
url: https://help.fanruan.com/finebi6.X/doc-view-1392.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:06
---

> 1. 概述语法VAR_AGG(array)根据当前分析维度，动态返回指标字段的方差，生成结果为一动态数据列，行数与当前分析维度行数一致。参数array必须为非聚合函数公式返回的结果，可以是某指标字段、维

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# VAR_AGG-方差
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1392.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| VAR_AGG(array)| 根据当前分析维度，动态返回指标字段的方差，生成结果为一动态数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为非聚合函数公式返回的结果，可以是某指标字段、维度或指标字段与普通公式的计算结果。  
## 2\. 注意事项
实时数据中支持使用单个数值类型参数。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段VAR_AGG(销量)返回的值为每日的销量方差。
当用户横轴为维度字段'月'时，VAR_AGG(销量)返回的值为每月的销量方差。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：COUNTD_AGG-去重计数](<index.php?doc-view-1388.html>)
[下一篇：STDEV_AGG-标准差 ![](/core/style/forward.png) ](<index.php?doc-view-1394.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
