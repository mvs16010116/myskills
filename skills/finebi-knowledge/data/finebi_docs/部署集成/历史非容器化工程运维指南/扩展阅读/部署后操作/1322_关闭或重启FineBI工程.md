---
title: 关闭或重启FineBI工程
doc_id: 1322
url: https://help.fanruan.com/finebi6.X/doc-view-1322.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:40
---

> 适用范围说明本文仅适用于非运维平台部署的&nbsp;FineBI&nbsp;工程。运维平台部署的工程，请通过运维平台进行关闭、启动、重启操作，详情请参见：组件管理1.&nbsp;概述1.1 版本Fine

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 关闭或重启FineBI工程
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[9](<edition-list-1322.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2026-04-07 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)**适用范围说明**
本文仅适用于**非运维平台部署** 的 FineBI 工程。
运维平台部署的工程，请通过运维平台进行关闭、启动、重启操作，详情请参见：[组件管理](<https://help.fanruan.com/fineops/doc-view-44.html>)
  

## 1\. 概述
### 1.1 版本
FineBI服务器版本| 功能变更  
---|---  
6.X  
| -  
### 1.2 应用场景
以下情况需要参考本文执行工程关闭或重启操作：
  * 需要重启工程以使配置变更生效
  * 需要完全关闭工程相关进程后再执行重启


### 1.3 文档说明
本文提供在 Linux 系统中，关闭和重启以下三种容器内 FineBI 工程的操作方法：
  * Tomcat
  * WebLogic
  * WebSphere


### 1.4 其他说明
1）部署在Tomcat、WebLogic、WebSphere、JBoss、Resin中间件中的工程，可通过关闭中间件，直接关闭工程
2）部署在中间件中的工程，若因用户操作不当等原因导致系统中存在残留线程，工程启动时，检测到残留线程后，将以平台消息的方式提示超管，通知内容如下所示：
  * 单机：检测到XXX号进程可能存在进程残留，为不影响当前应用正常运行，建议及时检查确认
  * 集群：检测到XXXXX（节点地址）节点下XXX号进程可能存在进程残留，为不影响当前应用正常运行，建议及时检查确认


## 2\. Tomcat 容器
示例：以下示例中，工程部署路径为 /home/wendy/tomcat-linux，请根据实际部署路径替换。
### 2.1 关闭工程
**步骤一：优化配置文件**
关闭工程前，建议对以下两个文件进行优化，以确保关闭操作更加可靠。
  * ${tomcat}/bin/catalina.sh文件：在该行PRGDIR=`dirname "$PRG"`下面新增一行内容CATALINA_PID=./CATALINA_PID
  * ${tomcat}/bin/shutdown.sh文件：最后一行改成exec "$PRGDIR"/"$EXECUTABLE" stop -force "$@"


**步骤二：执行关闭脚本**
使用 Tomcat 自带的 shutdown.sh 脚本关闭容器：
注：/home/wendy/tomcat-linux 为示例路径，请替换为工程的实际部署路径。
cd /home/wendy/tomcat-linux/bin
./shutdown.sh
### 2.2 清理遗留进程
执行 shutdown.sh 后，可能存在未完全退出的遗留进程，需手动清理。
1）查看工程相关进程：
注：tomcat-linux 为示例路径中的目录名，请替换为实际部署路径中对应的目录名。
ps -ef | grep tomcat-linux
![](/core/style/lod.png)
2）根据查询结果，逐一终止所有工程相关进程（将 <PID> 替换为实际进程号）：
kill -9 <PID>
![](/core/style/lod.png)
3）再次执行查询命令，确认所有相关进程已清除：
注：tomcat-linux 为示例路径中的目录名，请替换为实际部署路径中对应的目录名。
ps -ef | grep tomcat-linux
### 2.3 重启工程
1）进入工程 bin 目录，执行启动脚本：
注：/home/wendy/tomcat-linux 为示例路径，请替换为工程的实际部署路径。
cd /home/wendy/tomcat-linux/bin
./startup.sh
![](/core/style/lod.png)
2）查看实时日志，确认重启结果：
注：/home/wendy/tomcat-linux 为示例路径，请替换为工程的实际部署路径。
cd /home/wendy/tomcat-linux/logs
tail -f catalina.out
日志中出现类似以下内容，表示重启成功：
![](/core/style/lod.png)
## 3\. WebLogic 容器
### 3.1 关闭工程
1）查看工程相关进程：
ps -ef | grep weblogic
![](/core/style/lod.png)
2）根据查询结果，逐一终止所有工程相关进程（将 <PID> 替换为实际进程号）：
kill -9 <PID>
3）再次执行查询命令，确认所有相关进程已清除：
ps -ef | grep weblogic
![](/core/style/lod.png)
### 3.2 重启工程
1）进入 startWebLogic.sh 所在目录，以后台方式启动工程：
注：/web/weblogic/Oracle/Middleware/user_projects/domains 为示例路径，请替换为工程的实际部署路径。
cd /web/weblogic/Oracle/Middleware/user_projects/domains
nohup ./startWebLogic.sh &
2）验证工程已成功启动：
ps -ef | grep weblogic
查询结果中出现 WebLogic 相关进程，表示重启成功。
![](/core/style/lod.png)
## 4\. WebSphere 容器
### 4.1 关闭工程
1）查看工程相关进程：
ps -ef | grep WebSphere
![](/core/style/lod.png)
2）根据查询结果，逐一终止所有工程相关进程（将 <PID> 替换为实际进程号）：
kill -9 <PID>
![](/core/style/lod.png)
3）再次执行查询命令，确认所有相关进程已清除：
ps -ef | grep WebSphere
### 4.2 重启工程
1）进入 startServer.sh 所在目录：
注：/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin 为示例路径，请替换为工程的实际部署路径。
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
2）启动应用程序服务器（将 server1 替换为实际的服务器名称）：
./startServer.sh server1
3）验证工程已成功启动：
ps -ef | grep websphere
查询结果中出现 WebSphere 相关进程，表示重启成功。
![](/core/style/lod.png)
注：应用程序服务器名称（即上文的 server1 ），可在控制台查看。
![](/core/style/lod.png)
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux中启动FineBI](<index.php?doc-view-24.html>)
[下一篇：服务器部署向导页面介绍 ![](/core/style/forward.png) ](<index.php?doc-view-1268.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
