---
title: ATAN2-返回x、y坐标的反正切值
doc_id: 1445
url: https://help.fanruan.com/finebi/doc-view-1445.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:23:01
version: "7.X"
---

> 1. 概述语法ATAN2(x_num,y_num)返回x、y坐标的反正切值。返回角度为x轴与过（x_num,y_num）与坐标原点（0,0）的一条直线形成的角度。参数1x_num指定点的x坐标参数2y_

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# ATAN2-返回x、y坐标的反正切值
[__](<doc-edit-1445.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[1](<edition-list-1445.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
语法| ATAN2(x_num,y_num)| 返回x、y坐标的反正切值。返回角度为x轴与过（x_num,y_num）与坐标原点（0,0）的一条直线形成的角度。  
---|---|---  
参数1| x_num| 指定点的x坐标  
参数2| y_num| 指定点的y坐标  
## 2\. 注意事项
  * 支持两个数值参数
  * 正值表示从x轴开始以逆时针方式所得的角度；负值表示从x轴开始以顺时针方式所得的角度。 ATAN2(a,b)=ATAN(b/a)，a为0时除外。 当x_num与y_num都为0时，ATAN2返回错误信息*DIV/0!。 用角度制显示返回数值时，把返回数值乘以180/PI()。 返回值以弧度表示（返回值大于-pi且小于等于pi）。


## 3\. 示例
公式  
| 结果| 备注  
---|---|---  
ATAN2(-2,2)| 2.356194490192345| 弧度制的3*pi/4  
ATAN2(2,2)| 0.785398163| 弧度制的pi/4  
ATAN2(-2,2)*180/PI()| 135| 角度制  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：CEILING-向上取整](<index.php?doc-view-1438.html>)
[下一篇：ATAN-计算指定数值的反正切值 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1444.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
