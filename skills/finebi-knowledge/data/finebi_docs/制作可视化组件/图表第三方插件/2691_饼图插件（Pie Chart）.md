---
title: 饼图插件（Pie Chart）
doc_id: 2691
url: https://help.fanruan.com/finebi6.X/doc-view-2691.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:01:23
---

> 1. 概述插件饼图（Pie Chart）提供了传统饼图之外更加复杂丰富的图表可能性。多层圆环嵌套，可以直观展示各类别的占比与整体的关系。中心区提供总计显示等。1.1 版本FineBI 版本插件版本功能变

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# 饼图插件（Pie Chart）
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Dejiang.Wang](<user-space-3447105.html>)_
* 历史版本：[8](<edition-list-2691.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2025-12-08 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
插件饼图（Pie Chart）提供了传统饼图之外更加复杂丰富的图表可能性。
  * 多层圆环嵌套，可以直观展示各类别的占比与整体的关系。
  * 中心区提供总计显示等。


### 1.1 版本
FineBI 版本| 插件版本| 功能变动  
---|---|---  
6.1| 1.0. X| -  
### 1.2 应用场景
下图以一家农业企业为例，展示了农产品生产与销售数据的可视化结果。
饼图包含内外两个圆环（Circles）分别展示了畜牧业（内圈）种植业（外圈）的数据，每个扇区都配有图示，饼图中央进行总销售额的展示。
![2025-12-02_14-02-57.gif](/core/style/lod.png)
## 2\. 插件安装
获取插件安装包，在 FineBI 上安装此插件：
  * 获取插件包：[饼图](<https://market.fanruan.com/plugin/a69fc22c-728c-46fd-ac50-66d43c0bc3a4>)
  * FineBI 服务器安装插件，插件方法参见 [BI 插件管理](<https://help.fanruan.com/finebi6.0/doc-view-459.html>) 。 


## 3\. 示例
### 3.1 准备数据
1）用户登录 FineBI 系统，点击「我的分析」，点击「新建分析主题」。如下图所示：
![2025-11-12_11-09-02.png](/core/style/lod.png)
2）点击「本地Excel文件>上传数据」，上传数据。如下图所示：
示例数据：[pie_data.xlsx](<doc-download-/finebi6.X/uploads/file/20251112/pie_data.xlsx> "下载资料")
![2025-11-12_11-05-18.png](/core/style/lod.png)
### 3.2 创建饼图
1）点击左下角「组件」按钮，在图表类型下选择「Pie Chart」，将左侧待分析区域的字段依次拖入如下图的属性栏中。如下图所示：
![2025-12-02_14-05-26.png](/core/style/lod.png)
2）按照图示点击组件样式，向下找到「Conclusion 总计/结论」用于调整饼图中心汇总区。
在编辑框中将原有字段进行修改。代码为：
="<div style='text-align:center;'><div>Total</div> <div style='font-size:2rem;'>"&FORMAT(СУММ([@实际销售额 (千卢布)]))&"</div><div>mln $</div></div>"
![PixPin_2025-12-02_14-13-42.png](/core/style/lod.png)
3）按照图示向下找到「Values 数值」用于调整饼图扇区数值显示依据的字段。
在编辑框中将原有字段进行修改。代码为：
=[@实际销售额 (千卢布)]&"{image|}"
![PixPin_2025-12-02_14-08-52.png](/core/style/lod.png)
4）向下找到「Tooltip > Contents of the hint 悬浮提示 > 提示内容」，
在编辑框中将原有字段进行修改，代码为：
=[@行业分类] & " / " & [@农产品名称]& " / " & [@实际销售额 (千卢布)]
![PixPin_2025-12-02_14-09-18.png](/core/style/lod.png)
5）最终效果如下图所示：
![2025-12-02_14-02-57.gif](/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [制作可视化组件](<category-view-569>)
[![](/core/style/back.png)上一篇：直连数据仪表板编辑与预览内容不一致](<index.php?doc-view-490.html>)
[下一篇：误差图 ![](/core/style/forward.png) ](<index.php?doc-view-2692.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
