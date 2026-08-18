---
title: FineBI6.0.x小版本升级注意事项
doc_id: 2359
url: https://help.fanruan.com/finebi6.X/doc-view-2359.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:53
---

> 概述本文详细讲解 FineBI6.0 各个小版本之间升级的注意事项和兼容说明。6.0.181）取消内置FineDataLinkFineBI6.0.18 版本开始，不再内置 FineDataLink 相关

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineBI6.0.x小版本升级注意事项
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Carly](<user-space-222366.html>)_
* 历史版本：[6](<edition-list-2359.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2024-11-18 
[](<javascript:;>) [](<javascript:>)
## 概述
本文详细讲解 FineBI6.0 各个小版本之间升级的注意事项和兼容说明。  

## 6.0.18
#### **1）取消内置FineDataLink**  

FineBI6.0.18 版本开始，不再内置 FineDataLink 相关功能依赖的 JAR 包。  

建议升级到FineBI6.0.18及以上版本后，如需使用FineDataLink，请独立部署。
#### **2）取消内置 postgresql 相关驱动**
FineBI6.0.18 版本开始，fine-bi-engine-third-6.0.jar 中移除 postgresql 相关驱动
用户如需使用相关数据连接（postgresql、华为DWS等），必须确保已通过驱动管理手动上传相关驱动
## 6.0.17
#### **1）内置 FineDataLink4.1 版本 JAR 包**  

FineBI6.0.17版本，内置 FineDataLink4.1 版本 JAR 包。
升级前  
| 升级注意事项  
---|---  
FineBI未集成FineDataLink| 1）参考 [6.0.5之后的版本升级](<https://help.fanruan.com/finebi6.X/doc-view-2126.html>) 正常升级FineBI即可2）升级后产品内置 FineDataLink4.1 模块，如原本注册 license 不包含 FineDataLink 相关功能点，则 FineDataLink 功能显示为未注册状态，如需使用可联系销售增购  
FineBI集成FineDataLink4.1版本| 1）手动删除%Tomcat_HOME%/webapps/webroot/WEB-INF/lib目录下 fdl-xxx.jar 包2）再参考 [6.0.5之后的版本升级](<https://help.fanruan.com/finebi6.X/doc-view-2126.html>) 正常升级 FineBI3）升级后产品内置 FineDataLink4.1 模块，可正常使用  
FineBI集成FineDataLink4.0版本| **注意事项** 1）无法保留 FineDataLink4.0 版本，必须升级至 FineDataLink4.1 版本2）FineDataLink 4.1 版本功能点注册与 4.0 不兼容升级后如不再使用 FineDataLink 功能，无需重新注册升级后如需继续使用 FineDataLink 功能，需要重新生成 license 进行注册，请提前联系商务沟通**升级步骤** 1）手动删除%Tomcat_HOME%/webapps/webroot/WEB-INF/lib目录下 fdl-xxx.jar 包2）再参考 [6.0.5之后的版本升级](<https://help.fanruan.com/finebi6.X/doc-view-2126.html>) 正常升级 FineBI3）根据商务指导，参考 [服务器注册方式](<https://help.fanruan.com/finedatalink/doc-view-419.html>) 重新注册  
#### **2）适配插件版本更新**
插件  
| 说明  
---|---  
FineBI For Excel| 升级至FineBI6.0.17版本后，FineBI For Excel插件需要升级至**V7.0.16** 版本付费用户请联系帆软技术支持获取对应版本插件。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持注意事项：插件更新后，需要重启FineBI工程，方可生效  
  

## 6.0.16
#### **1）服务器数据集class文件替换**  

**兼容说明：**
从6.0.15及以下版本升级至6.0.16及以上版本，建议手动替换服务器数据集class文件。
本次替换，可确保后续任意升级无需手动替换class文件，即可使用最新「[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)」
**操作步骤：**
点击下载并解压：[6016+.zip](<doc-download-/finebi6.X/uploads/file/20240301/6016+.zip> "下载资料")
将其覆盖更新至工程%BI_HOME%/webroot/WEB-INF/classes/com/fr/log文件夹下
#### **2）适配插件版本更新**
插件  
| 说明  
---|---  
FineBI For Excel| 升级至FineBI6.0.16版本后，FineBI For Excel插件需要升级至**V7.0.15** 版本付费用户请联系帆软技术支持获取对应版本插件。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持注意事项：插件更新后，需要重启FineBI工程，方可生效  
## 6.0.15
#### **1）服务器数据集class文件替换**  

**兼容说明：**
从6.0.14及以下版本升级至6.0.15版本，需要手动替换以下服务器数据集class文件，方可使用最新「[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)」
**操作步骤：**
点击下载并解压：[6015class.zip](<doc-download-/finebi6.X/uploads/file/20240301/6015class.zip> "下载资料")
将其覆盖更新至工程%BI_HOME%/webroot/WEB-INF/classes/com/fr/log文件夹下
#### **2）适配插件版本更新**
插件  
| 说明  
---|---  
HTML5移动端展现| 升级至FineBI6.0.15版本后，HTML5移动端展现插件需要升级至**V11.0.88** 版本否则仪表板组件组，在移动端无法有效展示  
FineBI For Excel| 升级至FineBI6.0.15版本后，FineBI For Excel插件需要升级至**V7.0.14** 版本付费用户请联系帆软技术支持获取对应版本插件。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持注意事项：插件更新后，需要重启FineBI工程，方可生效  
## 6.0.14
#### **1）服务器数据集class文件替换**  

**兼容说明：**
从6.0.13及以下版本升级至6.0.14版本，需要手动替换以下服务器数据集class文件，方可使用最新「[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)」
**操作步骤：**
点击下载并解压：[6013+.zip](<doc-download-/finebi6.X/uploads/file/20240301/6013+.zip> "下载资料")
将其覆盖更新至工程%BI_HOME%/webroot/WEB-INF/classes/com/fr/log文件夹下
#### **2）适配插件版本更新**
插件  
| 说明  
---|---  
BI明细表导出CSV| 升级至FineBI6.0.14版本后，BI明细表导出CSV插件需要升级至**最新** 版本付费用户请联系帆软技术支持获取对应版本插件。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持  
## 6.0.13
#### **1）适配FineDataLink版本更新**  

对于FineBI集成FineDataLink的工程，如需升级FineBI至6.0.13版本，需要升级FineDataLink至**4.0.28.1** 版本
付费用户请联系帆软技术支持获取对应版本JAR包。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持
#### **2） DEF_ADD函数逻辑调整**
历史版本，合计-自动计算时，使用当前视图中所有维度，收起时则再次对计算结果再次进行合计
6.0.13版本，合计-自动计算时，使用当前合计视图所使用到的拼接维度
#### **3）服务器数据集class文件替换**  

**兼容说明：**
从6.0.12及以下版本升级至6.0.13版本，需要手动替换以下服务器数据集class文件，方可使用最新「[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)」
**操作步骤：**
点击下载并解压：[2023.08.30-6013+.zip](<doc-download-/finebi6.X/uploads/file/20240301/2023.08.30-6013+.zip> "下载资料")
将其覆盖更新至工程%BI_HOME%/webroot/WEB-INF/classes/com/fr/log文件夹下
#### **4）适配插件版本更新**
插件  
| 说明  
---|---  
FineBI For Excel| 升级至FineBI6.0.15版本后，FineBI For Excel插件需要升级至**V7.0.13** 版本付费用户请联系帆软技术支持获取对应版本插件。技术支持联系方式：[服务平台](<https://service.fanruan.com/>)>在线支持注意事项：插件更新后，需要重启FineBI工程，方可生效  
## 6.0.12
#### **1）取消内置FineDataLink**  

FineBI6.0.12 版本开始，不再内置 FineDataLink 相关功能依赖的 JAR 包。  

类型  
| 说明  
---|---  
全新安装| 不再内置 FineDataLink 相关功能如需集成使用 FineDataLink，请联系技术支持获取 FineDataLink 相关的 JAR 包  
低版本升级| FineBI6.0.11 及以下版本、集成 FineDataLink 功能的工程如需升级到 6.0.12 及以上版本，需要依次升级 FineBI 和 FineDataLink 相关的 JAR，才能正常使用请在联系技术支持获取最新 JAR 包时，表明自己需要 FineBI 和 FineDataLink 的 JAR   
#### **2）新增血缘层级限制**
FineBI6.0.12及之后版本，限制数据表的 [血缘层级](<https://help.fanruan.com/finebi6.X/doc-view-77.html>) 最高为 16 。
  * 全新制作的数据表，不可超过最高层级限制。
  * 历史制作的、超过层级深度限制的表，仍可使用其制作组件、仪表板。
  * 历史制作的、超过层级深度限制的表，不可使用其制作更深层级的子表，建议优化父表血缘层级。


#### **3）服务器数据集class文件替换**  

**兼容说明：**
从6.0.11及以下版本升级至6.0.12版本，需要手动替换以下服务器数据集class文件，方可使用最新「[BI系统配置数据集](<https://help.fanruan.com/finebi6.X/doc-view-2149.html>)」
**操作步骤：**
点击下载并解压：[log-2023.07.06.zip](<doc-download-/finebi6.X/uploads/file/20240301/log-2023.07.06.zip> "下载资料")
将其覆盖更新至工程%BI_HOME%/webroot/WEB-INF/classes/com/fr/log文件夹下
#### **4）适配插件版本更新**
插件  
| 说明  
---|---  
HTML5移动端展现| 升级至FineBI6.0.12版本后，HTML5移动端展现插件需要升级至**V11.0.83** 版本  
## 6.0.11
#### **1）屏蔽自助数据集历史步骤复制粘贴功能**  

6.0.11版本屏蔽了自助数据集历史步骤的复制粘贴功能入口
下个版本修复相关隐患后即会重新开放入口
#### **2）解决集群启动慢问题**
6.0.11版本支持解决集群启动慢问题。
管理员需要手动删除temp目录下spark缓存bitmap文件，再启动工程即可。
#### **3）weblogic部署FineBI集成FineDataLink暂缓升级**  

weblogic环境部署FineBI工程，如集成FineDataLink，普通用户登录工程出现异常报错。
  * 对于不使用FineDataLink的工程，请手动删除%Tomcat_HOME%/webapps/webroot/WEB-INF/lib目录下 fdl-xxx.jar 包
  * 对于使用FineDataLink的工程，请暂缓升级，建议直升6.0.17版本


## 6.0.10
  

#### **1）WebLogic环境冲突**
**问题描述：**
6.0.10 版本新增参数安全校验，因此改动了 cbb JAR 包，部分工程升级后，工程所用的weblogic容器中的JAR包与改动冲突。
如存在JAR包冲突，会导致工程启动失败或部分功能不可用，工程日志中有相关报错关键词「validation」/「validator」
**解决方案一：**
1）在/webroot/WEB-INF目录下查找weblogic.xml，如果不存在该文件，新建即可。
2）在weblogic.xml文件中配置过滤，优先使用应用内置的jar包。
3）保存文件后，重启工程生效。
点击下载并解压，获取示例文件：[weblogic.zip](<doc-download-/finebi6.X/uploads/file/20240301/weblogic.zip> "下载资料")
**![](/core/style/lod.png)**  

**解决方案二：**  

1）下载javax.validation.jar：[javax.validation.jar](<doc-download-/finebi6.X/uploads/file/20240301/javax.validation.jar> "下载资料")
2）上传并覆盖/weblogic/Oracle/Middleware/oracle common/modules目录下的低版本javax.validation.jar。
#### **2）WebSphere环境冲突**
**问题描述：**
11.0.16 版本新增参数安全校验，因此改动了 cbb JAR 包，部分工程升级后，工程所用的WebSphere容器中的JAR包与改动冲突。
如存在JAR包冲突，会导致工程启动失败或部分功能不可用，工程日志中有相关报错关键词「validation」/「validator」
**解决方案：**  

1）下载javax.j2ee.validation.jar：[javax.j2ee.validation.jar](<doc-download-/finebi6.X/uploads/file/20240301/javax.j2ee.validation.jar> "下载资料")
2）上传并覆盖%WebSphereHome%/AppServer/plugins目录下的javax.j2ee.validation.jar。
## 6.0.9
无  

## 6.0.8
#### **1）分析主题模型兼容**  

6.0.8 分析主题新增模型功能。一个主题只存在一个模型，这个模型对应主题内的所有数据和组件。
**分析主题内** 所有组件的 **待分析区域配置** 都会 **复制到主题模型** 上，用户使用该表/模型关联的多表制作其他组件可重复使用，提高制作效率。
分析主题内 **相同表制作组件** 的 **待分析区域配置** 会被复制到主题上，相同的配置会进行兼容。兼容详情如下所示：
注1：模型里同一张表制作的组件才会进行字段合并。
注2：字段兼容不会影响分析区域已添加的字段。
若使用钻取目录制作组件，钻取目录中的非首目录字段未在分析区域设置显示名，可能分析区域中钻取目录字段会出现 XX-1， XX-2 的字段名。
组件待分析区域配置  
| 兼容说明（复制并整合到主题上的配置项会同步到所有组件中）  
  
---|---  
钻取目录| 前提：当前主题内相同表制作的多个组件（组件1、组件2都使用表1制作）1）待分析区域钻取目录完全相同，则将钻取目录整合并保留
  * 组件1钻取目录：a>b>c
  * 组件2钻取目录：a>b>c
  * 升级后是一个钻取目录：a-b-c

2）若钻取目录不完全相同，则将这些钻取目录用到的字段复制，然后整合并保留
  * 组件1钻取目录：a>b>c 
  * 组件2钻取目录：a>b>d
  * 升级后有两个钻取目录：①a>b>c；②a-1>b-1>d

3）当同一个字段有的组件不在钻取目录，有的组件在钻取目录时，如果是第一个钻取字段会进行复制，其他的字段只保留一个
  * 组件1钻取目录：a>b>c
  * 组件2无钻取目录
  * 升级后有钻取目录a>b>c；复制字段a-1

  
复制的字段| 1）多个组件的待分析区域字段复制并整合到主题上2）满足以下条件只保留一个：复制的字段名称和配置完全相同  
计算字段| 1）多个组件的待分析区域字段复制并整合到主题上2）字段完全相同只保留一个  
参数| 1）多个组件的待分析区域字段复制并整合到模型上2）满足以下条件只保留一个：
  * 参数类型和参数名称相同，未绑定过滤组件
  * 参数类型和参数名称相同，绑定的过滤组件相同

  
维度转指标指标转维度| 同「计算字段」  
地理角色-指标地理角色-维度| 同「计算字段」  
明细过滤| 多个组件的待分析区域字段复制并整合到模型上满足以下条件只保留一个：
  * 过滤条件完全相同  

  * 若是明细过滤条件添加了绑定过滤组件的参数，参数需要符合条件：参数类型和参数名称相同，且被相同的过滤组件绑定

  
记录数| 1）多个组件的待分析区域字段复制并整合到模型上2）组件1用表1制作有记录数，设置明细过滤条件A组件2用表1制作有记录数，设置明细过滤条件B 升级后都会保留，结果为：记录数、记录数-1  
指标名称| 保留  
  
## 6.0.7
无  

## 6.0.6
无  

## 6.0.5
[6.0 兼容说明](<https://help.fanruan.com/finebi6.X/doc-view-1890.html>)  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：非容器化FineBI6.0.x小版本升级指南](<index.php?doc-view-2126.html>)
[下一篇：FineBI与FineReport版本适配说明 ![](/core/style/forward.png) ](<index.php?doc-view-1061.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
