---
title: EARLIER-获取当前行的值（只用于DEF类函数）
doc_id: 1991
url: https://help.fanruan.com/finebi/doc-view-1991.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:19
version: "7.X"
---

> 1. 概述注：本函数仅适用于自助分析主题。EARLIER ：获取当前行的值。只能用于 DEF 类函数中，一般用于行间过滤计算。语法EARLIER(参数)获取「当前行」和「参数字段列」交叉的单元格的值参数

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# EARLIER-获取当前行的值（只用于DEF类函数）
[__](<doc-edit-1991.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[20](<edition-list-1991.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-05-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**注：本函数仅适用于自助分析主题。**
EARLIER ：获取当前行的值。只能用于 DEF 类函数中，一般用于行间过滤计算。
语法  
| EARLIER(参数)  
| 获取「当前行」和「参数字段列」交叉的单元格的值  
---|---|---  
参数| 字段列| EARLIER 的参数为单个字段，不支持常量作为参数。  
## 2\. 示例-获取错行值
很多时候我们都需要获取错行值，比如计算上一个日期与下一个日期的差，又比如计算上一步数据到下一步数据的转化率。
这里以计算转化率为例，我们需要获取「上一行」的值，便于我们两列相除。
![40.png](https://help.fanruan.com/core/style/lod.png)
1）上传示例数据：[汽车行业销售漏斗.xlsx](<doc-download-/finebi6.0/uploads/file/20221116/汽车行业销售漏斗.xlsx> "下载资料")
将下载下来的数据上传至分析主题，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）求每个节点的客户数，添加计算字段，如下图所示：
![42.png](https://help.fanruan.com/core/style/lod.png)
3）先给这些节点按客户数排个名，由于这些节点有前后关系，客户数越多，说明这些节点越靠前。  

![41.png](https://help.fanruan.com/core/style/lod.png)
  

公式| 描述  
---|---  
DEF(COUNTD_AGG(关键节点)+1,[关键节点],[每个节点的客户数>EARLIER(每个节点的客户数)])| 
  * 指定维度：关键节点
  * 聚合指标计算：COUNTD_AGG(关键节点)+1
  * 过滤条件：每个节点的客户数>EARLIER(每个节点的客户数)，意思是过滤出所有客户数大于「当前节点客户数」的所有节点。

满足客户数大于「当前节点客户数」的节点，进行 COUNTD_AGG(关键节点)+1 的计算  
  
  
「排名」拖入分析区域后，可查看「排名」计算结果是否正确。  
![43.png](https://help.fanruan.com/core/style/lod.png)
4）计算当前节点的上一个节点的客户数，如下图所示：  

![44.png](https://help.fanruan.com/core/style/lod.png)
公式分解  
| 描述  
  
---|---  
SUM_AGG(客户数)| 求客户总数  
DEF(SUMS_AGG(客户数),[关键节点],排名+1=EARLIER(排名))| 
  * 指定维度：关键节点
  * 聚合指标计算：SUM_AGG(客户数)
  * 过滤条件：排名+1=EARLIER(排名)

过滤条件即为 排名=EARLIER(排名)-1 ，筛选到比「当前行排名」-1的那个节点，获得那个节点的客户数求和  
将「上一步的客户数」拖入分析区域，可查看计算结果是否正确。如下图所示：
![45.png](https://help.fanruan.com/core/style/lod.png)
5）计算转化率，使用公式：上一步的客户数/每个节点的客户数 ，即可求得。如下图所示：
![46.png](https://help.fanruan.com/core/style/lod.png)
6）将「转化率」拖入分析区域，并将数值格式改为百分比。如下图所示：
![47.png](https://help.fanruan.com/core/style/lod.png)
如此我们便完成了转化率分析。  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：DEF_SUB(分析区域维度-指定维度)](<index.php?doc-view-1990.html>)
[下一篇：CLEAN函数-清除所有过滤效果（只用于DEF类函数） ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2407.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
