---
title: Linux防火墙使用及配置
doc_id: 1372
url: https://help.fanruan.com/finebi6.X/doc-view-1372.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:45
---

> 1.&nbsp;概述工程部署到 Linux 系统中后，Linux&nbsp;系统需要开放工程端口，工程地址才能被其他电脑访问。2.&nbsp;Centos 7 firewall&nbsp;2.1 fir

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux防火墙使用及配置
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[2](<edition-list-1372.html>)
* 最近更新：[知识库](<user-space-567266.html>) 于 2021-06-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
工程部署到 Linux 系统中后，Linux 系统需要开放工程端口，工程地址才能被其他电脑访问。
## 2\. Centos 7 firewall 
### 2.1 firewalld 的基本使用
启动防火墙：systemctl start firewalld
关闭防火墙：systemctl stop firewalld
查看防火墙状态：systemctl status firewalld
开机禁用：systemctl disable firewalld
开机启用：systemctl enable firewalld
### 2.2 systemctl 的基本使用
启动一个服务：systemctl start firewalld.service  
关闭一个服务：systemctl stop firewalld.service  
重启一个服务：systemctl restart firewalld.service  
显示一个服务的状态：systemctl status firewalld.service  
在开机时启用一个服务：systemctl enable firewalld.service  
在开机时禁用一个服务：systemctl disable firewalld.service  
查看服务是否开机启动：systemctl is-enabled firewalld.service  
查看已启动的服务列表：systemctl list-unit-files|grep enabled  
查看启动失败的服务列表：systemctl --failed
### 2.3 配置 firewalld-cmd
查看版本：firewall-cmd --version
查看帮助：firewall-cmd --help
显示状态：firewall-cmd --state
查看所有打开的端口：firewall-cmd --zone=public --list-ports
更新防火墙规则：firewall-cmd --reload
查看区域信息：firewall-cmd --get-active-zones
查看指定接口所属区域：firewall-cmd --get-zone-of-interface=eth0
拒绝所有包：firewall-cmd --panic-on
取消拒绝状态：firewall-cmd --panic-off
查看是否拒绝：firewall-cmd --query-panic
### 2.4 开放端口步骤
#### 2.4.1 添加端口  

1）开启防火墙  

使用systemctl status firewalld查看防火墙状态，若未开启，使用systemctl start firewalld开启防火墙。
如下图所示：
![1623053464812396.png](/core/style/lod.png)
2）开放端口
使用firewall-cmd --list-port查看防火墙开放的端口，如果没有返回，证明没有开放端口。使用firewall-cmd --zone=public --add-port=8083/tcp --permanent开放端口，使用firewall-cmd --reload重新载入。如下图所示：
![1623053847724899.png](/core/style/lod.png)
#### 2.4.2 其他端口配置语句
1）查看端口
[code]
    firewall-cmd --zone=public --query-port=8083/tcp  
    
[/code]
![1623054006496865.png](/core/style/lod.png)
2）删除已开放端口
[code]
    firewall-cmd --zone=public --remove-port=8083/tcp --permanent  
    firewall-cmd --reload  
    
[/code]
![1623054143824576.png](/core/style/lod.png)
3）调整默认策略（默认拒绝所有访问，改成允许所有访问）
[code]
    firewall-cmd --permanent --zone=public --set-target=ACCEPT  
    firewall-cmd --reload  
    
[/code]
4）对某个 IP 开放多个端口
[code]
    firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source address="10.159.60.29" port   
    protocol="tcp" port="1:65535" accept"  
    firewall-cmd --reload  
    
[/code]
## 3\. Centos 6 iptables
### 3.1 iptables的基本使用
启动：service iptables start
关闭：service iptables stop
查看状态：service iptables status
开机禁用：chkconfig iptables off
开机启用：chkconfig iptables on
### 3.2 开放指定端口语句
1）允许本地回环接口（即运行本机访问本机）：iptables -A INPUT -i lo -j ACCEPT
注：-A和-I参数分别为添加到规则末尾和规则最前面。
2）允许已建立的或相关联的通行：iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
3）允许所有本机向外的访问：iptables -P INPUT ACCEPTiptables -A OUTPUT -j ACCEPT
4）允许访问22端口：
iptables -A INPUT -p tcp --dport 22 -j ACCEPT  
iptables -A INPUT -p tcp -s 10.159.1.0/24 --dport 22 -j ACCEPT   
注：-s后可以跟 IP 段或指定 IP 地址，如果有其他端口的话，规则也类似。
5）允许ping：iptables -A INPUT -p icmp -m icmp --icmp-type 8 -j ACCEPT
6）禁止其他未允许的规则访问：
iptables -A INPUT -j REJECT
iptables -A FORWARD -j REJECT
注：如果 22 端口未加入允许规则，SSH链接会直接断开。
### 3.3 屏蔽 IP
1）屏蔽单个IP：iptables -I INPUT -s 123.45.6.7 -j DROP
2）封整个段即从123.0.0.1到123.255.255.254：iptables -I INPUT -s 123.0.0.0/8 -j DROP
3）封IP段即从123.45.0.1到123.45.255.254：iptables -I INPUT -s 124.45.0.0/16 -j DROP
4）封IP段即从123.45.6.1到123.45.6.254：iptables -I INPUT -s 123.45.6.0/24 -j DROP
### 3.4 iptables 规则
**查看已有规则：** iptables -L -n
N：只显示IP地址和端口号，不将 IP 解析为域名
将所有 iptables 以序号标记显示，执行：iptables -L -n --line-numbers
**添加规则**
iptables -A和iptables -I
1）iptables -A
添加的规则是添加在最后面。如针对 INPUT 链增加一条规则，接收从 eth0 口进入且源地址为192.168.0.0/16网段发往本机的数据：
iptables -A INPUT -i eth0 -s 192.168.0.0/16 -j ACCEPT
2）iptables -I 
添加的规则默认添加至第一条。如果要指定插入规则的位置，则使用iptables -I时指定位置序号即可。
**删除规则**
如果删除指定规则，使用iptables -D命令。命令后可接序号或iptables -D接详细定义。
如果想把所有规则都清除掉，可使用iptables -F。
### 3.5 规则的保存与恢复
**备份iptables rules**
使用 iptables-save 命令，如：iptables-save > /etc/sysconfig/iptables.save
**恢复iptables rules**
使用 iptables 命令，如：iptables-restore < /etc/sysconfig/iptables.save
**iptables 配置保存**
做的配置修改，在设备重启后，配置将丢失。可使用service iptables save进行保存。
重启 iptables 的服务使其生效：service iptables save
添加规则后保存重启生效：service iptables restart
### 3.6 开放端口步骤
#### 3.6.1 方法一：通过命令行  

[code]
    iptables -A INPUT -p tcp --dport 80 -j ACCEPT  
    service iptables save  
    service iptables restart  
    
[/code]
#### 3.6.2 方法二：编辑配置文件
iptables的配置文件为/etc/sysconfig/iptables
编辑配置文件：vi /etc/sysconfig/iptables
1）配置文件中添加：  

[code]
    -A INPUT -p tcp --dport 80 -j ACCEPT  
    
[/code]
2）执行service iptables restart，重启生效。
## 4\. 注意事项
云服务器需要额外设置安全组，开放相关端口。
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：集群常见报错及解决方案](<index.php?doc-view-664.html>)
[下一篇：Windows服务器设置出入站规则 ![](/core/style/forward.png) ](<index.php?doc-view-1371.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
