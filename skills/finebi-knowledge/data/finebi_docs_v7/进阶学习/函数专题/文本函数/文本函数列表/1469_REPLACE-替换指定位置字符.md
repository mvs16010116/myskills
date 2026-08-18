---
title: REPLACE-替换指定位置字符
doc_id: 1469
url: https://help.fanruan.com/finebi/doc-view-1469.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:22:06
version: "7.X"
---

> 1. 用法一：已知替换内容1）概述语法REPLACE(text,textorreplace,replacetext)根据指定的字符串，用其他文本来代替原始文本中的内容参数1text需要被替换部分字符的文

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# REPLACE-替换指定位置字符
[__](<doc-edit-1469.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[9](<edition-list-1469.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-06-10 
[](<javascript:;>) [](<javascript:>)
## 1\. 用法一：已知替换内容
**1）概述**
语法  
| REPLACE(text,textorreplace,replacetext)| 根据指定的字符串，用其他文本来代替原始文本中的内容  
---|---|---  
参数1| text| 需要被替换部分字符的文本  
参数2| textorreplace| 指定的字符串  
参数3| replacetext| 需要替换部分旧文本的文本  
**2）注意事项**
支持使用三个任意类型参数
**3）示例**
例如需要将公司名称中的「有限公司」替换为「股份公司」，如下图所示：**  
**
![](https://help.fanruan.com/core/style/lod.png)
添加[ 计算字段](<https://help.fanruan.com/finebi7.0/doc-view-118.html>)，输入公式：REPLACE(客户名称,"有限","股份")，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
更多示例：
公式| 结果| 备注  
---|---|---  
REPLACE("abcd","a","re")| rebcd| -  
REPLACE("a**d","**d","rose")| arose| -  
## 2\. 用法二：已知替换起始位置
**1）概述**
语法| REPLACE(old_text,start_num,num_chars,new_text)| 根据指定的字符数，用其他文本串来替换某个文本串中的部分内容  
---|---|---  
参数1| Old_text| 需要被替换部分字符的文本  
参数2| Start_num| 需要用new_text来替换old_text中字符的起始位置  
参数3| Num_chars| 需要用new_text来替换old_text中字符的个数  
参数4| New_text| 需要替换部分旧文本的文本  
**2）注意事项**
使用的四个参数，第一个需要是任意类型，第二个第三个需要是数值类型，第四个需要是任意类型。
**3）实例**
例如对电话数据进行脱敏处理，
![](https://help.fanruan.com/core/style/lod.png)
公式| 结果| 备注  
---|---|---  
REPLACE("0123456789",5,4,"*")| 0123*89| -  
REPLACE("1980",3,2,"99")| 1999| -  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [进阶学习](<category-view-254>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：RIGHT-截取后几个字符串](<index.php?doc-view-1465.html>)
[下一篇：REPEAT-重复显示文本 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1462.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
