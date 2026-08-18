---
title: MySQL数据连接
doc_id: 183
url: https://help.fanruan.com/finebi/doc-view-183.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:41
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变动6.0-1.2 应用场景本文将介绍如何在 FineBI 中连接 MySQL 数据库。2. 准备工作2.1 版本和驱动下载驱动，并将其上传至 FineBI，

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# MySQL数据连接
[__](<doc-edit-183.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[62](<edition-list-183.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变动  
---|---  
6.0| -  
  
### 1.2 应用场景
本文将介绍如何在 FineBI 中连接 MySQL 数据库。
## 2\. 准备工作
### 2.1 版本和驱动
下载驱动，并将其上传至 FineBI，如何上传可参见：[驱动管理](<https://help.fanruan.com/finebi7.0/doc-view-1540.html?source=4>) 2.1 节
支持数据库版本 | 驱动包下载  
---|---  
V8.0、V5.6.31、V5.5、V5.5.5、V5.6.35、V5.7、V5.6.37、V5.5.46、V6.5、V5.7.16 、V5.6.29、V5.6.22、V5.6.34、V5.6.28、V5.1；| 已内置，无需下载  
  
**官方建议：** 为获得更好的取数性能，建议使用 Mysql5.5、5.6、5.7 版本的客户，更换 Mysql 数据库驱动为 5.1.37 版本为获得更好的取数性能。（5.1.37 版本的驱动不支持 V5.1、V8.0 的数据库）[mysql-connector-java-5.1.37.jar](<doc-download-/finebi5.1/uploads/file/20220104/mysql-connector-java-5.1.37.jar> "下载资料")  
用户若使用的是其他小版本的数据库，可以从 [MySQL官网](<https://mvnrepository.com/artifact/mysql/mysql-connector-java?__cf_chl_jschl_tk__=bad963851cd373b24d332079fc29357b8d74625e-1595226852-0-AXjEroU1u6LViDWoHTRjgQ5dR593TrOrc9YqPI0H3Tdb2oh6pRXWmaP8KMOeuDm7Fthvpyjac4nIACbRGkXmFwWGFnAvLnQOUZt3269ORgPXoSZnn-SOyFRvH9ZYs61I8eNbbymRv0MBnIgBsXUa2bd0oq7WYlPKdm-8RhvLV9RpicgbmqJ_mLCsHhSqKO-YSXL7rQkfwsxXSmHcLlPzNK3y4BNJ-5IvPEcA-lgikQtDgAzWqoF9w7kgduIOib9-Ytq9c1i6YO0ZuxKHD65S3Bmu6-Dfnxr5btiQyB_Iea2oW5soNdUIRHAl2ihxDkVw5FMYjKmdeicx-u1D1L1zrTsBTzNp7TR_D5GYAHhKPAcb0jsy3OHcjOPyRtX5y0JFmg>) 下载对应的连接驱动包。  
### 2.2 收集连接信息
在连接数据库之前，请收集以下信息：
  * 数据库所在服务器的 IP 地址和端口号；
  * 数据库的名称；
  * 数据库的用户名和密码；


## 3\. 具体连接步骤
1）以管理员身份登录 FineBI ，点击「管理系统>数据连接>数据连接管理>新建」，点击「数据连接」，如下图所示：  

注：如果非管理员用户想要配置数据连接，需要管理员给其分配管理系统下数据连接节点的权限，具体操作请查看 [数据连接权限](<https://help.fanruan.com/finebi7.0/doc-view-488.html?source=4>)
![](https://help.fanruan.com/core/style/lod.png)
2）找到 MySQL 的图标，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）驱动选择「默认」（若用户重新上传了驱动，可以切换为自定义后选择自己的驱动），然后输入 2.2 节的连接信息。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注：若出现中文乱码或日期错乱的情况，可在「数据连接URL」后加后缀，格式为：jdbc:mysql://hostname:port/database?generateSimpleParameterMetadata=true&useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
其中
serverTimezone=Asia/Shanghai -- 设置以"上海时区"为准  

characterEncoding=utf8 -- 编码转化
4）点击「测试连接」，若连接成功则「保存」该连接。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 添加数据库的表至 FineBI
有两种方式可以将数据库中的表添加至 FineBI ：
  * [添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html?source=4>)
  * [添加SQL数据集](<https://help.fanruan.com/finebi7.0/doc-view-890.html>)


![](https://help.fanruan.com/core/style/lod.png)
## 5\. 注意事项
### 5.1 数据库编码问题
若 MySQL 数据库编码为 UTF-8 ，需要在数据连接的 URL 后添加参数 ?useUnicode=true&characterEncoding=UTF-8
如果添加参数后仍然出现下图所示的乱码，那么需要将编码改为「默认」。
![1589868788448436.jpg](https://help.fanruan.com/core/style/lod.png)
### 5.2 添加数据表问题
#### 5.2.1 SQL 语句  

1）添加 SQL 数据集时，输入的 SQL 语句不支持添加注释。
2）添加 SQL 数据集时，输入的 SQL 语句不支持 top N 语句。
3）问题现象：添加SQL 数据集时，输入的 SQL 语句中带有 concat() 函数 ，例如 select concat( count(*) ,"个")from table GROUP BY table1，如果连接的字段类型不同，会出现乱码。 
解决方法：利用 MySQL 的字符串转换函数 CONVERT() 将参数格式化为 char 类型即可，例如：select concat( CONVERT(count(*),char),"个")from table GROUP BY table1。
#### 5.2.2 字段类型
1）当使用 MYSQL 数据连接并添加数据表时，若数据库版本为 MYSQL 5.6 ，请确保数据库中 varchar 文本类型字段不为空，否则添加表至 BI 后出现小方块![1574922930783691.png](https://help.fanruan.com/core/style/lod.png)乱码。
2）当使用 MYSQL 数据连接并添加数据表时，如果数据库中字段类型为年份 (year) 类型，在 BI 中会被识别成文本字段，且显示为年月日格式。如数据库中有 year 类型字段 2015，在 BI 中添加该数据表则会显示为 2015-01-01。  

#### 5.2.3 添加的数据集日期字段值和数据库记录的日期有误差
1）现象：仪表板或数据准备页面显示数据库的时间字段，比实际数据小了一天。
2）原因：mysql数据库默认使用的时区为CST，和当前时区不同。
3）解决方法：数据连接URL中增加参数 ?serverTimezone=Asia/Shanghai
#### 5.2.4 添加数据库表后不显示数据
1）现象：创建 MySQL 数据连接并添加数据库表，数据库中有数据但 FineBI 预览时没有数据。
2）解决方法：数据连接 URL 中增加参数 ?zeroDateTimeBehavior=convertToNull
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：Trino 数据连接](<index.php?doc-view-2000.html>)
[下一篇：IBM DB2数据连接 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-98.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
