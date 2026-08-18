---
title: AARRR 用户运营分析
doc_id: 1256
url: https://help.fanruan.com/finebi/doc-view-1256.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:24:46
version: "7.X"
---

> 1. 概述1.1 概念本文使用 AARRR 模型进行用户运营分析，AARRR 模型又叫海盗模型，是用户运营过程中常用的一种模型，解释了实现用户增长的 5 个指标：获客、激活、留存、收益、传播。从获客到传

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# AARRR 用户运营分析
[__](<doc-edit-1256.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[13](<edition-list-1256.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-07-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 概念
本文使用 AARRR 模型进行用户运营分析，AARRR 模型又叫海盗模型，是用户运营过程中常用的一种模型，解释了实现用户增长的 5 个指标：获客、激活、留存、收益、传播。从获客到传播推荐，整个 AARRR 模型形成了用户全生命周期的闭环模式，不断扩大用户规模，实现持续增长。
### 1.2 预期效果
每一个产品具体情况不同，但总体上都包括这 5 个方面的发展过程。本文利用 FineBI 对一买菜 APP 的这 5 个发展过程进行分析。
![10.png](https://help.fanruan.com/core/style/lod.png)
### 1.3 获取数据
本案例使用的示例数据：[AARRR示例数据.rar](<doc-download-/finebi5.1/uploads/file/20210308/AARRR示例数据.rar> "下载资料")
## 2\. 获客 
获客即拉新，即让用户知道了解认识到有这样一个 APP 并来试用。通常情况下会有多个渠道增加产品的曝光，但如何选出最优渠道，使用最少的预算获得最好的拉新效果呢，第一个要做的就是渠道分析。
通常情况下渠道分析有两个维度：获客数量和获客质量。（在本文中我们以平均打开 APP 的浏览时间作为获客质量评价标准。）
![2.png](https://help.fanruan.com/core/style/lod.png)
**结论** ：可以看到线下活动推广的数量与质量都是最优，可以加大线下活动的投入，在超市或菜市场附件做线下活动是最优选项。
## 3\. 激活
激活并不直接对等注册成功。激活要做的是活跃客户，更应该考虑的是用户对于产品核心功能的使用情况。
例如：短视频软件需要新用户观看到一定时长、聊天软件需要新用户完成一次对话才算激活。那么在买菜 APP 中，我们认为购买过一次的用户为激活用户。
对各月份的用户新增情况进行分析，折线图如下：
![3.png](https://help.fanruan.com/core/style/lod.png)
**结论** ：10 月份激活率下降，需要分析具体原因。同时辅助进行新客活动，并做精细化运营，在首页进行个性化推荐产品吸引用户。
## 4\. 留存
用户激活之后，不留存的话最终也都将流失，徒劳一场。
所以用户的留存统计也很重要。参考 [留存分析](<https://help.fanruan.com/finebi7.0/doc-view-1119.html?source=4>) 计算激活用户的一周留存率/两周留存率/30天留存率。如下图所示：
![5.png](https://help.fanruan.com/core/style/lod.png)
**结论** ：用户留存率有较大空间提高，需要分析流失原因，进一步提高产品体验，挽留已有客户。  

## 5\. 收益
当用户激活后成为了你的一名用户，需要考虑的就是如何获取收入，实现盈利。买菜软件的盈利与很多指标有关，这里我们暂且以提高用户的购买活跃度作为提高收入的的一个主要方式。
我们将用户分为三个大类：低活跃用户，普通用户，会员用户。使用漏斗图展示，如下图所示：
![8.png](https://help.fanruan.com/core/style/lod.png)
**结论** ：低活跃用户数量庞大，很有潜力。活跃低活跃的用户，保持会员用户。
## 6\. 传播
当产品有了一定规模的用户之后，就需要考虑激发用户间的自发传播。自传播的数据指标是K因子（推荐系数）：
**K = （平均每个用户向他的朋友们发出的邀请的数量）* （接收到邀请的人转化为新用户的转化率）**
K值的高低，直接体现自传播结果水平，当K值大于1时，将激发自传播巨大的力量，K值越大，力量越强。而若K值小于1，那么传播水平会逐步减弱，直至消失。
计算该 APP 的 K 值，如下图所示：
![9.png](https://help.fanruan.com/core/style/lod.png)
**结论** ：该 APP K值已经大于 1 ，拥有了自传播的力量。可以进一步通过“邀请获红包”等运营活动进一步提高 K 值，加快传播速度。
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：用户流入流出分析](<index.php?doc-view-1273.html>)
[下一篇：用户生命状态分析 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1261.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
