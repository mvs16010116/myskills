---
title: TODAY-当前日期
doc_id: 1421
url: https://help.fanruan.com/finebi6.X/doc-view-1421.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:04:32
---

> 1. 概述语法TODAY()是获取当前的日期。2. 注意事项没有参数。支持日期字段-数值写法。例如 today()-1相当于返回昨天的日期。若抽取数据版本需要计算当前日期的前一天，可使用DATEDELT

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# TODAY-当前日期
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[5](<edition-list-1421.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2022-06-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法  
| TODAY()| 是获取当前的日期。  
---|---|---  
## 2\. 注意事项
  * 没有参数。
  * 支持日期字段-数值写法。例如 today()-1相当于返回昨天的日期。


若抽取数据版本需要计算当前日期的前一天，可使用DATEDELTA(TODAY(),-1)，结果如下图所示：
![](/core/style/lod.png)
公式说明：
公式  
| 说明  
---|---  
TODAY()| 返回当前日期  
[DATEDELTA](<https://help.fanruan.com/finebi6.0/doc-view-7.html#13>)(TODAY(),-1)| 返回当前一个日期前一天的日期   
## 3\. 示例
公式  
| 结果| 备注  
---|---|---  
TODAY()| 2005-9-10| 如果系统日期是 2005 年 9 月 10 日  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：TIME-时间](<index.php?doc-view-1422.html>)
[下一篇：TODATE-转换为日期类型 ![](/core/style/forward.png) ](<index.php?doc-view-1406.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
