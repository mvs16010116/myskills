---
title: Switch-多条件赋值
doc_id: 360
url: https://help.fanruan.com/finebi/doc-view-360.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:50
version: "7.X"
---

> 1. 概述1）函数释义SWITCH 函数可对多种情况进行判断，并根据不同的值返回对应结果。注：不支持在 Switch 函数中增加 else 判断。语法SWITCH(表达式,值1,结果1,值2,结果2,…

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Switch-多条件赋值
[__](<doc-edit-360.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[11](<edition-list-360.html>)
* 最近更新：[Suki陈](<user-space-1778923.html>) 于 2023-09-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
**1）函数释义**
SWITCH 函数可对多种情况进行判断，并根据不同的值返回对应结果。
注：不支持在 Switch 函数中增加 else 判断。
语法  
| SWITCH(表达式,值1,结果1,值2,结果2,……，其他结果)| 如果表达式的结果是值1，整个函数返回结果1；如果表达式的结果是值2，整个函数返回结果2等等；如果没有符合要求的值，则返回其他结果。  
---|---|---  
参数1| 表达式| -  
参数2| 结果| 所有的结果1，结果2……必须为同类型数据。其他结果可以缺省，缺省时及表达式值没有对应的结果时返回值为空。  
**2）注意事项**
  * 至少三个参数
  * 实时数据中参数个数至少 3 个，且结果参数类型一致。
  * 如果参数类型是日期，那么需要嵌套日期类型函数，例如SWITCH(时间,TODATE("2022/01/01"),"1")  



**3）示例**  

公式| 结果  
| 备注  
---|---|---  
SWITCH(1+2,3,"今天星期三",4,"今天星期四")| 今天星期三| -  
SWITCH(5,3,"今天星期三",4,"今天星期四","星期五")| 星期五| -  
## 2\. 更多示例
当需要判断条件多的时候，使用 [IF 函数](<https://help.fanruan.com/finebi7.0/doc-view-1377.html>) 可能会觉得用要对每种情况都进行判断，比较麻烦，那么可以使用 switch 函数进行多条件赋值。
例如希望对班级进行设置：当前值是 Class1 则显示一班，如果是 Class2，则显示二班，如果是 Class3，则显示三班，否则显示四班。
示例数据：[成绩表 .zip](<doc-download-/finebi5.1/uploads/file/20211111/成绩表 .zip> "下载资料")
### 2.1 添加数据表
1）将「成绩表」添加至 FineBI 。点击「我的分析」，再点击「新建分析主题」弹出上传数据窗口，选择「本地Excel文件」点击「上传数据」，如下图所示：  

![](https://help.fanruan.com/core/style/lod.png)
![](https://help.fanruan.com/core/style/lod.png)
2）点击「上传数据」后，弹出文件选择窗口，选择下载好的示例数据「成绩表」，点击「打开」，可以预览上传的数据，再点击「确定」，成功上传数据并创建分析主题。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 2.2 进行条件赋值
1）进入数据集编辑界面，添加「新增公式列」，编辑公式：switch(班级,"Class1","一班","Class2","二班","Class3","三班","四班")，输入新增列名，「新增公式列名」为“中文班级”，点击「确定」，如下图所示：
注：公式中「班级」字段并非手动输入，而是在左侧字段中单击选择。 
![](https://help.fanruan.com/core/style/lod.png)
2）公式说明：
公式| 说明  
---|---  
switch(班级,"Class1","一班","Class2","二班","Class3","三班","四班")| 如果数据为 Class1，则赋值为一班，Class2 则赋值为二班，Class 三则赋值为三班，否则显示四班  
  
### 2.3 效果预览
效果如下图所示：
![](https://help.fanruan.com/core/style/lod.png)  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：OR](<index.php?doc-view-1384.html>)
[下一篇：IF函数的嵌套用法 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2510.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
