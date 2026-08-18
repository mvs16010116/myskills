---
title: INDEXOF-返回指定位置的字符
doc_id: 1467
url: https://help.fanruan.com/finebi/doc-view-1467.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:13
version: "7.X"
---

> 1. 概述语法INDEXOF(str1,index)返回字符串str1在index位置上的字符参数1str1字符串参数2index位置2. 注意事项index是从 0 开始计数的函数返回的数据类型为文本

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# INDEXOF-返回指定位置的字符
[__](<doc-edit-1467.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[2](<edition-list-1467.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-08-30 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| INDEXOF(str1,index)| 返回字符串str1在index位置上的字符  
---|---|---  
参数1| str1| 字符串  
参数2| index| 位置  
## 2\. 注意事项
  * index是从 0 开始计数的
  * 函数返回的数据类型为文本型
  * 支持使用两个参数，第一个为任意类型，第二个为数值类型


## 3\. 示例
例如，想过滤出门店编码末尾是 3 的数据。
![2022-08-30_16-23-56.png](https://help.fanruan.com/core/style/lod.png)
使用过滤条件：INDEXOF(门店编码,6)="3"，如下图所示：
注：因为函数返回的字段为文本类型，所以过滤条件中的数值 3 需要加双引号，改成文本类型。
![2022-08-30_16-22-36.png](https://help.fanruan.com/core/style/lod.png)
  

更多示例：
公式| 结果| 备注  
---|---|---  
INDEXOF("FineBI",0)| F|   
  
INDEXOF("FineBI",2)| n|   
  
INDEXOF("FineBI",5)| I|   
  
INDEXOF(["a","b","c"], 1)| b|   
  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：LEN-返回字符长度](<index.php?doc-view-1472.html>)
[下一篇：FORMAT-格式转换 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1454.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
