---
title: Keepalived+Nginx部署方案
doc_id: 1965
url: https://help.fanruan.com/finebi6.X/doc-view-1965.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:49
---

> 提示:运维平台部署的帆软项目，其中包含帆软内网关组件。其对帆软业务进行了定制调整，以均衡的分发用户请求，提升性能，因此不支持用户自备，不支持进行自定义修改。请勿参照本文对内网关组件进行任何修改！1. 概

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Keepalived+Nginx部署方案
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
* 历史版本：[3](<edition-list-1965.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-12-09 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
运维平台部署的帆软项目，其中包含帆软内网关组件。其对帆软业务进行了定制调整，以均衡的分发用户请求，提升性能，因此不支持用户自备，不支持进行自定义修改。**请勿参照本文对内网关组件进行任何修改！**
## 1\. 概述
Nginx 可以用来作为反向代理服务器，来提供负载均衡的能力，使我们的 Web 服务器，能够水平扩容，从而处理更多的用户请求。
但是反向代理服务器又变成了一个单点，当反向代理服务器挂了，整合 Web 服务器就不能被外界访问到，所以我们必须要保证反向代理服务器的高可用。
而 Keepalived 是一种高性能的服务器高可用或热备解决方案，可以用来防止服务器单点故障的发生，通过配合 Nginx 可以实现 Web 前端服务的高可用。
## 2\. 方案规划
注：VIP 为虚拟 IP ，不被占用前提下可自定义。  

VIP| 服务器 IP| 主机名| nginx 端口| 默认主从  
---|---|---|---|---  
192.168.5.200| 192.168.5.249  
| ethan3| 80| MASTER  
192.168.5.200| 192.168.5.103  
| localhost.localdomain| 80| BACKUP  
## 3\. 外网用户方案
### 3.1 安装 Nginx
两个服务器上安装配置 Nginx 。具体步骤请参见：[Linux系统安装配置Nginx](<https://help.fanruan.com/finebi6.X/doc-view-1532.html>)
### 3.2 安装 Keepalived
两个服务器上安装 Keepalived 。
执行命令：  

[code]
    yum -y install keepalived  
    
[/code]
### 3.3 设置 keepalived 服务开机启动
两个服务器都需要执行下面语句。语句如下所示：
[code]
    chkconfig keepalived on  
    
[/code]
![4.png](/core/style/lod.png)
### 3.4 修改 Keepalived 的配置文件
路径为：/etc/keepalived/keepalived.conf
#### 3.4.1 MASTER 节点配置文件
[code]
    ! Configuration File for keepalived  
    global_defs {  
    ## keepalived 自带的邮件提醒需要开启 sendmail 服务。 建议用独立的监控或第三方 SMTP  
     router_id ethan3 ## 标识本节点的字条串，通常为 hostname  
    }   
    ## keepalived 会定时执行脚本并对脚本执行的结果进行分析，动态调整 vrrp_instance 的优先级。如果脚本执行结果为 0，并且 weight 配置的值大于 0，则优先级相应的增加。如果脚本执行结果非 0，并且 weight配置的值小于 0，则优先级相应的减少。其他情况，维持原本配置的优先级，即配置文件中 priority 对应的值。  
    vrrp_script chk_nginx {  
     script "/etc/keepalived/nginx_check.sh" ## 检测 nginx 状态的脚本路径  
     interval 2 ## 检测时间间隔  
     weight -20 ## 如果条件成立，权重-20  
    }  
    ## 定义虚拟路由， VI_1 为虚拟路由的标示符，自己定义名称  
    vrrp_instance VI_1 {  
     state MASTER ## 主节点为 MASTER， 对应的备份节点为 BACKUP  
     interface eno16777736 ## 绑定虚拟 IP 的网络接口，与本机 IP 地址所在的网络接口相同。  
     virtual_router_id 33 ## 虚拟路由的 ID 号， 两个节点设置必须一样， 可选 IP 最后一段使用, 相同的 VRID 为一个组，他将决定多播的 MAC 地址  
     mcast_src_ip 192.168.5.249 ## 本机 IP 地址  
     priority 200 ## 节点优先级， 值范围 0-254， MASTER 要比 BACKUP 高  
     advert_int 1 ## 组播信息发送间隔，两个节点设置必须一样， 默认 1s  
     ## 设置验证信息，两个节点必须一致  
     authentication {  
      auth_type PASS  
      auth_pass 1111 ## 真实生产，按需求对应该过来  
     }  
     ## 将 track_script 块加入 instance 配置块  
     track_script {  
      chk_nginx ## 执行 Nginx 监控的服务  
     } #  
     # 虚拟 IP 池, 两个节点设置必须一样  
     virtual_ipaddress {  
      192.168.5.200 ## 虚拟 ip，可以定义多个  
     }  
    }  
    
[/code]
#### 3.4.2 BACKUP 节点配置文件
[code]
    ! Configuration File for keepalived  
    global_defs {  
     router_id localhost.localdomain  
    }  
    vrrp_script chk_nginx {  
     script "/etc/keepalived/nginx_check.sh"  
     interval 2  
     weight -20  
    }  
    vrrp_instance VI_1 {  
     state BACKUP  
     interface ens192  
     virtual_router_id 33  
     mcast_src_ip 192.168.5.103  
     priority 90  
     advert_int 1  
     authentication {  
      auth_type PASS  
      auth_pass 1111  
     }  
     track_script {  
      chk_nginx  
     }  
     virtual_ipaddress {  
      192.168.5.200  
     }  
    }  
    
[/code]
需要注意的配置说明：
1）router_id ethan3 ## 标识本节点的字条串，通常为 hostname 。
在服务器中使用语句hostname可得出。如下图所示：
![1641974851329444.png](/core/style/lod.png)
2）script "/etc/keepalived/nginx_check.sh" ## 检测 nginx 状态的脚本路径，无需修改，参考本文 3.5 节。
3）state MASTER/BACKUP ##说明主备。
4）interface eno16777736 ## 绑定虚拟 IP 的网络接口，与本机 IP 地址所在的网络接口相同。
使用ip a可得出。如下图所示：
注：主节点配置文件中该值为主节点网卡号；备节点配置文件中该值为备节点网卡号。
![1641974942332551.png](/core/style/lod.png)
5）mcast_src_ip 192.168.5.249 ## 本机 IP 地址。
6）priority 200 ## 节点优先级， 值范围 0-254， MASTER 要比 BACKUP 高。
7）virtual_ipaddress ##虚拟 ip，即VIP，可自定义，可定义多个。
### 3.5 编写 Nginx 状态启动脚本
两个服务器上都需要编写下面文件，根据实际情况修改 nginx 路径。  

编写 Nginx 状态检测脚本 /etc/keepalived/nginx_check.sh (已在 Keepalived.conf 中配置)脚本要求。
[code]
    #!/bin/bash  
    A=`ps -C nginx --no-header |wc -l`  
    if [ $A -eq 0 ];then  
    /usr/nginx/sbin/nginx  
    sleep 2  
    if [ `ps -C nginx --no-header |wc -l` -eq 0 ];then  
     killall keepalived  
    fi  
    fi  
    
[/code]
赋予文件权限：chmod +x /etc/keepalived/nginx_check.sh 
### 3.6 启动 Keepalived
两个服务器都执行下面语句：  

[code]
    systemctl start keepalived  
    
[/code]
### 3.7 效果查看
注：节点上有虚拟 IP 时，可通过虚拟 IP 访问相应的 nginx 及下面相应的文件。
1）使用ip addr语句，可以看到虚拟 IP 192.168.5.200 绑定在了 MASTER 服务器上面。如下图所示：
![1641973992565967.png](/core/style/lod.png)
而 BACKUP 节点上没有虚拟 IP 。如下图所示：
![1641974146900091.png](/core/style/lod.png)
2）使用systemctl stop keepalived停掉主节点的 keepalived 服务，备节点上有虚拟 IP 。如下图所示：
![1641974581124305.png](/core/style/lod.png)
## 4\. 内网用户方案
### 4.1 步骤说明
内网用户无法在线安装 Keepalived ，与外网用户方案不同点在于 3.2 节，其他步骤相同。
### 4.2 离线安装 Keepalived
两个服务器都需要做下面步骤。  

#### 4.2.1 安装步骤  

1）下载安装包。访问网址：<https://www.keepalived.org/download.html> 并下载 Keepalived 的安装包。
2）解压安装。
将安装包上传到服务器某个文件夹下（文档示例为：/wendy），进入安装包所在文件夹后，进行下面操作：
[code]
    cd /wendy  
    tar -zxvf keepalived-2.0.18.tar.gz   # 解压  
    
[/code]
[code]
    cd /wendy/keepalived-2.0.18  # 路径根据实际情况修改  
    
[/code]
[code]
    ./configure --prefix=/usr/local/keepalived   # 编译  
    
[/code]
[code]
    make && make install   # 安装  
    
[/code]
#### 4.2.2 将 Keepalived 安装成 Linux 系统服务
1）复制keepalived.conf文件到/etc/keepalived/下。
[code]
    mkdir /etc/keepalived  
    cp /wendy/keepalived-2.0.18/keepalived/etc/keepalived/keepalived.conf /etc/keepalived/  
    
[/code]
2）复制 keepalived 服务脚本到默认的地址：
[code]
    cp /wendy/keepalived-2.0.18/keepalived/etc/init.d/keepalived /etc/init.d/  
    cp /wendy/keepalived-2.0.18/keepalived/etc/sysconfig/keepalived /etc/sysconfig/  
    
[/code]
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux系统安装配置Nginx](<index.php?doc-view-1532.html>)
[下一篇：Nginx常见报错及解决方案 ![](/core/style/forward.png) ](<index.php?doc-view-536.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
