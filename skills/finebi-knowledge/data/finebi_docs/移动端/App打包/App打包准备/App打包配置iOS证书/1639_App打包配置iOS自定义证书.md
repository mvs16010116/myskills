---
title: App打包配置iOS自定义证书
doc_id: 1639
url: https://help.fanruan.com/finebi6.X/doc-view-1639.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:12:40
---

> 1. 概述1.1 应用场景若用户无法申请到苹果企业账号，可通过 Custom App 模式，完成&nbsp;iOS 版 App&nbsp; 定制。1.2 功能简介该操作是&nbsp;App 打包&nbs

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# App打包配置iOS自定义证书
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[4](<edition-list-1639.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2021-11-05 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
若用户无法申请到苹果企业账号，可通过 Custom App 模式，完成 iOS 版 App 定制。
### 1.2 功能简介
该操作是 [App 打包](<https://help.fanruan.com/finebi6.0/doc-view-344.html>) 前的准备工作，请需要生成 iOS 版 App 的用户执行该操作。
## 2\. 材料准备
需要[申请苹果商务账号](<https://support.apple.com/zh-cn/guide/apple-business-manager/apd402206497/1/web/1>)。创建苹果商务组织账号(是为了在 App 打包后，分发的时候使用)，目的是为了接收 Custom App。
点击登录：[苹果商务账号](<https://business.apple.com/>)
## 3\. 配置证书
### 3.1 登录帆软市场
登录 [帆软市场](<https://market.fanruan.com/usercenter/appoem>)，进入「用户中心」，在用户信息下找到「App 打包>iOS自定义证书」，如下图所示：  

注：进入 App 打包页面后，如果没有开通该功能，需要联系销售开通服务。
![2021-10-09_16-05-21.png](/core/style/lod.png)
### 3.2 配置证书
在「iOS自定义证书」tab页下，填入对应内容。完成后点击「申请证书」。申请证书需要一天时间，请关注邮件反馈。
![图片12.png](/core/style/lod.png)
填写内容说明：
  * **appID/bundle id：** 必须以com.fr.oem.xxx开头；
  * **组织ID &组织名称：**在苹果商务账号中可以获得，点击「设置>注册信息>组织信息」获取；
![2021-10-09_16-55-39.png](/core/style/lod.png)  

  * **邮件：** 设置主要用于接收证书及打包发布过程的异常问题，需正确填写；
  * **测试登录名 &测试登录密码：**若 App 中内置了服务器地址，打包发布的 App 苹果审核时需要有测试账号可以登录，此处填写可以登录内置服务器的测试账号。


### 3.3 下载证书
配置好的 iOS 企业证书如下图所示，点击「下载证书」![1634540531836096.png](/core/style/lod.png)
### 3.4 使用证书
1）配置完证书后进行 App 打包。参考文档：[App打包](<https://help.fanruan.com/finebi6.0/doc-view-344.html>)
注：App 打包审核被拒的可能原因：1）App图标和名称不能体现主要功能；2）模版里面没有使用到定位权限。
2）完成 App 打包后，使用下载的「iOS自定义证书」进行信鸽推送配置，使用户能在终端查看 App 消息推送。参考文档：[App 打包支持消息推送](<https://help.fanruan.com/finebi6.0/doc-view-1147.html>)
3）Custom App打包发布后，无法上架商城，需要通过分发下载链接的形式，让 App 用户下载。参考文档：[App打包自动分发插件](<https://help.fanruan.com/finebi6.0/doc-view-1643.html>)
## 4\. 更换证书
登录商城 OEM，进入 App 打包，点击「申请修改证书」，填入相关信息后，点击「确定」提交申请。
帆软工作人员将于 1 个工作日内进行审核并反馈结果，请耐心等待。
![2021-10-09_17-35-36.png](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](/core/style/back.png)上一篇：App打包配置iOS证书](<index.php?doc-view-956.html>)
[下一篇：App打包 ![](/core/style/forward.png) ](<index.php?doc-view-344.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
