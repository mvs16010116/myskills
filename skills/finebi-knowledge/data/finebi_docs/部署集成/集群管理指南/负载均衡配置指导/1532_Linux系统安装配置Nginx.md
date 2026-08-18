---
title: Linux系统安装配置Nginx
doc_id: 1532
url: https://help.fanruan.com/finebi6.X/doc-view-1532.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:48
---

> 提示:运维平台部署的帆软项目，其中包含帆软内网关组件。其对帆软业务进行了定制调整，以均衡的分发用户请求，提升性能，因此不支持用户自备，不支持进行自定义修改。请勿参照本文对内网关组件进行任何修改！1.&n

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Linux系统安装配置Nginx
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[27](<edition-list-1532.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-12-09 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
运维平台部署的帆软项目，其中包含帆软内网关组件。其对帆软业务进行了定制调整，以均衡的分发用户请求，提升性能，因此不支持用户自备，不支持进行自定义修改。**请勿参照本文对内网关组件进行任何修改！**
  

## 1\. 概述
### 1.1 版本
FineBI服务器版本| Nginx 版本  
---|---  
6.0| 1.21及以上版本，优先使用最新版本  
### 1.2 环境准备
**运行环境**|  必须有 gcc 和 gcc-c++ 环境，检查命令：gcc -v如果没有需自行安装，联网安装命令 yum install gcc gcc-c++  
---|---  
**安装包**| [nginx-1.22.1.tar.gz](<doc-download-/finebi6.X/uploads/file/20221028/nginx-1.22.1.tar.gz> "下载资料")注：nginx部分老版本存在一些安全问题，推荐使用 nginx-1.21以上版本，历史版本用户建议进行升级。  
**依赖包**|  必须下载 3 个依赖包，部署过程会用到[zlib-1.2.11.tar.gz](<doc-download-/finebi5.1/uploads/file/20210729/zlib-1.2.11.tar.gz> "下载资料")[pcre-8.42.tar.gz](<doc-download-/finebi5.1/uploads/file/20210729/pcre-8.42.tar.gz> "下载资料")[openssl-1.1.1a.tar.gz](<doc-download-/finebi5.1/uploads/file/20210729/openssl-1.1.1a.tar.gz> "下载资料")  
**补丁包**|  必须下载，主动健康检查补丁包为重要功能[ngx_healthcheck_module-master.zip](<doc-download-/finebi5.1/uploads/file/20210729/ngx_healthcheck_module-master.zip> "下载资料")  
## 2\. 安装过程
### 2.1 解压安装包
将安装包放在某个目录，例如/usr/nginx下，进行解压：
[code]
    mkdir /usr/nginx # 创建安装目录  
    cd /usr/nginx # 进入目录  
    tar zxvf nginx-1.22.1.tar.gz # 解压 nginx-1.22.1  
    tar zxvf pcre-8.42.tar.gz # 解压 pcre  
    tar zxvf zlib-1.2.11.tar.gz # 解压 zlib  
    tar zxvf openssl-1.1.1a.tar.gz # 解压 openssl  
    unzip ngx_healthcheck_module-master.zip # 解压 ngx_healthcheck_module-master  
    
[/code]
### 2.2 安装 Nginx
注：下面第三行命令中的「/usr/nginx」路径，需要与 2.1 节安装目录相同；由于第三行内容过长，建议用户将下面命令复制到本地，确认路径后再按序执行。
cd /usr/nginx/nginx-1.22.1 # 进入解压目录  
patch -p1 < /usr/nginx/ngx_healthcheck_module-master/nginx_healthcheck_for_nginx_1.14+.patch # 应用健康检查补丁  
./configure --prefix=/usr/nginx --with-pcre=/usr/nginx/pcre-8.42 --with-zlib=/usr/nginx/zlib-1.2.11 --with-http_ssl_module --with-openssl=/usr/nginx/openssl-1.1.1a --with-stream --add-module=/usr/nginx/ngx_healthcheck_module-master # 指定安装路径  
make && make install # 用 && 连接的两条命令，只有 make 无错误时，才会继续执行 make install 命令
## 3\. 修改配置
要想使用 Nginx 搭配 Web 容器发挥负载均衡的作用，必须还要对 Nginx 进行配置，下面提供通用配置和自定义配置。
### 3.1 通用配置
1）通用配置 ：[nginx.zip](<doc-download-/finebi6.X/uploads/file/20230605/nginx.zip> "下载资料")
文件下载到本地后，按照自己的环境，修改一些配置信息，如下图所示：
![](/core/style/lod.png)
  

![1658470602110308.png](/core/style/lod.png)
2）保存文件，然后替换原始的 /usr/nginx/conf/nginx.conf  

### 3.2 自定义配置
[code]
    vi /usr/nginx/conf/nginx.conf # 编辑配置文件 nginx.conf  
    
[/code]
参考 [nginx.conf 配置手册](<https://help.fanruan.com/finereport/doc-view-2815.html>) 中的 Nginx 配置参数说明，自行配置（修改 Nginx 端口、配置外网映射、配置 https 等）。
## 4\. 启动Nginx
### 4.1 运维命令
[code]
    cd /usr/nginx/sbin # 进入 sbin 目录  
    ./nginx # 启动 nginx  
    ./nginx -s stop # 停止 nginx  
    ./nginx -s reload # 热加载nginx，可以理解为重启，但是用户不会感知到  
    
[/code]
更多运维操作，详情参见：[Linux版集群运维手册](<https://help.fanruan.com/finereport/doc-view-2791.html>)  

### 4.2 测试是否成功
在浏览器输入ip:负载均衡端口号/status查看健康页面，可以看到节点健康状态，若为 up 状态则表示正常，如下图所示：
![1111.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：负载均衡配置指导](<index.php?doc-view-1964.html>)
[下一篇：Keepalived+Nginx部署方案 ![](/core/style/forward.png) ](<index.php?doc-view-1965.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
