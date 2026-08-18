---
title: temp文件夹占用空间过大
doc_id: 589
url: https://help.fanruan.com/finebi6.X/doc-view-589.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:38
---

> 1、描述现象描述：使用 FineBI 的过程中，发现BI占用内存较高，进一步查询发现是根目录下的 temp 文件夹占用空间较大。比如下图中，查看 temp 目录，发现存在几十、上百 G 的文件；操作简介

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# temp文件夹占用空间过大
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[susie](<user-space-58814.html>)_
* 历史版本：[3](<edition-list-589.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2021-02-01 
[](<javascript:;>) [](<javascript:>)
## 1、描述
**现象描述：**
  * 使用 FineBI 的过程中，发现BI占用内存较高，进一步查询发现是根目录下的 temp 文件夹占用空间较大。比如下图中，查看 temp 目录，发现存在几十、上百 G 的文件；
![1.png](/core/style/lod.png)


**操作简介：**
  * 该 temp 目录为 Spark 计算时生成的临时文件目录，BI 默认为自动清除 7 天内的临时文件（2019.7.15 之后的版本默认清除间隔时间已改为 1 小时），管理员可对默认清除间隔时间进行修改，清除不需要的文件以减少空间占用；


**适用人群：**
  * 管理员；


## 2、清除间隔时间修改
  1. finedb数据库中，找到 fine_conf_entity 表，如下图：
![1.png](/core/style/lod.png)  

  2. 使用命令查找 DistributedOptimizationConfig.spiderConfig.spark_temp_expired_time 参数，若没有则新建该参数；
[code]SELECT * FROM FINE_CONF_ENTITY WHERE ID='DistributedOptimizationConfig.spiderConfig.spark_temp_expired_time'
[/code]
  3. 修改该参数对应的 VALUE 值，单位为 s，即为清除的间隔时间。比如我们设置为 3600，即表示计算临时文件的清除时间为 1 小时。


  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](/core/style/back.png)上一篇：PUT、DELETE请求转成POST插件](<index.php?doc-view-1262.html>)
[下一篇：云端运维应用ID固定问题解决方案 ![](/core/style/forward.png) ](<index.php?doc-view-604.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
