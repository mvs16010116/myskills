---
title: JSON 数据集插件
doc_id: 489
url: https://help.fanruan.com/finebi/doc-view-489.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:08
version: "7.X"
---

> 1. 概述1.1 版本&nbsp;FineBI 版本新增功能6.0-1.2&nbsp;应用场景随着 JavaScript 的流行，JSON 格式的数据也被越来越广泛的使用，但是由于 JSON 格式的灵活

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# JSON 数据集插件
[__](<doc-edit-489.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[16](<edition-list-489.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-08-19 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 新增功能  
---|---  
6.0| -  
### 1.2 应用场景
随着 JavaScript 的流行，JSON 格式的数据也被越来越广泛的使用，但是由于 JSON 格式的灵活性，把这类数据结构和其他数据一起分析的时候，就会面临结构不统一导致无法分析的问题，在 FineBI 需要安装插件，本文详细介绍如何使用 JSON 数据集。 
### 1.3 功能简介
JSON 数据集插件可对 JSON 格式的数据进行处理，方便在 FineBI 中使用。  

## 2\. 插件介绍
### 2.1 安装插件
插件下载请点击：[JSON 数据集插件](<https://market.fanruan.com/plugin/6d1f2ca6-358a-4b0b-ac67-58e082d127dc>)
安装插件方法请参见：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html>)
### 2.2 定义 JSON 数据连接
1）以管理员身份进入数据决策系统，点击「管理系统>数据连接>数据连接管理>新建数据连接>所有」，可添加 JSON 数据连接，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
2）点击「JSON」，配置JSON数据连接。如下图所示：
帆软不提供在线json调试，仅提供本文示例json文件：[book.zip](<doc-download-/finebi6.X/uploads/file/20241218/book.zip> "下载资料")
请将book.json文件上传至你自己的服务器，生成可在线访问的链接。
![](https://help.fanruan.com/core/style/lod.png)
注：JSON 数据连接配置保存后，选中数据连接，点击右侧![](https://help.fanruan.com/core/style/lod.png)按钮，可修改数据连接名称。
注：如果数据量大，则需要在「网络连接」中修改连接池最大连接数。
设置项的详细说明如下表所示：
设置项|  说明  
---|---  
地址| 地址可以支持参数，和数据集一样，注意提供一个默认参数供设计的时候查询用注：支持 HTTP 和非自签名 SSL 证书的 HTTPS  
用户名密码| 输入用户名和密码进行认证，不需要认证就不填写  
请求类型 | GET 模式和 POST 模式的参数传递方式不一样，GET 是拼接到 URL 上，POST 是放到 HTTP 请求体中，并且 POST 模式的参数需要自己添加  
缓存有效期| 默认缓存时间为 0 ，表示不启用，且支持集群，可以有效的提升 JSON 数据集的效率  
注：V9.3.3 版本插件支持  
普通参数| 普通参数即放在 Body 中的，通常说的 GET 和 POST 即普通参数  
头参数| 头参数即放在 Head 里面的。常用不变的量一般都是走 header， 因为每次请求都带 header  
编码 | 如果文件是非 UTF-8 编码的，就需要在原始编码这一栏选择对应的编码，否则无法正确的解析文本信息  
  
需注意以下几点：
  * V9.3.3 版本的插件，脚本引擎支持自主选择 JavaScript V8 或者 Java（默认），在无法支持 JavaScript V8 的机器上自动使用 Java 版本的脚本引擎。
  * 添加参数类型取决于用户服务器需要接收什么类型的参数。
  * 建议用户获取参数时使用 .json 文件而不是单纯的接口。


### 2.3 新建 JSON 数据集
点击「服务器数据集>JSON数据集」，数据集名称为「JSON数据集」，选择创建的 JSON 数据连接，输入查询语句$.store.book[*]，点击「保存」按钮即可。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
设置项介绍如下表所示：
设置项| 说明| 本文示例  
---|---|---  
数据集名称| 用户可自定义，不可为空| JSON数据集  
数据连接名称| 选择已创建的 JSON 数据连接| 本文 3.1 节定义的JSON数据连接  
键排序| 是指对获取出来的列名做排序。默认即为不开启| 默认  
  
预读排名| 先遍历所有的数据，把列名获取出来，可用于 JSON 结构不整齐的情况，会稍微的降低效率。默认即为不开启| 默认  
查询语句| 输入查询语句| $.store.book[*]查询出书店中所有的书信息，查询结果如下图所示：![](https://help.fanruan.com/core/style/lod.png)注：$.store.book[*] 是 JSON 的固定引用方式，代表取出 store 下 book 的全部数据  
$.store.book[*].category 取出 category 列的数据，查询结果如下图所示：![](https://help.fanruan.com/core/style/lod.png)  
$.store.book[?(@.price<10)]取出价格小于 10 的书籍，查询结果如下图所示：![](https://help.fanruan.com/core/style/lod.png)  
### 2.4 传参方式介绍
三种传参方式区别如下表所示：
模式| 传递方式  
---|---  
GET| 拼接到 URL 上  
POST_FORM| 需要传的是 key-value，可以添加动态参数  
POST_RAW| 只要 value 就可以了，可以添加动态参数  
传参方式具体介绍请参见：[JSON 数据集插件](<https://help.fanruan.com/finereport/doc-view-1985.html>) 的 2.3 节内容。
## 3\. JSON 程序数据集
使用 JavaScript 脚本，将 JSON 对象转换为二维表。这种方式可以解决所有不能直接用 JSON 数据集的场景，可以根据用户自己的数据结构定制脚本，从而实现和报表的对接。
注： 新建和使用 JSON 程序数据集，需要使用 2019-04-03 及以后版本的 JAR 包，插件需要更新到 9.2.3 及以后版本。
### 3.1 新建 JSON 程序数据集
以管理员身份进入数据决策系统，点击「管理系统>数据连接>服务器数据集>JSON程序数据集」，数据集名称为「JSON程序数据集」，选择创建的 JSON 数据连接，输入脚本语句，点击「保存」按钮即可。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.2 取出所有语句
获取所有书籍的数据，脚本语句如下所示：
[code]
    var books = $.store.book;  
    var rowCount = books.length;  
    console.log("行数为:" + rowCount);  
    var table = [];  
    var column = [];  
    books.forEach(function(value, index) {  
        var row = [];  
        for (var key in value) {  
            row.push(value[key]);  
            column.push(key);  
        }  
        console.log("该行共有" + row.length + "列");  
        table.push(row);  
    });  
    return merge(table, unique(column))  
    
[/code]
脚本中内置函数和变量的说明如下表所示：
内置函数和变量|  含义  
---|---  
$|  表示 JSON 内容的对象  
unique(array)|  将数组进行去重，主要用于列名处理  
console.log(info)|  输出调试信息，会在日志文件中输出 INFO 级别的信息  
console.error(err)|  输出错误级别的信息，会在日志文件中输出 ERROR 级别的信息  
merge(table, column)|  合并数据集的内容和列名对象  
books.forEach  
|  JS 遍历数组方法  
查询出的数据如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.3 条件取数
取出价格小于 10 的书籍数据，脚本语句如下所示：
[code]
    var books = $.store.book;  
    var rowCount = books.length;  
    var table = [];  
    var column = [];  
    books.forEach(function(value, index) {  
        var row = [];  
        if (value.price < 10) {  
          for (var key in value) {  
            row.push(value[key]);  
            column.push(key);  
          }  
          table.push(row);  
        }  
    });  
       
    return merge(table, unique(column));  
      
    
[/code]
查询出的数据如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
### 3.4 取出其中某一列
取出所有书籍的作者集合，脚本语句如下所示：
[code]
    var books = $.store.book;  
    var rowCount = books.length;  
    var table = [];  
    var column = ["author"];  
    books.forEach(function(value, index) {  
        var row = [];  
        row.push(value.author);  
        table.push(row);  
    });  
       
    return merge(table, column);  
    
[/code]
查询出的数据如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 使用JSON数据集/程序数据集
1）以管理员身份进入数据决策系统，[添加数据库表](<https://help.fanruan.com/finebi7.0/doc-view-887.html>)  

2）点击「服务器数据集」，可添加已创建的JSON数据集/程序数据集，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
注：此处 JSON 数据若包含多种数据类型，则在前端使用中可能会有报错，建议尽量将数据处理成数据类型一致使用。 
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：阿里云Hologres数据连接](<index.php?doc-view-1347.html>)
[下一篇：新SAP BW数据集插件 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-256.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
