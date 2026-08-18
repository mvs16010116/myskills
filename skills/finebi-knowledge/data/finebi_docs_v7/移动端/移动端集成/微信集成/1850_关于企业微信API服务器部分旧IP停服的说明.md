---
title: 关于企业微信API服务器部分旧IP停服的说明
doc_id: 1850
url: https://help.fanruan.com/finebi/doc-view-1850.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:31:37
version: "7.X"
---

> 1. 概述1.1 背景说明企业微信发布了公告，由于运营商机房裁撤，企业微信 api 接口域名 qyapi.weixin.qq.com 的 IP 会停用部分旧 IP ，并启用新的IP地址。详情可以参考：h

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 关于企业微信API服务器部分旧IP停服的说明
[__](<doc-edit-1850.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[2](<edition-list-1850.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2022-05-12 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 背景说明
企业微信发布了公告，由于运营商机房裁撤，企业微信 api 接口域名 qyapi.weixin.qq.com 的 IP 会停用部分旧 IP ，并启用新的IP地址。
详情可以参考：<https://developer.work.weixin.qq.com/community/announcement/detail?content_id=16311614294857467685>
![2022-05-12_14-01-00.jpg](https://help.fanruan.com/core/style/lod.png)
### 1.2 对企业微信集成的影响
**企业微信插件代码中是使用的域名，没有使用IP地址。所以对大部分客户是没有影响的。只有部分以下场景的客户可能会有影响。**
**  
**
1）若客户的网络环境是配置了 host 或者防火墙配置只放开固定 IP 的方式来访问。则需要排查一下是否还在使用旧的 IP 地址。
DNS 已下线、将停服的旧 IP 列表：
[code]
    183.3.234.106   //2022.5.30停服  
      
    58.251.80.106   //2022.5.30停服  
      
    157.255.173.237   //2022.5.30停服  
      
    121.51.130.85   //2022.5.30停服  
      
    140.207.189.106   //2022.5.30停服  
      
    182.254.34.117  //2022.5.30停服  
      
    116.128.138.166  //2022.5.30停服  
      
    101.89.18.159  //2022.5.30停服  
      
    100.107.159.103  //2022.5.30停服  
      
    101.226.129.166 //2022.11.30停服  
      
    180.97.117.89 //2022.11.30停服  
      
    101.89.18.158 //2022.11.30停服  
      
    116.128.164.38 //2022.11.30停服  
      
    116.128.138.160 //2022.11.30停服  
      
    117.184.242.103 //2022.11.30停服  
      
    183.192.202.172 //2022.11.30停服  
      
    182.254.11.176 //2022.11.30停服  
      
    121.51.86.66 //2022.11.30停服  
      
    183.3.224.149 //2022.11.30停服  
      
    112.60.18.78 //2022.11.30停服  
      
    112.60.18.81 //2022.11.30停服  
      
    121.51.140.149 //2022.11.30停服  
      
    203.205.219.41 //2022.11.30停服  
      
    203.205.255.254 //2022.11.30停服  
    
[/code]
2）如果使用即将停服的旧 IP ，会有如下现象：
某个日期开始突然出现（比如5月30号、11月30号）添加应用失败、通讯录获取失败、推送失败、单点失败、创建群聊失败等。此时：
  * [微信调试工具](<https://help.fanruan.com/finereport/doc-view-2444.html#5>) 获取 AccessToken 失败
  * F12报错则是：网络异常，请检查网络配置


## 2\. 排查方式
1）通过 ping qyapi.weixin.qq.com，如果依然是旧 IP ，可能配置了 host ；
  * linux 环境请检查： /etc/hosts
  * windows 环境请检查：C:\Windows\System32\drivers\etc\hosts


2）通过 nslookup qyapi.weixin.qq.com 或者 dig qyapi.weixin.qq.com，出来的 A 记录如果依然包含有旧 IP ，可能 DNS 有缓存，请联系 DNS 管理员定位；
3）如果通过 nginx 来反向代理出口访问的，可查看 nginx 的访问日志看是否依然有请求到旧 IP 。如果有，请检查 nginx 的 resolver 配置是否和机器系统配置的 DNS 一致，也可通过重启 nginx 试试；
4）检查调用 qyapi.weixin.qq.com 程序代码里面是否有写死就 IP 访问的情况，请改为域名访问，可通过 tcpdump -i any -n host xxx.xxx.xxx.xxx and dst port 443 抓包检查是否依然有请求旧IP。（其中xxx.xxx.xxx.xxx请替换为某个旧IP）
## 3\. 获取最新IP的地址
1）最好不要通过配置死 IP 的方式来访问 qyapi.weixin.qq.com ，以免企业微信后续更新IP时造成访问失败；
2）如需获取 qyapi.weixin.qq.com 的最新接入IP，请通过 DNS 解析来获取，或者通过 [企业微信api地址接口](<https://developer.work.weixin.qq.com/document/path/92520?version=4.0.2.6023&platform=win>) 来获取。
### 附件列表 
  
下载次数：：0
    
**主题：** [移动端](<category-view-102>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：微信消息推送](<index.php?doc-view-1732.html>)
[下一篇：微信集成 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-348.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
