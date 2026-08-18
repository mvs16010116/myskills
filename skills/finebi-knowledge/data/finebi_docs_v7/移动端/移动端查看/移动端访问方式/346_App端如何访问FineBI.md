---
title: App端如何访问FineBI
doc_id: 346
url: https://help.fanruan.com/finebi/doc-view-346.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:11
version: "7.X"
---

> 1. 概述1.1 版本App 版本11.0.681.2 应用场景用户可在数据分析 App 中，配置自己的服务器，预览 FineBI 工程目录中的仪表板。1.3 功能描述打开数据分析 App，点击登录界面

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# App端如何访问FineBI
[__](<doc-edit-346.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[17](<edition-list-346.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2024-11-20 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
App 版本  
---  
11.0.68  
### 1.2 应用场景
用户可在数据分析 App 中，配置自己的服务器，预览 FineBI 工程目录中的仪表板。
### 1.3 功能描述
打开数据分析 App，点击登录界面左下角的服务器按钮，即可进入服务器列表，如下图所示：
数据分析 App 中，内置了 FineReport 和 FineBI Demo 服务器，用户可预览示例仪表板，了解帆软产品功能。
用户可在数据分析 App 中，切换、修改、新增、删除自有服务器。
![211.png](https://help.fanruan.com/core/style/lod.png)
## 2\. PC 端配置
### 2.1 环境确认
将 PC 设备与移动设备切换至同一网络环境下。有三种方法：
1）手机给电脑开热点。
2）手机和电脑连接同一热点。
3）给服务器配置外网可连接的环境。
注：为防止电脑 IP 未切换到无线网络的 IP，请拔掉有线网。
### 2.2 平台配置二维码
管理员登录系统，点击「管理系统>移动平台>APP配置>登录设置」，输入对应的「服务器名称」和「服务器地址」，点击「生成二维码」，即可在二维码方框中生成一个二维码。
本文以本地服务器为例，输入地址为 http://ip:端口号/工程名/decision ，如下图所示：
![生成二维码11111.png](https://help.fanruan.com/core/style/lod.png)
注：服务器地址一般为已经安装好的 PC 端工程 URL ，特殊情况请参考文档：[Tomcat 下通过 IP 直接访问数据决策系统](<https://help.fanruan.com/finebi7.0/doc-view-903.html?source=4#5>) 3.2节。
### 2.3 配置账号密码
如需在移动端访问模板，需要拥有一个FineBI的账号密码，具体设置方式请参见：[BI 查看用户](<https://help.fanruan.com/finebi7.0/doc-view-367.html>)
初始化成功后，本文以 FineBI 设计器内置用户 Alice 为例，其账号和密码分别为：Alice，1。
## 3\. App 配置服务器
注：App 下载及安装请参考：[App下载安装及使用](<https://help.fanruan.com/finebi7.0/doc-view-342.html>)
[App 下载](<https://www.fanruan.com/finemobile/download>) 安装后，打开数据分析 App，点击「服务器>新建服务器」，扫描 2.2 节配置的二维码。
确认服务器信息，点击右上角 √ 号，即可在服务器列表新增该工程，自动跳转到登录页。如下图所示：
注1：用户可扫描相册中保存的二维码。
注2：用户可手动输入服务器信息，服务器地址为：http://ip:端口号/工程名/decision 。
注3：为提升安全性，用户希望客户端与服务器通信时数据进行加密。若服务器已使用 HTTPS SSL 加密，App 添加服务器时也支持 HTTPS 协议。
![2020-07-28_16-06-24.png](https://help.fanruan.com/core/style/lod.png)
## 4\. App 登录服务器
在登录页输入管理员的账号和密码，即可进入该工程移动端首页/主目录，如下图所示：  

注1：若输入 FineReport 内置的用户账号和密码（非管理员），需要为该用户分配查看目录的权限，详情请参见：[根据用户分配权限说明](<https://help.fanruan.com/finereport/doc-view-2199>)
注2：FineReport10.0 平台采用了 AccessToken 验证，勾选自动登录后，AccessToken 有效期为 14 天，超过 14 天需要重新登录。
![2020-07-28_16-10-12.png](https://help.fanruan.com/core/style/lod.png)
## 5\. 服务器其他设置
### 5.1 编辑服务器
内置的 Demo 服务器不支持编辑，右边没有编辑按钮。
用户添加的服务器提供编辑，点击右边的编辑按钮，进入手动编辑服务器界面，其他操作与添加服务器一致，如下图所示：
![222](https://help.fanruan.com/core/style/lod.png)
### 5.2 删除服务器
1）内置的 FineBI 服务器以及自己添加的服务器，都可以删除。
2）手指左滑，就可以删除。
3）手指不放往右滑动，可以取消删除。
4）点击删除按钮，弹出提示“是否确定删除该服务器”，点击确定则删除，点击取消不进行任何操作。
![image.png](https://help.fanruan.com/core/style/lod.png)
### 5.3 切换服务器
1）在服务器列表，单击服务器后切换到该服务器的登录界面。
2）再点击服务器，则当前登录界面对应的服务器处于选中状态。
![2020-07-03_10-42-55.png](https://help.fanruan.com/core/style/lod.png)
## 6\. 服务器连接失败
**问题描述：**
移动端预览时，扫描二维码后提示服务器连接失败或无法打开网页。如下图所示：
![1576487651959562.jpg](https://help.fanruan.com/core/style/lod.png)
### 6.1 未配置网络环境
**原因分析：** 未配置移动设备与与电脑处于同一网络环境下。
解决方法：详情请参见本文 2.1 节。
### 6.2 防火墙阻拦
**原因分析：** 若确认已经按照文档流程操作且应用配置符合要求，该报错可能是由 Windows 防火墙引起。
**解决方案：** 用户可直接关闭 Windows 防火墙，再进行移动端预览操作即可。或按照下文设置 Windows 防火墙打开未允许端口。
1）打开「Windows安全中心>防火墙和网络保护>高级设置」，选择「入站规则>新建规则」，如下图所示：
![1.png](https://help.fanruan.com/core/style/lod.png)
2）设置规则类型为「端口」，协议为「TCP」，端口为特定本地端口，设置为工程端口，保存即可。如下图所示：
![2.png](https://help.fanruan.com/core/style/lod.png)
### 6.3 手机跟服务器不在同一网络
如果是在内网环境下，出现服务器连接失败的问题，需要先确认下自己的手机跟服务器是否在同一网络下。
![1608688641740992.png](https://help.fanruan.com/core/style/lod.png)
### 6.4 移动平台用户限制
「用户管理」配置了 [平台使用用户](<https://help.fanruan.com/finebi7.0/doc-view-170.html#9>) 后，未在「移动端使用用户」中添加对应用户导致的报错「您暂无权使用移动端，请联系管理员」。
![b4a5451b1365a14d2c6c7bcf40f23705.jpg](https://help.fanruan.com/core/style/lod.png)
可以使用默认的不限人数的设置方式，或者在移动端使用用户中，添加对应的用户。详情参考 [平台使用用户](<https://help.fanruan.com/finebi7.0/doc-view-170.html#9>) 。
![](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：HTML5端如何访问FineBI](<index.php?doc-view-452.html>)
[下一篇：移动端查看技巧 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-412.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
