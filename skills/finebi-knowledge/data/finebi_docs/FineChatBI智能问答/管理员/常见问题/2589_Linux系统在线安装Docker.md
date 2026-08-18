---
title: Linux系统在线安装Docker
doc_id: 2589
url: https://help.fanruan.com/finebi6.X/doc-view-2589.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:31
---

> 1. 概述Docker 对 Linux 系统版本有一定的要求，在 Docker 安装帮助页面&nbsp;查看支持的系统版本。基本要求：Linux要求内核3.0以上、CentOS 需要是 7 及以上版本，

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux系统在线安装Docker
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[TW](<user-space-1900999.html>)_
* 历史版本：[3](<edition-list-2589.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2025-08-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
Docker 对 Linux 系统版本有一定的要求，在 [Docker 安装帮助页面](<https://docs.docker.com/engine/install/centos/>) 查看支持的系统版本。
基本要求：Linux要求内核3.0以上、CentOS 需要是 7 及以上版本，或 Ubuntu 版本 20 及以上
Windows 系统安装 Docker 请参考 https://learn.microsoft.com/zh-cn/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce
## 2\. 检查 Linux 系统版本
1）使用命令检查系统版本，命令：cat /etc/os-release
![1.png](/core/style/lod.png)
2）若系统版本不符合要则需要进行升级至 Docker 支持的系统版本。
## 3\. Docker 在线安装
### 3.1 CentOS
1）如果已经安装过Docker，先卸载已安装的Docker，命令：
yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
未安装的Docker的系统运行此命令，如下图所示：
![2.png](/core/style/lod.png)
2）安装 yum 工具包和存储驱动，命令：yum install -y yum-utils
![2024-02-28_10-54-42.png](/core/style/lod.png)
3）设置镜像仓库，命令：
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
![4.png](/core/style/lod.png)
4）更新 yum 软件包索引，命令：yum makecache fast
![5.png](/core/style/lod.png)
5）安装 docker，docker-ce 社区版 而 ee 是企业版，此处使用社区版即可。命令为：yum install docker-ce docker-ce-cli containerd.io
![2024-02-28_11-17-57.png](/core/style/lod.png)
输入y，确认即可进行下载，如下图所示：  

![7.png](/core/style/lod.png)
输入y，确认即可进行安装，如下图所示：
![8.png](/core/style/lod.png)
6）启动 docker，命令为：systemctl start docker
### 3.2 Ubuntu
  1. 更新系统软件包  
sudo apt update
  2. 安装依赖包  
sudo apt install apt-transport-https ca-certificates curl software-properties-common
  3. 添加Docker官方GPG密钥，依次执行  
sudo -i  
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-ce.gpg  
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg  
chmod a+r /etc/apt/trusted.gpg.d/docker-ce.gpg  
chmod a+r /usr/share/keyrings/docker-archive-keyring.gpg  
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null  

  4. 验证，0EBFCD88 是公钥的指纹。执行这个命令后，系统会显示与该指纹相关的公钥信息。  
sudo apt-key fingerprint 0EBFCD88  

  5. 添加Docker阿里稳定版软件源  
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
  6. 再次更新软件包  
sudo apt update
  7. 安装默认最新版  
sudo apt install docker-ce docker-ce-cli containerd.io
  8. 测试，安装好后默认启动。显示版本则表示Docker已经成功安装。  
sudo docker --version


### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：传统部署方式升级](<index.php?doc-view-2585.html>)
[下一篇：判断大模型是否满足 FineChatBI 能力要求 ![](/core/style/forward.png) ](<index.php?doc-view-2612.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
