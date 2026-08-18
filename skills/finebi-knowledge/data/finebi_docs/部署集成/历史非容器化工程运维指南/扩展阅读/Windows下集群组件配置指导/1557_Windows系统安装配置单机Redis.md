---
title: Windows系统安装配置单机Redis
doc_id: 1557
url: https://help.fanruan.com/finebi6.X/doc-view-1557.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:53
---

> 1. 概述Redis 是一个开源的底层使用 C 语言编写的 Key-Value 存储数据库。Redis 在 Web 集群中用来做状态服务器，主要用于存储缓存登录、模板锁、 sessionID 等，发挥并

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统安装配置单机Redis
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[4](<edition-list-1557.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-07-18 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
Redis 是一个开源的底层使用 C 语言编写的 Key-Value 存储数据库。
Redis 在 Web 集群中用来做状态服务器，主要用于存储缓存登录、模板锁、 sessionID 等，发挥并对所有的访问和操作进行验证的作用。
## 2\. 操作步骤
### 2.1 下载 Redis
在 GitHub 上可以下载 Windows 系统对应版本，下载地址：<https://github.com/MicrosoftArchive/redis/releases>，可以选择最新的版本下载。
注：mis 文件是微软安装版、zip 文件是解压版，这里我们下载 zip 包，解压即可使用。
如果不能上 GitHub 的用户，也可以点击直接下载：Redis-x64-3.2.100.zip ：[Redis-x64-3.2.100.zip](<doc-download-/finebi5.1/uploads/file/20210810/Redis-x64-3.2.100.zip> "下载资料")
### 2.2 安装 Redis
在 D 盘新建个文件夹，例如D:\redis，将 Redis-x64-3.2.100.zip 里的文件解压到该文件夹
### 2.3 修改配置文件
编辑配置文件redis.windows.conf，修改以下内容：
[code]
    bind 127.0.0.1 ---> # bind 127.0.0.1  
    protected-mode yes ---> protected-mode no  
    # requirepass foobared ---> requirepass 123456  #123456为密码可任意替换  
    port 6379 ---> port 7379  # 将端口改为 7379  
    maxmemory 4294967296  # 配置内存为 4G 单位是 byte，也可以配置成其他大小，推荐大小为4G（需添加内容）  
    maxmemory-policy noeviction #代表Redis内存达到最大限制时，Redis不会自动清理或删除任何键来释放内存，新的写入请求将会被拒绝  
    
[/code]
### 2.4 启动 Redis
cmd 进入 Redis 目录，执行redis-server.exe redis.windows.conf语句，出现以下内容，则代表启动成功：
![1628562677654741.png](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Windows系统安装配置Nginx](<index.php?doc-view-1534.html>)
[下一篇：Windows系统配置FTP服务 ![](/core/style/forward.png) ](<index.php?doc-view-1562.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
