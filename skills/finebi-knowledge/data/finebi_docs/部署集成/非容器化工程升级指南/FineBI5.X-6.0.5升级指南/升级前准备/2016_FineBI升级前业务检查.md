---
title: FineBI升级前业务检查
doc_id: 2016
url: https://help.fanruan.com/finebi6.X/doc-view-2016.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:56
---

> 1. 概述1.1 应用场景FineBI 5.1升级到6.0。升级前后对模板、数据集进行检查。1.2 功能简介FineBI检查工具，可以进行模板检查和数据集检查。模板检查工具：自动预览BI目录中的所有模板

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI升级前业务检查
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[8](<edition-list-2016.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-07-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
FineBI 5.1升级到6.0。升级前后对模板、数据集进行检查。  

### 1.2 功能简介
FineBI检查工具，可以进行模板检查和数据集检查。  

  * 模板检查工具：自动预览BI目录中的所有模板，截图并记录模板中是否有组件报错。（原理是页面自动化，控制浏览器逐个点击预览模板。运行速度较慢）
  * 数据集检查工具：自动预览BI中的所有数据集，包括数据库表、SQL数据集、Excel数据集、自助数据集。输出报告中会列出所有预览异常的表。（原理是web接口自动化，默认使用多线程，运行速度快）


注：工具只支撑在 windows系统运行。
## 2\. 准备工作
1）BI工程的「外观配置>平台主题」设为默认的“经典”主题。
2）为了尽量保证模板截图的效果，建议禁用插件：FineBI小助手插件、BI新手引导插件。
3）保证执行工具的账号，在工具执行过程中，不会在其他浏览器登录。
4）下载FineBI检查工具：[FineBI检查工具](<https://fine-build.oss-cn-shanghai.aliyuncs.com/test_tools/FineBI%E6%A3%80%E6%9F%A5%E5%B7%A5%E5%85%B7/FineBI%E6%A3%80%E6%9F%A5%E5%B7%A5%E5%85%B7-windows.zip>)
## 3\. 运行生成升级报告
下载并解压zip文件，找到FineBI检查工具1.x.x.exe，双击运行。
![2022-09-26_13-44-56.png](/core/style/lod.png)
### 3.1 模板检查工具
主界面默认是模板检查工具的参数面板：
![2022-09-26_13-46-47.png](/core/style/lod.png)
输入FineBI工程的URL、账号、密码，点击测试连接，可以测试与工程的连接情况。
![2022-09-26_13-47-17.png](/core/style/lod.png)
工具配置介绍：
设置项| 说明  
---|---  
输出路径| 输出结果的存放路径  
预览模式| 隐藏或展示模板遍历过程  
  
开始序号| 从第N张模板开始预览  
  
终止序号| 到第N张模板结束预览  
  
设置完工具配置，点击「开始运行」。需要设置输出报告文件夹名称。如下图所示：
如果未设置输出路径，此处会弹出结果存放路径。
![2022-09-26_14-46-44.png](/core/style/lod.png)
完成后，可在路径下查看运行结果。如下图所示：
![2022-09-26_15-39-36.png](/core/style/lod.png)
设置完存放路径后。点击「结果对比」可以选择升级前后的csv文件进行对比，对比结束会显示对比结果的存放路径。如下图所示：
![2022-09-26_16-51-44.png](/core/style/lod.png)
在路径下查看报告。如下图所示：
![2022-09-26_18-05-11.png](/core/style/lod.png)
打开文件，可以查看检查工具升级前后生成的两个csv文件有何不同。如下图所示：
![2022-09-26_17-32-47.png](/core/style/lod.png)
### 3.2 数据集检查工具
1）点击「数据集检查工具」可以切换到对应的参数面板。
2）连接工程。输入 FineBI 工程的 URL、账号、密码， 然后点击「测试连接」，连接成功即可。
![](/core/style/lod.png)
3）进行工具配置。完成后点击「开始运行」。输入生成的检查报告名称。即可进入检查。如下图所示：
注：如工具配置界面有「血缘分析」、「忽略子表」、「更新信息」、「自助数据集详细步骤筛选」等按钮，请勿勾选，会导致检测失败。
![](/core/style/lod.png)
4）完成后在对应路径生成报告。如下图所示：
![](/core/style/lod.png)
生成的报告如下图所示：
![2022-09-26_18-14-34.png](/core/style/lod.png)
5）对生成的报告数据集检查.csv进行升级前后对比，点击「结果对比」。操作步骤同 3.1 节。
## 4\. 查看报告
工具运行结束后生成报告 report.html 和 report.csv 。如下图所示：
![2022-09-26_18-05-11.png](/core/style/lod.png)
### 4.1 模板检查报告
预览异常的模板会以黄色背景显示。如下图所示：
![图片1.png](/core/style/lod.png)
点击截图可以查看模板具体情况。如下图所示：
![图片2.png](/core/style/lod.png)
### 4.2 数据集检查报告
需要注意的是，数据集检查报告中只会记录预览异常的表，预览正常的表不会出现在报告中。
![图片3.png](/core/style/lod.png)
预览表常见的异常信息。如下表所示：
异常信息| 含义  
---|---  
计算结果为空| 预览显示"计算结果为空"  
标红| BI中标红显示的表  
更新失败| 表更新失败  
HTTPConnectionPool: Read timed out. (read timeout=30)| 响应超时。可能是表返回结果太慢，也可能是网络原因，需要实际预览一下看看  
errorMsg：数据集:cs 未抽取数据(分布式表[T_84617B]不存在), 请先抽取数据| 预览失败，点击"详细信息"看到的结果  
errorCode: 61300424| 返回的错误码  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：确认升级模式](<index.php?doc-view-2527.html>)
[下一篇：FineBI升级前环境检查 ![](/core/style/forward.png) ](<index.php?doc-view-2001.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
