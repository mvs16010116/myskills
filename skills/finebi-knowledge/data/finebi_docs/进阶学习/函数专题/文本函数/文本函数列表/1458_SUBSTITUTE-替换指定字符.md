---
title: SUBSTITUTE-替换指定字符
doc_id: 1458
url: https://help.fanruan.com/finebi6.X/doc-view-1458.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:03:59
---

> 1. 概念语法SUBSTITUTE(text,old_text,new_text,instance_num)用 new_text 替换文本串中的 old_text&nbsp;参数1text文本串参数2o

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# SUBSTITUTE-替换指定字符
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1458.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2023-02-07 
[](<javascript:;>) [](<javascript:>)
## 1\. 概念
语法| SUBSTITUTE(text,old_text,new_text,instance_num)| 用 new_text 替换文本串中的 old_text   
---|---|---  
参数1| text| 文本串  
参数2| old_text| 旧文本串  
参数3| new_text| 新文本串  
参数4| instance_num| 指定位置  
  * 如果需要替换字段值中的指定文本，则使用 SUBSTITUTE 函数；  

  * 如果需要替换字段值中指定位置上的任意文本，则使用 [REPLACE-替换指定位置字符](<https://help.fanruan.com/finebi6.0/doc-view-1469.html>) 函数。


## 2\. 注意事项
  * 直连数据中无法使用此函数。  

  * 参数1、2、3可使用任意类型参数；第四个参数是数值参数，可以缺省。


## 3\. 示例
例如想要把客户名称中的「有限公司」替换为「分公司」，输入公式：SUBSTITUTE(客户名称,"有限公司","分公司")，如下图所示：
![2022-08-30_16-12-49.png](/core/style/lod.png)
更多示例：
公式| 结果| 备注  
---|---|---  
SUBSTITUTE("data base","base","model")| data model|   
  
SUBSTITUTE("July 28, 2000","2","1",1)| July 18, 2000|   
  
SUBSTITUTE("July 28, 2000","2","1")| July 18, 1000|   
  
SUBSTITUTE("July 28, 2000","2","1",2)| July 28, 1000|   
  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](/core/style/back.png)上一篇：TODOUBLE-将文本转换成 Double 对象](<index.php?doc-view-1466.html>)
[下一篇：STARTWITH-判断字符串 str1 是否以 str2 开始 ![](/core/style/forward.png) ](<index.php?doc-view-1477.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
