---
title: FineReport 设计器远程连接 FineBI 工程
doc_id: 931
url: https://help.fanruan.com/finebi6.X/doc-view-931.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:21
---

> 1. 概述1.1 版本远程连接需要 FineReport 和 FineBI 版本适配。请参见：FineBI&nbsp;与&nbsp;FineReport&nbsp;版本适配说明1.2 预期效果当 Fin

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineReport 设计器远程连接 FineBI 工程
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[16](<edition-list-931.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-02-28 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
远程连接需要 FineReport 和 FineBI 版本适配。请参见：[FineBI 与 FineReport 版本适配说明](<https://help.fanruan.com/finebi6.0/doc-view-1061.html>)  

### 1.2 预期效果
当 FineReport 设计器成功远程连接 FineBI ，点击「测试连接」会跳出远程连接成功提示，效果如下图所示：
![1578620310888372.png](/core/style/lod.png)
### 1.3 实现思路
在 Finereport 设计器上新建工作目录，配置 FineBI 服务器信息之后，测试连接成功，完成配置。
### 1.4 作用范围
使用 Finereport 设计器连接 FineBI 后，只有超级管理员能在 Finereport 设计器中 [创建服务器数据集](<https://help.fanruan.com/finebi6.0/doc-view-253.html>) ，其他用户可以进行 [远程连接](<https://help.fanruan.com/finereport/doc-view-902.html>)，但无法创建服务器数据集，无法对数据连接进行编辑，只能对有权限的数据连接进行使用。
## 2\. 操作步骤
### 2.1 下载安装 Finereport 设计器
下载安装 Finereport 设计器详情请参见：[设计器安装](<https://help.fanruan.com/finereport/doc-view-69.html>)
### 2.2 新建工作目录
下载安装完成后，需要将 Finereport 设计器与 BI 的服务器建立远程连接。
1）首先打开设计器，在菜单栏中选择「文件>切换工作目录>其他」，如下图所示：
![h.png](/core/style/lod.png)
2）在弹出的「配置工作目录」的界面中，点击+，新建一个远程服务器连接目录，如下图所示：
![1578573358130877.png](/core/style/lod.png)
### 2.3 配置 FineBI 远程服务器
新增了一项远程服务器连接之后，将远程服务器连接名修改为 FineBI ，右侧界面出现远程服务器的连接配置，填入需要的配置信息。
  * 配置信息如下表所示：

主机名/IP| BI 所在的主机名/IP  
---|---  
端口号| BI 对应端口号  
WEB应用| 默认 webroot  
Servlet| 默认 decison  
主机位置| BI 主机所在位置，默认为：http://${IP}:37799/webroot/decision  
用户名| BI 数据决策系统用户名（一般为管理员账户）注：若需要创建服务器数据集，需要使用超级管理员账户  
密码| BI 数据决策系统密码  
  * 远程服务器配置界面如下图所示：


![1578620169197822.png](/core/style/lod.png)
注：在进行远程连接时，请确保 BI 服务器已经运行。
### 2.3 测试连接
点击「测试连接」可以看到远程连接成功提示。点击「确定」，Finereport 与 BI 的远程连接建立成功。如下图所示：
![1578620310888372.png](/core/style/lod.png)
注：若提示远程连接失败，请查看日志是否提示没有注册远程设计功能点，具体请参见：[注册管理](<https://help.fanruan.com/finebi6.X/doc-view-177.html>) 文档中远程设计功能点相关内容。
## 3\. 注意事项
### 3.1 SAP BW 插件添加数据集字段显示异常
**问题描述**  

FineReport 设计器 [添加SAP BW数据集](<https://help.fanruan.com/finebi6.0/doc-view-256.html>)，FineReport 环境下数据集展示正常；FineReport 远程连接部署到 Weblogic 的 BI 工程后，添加 SAP BW 数据集，数据列名会部分转换为英文，如下图所示：
![1611884278133495.png](/core/style/lod.png)
**原因分析**
FineReport 和 FineBI 的语言环境不一致，修改 FineBI 的语言环境即可。
**解决方案：**
1）查看 FineReport 和 FineBI 环境的 SAP BW 插件版本，令其保持一致。
2）修改 FineBI 环境中，fine_conf_entity 表的LanguageConfig.locale字段值，值为zh_CN，修改后重启 FineBI 。
注：若没有该字段，需手动添加；由于 FineDB 的修改非常重要，影响较大，建议联系技术支持修改，技术支持联系方式：「[服务平台](<https://service.fanruan.com/>)>在线支持」、电话「400-811-8890」。
3）FineReport 切换工作目录到 FineBI 工程下，单元格中输入i18n("Fine-Plugin_SAPBW_Code")，获得的结果是中文的编码，为正常。
![4.png](/core/style/lod.png)
4）修改 FineBI 环境的系统语言。输入：LANG="Zn_CN.UTF-8"，查看系统语言：echo $LANG，如下图所示：
![1611886106260036.png](/core/style/lod.png)
5）重启 FineBI 。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineReport 集成到 FineBI](<index.php?doc-view-67.html>)
[下一篇：报表对接简道云插件 ![](/core/style/forward.png) ](<index.php?doc-view-1521.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
