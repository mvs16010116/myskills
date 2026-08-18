---
title: App打包配置iOS证书
doc_id: 956
url: https://help.fanruan.com/finebi6.X/doc-view-956.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:12:40
---

> 1. 概述该操作是 App 打包前的准备工作，请需要生成 iOS 版 App 的用户执行该操作。2. 获取证书使用企业开发者账号获取 iOS 证书的步骤请参考：1）申请 iOS 企业开发者账号2）获取&

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# App打包配置iOS证书
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[4](<edition-list-956.html>)
* 最近更新：[Fay](<user-space-1771067.html>) 于 2022-12-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
该操作是 App 打包前的准备工作，请需要生成 iOS 版 App 的用户执行该操作。
## 2\. 获取证书
使用企业开发者账号获取 iOS 证书的步骤请参考：
1）[申请 iOS 企业开发者账号](<https://help.fanruan.com/finebi6.0/doc-view-954.html>)
2）[获取 iOS 证书](<https://help.fanruan.com/finebi6.0/doc-view-955.html>)
注1：帆软 App 打包仅支持通过企业开发者账号获取 iOS 证书，不支持个人/公司开发者账号获取的证书。
注2：iOS证书中如不包含消息推送功能，则无法使用 [帆软 App 消息推送功能](<https://help.fanruan.com/finereport/doc-view-3027.html>) 。
## 3\. 配置证书
### 3.1 登录帆软市场
登录 [帆软市场](<https://market.fanruan.com/usercenter/appoem>)，进入用户中心，在用户信息下找到App 打包>iOS企业证书，如下图所示：  

注：进入 App 打包页面后，如果没有开通该功能，需要联系销售开通服务。
![image.png](/core/style/lod.png)
### 3.2 上传证书
在 App 打包页面，选择 iOS 企业证书，上传xx.p12和xx.mobileprovision文件，并输入certificate password。
上传后，点击检查证书，会自动读取到bundle id和过期时间。
![image.png](/core/style/lod.png)
若读取到的bundle id中含有通配符，则输入框中提示「当前证书bundle id为xx.xx.＊，＊号通配符可自定义」。
此时用户可手动编辑bundle id，*号可修改为数字、大小写字母、“.”的任意组合，修改完成后自动触发校验。
注1：若修改后的 bundle id 不符合规则，则提示「证书校验不合格，appID/budle id 格式错误」，如下图所示：
![](/core/style/lod.png)
注2：若证书校验出错，则提示「证书校验不合格，错误代码：XXX」，详情请参见：[App 打包错误码一览](<https://help.fanruan.com/finereport/doc-view-3536.html>)
![](/core/style/lod.png)
### 3.3 保存证书
点击保存，配置好的 iOS 企业证书如下图所示：
![](/core/style/lod.png)
## 4\. 更换证书
iOS 企业证书有效期三年，Profile 文件有效期一年。
App 的唯一标识是 AppID ，App 是由 Profile 文件打出来的，因此最多使用一年。  

App 到了使用期限后将无法使用，因此需要及时使用最新的证书 / Profile文件重新 OEM 打包，并下发给最终用户更新。  

重新打包以后，只要 Profile 文件对应的 AppID 不变，打包生成的新 App 可以在原 App 基础上时更新覆盖，无需卸载重装。
### 4.1 申请新证书
用户可参考 [获取 iOS 证书第 6、7 章](<https://help.fanruan.com/finebi6.0/doc-view-955.html>) 重新申请新证书。但需注意以下几点：  

  * 不要轻易撤销证书（有效期三年），证书被撤销后，该证书相关的所有App都将无法使用。
  * 撤销证书前，请确保所有使用该证书的最终用户都已经更新到新证书打包的App。
  * 证书最多同时申请两个。
  * Profile文件（有效期一年）到期前（建议提前3-6个月），请及时创建新的Profile文件（关联相同的AppID），并使用新的Profile文件打包新的App下发给最终用户更新。


### 4.2 上传新证书
登录商城 OEM，进入 App 打包，点击「申请修改证书」，更换证书原因填写「证书过期更换」。
帆软工作人员将于 1 个工作日内进行审核并反馈结果，请耐心等待。
![](/core/style/lod.png)
注：推荐用户采用版本更新控制，详见 [如何实现版本自主管理](<https://wiki.fanruan.com/pages/viewpage.action?pageId=8880206>)，当 App 需要变更时，用户端可以自动提示有新版本并可强制更新。
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](/core/style/back.png)上一篇：获取iOS证书](<index.php?doc-view-955.html>)
[下一篇：App打包配置iOS自定义证书 ![](/core/style/forward.png) ](<index.php?doc-view-1639.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
