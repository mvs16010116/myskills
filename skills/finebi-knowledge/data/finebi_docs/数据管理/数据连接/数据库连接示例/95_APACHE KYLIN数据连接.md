---
title: APACHE KYLIN数据连接
doc_id: 95
url: https://help.fanruan.com/finebi6.X/doc-view-95.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:07:14
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何连接 Apache Kylin 数据库。2. 准备工作2.1 版本和驱动下载驱动，并将其上传至 FineBI 。如何

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# APACHE KYLIN数据连接
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[27](<edition-list-95.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-11-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本  
| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何连接 Apache Kylin 数据库。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动，并将其上传至 FineBI 。如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi6.0/doc-view-1540.html?source=4>) 2.1 节  

注：在上传驱动包时，需要解压下面的「日志jar」文件，一起上传至 FineBI。
支持的数据库版本| 驱动包下载  
| 日志jar下载  
---|---|---  
1.5.0；2.2 | 请根据数据库版本从 [官网](<https://kylin.apache.org/docs/integration/jdbc>) 下载对应插件| [日志jar.rar](<doc-download-/finebi5.1/uploads/file/20211213/日志jar.rar> "下载资料")  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；
  * 要连接的数据库模式；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理」，点击「新建数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<http://help.finereport.com/doc-view-2457.html>)
![](/core/style/lod.png)
2）找到 Apache Kylin 数据库，如下图所示：
![](/core/style/lod.png)
3）驱动切换为「自定义」选择 2.1 节上传的驱动，并输入 2.2 节收集的连接信息。
模式需要连接数据库后才可以选择，所以需要先点击「点击连接数据库」后，再选择「模式」，如下图所示：
![](/core/style/lod.png)
4）点击「测试连接」，若连接成功则点击「保存」，如下图所示：
![](/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi6.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi6.0/doc-view-890.html>)


![2.png](/core/style/lod.png)
## 5\. 注意事项
### 5.1 时差问题
不管设置的时区在哪里，kylin 给数据的时候会强制设置到格林威治时间，所以总有 8 小时的时差。例如 kylin 查询结果为 2018-01-01，取数过来的查询结果为 2017-12-31。
所以需要用户在写 SQL 语句时手动加上 8 h。
### 5.2 直连属性的数据表
由于 KYLIN 数据库不支持相关功能，直连属性的数据表有以下限制：  

1）从 KYLIN 数据库取出来的直连属性的数据表，因为 KYLIN 数据库本身的原因，不支持以下函数：
[CHAR-返回指定数值的字符](<https://help.fanruan.com/finebi6.X/doc-view-1473.html>)| [CODE-返回数值代码](<https://help.fanruan.com/finebi6.X/doc-view-1474.html>)  
---|---  
[REPEAT-重复显示文本](<https://help.fanruan.com/finebi6.X/doc-view-1462.html>)| [RANDBETWEEN-返回两个数相同整数部分](<https://help.fanruan.com/finebi6.X/doc-view-1435.html>)  
[INDEXOF-返回指定位置的字符](<https://help.fanruan.com/finebi6.X/doc-view-1467.html>)|   
  
2）直连属性的数据表中 DATE 和 TIMESTAMP 字段无法进行左右合并。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据管理](<category-view-285>)
[![](/core/style/back.png)上一篇：阿里云MaxCompute数据连接](<index.php?doc-view-1127.html>)
[下一篇：HP Vertica数据连接 ![](/core/style/forward.png) ](<index.php?doc-view-97.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
