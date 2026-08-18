---
title: ROUND-保留几位小数
doc_id: 1379
url: https://help.fanruan.com/finebi/doc-view-1379.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:06
version: "7.X"
---

> 1. 概述语法ROUND(number,num_digits)返回某个数字按指定位数舍入后的数字。参数1number需要进行舍入的数字。参数2num_digits按此位数进行舍入，小于0，则在小数点左侧

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# ROUND-保留几位小数
[__](<doc-edit-1379.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1379.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-08-14 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| ROUND(number,num_digits)| 返回某个数字按指定位数舍入后的数字。  
---|---|---  
参数1| number| 需要进行舍入的数字。  
参数2| num_digits| 按此位数进行舍入，小于0，则在小数点左侧进行舍入。等于0，则舍入到最接近的整数。大于0，则舍入到指定的小数位。  
## 2\. 注意事项
1）支持两个数值参数。
2）一般情况下 ROUND 函数遵循四舍五入的规则。
若在特殊情况下精度发生偏差，可使用函数 old_round 进行计算，替代 ROUND 函数。
## 3\. 示例
示例数据：[商品销售明细表.xlsx](<doc-download-/finebi6.X/uploads/file/20230811/商品销售明细表.xlsx> "下载资料")
1）使用示例数据「商品销售明细表」，需要将「销售额」数值统一为保留小数点后一位。
在主题中使用 [新增列](<https://help.fanruan.com/finebi7.0/doc-view-509.html>) ，点击「新增公式列」，「新增公式列名」设为“销售额保留一位小数”，命名后输入公式ROUND(销售额,1)，点击「确定」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
此时自助数据集中出现保留一位小数后的数据，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）更多数据示例如下所示：
公式| 结果  
| 备注  
---|---|---  
ROUND(2.15,1)| 2.2|   
  
ROUND(2.149,1)| 2.1|   
  
ROUND(-1.475,2) | -1.48|   
  
ROUND(21.5,-1) | 20|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：INT](<index.php?doc-view-1380.html>)
[下一篇：聚合函数概述 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-4.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
