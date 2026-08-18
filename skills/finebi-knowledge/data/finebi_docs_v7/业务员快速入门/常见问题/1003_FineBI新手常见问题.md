---
title: FineBI新手常见问题
doc_id: 1003
url: https://help.fanruan.com/finebi/doc-view-1003.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:17:16
version: "7.X"
---

> 概述整理了一些新手常见的问题，方便大家学习。内容在持续补充中~我的分析-框架Q：组件里对字段进行过滤、复制、重命名，为何数据中的表字段没有变化？A：分析主题的表，只有编辑数据时会改变表的内容。组件中分析

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI新手常见问题
[__](<doc-edit-1003.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[49](<edition-list-1003.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2023-08-22 
[](<javascript:;>) [](<javascript:>)
## 概述
整理了一些新手常见的问题，方便大家学习。内容在持续补充中~
## 我的分析-框架
#### **Q：组件里对字段进行过滤、复制、重命名，为何数据中的表字段没有变化？**
A：分析主题的表，只有编辑数据时会改变表的内容。
组件中分析时：
  * 左侧待分析区域的操作（复制、明细过滤、删除）会同步到分析主题的模型中（这是前端看不到的），在制作组件可反复使用，但不会同步到组件的来源表
  * 右侧分析区域制作组件的操作，只会保存在当前组件中，不会同步。


#### **Q：计算字段入口找不到了？**
A：在 FineBI 6.0.8 迭代改变了计算字段的入口，在「...」中添加。
![2023-08-22_15-46-10.png](https://help.fanruan.com/core/style/lod.png)
## 我的分析-数据
#### **添加数据  
**
#### **Q：找不到添加excel的入口**
A：在「我的分析>分析主题>数据>添加>上传Excel文件」中添加。详情参见文档：[添加Excel数据](<https://help.fanruan.com/finebi7.0/doc-view-1903.html>)
![2022-11-10_14-00-08.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：上传到BI的excel字段类型变了/乱码**
A：点击表头，下拉修改字段类型。详情参见文档：[添加Excel数据](<https://help.fanruan.com/finebi7.0/doc-view-1903.html>)
![2022-11-10_14-01-18.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：无法成功上传excel**
A：可能原因如下。详情参见文档：[添加Excel数据](<https://help.fanruan.com/finebi7.0/doc-view-1903.html>)
1）FineBI 可上传的表类型为 csv、xls、xlsx 三种格式 。  

注：支持上传 2003 和 2007 版本且后缀为 xls、xlsx 的 Excel 文件，不支持上传保存类型为 Excel 5.0/95 的后缀为 xls 的 Excel 文件。不支持上传加密 Excel 文件。
2）在上传 csv 格式文件前，需要进入「管理系统>安全管理>安全防护 」中，关闭「文件上传校验」，才能上传成功。  

3）上传前需要确认，添加的 Excel 首行不能有合并单元格，否则会上传失败。  

4）上传的 Excel 中不能有 Excel 函数计算的内容，例如：vlookup，sumifs 函数等。  

#### **Q：怎么更新excel**
A：在「我的分析>分析主题>数据」中选择改表，进入编辑状态。选择分析步骤第一步「数据>...>更新Excel」。
![2022-11-10_14-07-56.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：是否可以跨主题添加数据**
A：可以。详情参见：[添加当前工程上的数据](<https://help.fanruan.com/finebi7.0/doc-view-1902.html>)
#### **Q：添加数据后，在【我的分析】列表看不到该数据**
A：需要刷新界面。
#### **Q：公共数据添加到分析主题，数据膨胀会不会影响性能**
A：如果引用公共的数据不编辑的话逻辑上是最简表，顶多就是配置存储多一点影响不大，不会影响整体编辑性能
#### **编辑数据**
#### **Q：点了【保存】之后组件数据没更新**
A：需要点击「保存并更新」，数据才会更新。
#### **Q：添加公共数据后编辑，会不会影响公共数据**
A：不会，添加到分析主题的数据，是公共数据的子表
#### **Q：数据发布之后再进行编辑，会不会影响发布在公共数据里的数据集**
A：会的。
## 我的分析-组件
#### **Q：怎么复用组件**
A：在分析主题编辑界面。点击组件tab，选择「复制到」。
![2022-11-10_14-12-12.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：怎么生成图例**
A：在 [图表属性](<https://help.fanruan.com/finebi7.0/doc-view-219.html>) 中的颜色、大小、形状、热力色、半径中添加字段，则可生成对应图例。
#### **Q：表格字体怎么居中**
A：在「组件样式」中设置表格字体。详情参见：[表格字体](<https://help.fanruan.com/finebi7.0/doc-view-1694.html>)
####   

## 我的分析-仪表板
#### **Q：仪表板内对组件过滤了，但是组件编辑页面没变化**
A：组件里面是不受外面的过滤组件影响的，添加到仪表板里面才影响。
## 分享协作
#### **Q：怎样分享分析内容**
A：点击仪表板tab，选择想要分享的方式。详情参见文档：[分享分析案例](<https://help.fanruan.com/finebi7.0/doc-view-1984.html>)
![2022-11-10_13-40-01.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：分享方式的区别**
A：详情参见文档：[分享分析案例](<https://help.fanruan.com/finebi7.0/doc-view-1984.html>)
  * **协作** ：通过协作可以分享整个分析主题，用户能知道分析结果是如何一步步得到的 ；还支持多个用户协同编辑分析主题。
  * **发布** ：将仪表板发布到目录、将个人数据发布到公共数据，给企业其他用户查看；比较固定，适合给企业部门同事长期查看。
  * **分享公共链接** ：不需要登录 BI ，即可查看；比较灵活，适合小群体查看。


#### **Q：是否可多人同时协作**
A：可以。
详情参见文档：[协作](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)
#### **Q：协作可以只查看吗**
A：可以。
详情参见文档：[协作](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)
#### **Q：发布一定要管理员审批吗**
A：如果有发布目录节点的管理权限，并且发布选择了改路径，可以不用审批。
详情参见文档：[](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)[发布仪表板](<https://help.fanruan.com/finebi7.0/doc-view-165.html>)
#### **Q：怎么取消发布**
A：在分析主题，找到仪表板，取消发布。详情参见文档：[发布仪表板](<https://help.fanruan.com/finebi7.0/doc-view-165.html>)
![2022-11-10_13-44-54.png](https://help.fanruan.com/core/style/lod.png)
#### **Q：【添加协作者】里面找不到想要协作的人**
A：管理员需要先设置这个用户可协作给谁，「普通权限配置->权限快速配置->部门/角色->共享权限->资源协作」。
详情参见文档：[协作](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)
#### **Q：公共链接打不开**
A：详情参见文档：[公共链接分享仪表板](<https://help.fanruan.com/finebi7.0/doc-view-164.html>) 第4节
  * 若使用的局域网，则分享者和被分享者需在在同一局域网内才能访问。
  * 若用户把 bi 工程安装在本地，没有部署到外网可以访问的服务器上，比如访问地址为：http://localhost:37799/webroot/decision，则生成的仪表板公共链接也为 localhost 开头的链接。该链接直接复制分享给非本机的用户是没法访问的，需要将该 localhost 改成当前服务器的 IP 。
  * 若是用户使用的 FineBI 端口不是37799，就需要在防火墙入站规则中将特地本地端口更改成用户自己的端口号。


#### **Q：看不到某个发布到目录的仪表板/看不到仪表板内数据**
A：没有改仪表板的数据权限。
详情参见文档：[数据权限概述](<https://help.fanruan.com/finebi7.0/doc-view-248.html>)
  

## 更多问题
更多BI使用问题查看：[BI使用问题汇总](<https://help.fanruan.com/finebi7.0/doc-view-2049.html>)
#### **Q：回收站是否会按时自动清空**
否，需要自己手动清理。详情请参见：[回收站](<https://help.fanruan.com/finebi7.0/doc-view-1953.html>)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [业务员快速入门](<category-view-96>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI使用问题汇总](<index.php?doc-view-2049.html>)
[下一篇：分析主题简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2769.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
