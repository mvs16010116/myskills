---
title: RANK_ANLS-排名
doc_id: 1216
url: https://help.fanruan.com/finebi/doc-view-1216.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:58
version: "7.X"
---

> 1. 概念语法rank_anls(x_agg(array), range, order)根据横纵轴或行列维度添加的字段对指标进行跨行排名的计算。参数1x_agg(array)第一个参数为用户计算的指标，

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# RANK_ANLS-排名
[__](<doc-edit-1216.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[13](<edition-list-1216.html>)
* 最近更新：[奶味小张](<user-space-3372890.html>) 于 2025-10-28 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法  
| rank_anls(x_agg(array), range, order)| 根据横纵轴或行列维度添加的字段对指标进行跨行排名的计算。  
---|---|---  
参数1| x_agg(array)| 第一个参数为用户计算的指标，该指标必须为聚合函数或聚合指标。聚合指标即使用[聚合函数](<https://help.fanruan.com/finebi7.0/doc-view-4.html>)计算得到的结果  
参数2| range| 第二个参数range为用户设置计算的范围，0为对所有行进行排名，1为对组内所有行进行排名。  
参数3| order| 第三个参数order为排名的计算规则，"asc"为升序排名，"desc"为降序排名。  
## 2\. 注意事项
  * 第三个参数支持DESC、ASC，不区分大小写。
  * 第二第三参数不支持 IF、SWITCH 函数等动态变量，否则可能产生不断嵌套解析的问题


## 3\. 示例
rank_anls(sum_agg(amount),0,"asc")用户横轴拖拽省份，则该指标计算结果为，根据省份对销量进行分组汇总，然后计算每个省份的销量在所有省份中的升序排名情况。
示例数据：[地区数据分析.xlsx](<doc-download-/finebi6.X/uploads/file/20230816/地区数据分析.xlsx> "下载资料")
对合同金额求排名，例如按照每个省份合同金额从小到大升序排名。
### 3.1 计算地区合同金额排名
新增 [计算字段](<https://help.fanruan.com/finebi7.0/doc-view-118.html>)，命名为「排名」字段，输入公式：RANK_ANLS(SUM_AGG(合同金额),0,"asc")，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
函数写法请参见：[函数计算格式](<https://help.fanruan.com/finebi7.0/doc-view-2.html>)
将「省份」、「合同金额」、「排名」拖入分析区域，并设置合同金额升序排列，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 效果查看
按照每个省份合同金额从小到大升序排名，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 拓展阅读
[排名（快速计算）](<https://help.fanruan.com/finebi7.0/doc-view-1678.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [制作可视化组件](<category-view-569>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：PREVIOUS_PERIOD-环期](<index.php?doc-view-1213.html>)
[下一篇：SAME_PERIOD-同期 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1212.html>)


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
