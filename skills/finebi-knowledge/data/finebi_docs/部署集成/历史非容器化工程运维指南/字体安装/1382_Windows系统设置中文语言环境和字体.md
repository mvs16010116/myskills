---
title: Windows系统设置中文语言环境和字体
doc_id: 1382
url: https://help.fanruan.com/finebi6.X/doc-view-1382.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:33
---

> 提示:本文为第三方解决方案或非产品相关操作指南，仅提供给具备自主开发能力的用户使用。本文仅面向Windows服务器中非运维平台部署的帆软项目运维平台部署的项目，在工程外挂目录/customlib/fon

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# Windows系统设置中文语言环境和字体
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
* 历史版本：[10](<edition-list-1382.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-06-17 
[](<javascript:;>) [](<javascript:>)
![icon](/core/style/lod.png)提示:
**本文为第三方解决方案或非产品相关操作指南，仅提供给具备自主开发能力的用户使用。**
本文仅面向Windows服务器中**非运维平台部署** 的帆软项目
运维平台部署的项目，在**工程外挂目录/customlib/fonts** 文件夹中，可存放客户自定义的字体文件，等同于直接放置在工程的**/usr/share/fonts** 下
  

## 1\. 概述
### 1.1 问题描述
工程部署在Windows系统中时，有时我们访问工程会遇到中文乱码。
  * 服务器导出文字重叠。
  * 导出 pdf 时图表里的中文变成框框。
  * 插入斜线乱码，斜线为方框。


### 1.2 原因分析
出现这个情况有多种原因：
1）工程所在的Windows服务器，没有设置中文为默认语言。
2）工程所在的Windows服务器，没有安装模板对应的字体包。
本文以 Windows11 系统为例。其他 Windows 版本安装步骤有所不同，请根据你的系统需求自行调整。
注：需要排查集群全部工程节点所在服务器、用户客户端环境。
## 2\. 更改系统区域和语言设置
管理员应当确认Windows服务器中的系统区域是否是中国。
1）打开控制面板，进入「时间和语言」（Windows11）/「时钟和区域」（Windows10）/「区域和语言」（Windows7和Windows Server 2008）。
2）在「区域」或「格式」选项卡中，选择合适的区域和语言设置。
  * 国家或地区：选择「中国」
  * 区域格式：选择「推荐的项目」/中文(简体，中国)


3）点击「应用」或「确定」，然后重新启动服务器。
![](/core/style/lod.png)
## 3\. 安装中文字体
### 3.1 检测缺失字体
**1）检查缺失字体**
仪表板中乱码的部分用的什么字体，为缺失字体。
假设分组表导出后，表头乱码，表头用的为黑体，则缺少黑体字体包。
![](/core/style/lod.png)
  

### 3.2 安装缺失字体
**1）下载字体文件**  

请从信任的来源获取所需的字体文件，帆软不提供此部分资源。
通常字体文件是以 .ttf 或 .otf 扩展名结尾的文件。
**2）安装字体**
请将字体文件上传到需要安装字体的Windows服务器。
选中该文件，右键，点击「安装」即可。
![](/core/style/lod.png)
**3）重启工程**
字体安装好后，重启FineBI工程。预览、导出、打印时就会显示处对应的字体。
注：字体安装好后，若遇到读取不到字体的情况，可以将字体拷贝到服务器 JDK_HOME/jre/lib/fonts 目录下，重启工程所在的Tomcat容器。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Linux系统设置中文语言环境和字体](<index.php?doc-view-1381.html>)
[下一篇：平台字体可配置插件 ![](/core/style/forward.png) ](<index.php?doc-view-2363.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
