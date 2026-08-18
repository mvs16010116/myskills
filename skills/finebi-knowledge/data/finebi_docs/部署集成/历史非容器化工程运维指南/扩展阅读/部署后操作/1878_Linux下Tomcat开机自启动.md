---
title: Linux下Tomcat开机自启动
doc_id: 1878
url: https://help.fanruan.com/finebi6.X/doc-view-1878.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:36
---

> 1. 概述本文介绍 Linux 系统安装 Tomcat 后，设置开机自启动的方法。注：Tomcat 设置开机自启动后，日志路径会变化，建议指定日志路径。指定日志路径文档请参见：Tomcat 中指定日志/

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux下Tomcat开机自启动
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Leo.Tsai](<user-space-238588.html>)_
* 历史版本：[6](<edition-list-1878.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-08-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文介绍 Linux 系统安装 Tomcat 后，设置开机自启动的方法。  

注：Tomcat 设置开机自启动后，日志路径会变化，建议指定日志路径。指定日志路径文档请参见：[Tomcat 中指定日志/临时文件路径](<https://help.fanruan.com/finebi6.X/doc-view-438.html>)
## 2\. Ubuntu16.04及之前&CentOS6.x&RedHat6.x配置 Tomcat 开机自启动
### 2.1 创建 Tomcat 的管理脚本
1）首先，在系统的/etc/init.d/目录下创建tomcat文件：
[code]
    vi /etc/init.d/tomcat  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    #!/bin/bash   
    # tomcat startup script for the Tomcat server   
    # chkconfig: 35 80 20   
    # description: start the tomcat deamon   
    #prog=tomcat   
    #EDISPORT=8080   
    #默认为 8080，若有调整请修改为实际的端口号  
    #EXEC=/usr/tomcat/bin/startup.sh   
    #tomcat 容器的启动路径  
    #CONF="/usr/tomcat/bin/catalina.sh"   
    #配置文件路径  
    #<---------------jdk--------------->#  
    #. /etc/rc.d/init.d/functions  
    #prog=tomcat   
    #JAVA_HOME=/usr/jdk/jdk1.8.0_181  
    #export CLASSPATH=$CLASSPATH:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.  
    #export PATH=$PATH:$JAVA_HOME/bin  
    #export JAVA_HOME#CATALANA_HOME=/usr/tomcat/  
    #export CATALINA_HOME  
    #<---------------jdk--------------->#  
    CATALANA_HOME=/usr/tomcat/  
    export CATALINA_HOME  
    case "$1" in start)   
    echo "Starting Tomcat..."  
    $CATALANA_HOME/bin/startup.sh   
    ;;   
    stop)   
    echo "Stopping Tomcat..."  
    $CATALANA_HOME/bin/shutdown.sh   
    ;;   
    restart)   
    echo "Stopping Tomcat..."  
    $CATALANA_HOME/bin/shutdown.sh   
    sleep 2   
    echo  
    echo "Starting Tomcat..."  
    $CATALANA_HOME/bin/startup.sh   
    ;;   
    *)   
    echo "Usage: $prog {start|stop|restart}"  
    ;;   
    esac   
    exit 0  
    
[/code]
对于自定义编译安装的 Tomcat（帮助文档中提供的即是此种方式），需要根据安装路径修改脚本中这几项配置：
[code]
    CATALANA_HOME=/usr/tomcat/ ====> tomcat/bin/目录下 catalana.sh 的根目录  
    
[/code]
2）保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /etc/init.d/tomcat  
    
[/code]
3）然后，就可以通过该脚本对 tomcat 服务进行管理了：
[code]
    /etc/init.d/tomcat start  
    /etc/init.d/tomcat stop  
    
[/code]
### 2.2 使用 chkconfig 设置开机自启动
1）上面的步骤完成了用脚本管理 Tomcat 服务的功能，接下来我们就可以使用 chkconfig 来设置 Tomcat 开机启动了。
先将 Tomcat 服务加入 chkconfig 管理列表：
[code]
    chkconfig --add /etc/init.d/tomcat  
    
[/code]
2）配置完以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    chkconfig tomcat on     # 设置开机自启动  
    chkconfig tomcat off    # 停止开机自启动  
    service tomcat start    # 启动 tomcat 服务  
    service tomcat stop     # 停止 tomcat 服务  
    service tomcat restart  # 重启 tomcat 服务  
    
[/code]
## 3\. Ubuntu16.10及之后&CentOS7.x&RedHat7.x配置 Tomcat 开机自启动
### 3.1 创建 Tomcat 的管理脚本
1）首先，在系统的/usr/lib/systemd/system/目录下创建tomcat.service文件：
[code]
    vi /usr/lib/systemd/system/tomcat.service  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    [Unit]  
    Description=tomcat service  
    After=network.target  
    [Service]  
    Type=forking  
    ExecStart=/usr/tomcat/bin/startup.sh  
    ExecReload=/usr/tomcat/bin/startup.sh -s reload  
    ExecStop=/usr/tomcat/bin/shutdown.sh  
    PrivateTmp=true  
    [Install]  
    WantedBy=multi-user.target  
    
[/code]
注：需要根据实际路径修改脚本中的 Tomcat 安装路径「/usr/tomcat」。
2）保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /usr/lib/systemd/system/tomcat.service  
    
[/code]
### 3.2 指定 Tomcat 的启动 JRE 路径
1）编辑 Tomcat 的 bin 目录下 setclasspath.sh 文件：
[code]
    vi /usr/tomcat/bin/setclasspath.sh   #自己的tomcat路径  
    
[/code]
注：正常这个文件是有内容的，如果没有内容，请编辑 Tomcat/bin/setenv.sh。如果文件不存在，可以创建一个新的setenv.sh文件。
2）增加 JRE 环境变量：
[code]
    export JAVA_HOME=/usr/local/java/jdk1.8.0_151 #自己的java路径  
    export JRE_HOME=/usr/local/java/jdk1.8.0_151/jre #自己的jre路径  
    
[/code]
加入后效果：
![20161018141757039.png](/core/style/lod.png)
保存，退出。
### 3.3 使用 systemctl 设置开机自启动
配置完脚本以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    systemctl enable tomcat.service          # 设置开机自启动  
    systemctl disable tomcat.service         # 停止开机自启动  
    systemctl start tomcat.service　         # 启动 tomcat 服务  
    systemctl stop tomcat.service　          # 停止服务  
    systemctl status tomcat.service          # 查看服务当前状态  
    systemctl list-units --type=service    # 查看所有已启动的服务
[/code]
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Resin下通过IP直接进入平台系统界面](<index.php?doc-view-666.html>)
[下一篇：Redis集群开机自启动 ![](/core/style/forward.png) ](<index.php?doc-view-1879.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
