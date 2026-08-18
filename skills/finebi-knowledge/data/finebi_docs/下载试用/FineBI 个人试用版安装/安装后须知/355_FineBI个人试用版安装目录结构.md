---
title: FineBI个人试用版安装目录结构
doc_id: 355
url: https://help.fanruan.com/finebi6.X/doc-view-355.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 14:57:30
---

> 1. 概述在 FineBI 安装完成以后，进入安装目录可以看到安装文件。FineBI 安装文件本质上就是一个 Tomcat 。本文详细介绍安装目录结构。2. 安装根目录每个文件存放的内容如下表所示：文件

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI个人试用版安装目录结构
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[33](<edition-list-355.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-02-26 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
在 FineBI 安装完成以后，进入安装目录可以看到安装文件。FineBI 安装文件本质上就是一个 Tomcat 。本文详细介绍安装目录结构。
## 2\. 安装根目录
![2023-01-13_11-29-08.png](/core/style/lod.png)
每个文件存放的内容如下表所示：
文件| 内容  
---|---  
.install4j| FineBI 的图片  
bin| 
  * BI 工程启动文件所在的目录，其中可以在 finebi.vmoptions 中修改 BI 分配的内存大小和编码方式
  * 这个目录下的 ROOT 文件夹下是所有的数据表以及临时数据表，也是默认进行数据更新存放位置，可自行调整位置，详情参见：[数据更新构成与存放](<https://help.fanruan.com/finebi6.0/doc-view-383.html>)
  * 这个目录下的 output.log 存放的是访问前端时输出的信息概况
  * bin 下面的 log 相关文件可以清理

  
jre| 是在 Java 运行环境下支持 Java 应用程序  
lib| 存放 BI 启动的时候的加载动画的 JAR 包  
logs| 包含工程运行日志、GC日志注：清空一般不会对运行带来影响。  
server| Tomcat 的根目录，包含 Tomcat 的配置文件夹以及 Tomcat 自带的依赖文件夹  
temp| 
  * 存放 Tomcat 运行过程中产生的临时文件
  * 同时为导出 Excel 文件的缓存路径，可在 %FineBI%/bin 目录下的 finebi.vmoptions 文件中通过修改参数Djava.io.tmpdir=.\temp 来自行修改缓存存放位置
  * 可以在工程停机后删除文件夹，释放内存  


注：temp 临时目录在工程运行时不建议做清理，需要在工程停机时清理，如果清理后提示报错需要工程重启  
webapps| 存放应用程序，当服务启动时会去加载 webapps 目录下的应用程序  
LICENSE| 许可证，里面记录了 Tomcat 的一些条款等等  
NOTICE| 记录 Tomcat 的新的通知，公告  
RELEASE-NOTES| 记录的是发行版本的说明，一些捆绑的 API ，新特性等等  
RUNNING.txt| 记录 Tomcat 的运行环境以及怎样配置参数，变量，启动等等  
uninstall.exe| 自带卸载 exe ，双击即可调用卸载功能  
## 3\. webroot 目录
![2023-01-13_13-33-46.png](/core/style/lod.png)
每个文件存放的内容如下表所示：
文件| 内容  
---|---  
bi-data| bi抽取数据的文件夹  
Demo_files| 存放工程自带的 DEMO 展示需要的文件  
logs| 存放日志文件，记录系统登录信息、模板访问信息、报错信息等  
WEB-INF| BI 工程主目录  
Web组件.html| 这是一个 Web 组件，写入的超链接地址即可。比如这是一个自定义的 HTML 文件，内置在工程内部 %/webroot/这个目录之下  
## 4\. WEB-INF 目录
![2023-01-13_13-35-12.png](/core/style/lod.png)
每个文件存放的内容如下表所示：
文件| 内容  
---|---  
assets| 资源文件夹，存放工程用到的资源文件等其中 temp_attach 中存放着上传的图片和 Excel 数据。  
assist| 辅助文件夹，存放一些辅助文件  
classes| class 文件存放目录  
embed| 内置数据库配置目录  
lib| BI 工程依赖的 JAR 包文件夹  
reportlets| 存放 FineReport 报表 cpt 、frm文件  
resources| 存放工程相关的资源配置文件  
treasures| 包含报表的功能点及 BI 的埋点信息，正常情况下一个月会自动生成一次  
## 5\. resources 目录
![2023-06-09_17-51-20.png](/core/style/lod.png)
每个文件存放的内容如下表所示：
文件| 内容  
---|---  
certificates| 放数据源SSH或者SSL的证书  
direct| 存放实时数据相关配置信息  
cpu.xml| CPU 开关，处理 sigard 导致 JVM 虚拟机崩溃问题时使用  
FanRuan.lic| 工程证书文件  
## 6\. backup 目录
![2024-02-26_10-28-00.png](/core/style/lod.png)
放置[备份还原](<https://help.fanruan.com/finebi6.X/doc-view-400.html?source=4>)的文件，如下图所示：
文件  
| 内容  
---|---  
config| 存储平台配置文件的备份  
jar  
| 存储FineBI jar包的备份  
plugins  
| 存储平台安装的插件的备份  
reportlets  
| 存储报表模板的备份  
## 7\. 注意事项
### 7.1 error.log 文件介绍
部分用户工程的%FineBI_HOME%\bin目录中存在 error.log 文件，该文件不会根据日期进行拆分，记录所有日期 error 级别的日志和一些相关的 info 信息。
若用户觉得该文件占用磁盘空间过大，可手动删除、写脚本定时删除或者写脚本监控大小删除。
注1：建议确认 fanruan.log 日志已够用，再考虑是否删除 error.log 文件。
注2：若工程部署在 Tomcat 的容器中，bin 目录下不会有 error.log 文件。
### 附件列表 
  
下载次数：：0
    
**主题：** [下载试用](<category-view-541>)
[![](/core/style/back.png)上一篇：FineBI个人试用版端口开放列表](<index.php?doc-view-359.html>)
[下一篇：生成安全密钥文件按钮说明 ![](/core/style/forward.png) ](<index.php?doc-view-996.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
