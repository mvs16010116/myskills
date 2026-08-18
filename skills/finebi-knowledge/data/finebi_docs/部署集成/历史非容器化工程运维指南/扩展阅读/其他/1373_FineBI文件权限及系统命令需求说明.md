---
title: FineBI文件权限及系统命令需求说明
doc_id: 1373
url: https://help.fanruan.com/finebi6.X/doc-view-1373.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:55
---

> 工程文件权限配置建议：请对安装FineBI的用户，授予FineBI安装目录的所有者和读写执行权限文件权限缺失导致的问题：无法读取工程配置、工程JAR包，工程启动失败无法成功加载插件、报表、仪表板资源。内

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI文件权限及系统命令需求说明
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[知识库](<user-space-567266.html>)_
* 历史版本：[2](<edition-list-1373.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-02-25 
[](<javascript:;>) [](<javascript:>)
## 工程文件权限
**配置建议：**  

请对安装FineBI的用户，授予FineBI安装目录的所有者和读写执行权限
**文件权限**缺失** 导致的问题：**
无法读取工程配置、工程JAR包，工程启动失败
无法成功加载插件、报表、仪表板资源。内置数据库等，模板预览失败
无法读取lic文件，注册失败等
**配置方法：**
1）对于准备的FineBI安装目录，请指定服务器用户为该文件夹的**所有者**  

chown -R 用户名 /目录绝对路径
例如指定/home/fanruan目录的所有者为dev：chown -R dev /home/fanruan
2）对于准备的FineBI安装目录，请确保服务器用户有该文件夹的**读写执行权限**
chmod -R 755 /目录绝对路径
例如指定/home/fanruan目录的所有者有该文件夹的**读写执行权限** ：chmod -R 755 /home/fanruan
## 进程说明
产品运行过程中，某些进程会对服务器执行一些系统指令和请求。本文列出这些系统命令，方便用户进行安全报备。
模块  
| Linux命令| 用途  
  
---|---|---  
BI| bash| 检查bash  
ifconfig -a| 获取MAC地址  
sh -c cat /proc/cpuinfo | grep processor |wc -l| CPU 信息  
free -g| 内存信息  
sysctl vm.max_map_countsysctl vm.overcommit_memorysysctl vm.overcommit_ratio| 虚拟信息  
date -R| 时区信息  
sh -c echo $LANG| 语言信息  
sh -c hostname| host信息  
cat /etc/hosts| host文件信息  
gcc --versionsh -c strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX_3.4.22sh -c strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX_3.4.22| gcc信息  
fc-list :lang=zh| 字体信息  
sh -c ulimit -a | grep 'open files'| 打开文件数信息  
云端运维  
| cat /etc/redhat-release| 获取系统信息  
cat /etc/issue| 获取系统信息  
java -version| 获取 jdk 版本信息  
cat /proc/cpuinfo | grep -w "model name" | uniq| 获取CPU型号  
cat /proc/cpuinfo |grep processor | wc -l| 获取主板核心数  
ps -aux | sort -k6nr | sed -n 2p | awk '{print $6}'| 查看内存占用第二的进程占用内存大小  
ps -aux | sort -k6nr | sed -n 1p | awk '{print $6}'| 查看内存占用最大的进程占用内存大小  
dmidecode -t 1| 查看主板信息  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统搭建Web集群](<index.php?doc-view-1571.html>)
[下一篇：Linux常见问题 ![](/core/style/forward.png) ](<index.php?doc-view-25.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
