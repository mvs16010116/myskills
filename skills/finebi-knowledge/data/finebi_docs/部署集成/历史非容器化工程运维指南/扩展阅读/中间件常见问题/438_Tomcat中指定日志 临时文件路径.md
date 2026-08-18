---
title: Tomcat中指定日志/临时文件路径
doc_id: 438
url: https://help.fanruan.com/finebi6.X/doc-view-438.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:50
---

> 1. 自定义日志存储路径应用场景：工程部署到 Tomcat 环境下，日志文件默认存储在%Tomcat_HOME%\logs路径下，但部分用户希望自定义日志存储路径。由于启动位置不在 Tomcat 的

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Tomcat中指定日志/临时文件路径
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[4](<edition-list-438.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2023-06-15 
[](<javascript:;>) [](<javascript:>)
## 1\. 自定义日志存储路径
**应用场景：**  

  * 工程部署到 Tomcat 环境下，日志文件默认存储在%Tomcat_HOME%\logs路径下，但部分用户希望自定义日志存储路径。
  * 由于启动位置不在 Tomcat 的 bin 目录下，fanruan.log 有时候在 Tomcat 的 logs 目录下找不到，希望自定义日志存储路径。


**实现思路：**  

在%Tomcat_HOME%\webapps\webroot\WEB-INF\lib路径下，将 fine-core-11.0.jar 文件解压到其他文件夹中。
修改com\fr\general\log\log4j2.xml文件中的路径，然后将修改后的 log4j2.xml 文件放到%Tomcat_HOME%\webapps\webroot\WEB-INF\config路径下，重启工程即可。
### 1.1 查找日志路径
1）执行命令：jcmd pid VM.system_properties，Linux 和 Windows 通用。如下图所示：
注：「pid」 为工程进程号。
![](/core/style/lod.png)
2）找到user.dir，该路径是启动位置，该启动位置的上级路径下就有 logs 文件夹。如下图所示：
![](/core/style/lod.png)
如果user.dir=/，说明是在根目录下启动的，logs 也就是在根目录下
### 1.2 解压 fine-core-11.0.jar 文件
1）在%Tomcat_HOME%\webapps\webroot\WEB-INF\lib路径下，找到 fine-core-11.0.jar 文件，将该文件解压到其他文件夹中，如下图所示：
![1638157582912185.png](/core/style/lod.png)
2）解压文件夹进入com\fr\general\log\目录下，找到 log4j2.xml 文件，如下图所示：
![1656492366296029.png](/core/style/lod.png)
### 1.3 修改日志输出路径
1）编辑 log4j2.xml 文件，修改fileName="${sys:LOG_HOME}/../logs/fanruan.log" 这一行即可。如下图所示：
![](/core/style/lod.png)
2）然后把文件放到%Tomcat_HOME%\webapps\webroot\WEB-INF\config下，如下图所示：
![](/core/style/lod.png)
3）重启工程即可生效。
## 2\. 自定义临时文件存储路径
**应用场景：**  

  * 工程部署到 Tomcat 环境下，临时文件一般保存在%Tomcat_HOME%\temp路径下，但部分用户希望自定义临时文件存储路径。
  * 服务器在运行过程中，会遇到 Java io 操作的临时目录满了，此时需要修改Java 的临时目录。  



**实现思路：**
CATALINA_TMPDIR是Tomcat中用于存储临时文件的目录路径。
Linux 环境中，修改%Tomcat_HOME%\bin路径下的 setenv.sh 文件中的临时目录路径
Windows 环境中，修改%Tomcat_HOME%\bin路径下的 setenv.bat 文件中的临时目录路径
修改路径后，重启工程即可。
### 2.1 Linux
1）进入%Tomcat_HOME%\bin目录。寻找名为setenv.sh的文件。如果文件不存在，可以创建一个新的setenv.sh文件。
注：请确保setenv.sh文件具有可执行权限。如果没有可执行权限，可以使用以下命令进行设置：chmod +x setenv.sh
2）使用文本编辑器打开setenv.sh文件。在文件中添加以下行来设置CATALINA_TMPDIR环境变量，并替换为你想要使用的新的临时目录路径：
注：请确保此路径为有效的目录路径。请确保Tomcat用户具有必要的权限来访问和写入该目录。
export CATALINA_TMPDIR=/path/to/new/tmpdir
3）保存并关闭setenv.sh文件。  

4）重启Tomcat服务器以使修改生效。
### 2.2 Windows
1）进入%Tomcat_HOME%\bin目录。寻找名为setenv.bat的文件。如果文件不存在，可以创建一个新的setenv.bat文件。
2）使用文本编辑器打开setenv.sh文件。在文件中添加以下行来设置CATALINA_TMPDIR环境变量，并替换为你想要使用的新的临时目录路径：
注：请确保此路径为有效的目录路径，并且使用反斜杠（\）作为目录分隔符。请确保Tomcat用户具有必要的权限来访问和写入该目录。
set "CATALINA_TMPDIR=C:\path\to\new\tmpdir"
3）保存并关闭setenv.bat文件。  

4）重启Tomcat服务器以使修改生效。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Resin服务器内存修改](<index.php?doc-view-667.html>)
[下一篇：JAVA环境变量常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-1374.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
