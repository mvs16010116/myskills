---
title: COUNT_AGG-计数
doc_id: 1386
url: https://help.fanruan.com/finebi/doc-view-1386.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:10
version: "7.X"
---

> 1. 概述COUNT_AGG() 为对指定维度（拖入分析栏）数据进行计数（非空），且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。语法COUNT_AGG(array)根据当前分析维度，返回某字

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# COUNT_AGG-计数
[__](<doc-edit-1386.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[12](<edition-list-1386.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
COUNT_AGG() 为对指定维度（拖入分析栏）数据进行计数（非空），且随着用户分析维度的切换，计算字段会自动跟随维度动态调整。
语法  
| COUNT_AGG(array)| 根据当前分析维度，返回某字段的计数，生成结果为一数据列，行数与当前分析维度行数一致。  
---|---|---  
**参数**|  array| 必须为任意非聚合表达式  
## 2\. 注意事项
实时数据支持使用一个任意类型的参数。
## 3\. 示例
用户横轴为维度字段'日'时，纵轴的计算字段COUNT_AGG(销量)返回的值为每日的销量的个数。
当用户横轴为维度字段'月'时，COUNT_AGG(销量)返回的值为每月的销量的个数。
例如使用「合同事实表」，希望计算每年的合同签约数量，则首先将「合同签约时间」拖入横轴，并设置分组方式为「年」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
1）创建计算字段，命名为「合同量」，输入公式：COUNT_AGG(合同ID)，点击「确定」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
2）即可得到结果，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
3）当然，直接将 [记录数](<https://help.fanruan.com/finebi7.0/doc-view-362.html>) 拖入分析栏也是一样的效果，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 拓展阅读
记录数(行数)=COUNT_AGG(1)，详情参见：[记录数](<https://help.fanruan.com/finebi7.0/doc-view-362.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：AVG_AGG-平均值](<index.php?doc-view-1393.html>)
[下一篇：COUNTD_AGG-去重计数 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1388.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
