---
title: 清理Tomcat日志文件
doc_id: 2220
url: https://help.fanruan.com/finebi6.X/doc-view-2220.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:46
---

> 1. 问题描述帆软应用部署在Tomcat服务器上，随着运行时间的增加，会产生大量的日志文件，如果不及时清理，会对系统的稳定性造成一定影响。2. 解决方案2.1 方案一：修改日志输出级别打开%TOMCAT

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 清理Tomcat日志文件
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[1](<edition-list-2220.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 问题描述
帆软应用部署在Tomcat服务器上，随着运行时间的增加，会产生大量的日志文件，如果不及时清理，会对系统的稳定性造成一定影响。
## 2\. 解决方案
### 2.1 方案一：修改日志输出级别
打开%TOMCAT_HOME%/conf/logging.properties配置文件，修改以下语句以提高输出日志的级别。
一般日志的级别： SEVERE (highest value) > WARNING > INFO > CONFIG > FINE > FINER > FINEST (lowest value)
建议将日志级别提升到 WARNING 或以上，也可以设置成 OFF，直接禁用掉。
[code]
    1catalina.org.apache.juli.FileHandler.level = WARNING    
    1catalina.org.apache.juli.FileHandler.directory = ${catalina.base}/logs    
    1catalina.org.apache.juli.FileHandler.prefix = catalina.    
        
    2localhost.org.apache.juli.FileHandler.level = WARNING    
    2localhost.org.apache.juli.FileHandler.directory = ${catalina.base}/logs    
    2localhost.org.apache.juli.FileHandler.prefix = localhost.    
        
    3manager.org.apache.juli.FileHandler.level = FINE    
    3manager.org.apache.juli.FileHandler.directory = ${catalina.base}/logs    
    3manager.org.apache.juli.FileHandler.prefix = manager.    
        
    4host-manager.org.apache.juli.FileHandler.level = FINE    
    4host-manager.org.apache.juli.FileHandler.directory = ${catalina.base}/logs    
    4host-manager.org.apache.juli.FileHandler.prefix = host-manager.    
        
    java.util.logging.ConsoleHandler.level = WARNING    
    java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter  
    
[/code]
### 2.2 方案二：禁用项目访问日志
打开 %TOMCAT_HOME%/conf/server.xml 文件，注释掉以下代码，以禁用项目访问日志。
[code]
    <Valve className="org.apache.catalina.valves.AccessLogValve"    
             directory="logs"  prefix="localhost_access_log." suffix=".txt"    
             pattern="common" resolveHosts="false"/>  
    
[/code]
### 2.3 方案三：降低同步用户频率
[同步用户](<https://help.fanruan.com/finereport/doc-view-704.html>) 的「同步频率」不宜过高，否则会导致后台日志不断刷新，日志体积不断膨胀。
![](/core/style/lod.png)
### 2.4 方案四：定期清理日志文件
Tomcat 服务器下生成的日志文件主要有4种，一般存放在%TOMCAT_HOME%\logs目录下：  

  * catalina.log：表示引擎的日志文件
  * localhost.log：表示 Tomcat 下内部代码丢出的日志
  * manager.log：表示默认 manager 应用日志
  * host-manager.log：表示虚拟主机方面的日志


建议根据自身工程运行情况，定期清理X天前的日志，可设置清理脚本，具体方法建议百度。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows服务器设置出入站规则](<index.php?doc-view-1371.html>)
[下一篇：Tomcat部署相关问题 ![](/core/style/forward.png) ](<index.php?doc-view-47.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
