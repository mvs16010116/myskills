---
title: EARLIER-获取当前行的值（只用于DEF类函数）
doc_id: 1991
url: https://help.fanruan.com/finebi6.X/doc-view-1991.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:13
---

> 1. 概述[helpvideo]5521[/helpvideo]1.1 函数简介EARLIER ：获取当前行的值。只能用于 DEF 类函数中，一般用于行间过滤计算。语法EARLIER(参数)获取「当前行

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# EARLIER-获取当前行的值（只用于DEF类函数）
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[13](<edition-list-1991.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-06-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 函数简介
EARLIER ：获取当前行的值。只能用于 DEF 类函数中，一般用于行间过滤计算。
语法  
| EARLIER(参数)  
| 获取「当前行」和「参数字段列」交叉的单元格的值  
---|---|---  
参数| 字段列| EARLIER 的参数为单个字段，不支持常量作为参数。  
### 1.2 注意事项
**问题描述：** 数据更新时提示更新失败，报错「更新时检测使用到 earlier 函数不等式导致计算数据严重膨胀，操作中止，请检查公式中 earlier 函数，去掉 earlier 的不等式或者控制数据量大小。」
**原因分析：** earlier 函数，对自助数据集存在数据限制，若自助数据集数据量超过 1000000 ，就会出现该报错。
**解决方案：** 请换用其他函数，或控制底表数据在1000000以内。
## 2\. 示例-获取错行值
很多时候我们都需要获取错行值，比如计算上一个日期与下一个日期的差，又比如计算上一步数据到下一步数据的转化率。
这里以计算转化率为例，我们需要获取「上一行」的值，便于我们两列相除。
![40.png](/core/style/lod.png)
1）上传示例数据：[汽车行业销售漏斗.xlsx](<doc-download-/finebi6.X/uploads/file/20221116/汽车行业销售漏斗.xlsx> "下载资料")
将下载下来的数据上传至分析主题，如下图所示：
![](/core/style/lod.png)
2）求每个节点的客户数，添加计算字段，如下图所示：
![2024-10-29_11-00-19.png](/core/style/lod.png)
3）先给这些节点按客户数排个名，由于这些节点有前后关系，客户数越多，说明这些节点越靠前。  

![](/core/style/lod.png)
  

公式| 描述  
---|---  
DEF(COUNTD_AGG(关键节点),[关键节点],[每个节点的客户数>=EARLIER(每个节点的客户数)])| 
  * 指定维度：关键节点
  * 聚合指标计算：COUNTD_AGG(关键节点)
  * 过滤条件：每个节点的客户数>=EARLIER(每个节点的客户数)，意思是过滤出所有客户数大于等于「当前节点客户数」的所有节点。

求得满足客户数大于等于「当前节点客户数」的节点，即可得到节点排名  
  
「排名」拖入分析区域后，可查看「排名」计算结果是否正确。  
![43.png](/core/style/lod.png)
  

4）计算当前节点的上一个节点的客户数，如下图所示：
![2024-11-20_17-51-42.png](/core/style/lod.png)
公式分解  
| 描述  
  
---|---  
SUM_AGG(客户数)| 求客户总数  
DEF(SUM_AGG(客户数),[关键节点],排名+1=EARLIER(排名))| 
  * 指定维度：关键节点
  * 聚合指标计算：SUM_AGG(客户数)
  * 过滤条件：排名+1=EARLIER(排名)

过滤条件即为 排名=EARLIER(排名)-1 ，筛选到比「当前行排名」-1的那个节点，获得那个节点的客户数求和  
将「上一步的客户数」拖入分析区域，可查看计算结果是否正确。如下图所示：
![45.png](/core/style/lod.png)
5）计算转化率，使用公式：当前客户数/上一步的客户数 ，即可求得。如下图所示：
![2024-11-20_17-50-30.png](/core/style/lod.png)
6）将「转化率」拖入分析区域，并将数值格式改为百分比。如下图所示：
![47.png](/core/style/lod.png)
  

如此我们便完成了转化率分析  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：DEF_SUB(分析区域维度-指定维度)](<index.php?doc-view-1990.html>)
[下一篇：CLEAN函数-清除所有过滤效果（只用于DEF类函数） ![](/core/style/forward.png) ](<index.php?doc-view-2407.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
