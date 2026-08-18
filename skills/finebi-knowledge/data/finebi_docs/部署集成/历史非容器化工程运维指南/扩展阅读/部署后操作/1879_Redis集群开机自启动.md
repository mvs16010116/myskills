---
title: Redis集群开机自启动
doc_id: 1879
url: https://help.fanruan.com/finebi6.X/doc-view-1879.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:37
---

> 1. 创建 Redis 集群的管理脚本&nbsp;redis-cluster 文件修改说明：请根据实际情况修改配置文件中的以下圈红内容&nbsp;redis-cluster&nbsp;文件配置说明：#!

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Redis集群开机自启动
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
* 历史版本：[1](<edition-list-1879.html>)
[](<javascript:;>) [](<javascript:>)
## 1\. 创建 Redis 集群的管理脚本
redis-cluster 文件修改说明：
请根据实际情况修改配置文件中的以下圈红内容
![60.png](/core/style/lod.png)  

redis-cluster 文件配置说明：
[code]
    #!/bin/sh  
    # chkconfig:   2345 90 10  
    # description:  Redis is a persistent key-value database  
       
    # 相关配置项，应该根据实际环境信息进行改动，包括for循环中的PIDFILE和CONF  
    REDISPORT=(7000 7001 7002 7003 7004 7005)  
    EXEC=/usr/local/bin/redis-server  
    CLIEXEC=/usr/local/bin/redis-cli  
    # redis集群密码，如未设置密码，该配置项可去除，第43行中redis集群关闭指令也需要做相应修改  
    PASSWD=admin123456  
       
    for((i=0;i<${#REDISPORT[@]};i++)) do  
        PIDFILE=/var/run/redis_${REDISPORT[i]}.pid # 进程守护文件  
        CONF=/usr/local/redis_cluster/${REDISPORT[i]}/redis.conf # redis节点配置文件  
           
        case "$1" in  
            start)  
                if [ -f $PIDFILE ]  
                then  
                        echo "$PIDFILE exists, process is already running or crashed"  
                else  
                        echo "Starting Redis cluster server ${REDISPORT[i]} ..."  
                        #不输出启动信息：nohup $EXEC $CONF > /dev/null 2>&1 &  
                        $EXEC $CONF &&  
                        sleep 1  
                        if [ -f $PIDFILE ]  
                        then  
                                echo "Redis cluster ${REDISPORT[i]} startup succeeded!"  
                        else  
                                echo "ERROR: Redis cluster ${REDISPORT[i]} startup failed!"  
                        fi  
                fi  
                ;;  
            stop)  
                if [ ! -f $PIDFILE ]  
                then  
                        echo "$PIDFILE does not exist, process is not running"  
                else  
                        PID=$(cat $PIDFILE)  
                        echo "Stopping Redis cluster ${REDISPORT[i]} ..."  
                        # 如果redis集群未设置密码，关闭指令改为：$CLIEXEC -p ${REDISPORT[i]} shutdown  
                        $CLIEXEC -p ${REDISPORT[i]} -a $PASSWD shutdown  
                        while [ -x /proc/${PID} ]  
                        do  
                            echo "Waiting for Redis cluster ${REDISPORT[i]} to shutdown ..."  
                            sleep 1  
                        done  
                        echo "Redis cluster ${REDISPORT[i]} stopped!"  
                fi  
                ;;  
            *)  
                echo "Please use start or stop as first argument"  
                ;;  
        esac  
       
    done  
    
[/code]
## 2\. Centos 6.x & Redhat 6.x环境
将 redis-cluster 文件放到 /etc/init.d/ 下，并赋予执行权限：
[code]
    chmod +x /etc/init.d/redis-cluster  
    
[/code]
相关命令：
[code]
    chkconfig --add redis-cluster  # 注册为系统服务  
    chkconfig redis-cluster on  # 开机自启动  
    service redis-cluster stop  # 关闭 redis 集群  
    service redis-cluster start  # 启动 redis 集群  
    
[/code]
## 3\. Centos 7.x & Redhat 7.x环境
将 redis-cluster 文件放到 /etc/rc.d/init.d/下，并赋予执行权限：
[code]
    chmod +x /etc/rc.d/init.d/redis-cluster  
    
[/code]
相关命令：
[code]
    chkconfig --add redis-cluster   # 注册为系统服务  
    chkconfig redis-cluster on  # 开机自启动  
    service redis-cluster stop  # 关闭 redis 集群  
    service redis-cluster start  # 启动 redis 集群
[/code]
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux下Tomcat开机自启动](<index.php?doc-view-1878.html>)
[下一篇：Redis单机开机自启动 ![](/core/style/forward.png) ](<index.php?doc-view-1880.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
