---
title: 导出Excel报错
doc_id: 578
url: https://help.fanruan.com/finebi/doc-view-578.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:20:31
version: "7.X"
---

> 1. java.lang.NullPointerException问题描述：仪表板组件导出 Excel 后，打开 Excel 报错：errorCode:500, errorMsg: java.lang.

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 导出Excel报错
[__](<doc-edit-578.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[doreen0813](<user-space-83193.html>)_
* 历史版本：[17](<edition-list-578.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-03-27 
[](<javascript:;>) [](<javascript:>)
## 1\. java.lang.NullPointerException
**问题描述：**
仪表板组件导出 Excel 后，打开 Excel 报错：errorCode:500, errorMsg: java.lang.NullPointerException，如下图所示：
![1.png](https://help.fanruan.com/core/style/lod.png)
查看 FineBI 日志%FineBI%/logs/fanruan.log，对应的报错如下：
[code]
    java.lang.NullPointerException  
    at sun.awt.FontConfiguration.getVersion(FontConfiguration.java:1264)  
    at sun.awt.FontConfiguration.readFontConfigFile(FontConfiguration.java:219)  
    at sun.awt.FontConfiguration.init(FontConfiguration.java:107)  
    at sun.awt.X11FontManager.createFontConfiguration(X11FontManager.java:774)  
    at sun.font.SunFontManager$2.run(SunFontManager.java:431)  
    at java.security.AccessController.doPrivileged(Native Method)  
    at sun.font.SunFontManager.<init>(SunFontManager.java:376)  
    at sun.awt.FcFontManager.<init>(FcFontManager.java:35)  
    at sun.awt.X11FontManager.<init>(X11FontManager.java:57)  
    at sun.reflect.GeneratedConstructorAccessor654.newInstance(Unknown Source)  
    at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)  
    at java.lang.reflect.Constructor.newInstance(Constructor.java:423)  
    at java.lang.Class.newInstance(Class.java:442)  
    at sun.font.FontManagerFactory$1.run(FontManagerFactory.java:83)  
    at java.security.AccessController.doPrivileged(Native Method)  
    at sun.font.FontManagerFactory.getInstance(FontManagerFactory.java:74)  
    at java.awt.Font.getFont2D(Font.java:491)  
    at java.awt.Font.canDisplayUpTo(Font.java:2060)  
    at java.awt.font.TextLayout.singleFont(TextLayout.java:470)  
    at java.awt.font.TextLayout.<init>(TextLayout.java:531)  
    at com.fr.third.v2.org.apache.poi.ss.util.SheetUtil.getDefaultCharWidth(SheetUtil.java:254)  
    
[/code]
**原因分析：**
该报错是由于 Linux 系统没有相关 font 资源导致，需要为系统安装字体管理器。
**解决方案：**
在 Linux 中执行如下命令安装字体管理：
[code]
    yum install fontconfig
[/code]
如果使用 docker 制作基础镜像运行以下命令：
[code]
    RUN yum -y install fontconfig
    RUN fc-cache --forc
[/code]
## 2\. java.lang.IllegalArgumentException:The workbook already contains a sheet of this name
**问题描述：**
导出 Excel，打开 Excel 报错如下：
**![image.png](https://help.fanruan.com/core/style/lod.png)**
**原因分析：**
Excel中 sheet 命名有如下规则：
1）sheet 名称不能多于31个（包含英文、汉字、| 、（）等，但是不能包含： 、/、？、*、[]等 )，程序中使用 poi 工具来生成的时候，传进去大于 31 个长度的字符串时，会被自动截取，便会导致两个名字变为一样的，出现sheet同名异常
2）sheet 名字不能为空，为空也会报错。
**解决方案：**
修改组件名称以及对应的长度，使其符合excel命名规则。
## 3\. Could not initialize class sun.awt.X11GraphicsEnvironment
**问题描述：**
Linux 环境下导出 Excel 失败，查看日志或按 F12 进入控制台，出现报错：Could not initialize class sun.awt.X11GraphicsEnvironment  

**原因分析：  
**
在Linux下，仪表板导出 Excel 时，会用到 Java 的图片包来处理图片。而 Java 虚拟机在处理图片时需要本地的 x-server 支持，若是没有就会出现该报错。
**解决方案：**
  * 直接安装的 FineBI  



在路径 %FineBI5.1%\bin 下找到finebi.vmoption文件，在文件内新增-Djava.awt.headless=true __，__ 保存文件。如下图所示：
![image.png](https://help.fanruan.com/core/style/lod.png)
  * 部署到 Tomcat 的 FineBI


进入%Tomcat%/bin目录，找到并编辑配置文件catalina.sh，增加-Djava.awt.headless=true __参数，__ 详情请参见：[导出 Excel 设置](<https://help.fanruan.com/finebi7.0/doc-view-56.html#9>)。
## 4\. com.finebi.common.exception.execute.FineOutOfMaxRowException: out of row restriction: xxxxxxx
**问题描述：**
导出 Excel，打开 Excel 报错如下：
![](https://help.fanruan.com/core/style/lod.png)
**原因分析：**
导出的 Excel 数据量超过数据量限制。
**解决方案：**
通过筛选等方式减少导出数据量。
## 5\. 数据量超过限制：Export Column Out Of Limit!
**问题描述：**
仪表板导出 Excel 时报错数据量超过限制：超过100列无法导出，请联系管理员，如下图所示：
![2.png](https://help.fanruan.com/core/style/lod.png)
**原因分析：**
如遇交叉表出现此提示，需注意多级表头的问题。交叉表下总列数的计算方式为，列维度数量*指标数量（指标名称也算做一列）。
**解决方案：**
在工程配置库 finedb 的 fine_conf_entity 表中添加一个参数  

  * id为：SystemOptimizationConfig.crossExportColumnLimit
  * value为：数值，不建议将数值修改很大。


### 附件列表 
  
下载次数：：0
    
**主题：** [制作可视化组件](<category-view-569>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：联动报错](<index.php?doc-view-575.html>)
[下一篇：仪表板不支持的特殊字符 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-905.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
