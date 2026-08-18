---
title: Excel 上传失败
doc_id: 830
url: https://help.fanruan.com/finebi/doc-view-830.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:56
version: "7.X"
---

> 1. CSV 文件上传失败1.1 问题描述添加 Excel 数据集，选择 CSV 文件，上传失败。如下图所示：1.2 原因分析CSV 文件的本身漏洞导致了它有信息泄露的风险，所以 FineBI 对 CS

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Excel 上传失败
[__](<doc-edit-830.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[10](<edition-list-830.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-07-07 
[](<javascript:;>) [](<javascript:>)
## 1\. CSV 文件上传失败
### 1.1 问题描述
添加 Excel 数据集，选择 CSV 文件，上传失败。如下图所示：
![128.png](https://help.fanruan.com/core/style/lod.png)
### 1.2 原因分析
CSV 文件的本身漏洞导致了它有信息泄露的风险，所以 FineBI 对 CSV 文件的上传做了一定的限制。
### 1.3 解决方法
进入管理系统>安全管理,关闭文件上传校验的按钮，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 2\. 集群环境下上传大数据量 Excel 失败
### 2.1 问题描述
集群环境下，导入大数据量 Excel 时出现上传失败弹窗，如下图所示：FT
![132.png](https://help.fanruan.com/core/style/lod.png)
### 2.2 原因分析
上传 Excel 的大小超过了最大限制量。
### 2.3 解决方法
打开集群环境下/usr/nginx/conf/nginx.conf文件，查看并调整 Excel 文件上传大小的限制量，如下图所示：
详细请参见：[niginx_conf](<https://help.fanruan.com/finereport/doc-view-2815.html>)
![image.png](https://help.fanruan.com/core/style/lod.png)
## 3\. Excel、图片同时上传失败
### 3.1 问题描述
集群环境下 Excel 上传失败，并且在图片组件中上传图片也失败。
### 3.2 原因分析
集群配置时配置错误，导致文件用户与 FTP 的 user 不一致。   

### 3.3 解决方法
在配置 FTP 服务时可以看到 FTP 的 user 名，如何配置 FTP 服务（包括 FTP 用户名配置）详细请参见 ：
[Linux系统安装配置FTP](<https://help.fanruan.com/finereport/doc-view-2645.html>)
[Windows系统配置FTP服务](<https://help.fanruan.com/finereport/doc-view-2817.html>)
选择管理系统>集群配置，将文件用户名改成与 FTP 的用户名一致，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 4\. 加密的 Excel 上传失败
### 4.1 问题描述
设置了密码的 Excel 文件上传失败。  

### 4.2 原因分析
加密过的 Excel 无法上传到 FineBI。
### 4.3 解决方法
对 Excel 加密文件解除加密后，该文件即可上传 FineBI。
### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：上传 Excel 能被正确识别的字段类型](<index.php?doc-view-628.html>)
[下一篇：Excel 数据集常见问题 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-831.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
