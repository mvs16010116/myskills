---
title: FIELD_IN(判断数组是否属于)
doc_id: 2638
url: https://help.fanruan.com/finebi/doc-view-2638.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:43
version: "7.X"
---

> 1. 概述1.1 版本FineBI版本功能变动7.0-1.2 函数简介语法FIELD_IN([field_1],[field_2])判断数组 field_1 中是否完全包含数组 field_2（忽略数组

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FIELD_IN(判断数组是否属于)
[__](<doc-edit-2638.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-2638.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-07-14 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI版本  
| 功能变动  
---|---  
7.0| -  
### 1.2 函数简介
语法  
| FIELD_IN([field_1],[field_2])| 判断数组 field_1 中是否完全包含数组 field_2（忽略数组内部值的顺序）  
---|---|---  
参数| [field_1],[field_2]| 必须为两个参数，写法上需要为字段声明数组，如[省份,城市]  
### 1.3 注意事项
应用范围：指标中心、组件（不包括明细表）
匹配规则：遵循「字段id」一致的规则，即同一个字段即可匹配上。字段设置了「自定义分组」或「时间分组」也能匹配。
## 2\. 动态层级成本分析
如何在企业用「一份数据模型」适应不同分析层级的成本展示需求，无需切换数据源或计算字段。查看从公司到个人层级的成本情况？
用户角色| 分析需求| 关注指标  
---|---|---  
CFO/财务总监/部门经理| 查看公司各区域、部门的人力成本情况| 公司成本   
= 员工薪资及福利 + 办公场地租赁 + 设备折旧等  
人力资源分析师| 查看每员工的个人成本，分析个人效益比| 个人成本  
= 员工个人的薪资及福利  
  

**实现思路：**
配合 [FIELD_IN()](<https://help.fanruan.com/finebi7.0/doc-view-2638.html>) 函数动态的判断分析区是否引入了某维度。如果分析区拖入了「员工姓名」维度，则函数计算中使用「个人成本」，不然则使用「公司成本」。
成本额=IF(FIELD_IN(ADD_DIM(), [员工姓名]), 个人成本, 公司成本)
**详情请参见文档：**[**动态层级维度成本分析**](<https://help.fanruan.com/finebi7.0/doc-view-2643.html>)
### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：SUB_DIM(引用维度-指定维度)](<index.php?doc-view-2624.html>)
[下一篇：动态层级维度成本分析 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2643.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
