---
title: 非容器化FineBI6.0.x小版本升级指南
doc_id: 2126
url: https://help.fanruan.com/finebi6.X/doc-view-2126.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:10:53
---

> 本文仅用于指导非运维平台部署的FineBI6.0.x工程升级。运维平台部署的FineBI工程，请通过运维平台进行升级，详情请参见：外网升级运维项目、内网升级运维项目1. 概述1.1 版本FineBI服务

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 非容器化FineBI6.0.x小版本升级指南
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[22](<edition-list-2126.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2025-09-18 
[](<javascript:;>) [](<javascript:>)
本文仅用于指导**非运维平台部署** 的FineBI6.0.x工程升级。
**运维平台部署的FineBI工程，请通过运维平台进行升级，详情请参见：[外网升级运维项目](<https://help.fanruan.com/fineops/doc-view-53.html>)、[内网升级运维项目](<https://help.fanruan.com/fineops/doc-view-55.html>)**
  

## 1\. 概述
### 1.1 版本
FineBI服务器版本| 功能变更  
---|---  
6.0.5| -  
6.0.16| 新增版本更新推送和问题反馈入口  
### 1.2 功能介绍
为满足客户的新需求以及完善之前版本某些功能的不足之处，我们的产品在不断地更新迭代。
本文主要介绍FineBI工程在6.0.x**小版本** 内（例如FineBI6.0.5升级FineBI6.0.9）升级的情况。
本文提供两种升级方式，请任选其一进行。
## 2\. BI版本管理工具升级方案
仅面向购买了技术支持服务的付费用户。  

### 2.1 准备步骤
  
| 步骤  
| 说明  
---|---|---  
1| 了解升级注意事项| 请在升级前，认真查看升级注意事项，确保了解各个版本的兼容问题：[FineBI小版本升级注意事项](<https://help.fanruan.com/finebi6.X/doc-view-2359.html>)  
2| 备份工程| 在进行工程升级前，为避免升级失败，导致工程文件丢失无法回退等问题，请务必对原工程进行备份后再进行后续操作请参考 [工程备份还原方案](<https://help.fanruan.com/finebi6.X/doc-view-2224.html>) 3.1节，对工程进行备份  
3| 确认FineReport适配情况（没有可忽略）| **1）集成的FineReport** 如为FineBI与FineReport集成工程，升级FineBI即可，其中包含FineReport相关JAR，无需再单独升级FineReport**2）独立匹配使用的FineReport** 如有完全独立部署、需要匹配使用的独立FineReport工程，请在升级前确认版本匹配情况：[FineReport版本适配说明](<https://help.fanruan.com/finebi6.X/doc-view-1061.html>)  
4| 确认FineDataLink适配情况（没有可忽略）| **1）集成的FineDataLink** FineBI6.0.18 版本开始，不再内置 FineDataLink 相关功能依赖的 JAR 包，升级后不再支持两者集成  
如为FineBI与FineDataLink集成工程，如需升级至FineBI6.0.18及以上版本，请在升级前联系FineDataLink客户成功，进行FineDataLink独立部署**2）独立匹配使用的FineDataLink** 如有完全独立部署、需要匹配使用的独立FineDataLink工程，请在升级前确认版本匹配情况：[FineDataLink版本适配说明](<https://help.fanruan.com/finedatalink/doc-view-566.html>)  
5| 获取BI版本管理工具| 付费用户请联系帆软技术支持，索要最新/指定版本的「BI版本管理工具」请说明你的工程环境（Linux/Linux_arm/Windows）技术支持联系方式：前往「[服务](<https://service.fanruan.com/>)>在线支持」  
  
### 2.2 升级步骤-Linux
  
| 步骤| 说明  
---|---|---  
1| 关闭工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，关闭单机工程节点/集群每一个工程节点  
2| 使用「BI版本管理工具」执行换JAR升级| 本步骤操作，需在单机工程节点/集群每一个工程节点服务器均执行一次**1）上传解压工具** 请将技术支持提供的BI版本管理工具压缩包，上传至工程所在服务器请上传至有操作权限的目录下并解压，本示例上传至/home/bi目录下cd /home/biunzip fine-bi-version-manager-linux.zip![](/core/style/lod.png)**2）启动工具** 进入「BI版本管理工具」bin目录下，执行启动语句cd /home/bi/fine-bi-version-manager-linux/bin/./start-version-manager.sh**3）确认工程是否关 闭**  

  * 如输入「1」：无法继续执行升级
  * 如输入「2」：可敲击回车键继续

**4） 选择工程路径**请输入待升级工程的webroot路径，请输入绝对路径，敲击回车键继续  
**5） 检测是否存在不兼容JAR包**如检测到待升级工程版本为6.0.18及以上，且当前工程存在fdl有用JAR包提示「6.0.18及之后版本不支持fdl集成，请确认已拆分fdl独立部署」（即准备步骤中的确认FineDataLink适配情况步骤是否已完成）
  * 如输入「1」：终止升级，请拆分fdl独立部署后再尝试升级
  * 如输入「2」：可敲击回车键继续

**6） 确认执行升级******
  * 如输入「1」 ：敲击回车键，即自动替换JAR包进行升级
  * 如输入「2」：终止升级

请耐心等待，直到出现提示「新版工程准备完毕，请启动工程执行升级」，说明JAR包替换成功![](/core/style/lod.png)  
3| 启动工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，启动工程节点如为集群工程，请确保所有工程节点均执行了上一步的升级操作后再启动工程如为集群工程，请先启动一个节点，等该节点启动成功后，再启动其他的节点，不可以同时启动  
### 2.3 升级步骤-Windows
  
| 步骤  
| 说明  
---|---|---  
1| 关闭工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，关闭单机工程节点/集群每一个工程节点  
2| 使用「BI版本管理工具」执行换JAR升级| 本步骤操作，需在单机工程节点/集群每一个工程节点服务器均执行一次**1）上传解压工具** 请将技术支持提供的BI版本管理工具压缩包，上传至工程所在服务器请上传至有操作权限的目录下，例如D盘请解压获取「BI版本管理工具」**2）启动工具** 双击「BI版本管理工具」bin目录下的「start-version-manager.bat」，即可启动该工具![](/core/style/lod.png)**3）确认工程是否关 闭**  

  * 如选择「未关闭」：下一步按钮灰化，无法继续执行升级
  * 如选择「已关闭」：可点击「下一步」继续

![](/core/style/lod.png)**4） 选择工程路径**请详细阅读升级须知（即上一节准备步骤相关内容）请选择待升级工程的webroot文件夹，点击进入下一步![](/core/style/lod.png)**5） 检测是否存在不兼容JAR包**如检测到待升级工程版本为6.0.18及以上，且当前工程存在fdl有用JAR包提示「6.0.18及之后版本不支持fdl集成，请确认已拆分fdl独立部署」（即准备步骤中的确认FineDataLink适配情况步骤是否已完成）
  * 点击「否」：终止升级，请拆分fdl独立部署后再尝试升级
  * 点击「是」：进入下一步

![](/core/style/lod.png)**6） 确认版本信息**请确认待升级工程版本，是否与预期相同如目标版本正确，点击「开始替换」，即进入自动升级环节。![](/core/style/lod.png)**7） 自动换JAR升级**请耐心等待出现提示「新版本准备完毕」，即为换JAR成功点击「下一步」![](/core/style/lod.png)此时将明确列出工程原版本和新版本，并提示「新版工程准备完毕，请启动工程执行升级」，点击「替换完成」，自动关闭BI版本管理工具![](/core/style/lod.png)  
3| 启动工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，启动工程节点如为集群工程，请确保所有工程节点均执行了上一步的升级操作后再启动工程如为集群工程，请先启动一个节点，等该节点启动成功后，再启动其他的节点，不可以同时启动  
## 3\. 手动换JAR升级方案
### 3.1 准备步骤
  
| 步骤  
| 说明  
---|---|---  
1| 了解升级注意事项| 请在升级前，认真查看升级注意事项，确保了解各个版本的兼容问题：[FineBI小版本升级注意事项](<https://help.fanruan.com/finebi6.X/doc-view-2359.html>)  
2| 备份工程| 在进行工程升级前，为避免升级失败，导致工程文件丢失无法回退等问题，请务必对原工程进行备份后再进行后续操作请参考 [工程备份还原方案](<https://help.fanruan.com/finebi6.X/doc-view-2224.html>) 3.1节，对工程进行备份  
3| 确认FineReport适配情况（没有可忽略）| **1）集成的FineReport** 如为FineBI与FineReport集成工程，升级FineBI即可，其中包含FineReport相关JAR，无需再单独升级FineReport**2）独立匹配使用的FineReport** 如有完全独立部署、需要匹配使用的独立FineReport工程，请在升级前确认版本匹配情况：[FineReport版本适配说明](<https://help.fanruan.com/finebi6.X/doc-view-1061.html>)  
4| 确认FineDataLink适配情况（没有可忽略）| **1）集成的FineDataLink** FineBI6.0.18 版本开始，不再内置 FineDataLink 相关功能依赖的 JAR 包，升级后不再支持两者集成  
如为FineBI与FineDataLink集成工程，如需升级至FineBI6.0.18及以上版本，请在升级前联系FineDataLink客户成功，进行FineDataLink独立部署**2）独立匹配使用的FineDataLink** 如有完全独立部署、需要匹配使用的独立FineDataLink工程，请在升级前确认版本匹配情况：[FineDataLink版本适配说明](<https://help.fanruan.com/finedatalink/doc-view-566.html>)  
5| 获取升级JAR包| 用户可以安装最新版本 FineBI 后，在安装目录 %FineBI_Home%/webapps/webroot/WEB-INF/lib 下拷贝获取最新版本 JAR 包。  
  
### 3.2 升级步骤
  
| 步骤| 说明  
---|---|---  
1| 关闭工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，关闭单机工程节点/集群每一个工程节点  
2| 删除冗余JAR包| 请删除单机工程节点/集群每一个工程节点/webapps/webroot/WEB-INF/lib下，以下两类文件：
  * 删除netty-all-*.Final.jar（不存在可忽略）
  * 删除fdl-*-4.0.jar（不存在可忽略）

  
3| 删除impl文件| 请删除单机工程节点/集群每一个工程节点/webapps/webroot/WEB-INF/classes/com/fr/data下impl文件夹中的所有文件（不存在可忽略）  
4| 替换升级JAR包| 请将准备步骤获取的JAR包，上传覆盖更新到单机工程节点/集群每一个工程节点/webapps/webroot/WEB-INF/lib下  
5| 启动工程| 请参考 [关闭或重启FineBI工程](<https://help.fanruan.com/finebi6.X/doc-view-1322.html>) 文档，启动工程节点如为集群工程，需要先启动一个节点，等该节点启动成功后，再启动其他的节点，不可以同时启动  
## 4\. 升级后操作
### 4.1 检查升级是否成功
管理员登录FineBI系统，点击「管理系统>注册管理>版本信息」。
可查看当前JAR版本，确认是否是自己所需的工程版本。如下图所示：
![](/core/style/lod.png)
### 4.2 升级插件
工程升级完成后，建议登录FineBI系统，点击「系统管理>插件管理」，对存在新版本的插件一一进行升级。
![](/core/style/lod.png)
### 4.3 更新数据
工程升级完成后，建议登录FineBI系统，点击常用数据集进行[数据更新](<https://help.fanruan.com/finebi6.X/doc-view-93.html>)验证数据集更新是否可用以及更新后数据是否准确。
### 4.4 用户登录
工程升级完成后，建议分别使用超管和普通用户账号，依次登录FineBI系统，查看是否能正常登录，确保升级成功。
### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：FineBI版本升级简介](<index.php?doc-view-276.html>)
[下一篇：FineBI6.0.x小版本升级注意事项 ![](/core/style/forward.png) ](<index.php?doc-view-2359.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
