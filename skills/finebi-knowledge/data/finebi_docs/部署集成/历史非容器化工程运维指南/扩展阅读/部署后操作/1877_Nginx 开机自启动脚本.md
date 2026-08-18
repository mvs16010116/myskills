---
title: Nginx 开机自启动脚本
doc_id: 1877
url: https://help.fanruan.com/finebi6.X/doc-view-1877.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:39
---

> 虽然使用命令行可以对 Nginx 进行各种操作，比如启动等，但是还是不太方便，下面介绍在 Linux 下安装 Nginx 后，如何设置其开机自启动。1. CentOS6.x&amp;RedHat6.x

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Nginx 开机自启动脚本
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
* 历史版本：[2](<edition-list-1877.html>)
* 最近更新：[Leo.Tsai](<user-space-238588.html>) 于 2022-06-14 
[](<javascript:;>) [](<javascript:>)
虽然使用命令行可以对 Nginx 进行各种操作，比如启动等，但是还是不太方便，下面介绍在 Linux 下安装 Nginx 后，如何设置其开机自启动。
## 1\. CentOS6.x&RedHat6.x 配置 Nginx 开机自启动
### 1.1 创建 Nginx 的管理脚本
首先，在系统的/etc/init.d/目录下创建 nginx 文件：
[code]
    vi /etc/init.d/nginx  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    #!/bin/sh  
    #  
    # nginx - this script starts and stops the nginx daemon  
    #  
    # chkconfig:   - 85 15  
    # description:  NGINX is an HTTP(S) server, HTTP(S) reverse \  
    #               proxy and IMAP/POP3 proxy server  
    # processname: nginx  
    # config:      /etc/nginx/nginx.conf  
    # config:      /etc/sysconfig/nginx  
    # pidfile:     /var/run/nginx.pid  
    # Source function library.  
    . /etc/rc.d/init.d/functions  
    # Source networking configuration.  
    . /etc/sysconfig/network  
    # Check that networking is up.  
    [ "$NETWORKING" = "no" ] && exit 0  
    nginx="/usr/sbin/nginx"  
    prog=$(basename $nginx)  
    NGINX_CONF_FILE="/etc/nginx/nginx.conf"  
    [ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx  
    lockfile=/var/lock/subsys/nginx  
    make_dirs() {  
      # make required directories  
      user=`$nginx -V 2>&1 | grep "configure arguments:" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`  
      if [ -z "`grep $user /etc/passwd`" ]; then  
         useradd -M -s /bin/nologin $user  
         fi  
         options=`$nginx -V 2>&1 | grep 'configure arguments:'`    
         for opt in $options; do  
            if [ `echo $opt | grep '.*-temp-path'` ]; then  
              value=`echo $opt | cut -d "=" -f 2`  
              if [ ! -d "$value" ]; then  
                 # echo "creating" $value  
                 mkdir -p $value && chown -R $user $value  
                 fi  
            fi  
         done  
      }  
      start() {  
        [ -x $nginx ] || exit 5  
        [ -f $NGINX_CONF_FILE ] || exit 6  
        make_dirs  
        echo -n $"Starting $prog: "  
        daemon $nginx -c $NGINX_CONF_FILE  
        retval=$?  
        echo  
        [ $retval -eq 0 ] && touch $lockfile  
        return $retval  
      }  
      stop() {  
        echo -n $"Stopping $prog: "  
        killproc $prog -QUIT  
        retval=$?  
        echo  
        [ $retval -eq 0 ] && rm -f $lockfile  
        return $retval  
      }restart() {  
        configtest || return $?  
        stop  
        sleep 1  
        start  
      }  
      reload() {  
        configtest || return $?  
        echo -n $"Reloading $prog: "  
        killproc $nginx -HUP  
        RETVAL=$?  
        echo  
      }  
      force_reload() {  
        restart  
      }  
      configtest() {  
        $nginx -t -c $NGINX_CONF_FILE  
      }rh_status() {  
        status $prog  
      }  
      rh_status_q() {  
        rh_status >/dev/null 2>&1  
      }  
      case "$1" in  
        start)  
            rh_status_q && exit 0  
            $1  
            ;;  
        stop)  
            rh_status_q || exit 0  
            $1  
            ;;  
        restart|configtest)  
            $1  
            ;;  
        reload)  
            rh_status_q || exit 7  
            $1  
            ;;  
        force-reload)  
            force_reload  
            ;;  
        status)  
            rh_status  
            ;;  
        condrestart|try-restart)  
            rh_status_q || exit 0  
            ;;  
        *)  
            echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"          
            exit 2  
      esac  
    
[/code]
以上脚本内容来自于 Nginx 官方，脚本地址：[http://wiki.nginx.org/RedHatNginxInitScript](<http://wiki.nginx.org/RedHatNginxInitScript?spm=a2c4e.11153940.blogcont608222.9.58712715fm8z2b>)
注意，对于自定义编译安装的 Nginx（帮助文档中提供的即是此种方式），需要根据安装路径修改脚本中这两项配置：
[code]
    nginx="/usr/nginx/sbin/nginx" ====>nginx执行程序的路径  
    NGINX_CONF_FILE="/usr/nginx/conf/nginx.conf" ====>配置文件的路径  
    
[/code]
保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /etc/init.d/nginx  
    
[/code]
然后，就可以通过该脚本对 Nginx 服务进行管理了：
[code]
    /etc/init.d/nginx start  
    /etc/init.d/nginx stop  
    
[/code]
### 1.2 使用 chkconfig 设置开机自启动
上面的步骤完成了用脚本管理 Nginx 服务的功能，接下来我们就可以使用 chkconfig 来设置 Nginx 开机启动了。
先将nginx服务加入 chkconfig 管理列表：
[code]
    chkconfig --add /etc/init.d/nginx      
    
[/code]
配置完以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    chkconfig nginx on     #设置开机自启动  
    chkconfig nginx off    #停止开机自启动  
    service nginx start    #启动 Nginx 服务  
    service nginx stop     #停止 Nginx 服务  
    service nginx restart  #重启 Nginx 服务  
    service nginx status   #查看 Nginx 状态  
    
[/code]
## 2\. CentOS7.x&RedHat7.x 配置 Nginx 开机自启动
### 2.1 创建 Nginx 的管理脚本
首先，在系统的/lib/systemd/system/目录下创建 nginx.service文件：
[code]
    vi /lib/systemd/system/nginx.service  
    
[/code]
点击 i 键，在脚本中添加如下内容：
[code]
    [Unit]  
    Description=nginx service  
    After=network.target  
    [Service]  
    Type=forking  
    ExecStart=/usr/nginx/sbin/nginx  
    ExecReload=/usr/nginx/sbin/nginx -s reload  
    ExecStop=/usr/nginx/sbin/nginx -s quit  
    PrivateTmp=true  
    [Install]  
    WantedBy=multi-user.target  
    
[/code]
注意，对于自定义编译安装的 Nginx（帮助文档中提供的即是此种方式），需要根据实际路径修改脚本中的 Nginx 启动路径“/usr/nginx/sbin/nginx”。
保存脚本文件后设置文件的执行权限：
[code]
    chmod a+x /lib/systemd/system/nginx.service  
    
[/code]
### 2.2使用 systemctl 设置开机自启动
配置完脚本以后，就可以使用以下命令设置开机自启动等操作了：
[code]
    systemctl enable nginx.service          #设置开机自启动  
    systemctl disable nginx.service         #停止开机自启动  
    systemctl start nginx.service　         #启动 Nginx 服务  
    systemctl stop nginx.service　          #停止服务  
    systemctl status nginx.service          #查看服务当前状态  
    systemctl list-units --type=service     #查看所有已启动的服务  
    
[/code]
## 3\. 注意事项
如果 Centos8.5 环境 Nginx 和 Tomcat 都放在 /home 目录下，注册服务不能启动的话，可以放到 /usr 底去。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows下Tomcat开机自启动](<index.php?doc-view-1881.html>)
[下一篇：Linux中启动FineBI ![](/core/style/forward.png) ](<index.php?doc-view-24.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
