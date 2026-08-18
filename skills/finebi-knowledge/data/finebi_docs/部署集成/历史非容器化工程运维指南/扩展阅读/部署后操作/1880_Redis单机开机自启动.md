---
title: Redis单机开机自启动
doc_id: 1880
url: https://help.fanruan.com/finebi6.X/doc-view-1880.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:38
---

> 虽然使用命令行可以对redis进行各种操作，比如启动等，但是还是不太方便，本文介绍在Linux下安装Redis后，如何设置其开机自启动。1. CentOS6.x&amp;RedHat6.x 配置 Red

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Redis单机开机自启动
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
* 历史版本：[1](<edition-list-1880.html>)
[](<javascript:;>) [](<javascript:>)
虽然使用命令行可以对redis进行各种操作，比如启动等，但是还是不太方便，本文介绍在Linux下安装Redis后，如何设置其开机自启动。
## 1\. CentOS6.x&RedHat6.x 配置 Redis 开机自启动
### 1.1 创建 Redis 的管理脚本
首先，在系统的/etc/init.d/目录下创建 redis 文件：
[code]
    vi /etc/init.d/redis  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    #!/bin/sh  
    # chkconfig: 2345 10 90   
    # description: Start and Stop redis  
    REDISPORT=7379  
    EXEC=/usr/redis/redis-5.0.4/src/redis-server  
    CLIEXEC=/usr/redis/redis-5.0.4/src/redis-cli  
    PIDFILE=/var/run/redis_${REDISPORT}.pid  
    CONF="/usr/redis/redis-5.0.4/redis.conf"  
    case "$1" in  
      start)  
        if [ -f $PIDFILE ]  
        then  
            echo "$PIDFILE exists, process is already running or crashed"  
        else  
            echo "Starting Redis server..."  
            $EXEC $CONF &  
        fi  
        ;;  
      stop)  
        if [ ! -f $PIDFILE ]  
        then  
            echo "$PIDFILE does not exist, process is not running"  
        else  
            PID=$(cat $PIDFILE)  
            echo "Stopping ..."  
            $CLIEXEC -p $REDISPORT shutdown  
            while [ -x /proc/${PID} ]  
            do  
              echo "Waiting for Redis to shutdown ..."  
              sleep 1  
            done  
            echo "Redis stopped"  
        fi  
        ;;  
      restart)  
        "$0" stop  
        sleep 3  
        "$0" start  
        ;;  
      *)  
        echo "Please use start or stop or restart as first argument"  
        ;;  
    esac  
    
[/code]
注意，对于自定义编译安装的 Redis（帮助文档中提供的即是此种方式），需要根据安装路径修改脚本中这几项配置：
[code]
    EDISPORT=7379 ====>默认为7379，若有调整请修改为实际的端口号  
    EXEC=/usr/redis/redis-5.0.4/src/redis-server ====>Redis 服务的启动路径  
    CLIEXEC=/usr/redis/redis-5.0.4/src/redis-cli ====>Redis 客户端的启动路径  
    CONF="/usr/redis/redis-5.0.4/redis.conf" ====>配置文件路径  
    
[/code]
保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /etc/init.d/redis  
    
[/code]
然后，就可以通过该脚本对 Redis 服务进行管理了：
[code]
    /etc/init.d/redis start  
    /etc/init.d/redis stop  
    
[/code]
### 1.2 使用 chkconfig 设置开机自启动
上面的步骤完成了用脚本管理 Redis 服务的功能，接下来我们就可以使用 chkconfig 来设置 Redis 开机启动了。
先将 Redis 服务加入 chkconfig 管理列表：
[code]
    chkconfig --add /etc/init.d/redis  
    
[/code]
配置完以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    chkconfig redis on     #设置开机自启动  
    chkconfig redis off    #停止开机自启动  
    service redis start    #启动redis服务  
    service redis stop     #停止redis服务  
    service redis restart  #重启redis服务  
    
[/code]
## 2\. CentOS7.x&RedHat7.x 配置 redis 开机自启动
### 2.1 创建 Redis 的管理脚本
首先，在系统的/lib/systemd/system/目录下创建 redis.service 文件：
[code]
    vi /lib/systemd/system/redis.service  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    [Unit]  
    Description=The redis-server Process Manager  
    After=syslog.target network.target  
    [Service]  
    Type=forking  
    PIDFile=/var/run/redis_7379.pid  
    ExecStart=/usr/redis/redis-5.0.4/src/redis-server /usr/redis/redis-5.0.4/redis.conf  
    ExecReload=/bin/kill -USR2 $MAINPID  
    ExecStop=/bin/kill -SIGINT $MAINPID   
    [Install]  
    WantedBy=multi-user.target  
    
[/code]
注意，对于自定义编译安装的 Redis（帮助文档中提供的即是此种方式），需要根据实际路径修改脚本中的 Redis启动路径“/usr/redis/sbin/redis”。
保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /lib/systemd/system/redis.service  
    
[/code]
### 2.2 使用 systemctl 设置开机自启动
配置完脚本以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    systemctl enable redis.service          #设置开机自启动  
    systemctl disable redis.service         #停止开机自启动  
    systemctl start redis.service　         #启动 Redis 服务  
    systemctl stop redis.service　          #停止服务  
    systemctl status redis.service          #查看服务当前状态  
    systemctl list-units --type=service     #查看所有已启动的服务
[/code]
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Redis集群开机自启动](<index.php?doc-view-1879.html>)
[下一篇：Windows下Tomcat开机自启动 ![](/core/style/forward.png) ](<index.php?doc-view-1881.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
