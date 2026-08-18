---
title: Custom App分发插件
doc_id: 1643
url: https://help.fanruan.com/finebi/doc-view-1643.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:32:00
version: "7.X"
---

> 1. 概述1.1 应用场景Custom App打包发布后，无法上架商城，需要通过分发下载链接的形式，让 App 用户下载。1.2 功能简介在自己的工程上安装 Custom App分发插件，插件中实现动态

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Custom App分发插件
[__](<doc-edit-1643.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-1643.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-01-13 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
Custom App打包发布后，无法上架商城，需要通过分发下载链接的形式，让 App 用户下载。
### 1.2 功能简介
在自己的工程上安装 Custom App分发插件，插件中实现动态生成兑换码安装链接，安装打包发布好的 Custom App。
## 2\. 操作步骤
### 2.1 准备工作
#### 2.1.1 成功打包发布 Custom App  

1）成功申请到[](<https://help.fanruan.com/finereport/doc-view-4252.html>)[iOS自定义证书](<https://help.fanruan.com/finebi7.0/doc-view-1639.html>)。  

2）完成[ Custom App打包发布](<https://help.fanruan.com/finebi7.0/doc-view-344.html>)。
#### 2.1.2 获取Excel兑换码文件  

Custom App分发需要用到该兑换码 Excel 文件，在客户的商务组织账号管理台进行操作。
1）购买App安装许可  

Custom App 打包成功后，会自动提交苹果进行审核。审核完毕，在客户的商务组织账号管理台「自定 App」可以看到发布的应用。  

我们需要购买该自定 App的安装许可，选择「兑换码」许可类型，「数量」设置足够多，点击「获取」即可，目前自定APP的安装许可免费。如下图所示：
![1634110989712873.png](https://help.fanruan.com/core/style/lod.png)
2）获取兑换码  

获取之后，苹果会返回兑换码清单，需要将兑换码发放给 App 用户，才可以进行安装，且每个兑换码只能被使用一次。
点击「下载」即可获取兑换码 Excel ，如下图所示：
注：终端用户下载后，若app更新，将会自动更新，不需要使用兑换码重新安装。
![1634111439577425.png](https://help.fanruan.com/core/style/lod.png)
### 2.2 安装插件
插件下载请点击：[Custom App分发](<https://market.fanruan.com/plugin/53da7bd8-596b-494c-85ae-837b5e329c5a>)
安装方法请参见：[插件管理](<https://help.fanruan.com/finebi7.0/doc-view-459.html>)
### 2.3 新建Custom App
安装好插件后，进入「管理系统>Custom App分发」，点击「创建Custom App」，输出Custom App名称后点击「确认」成功创建。如下图所示：
![2021-10-18_15-24-32.png](https://help.fanruan.com/core/style/lod.png)
### 2.4 上传 Excel 兑换码
对已新建的 Custom App 点击「上传」按钮。选择 2.1.2 节已经下载好的 Excel 兑换码文件上传。如下图所示：
![2021-10-18_15-28-56.png](https://help.fanruan.com/core/style/lod.png)
上传成功后，灰化的「超链接」按钮变为可选状态。显示上传的兑换码数量信息。如下图所示：
注：上传后显示兑换码总数及可用兑换码数，每次刷新Custom App分发页面时，都会重新读取最新数据（如果快用完了，可以重新上传兑换码）。
![2021-10-18_15-35-25.png](https://help.fanruan.com/core/style/lod.png)
### 2.5 分发App下载连接
上传成功即可，点击「超链接」按钮，「复制链接」，将 Custom App 的下载连接分发给用户。如下图所示：
注：若当前 App 被删除了，历史生成的下载链接将无法使用。
![2021-10-18_15-36-23.png](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：App打包支持版本管理](<index.php?doc-view-2124.html>)
[下一篇：移动端常见问题 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2023.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
