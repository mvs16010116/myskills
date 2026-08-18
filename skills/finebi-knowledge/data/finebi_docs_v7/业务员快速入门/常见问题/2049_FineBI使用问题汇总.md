---
title: FineBI使用问题汇总
doc_id: 2049
url: https://help.fanruan.com/finebi/doc-view-2049.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:17:16
version: "7.X"
---

> 1. 概述帮助使用 FineBI 的用户解决入门级的使用问题。首先是解决业务人员如何查看仪表板的问题，其次是引导分析用户如何制作仪表板。2. 入门常见问题关于 BI 的入门使用的常见问题，如下表所示：问

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI使用问题汇总
[__](<doc-edit-2049.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[April陶](<user-space-431758.html>)_
* 历史版本：[13](<edition-list-2049.html>)
* 最近更新：[April陶](<user-space-431758.html>) 于 2025-11-22 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
帮助使用 FineBI 的用户解决入门级的使用问题。首先是解决业务人员如何查看仪表板的问题，其次是引导分析用户如何制作仪表板。
## 2\. 入门常见问题
关于 BI 的入门使用的常见问题，如下表所示：
问题  
| 方案  
---|---  
1）如何使用 FineBI 快速上手2）下载了 BI 后从哪里开始分析呢| 学习[5分钟上手BI](<https://help.fanruan.com/finebi7.0/doc-view-818.html>)，掌握 FineBI 快速入门的操作技巧。  
1）浏览器老崩溃2）设置后不显示效果3）加载页面出不来| 清一下浏览器缓存  
错误代码| [错误代码汇总](<https://help.fanruan.com/finebi7.0/doc-view-530.html>)  
注：操作过程中涉及管理员权限分配的限制，如果未被分配对应权限，会出现功能缺失，权限不足等问题，对应权限问题及平台其他问题可参考：[管理系统问题汇总](<https://help.fanruan.com/finebi7.0/doc-view-999.html>)
## 3\. FineBI 小词典
FineBI 详情请参见： [FineBI 特有名词解释](<https://help.fanruan.com/finebi7.0/doc-view-829.html>)
## 4\. 业务人员查看
帮助业务员查看一张做好的仪表板，参考文档如下表所示：  

问题  
| 方案  
---|---  
业务人员查看第一张仪表板| [查看用户操作指南](<https://help.fanruan.com/finebi7.0/doc-view-746.html>)  
## 5\. 我的分析-数据
在实际的数据分析场景中，IT 部门提供的数据不能完全覆盖分析人员的需求，需要对数据进行进一步处理，一些复杂的数据分析才能实现。
### 5.1 数据合并
进行数据加工时时常需要数据合并，数据合并可以在我的分析下编辑数据，也可以使用其他方法实现，常见问题汇总如下表所示：  

问题  
| 方案  
---|---  
1）有什么办法把几个表的数据放在一起进行展示2）两个表如何一起分析| 1）用 [左右合并](<https://help.fanruan.com/finebi7.0/doc-view-512.html>) 和 [上下合并](<https://help.fanruan.com/finebi7.0/doc-view-513.html>)；2）用 SQL 写 UNION ；3）添加关联。  
1）从不同数据表选择字段做分析2）把多张表的栏目合并成一张表| 有关联的表通过 [选择字段](<https://help.fanruan.com/finebi7.0/doc-view-506.html>) 分析，需要按照逻辑来。没有关联或者无法建立关联的的情况下，可以用[左右合并](<https://help.fanruan.com/finebi7.0/doc-view-512.html>)  
1）左右合并什么意思2）数据有多对多的场景，如何解决3）n:n的关联怎么实现4）两个表没有关联关系如何合并| [左右合并](<https://help.fanruan.com/finebi7.0/doc-view-512.html>)  
左右合并和关联的区别| 左右合并：实现多表的合并，进行数据分析关联：用于权限设置中使用  
企业中存在复杂的层级关系，不同层级的用户拥有不同的的数据权限，并希望不同层级的用户仅可查看自己所拥有权限下的数据| 参考：[四联表模型](<https://help.fanruan.com/finebi7.0/doc-view-2137.html>)  
1）上下合并是是么意思2）字段一致，值不同的两张表怎么合并3）两个表的表头相同，如何将他们的数据合并| [上下合并](<https://help.fanruan.com/finebi7.0/doc-view-513.html>)  
1）什么情况数值以科学计数法展示  
2）为什么会出现「1e-9」这种情况![1609401481782058.png](https://help.fanruan.com/core/style/lod.png)| 当数值在 -0.01~0.01 之间（不包括 0 ），BI 中会显示为科学计数法，即图示中的情况  
### 5.2 数据分析
数据加工在数据编辑界面实现，常见问题汇总如下表所示：
问题| 方案  
---|---  
1）数据量限制2）报错提示占用过多内存| [数据量说明](<https://help.fanruan.com/finebi7.0/doc-view-1959.html>)  
  
数据分析的什么操作会影响到性能| 左右合并，分组汇总求记录数等类似操作  
数据分析可以叠加处理的吗| 可以  
1）如何将二维数据转成一维数据2）字段是日期的话，怎么按照行进行分析![å¾ç.png](https://help.fanruan.com/core/style/lod.png)3）如何逆透视二维表格转换成一维表格源表格：![image.png](https://help.fanruan.com/core/style/lod.png)  
转换成一维表格：![image.png](https://help.fanruan.com/core/style/lod.png)| [行列转换之列转行](<https://help.fanruan.com/finebi7.0/doc-view-366.html>)  
新增列怎么使用| [新增列](<https://help.fanruan.com/finebi7.0/doc-view-509.html#>)  
新增列后的数据，如何让文本变成数值| [字段类型转换](<https://help.fanruan.com/finebi7.0/doc-view-1089.html>) ，点击右上角改变字段类  
  
把日期里的年月日新增一列只有年月| 参考文档：[新增列](<https://help.fanruan.com/finebi7.0/doc-view-509.html#5>)  
取某年的数据，过滤条件写哪里| [过滤](<https://help.fanruan.com/finebi7.0/doc-view-507.html>)  
对数据进行过滤| 1）在数据中 [过](<https://help.fanruan.com/finebi7.0/doc-view-507.html>)[滤](<https://help.fanruan.com/finebi7.0/doc-view-507.html>)；2）在组件中过滤 [过滤器入门](<https://help.fanruan.com/finebi7.0/doc-view-2403.html>)3）在仪表板中过滤：增加[过滤组件](<https://help.fanruan.com/finebi7.0/doc-view-382.html>)，进行联动过滤  
### 5.3 函数
数据加工时需要用函数进行计算，关于函数常见问题如下表所示：
问题| 方案  
---|---  
1）BI 函数的使用2）关于 FineBI 各种函数公式的用法有说明| [函数概述](<https://help.fanruan.com/finebi7.0/doc-view-2.html>)  
在组件里面有没有添加函数公式的地方| 有，[添加计算字段](<https://help.fanruan.com/finebi7.0/doc-view-118.html>)  
可以快速计算同环比的函数| [快速计算函数](<https://help.fanruan.com/finebi7.0/doc-cate-393.html>)  
通过函数来筛选一张表中某个状态值有多少条| 使用 [记录数](<https://help.fanruan.com/finebi7.0/doc-view-362.html>)  
1）什么是聚合函数2）如何使用聚合函数3）SUM_AGG 函数| [聚合函数](<https://help.fanruan.com/finebi7.0/doc-view-4.html>)  
1）在函数中写条件2）IF 函数| 使用 [IF 函数](<https://help.fanruan.com/finebi7.0/doc-view-3.html#3>)  
1）指标根据维度得到占比2）算比例的时候，函数怎么写| [如何计算组内占比](<https://help.fanruan.com/finebi7.0/doc-view-498.html>)  
公式不合法| [公式不合法原因排查](<https://help.fanruan.com/finebi7.0/doc-view-849.html>)  
### 5.4 数据清洗
问题  
| 方案  
---|---  
数据清洗定义  
| 将重复、多余的数据筛选清除，将缺失的数据补充完整，将错误的数据纠正或者删除，最后整理成为我们可以进一步加工、使用的数据。  
1）修改数值单位2）将数值修改“万”为单位| [自定义数值单位](<https://help.fanruan.com/finebi7.0/doc-view-864.html>)  
## 6\. 我的分析-组件
数据加工结束，需要将处理过的数据制作成可视化的组件进行展示分析。常见问题如下表所示：  

问题| 方案  
---|---  
1）组件跳转到其他模板2）类似一个组件跳转到一个网页，中间通过一个字段去传递过滤| [跳转](<https://help.fanruan.com/finebi7.0/doc-view-149.html>)  
1）组件名称标题修改2）自定义标题样式3）动态标题显示4）在标题中增加指标| [组件标题](<https://help.fanruan.com/finebi7.0/doc-view-152.html>)  
组件中添加过滤条件  
| [可视化过滤总结](<https://help.fanruan.com/finebi7.0/doc-view-838.html>)  
  
一个过滤组件控制了若干表，怎么使过滤组件控制指定表？| [自定义控制范围](<https://help.fanruan.com/finebi7.0/doc-view-140.html#7>)  
  
仪表板因为双击日期变大了，怎么恢复正常视角| [清除联动](<https://help.fanruan.com/finebi7.0/doc-view-150.html#5>)  
1）联动是指什么2）联动传递过滤条件3）同个仪表板里面不同数据集的组件联动| [联动](<https://help.fanruan.com/finebi7.0/doc-view-150.html>)  
怎么将结果换成百分比| 组件制作时直接修改下字段数值格式，参考文档：[表格数值格式](<https://help.fanruan.com/finebi7.0/doc-view-132.html#3>)  
1）数据钻取怎么设置2）柱状图钻取| [普通数据钻取](<https://help.fanruan.com/finebi7.0/doc-view-133.html>)  
创建钻取目录是什么意思| [创建钻取目录](<https://help.fanruan.com/finebi7.0/doc-view-103.html#3>) 2.1节  
钻取地图怎么实现| [地图钻取](<https://help.fanruan.com/finebi7.0/doc-view-865.html>)  
联动报错| [联动报错](<https://help.fanruan.com/finebi7.0/doc-view-575.html>)  
### 6.1 表格
组件制作中，表格组件包括[交叉表](<https://help.fanruan.com/finebi7.0/doc-view-122.html>)、[明细表](<https://help.fanruan.com/finebi7.0/doc-view-123.html>)、[分组表](<https://help.fanruan.com/finebi7.0/doc-view-121.html>)，常见问题如下表所示：
问题| 方案  
---|---  
将表头字段的部分值，合在一起做一个新字段展示| [自定义分组](<https://help.fanruan.com/finebi7.0/doc-view-128.html##5>)  
1）交叉表制作2）怎么在表格组件中，设置增加是绿色，减少是红色| [交叉表](<https://help.fanruan.com/finebi7.0/doc-view-122.html>)  
隐藏表格中的一列| [表格隐藏字段](<https://help.fanruan.com/finebi7.0/doc-view-531.html>)  
如何在仪表板中设置，不让一个字段中的相同数值自动合并成一个数值| 选择[明细表](<https://help.fanruan.com/finebi7.0/doc-view-123.html>)展示数据  
分组表的数据行隐藏了怎么保持打开状态| [](<https://help.fanruan.com/finebi7.0/doc-view-989.html#11>)[合计行/列](<https://help.fanruan.com/finebi7.0/doc-view-1697.html>)  
  
最大最小值突出标记| [将最大值最小值用特殊颜色标记](<https://help.fanruan.com/finebi7.0/doc-view-812.html>)  
### 6.2 图形
组件制作中图形常见问题如下表所示：  

问题| 方案  
---|---  
1）选择自己需要的图表2）如何使用某一图表3）图表类型说明| [图表类型简介](<https://help.fanruan.com/finebi7.0/doc-view-801.html>)  
图表类型里面灰色的图表怎么才能使用| 将字段拖入横纵轴，满足对应图表使用条件后，图表自动会变成可用状态。不同的图表的使用条件参考：[可视化分析概述](<https://help.fanruan.com/finebi7.0/doc-view-102.html>)  
组件的图形颜色，大小，细粒度等设置区域地图颜色设置| [图形属性](<https://help.fanruan.com/finebi7.0/doc-view-219.html>)  
1）组件中支持的图表组件样式2）图表边框设置问题3）图表的背景设置4）组件字体调整5）柱形图之间的距离调整| [图表组件样式](<https://help.fanruan.com/finebi7.0/doc-view-231.html>)  
1）不显示横坐标的值和横坐标的标题2）横轴字体斜着显示| [设置分类轴](<https://help.fanruan.com/finebi7.0/doc-view-235.html>)  
1）设置右轴值和左轴值2）调整图表刻度3）柱形图做 2 个轴| [设置值轴](<https://help.fanruan.com/finebi7.0/doc-view-873.html>)  
怎么设置图表按降序排列| [图表排序](<https://help.fanruan.com/finebi7.0/doc-view-232.html>)  
1）设置分析线2）如何给图添加趋势线3）添加警戒线，分析预警| [](<https://help.fanruan.com/finebi7.0/doc-view-240.html#5>)[图表设置分析线](<https://help.fanruan.com/finebi7.0/doc-view-240.html>)地图预警：[异常值预警（地图）](<https://help.fanruan.com/finebi7.0/doc-view-876.html>)  
柱形图和折线怎么在一个组件中显示| [](<https://help.fanruan.com/finebi7.0/doc-view-206.html>)[自定义图表](<https://help.fanruan.com/finebi7.0/doc-view-1067.html>)  
数据库有每个人登录的经纬度数据，这个能在仪表板地图中用经纬度呈现么| [点地图](<https://help.fanruan.com/finebi7.0/doc-view-212.html>)  
地理信息匹配，直辖市例如北京市、上海市、天津市、重庆市、台湾省、香港特别行政区、澳门特别行政区等匹配不上如何解决| [直辖市匹配地理角色(城市)](<https://help.fanruan.com/finebi7.0/doc-view-847.html>)  
繁体字数据表制作地图组件| [繁体数据地图匹配问题](<https://help.fanruan.com/finebi7.0/doc-view-815.html>)  
一个用户打开一个模板，是算一个 http 请求，还是多个  
| **组件查看发送请求说明：** 一个组件非绝对匹配一个 http 的线程请求，图表后台请求一般为 2-3 个请求查询**具体说明：** 打开一张仪表板后，会根据仪表板组件情况发出多个请求查询，一般图表组件会发出 2-3个 请求查询高并发场景下，不建议一个仪表板下面做很多的图表组件，会影响性能  
## 7\. 我的分析-仪表板
将表中数据通过数据加工处理后，制作成可视化组件后，需要将组件布局到仪表板上进行展示。
### 7.1 过滤组件
在仪表板界面，添加过滤组件对其他组件进行过滤，常见问题如下表所示：
问题| 方案  
---|---  
1）过滤组件说明2）在仪表板页面进行过滤3）图表联动过滤组件| [过滤组件](<https://help.fanruan.com/finebi7.0/doc-view-382.html>)  
1）过滤组件控制多个表怎么弄2）一个过滤控件对几个不同的表做过滤3）通过一个查询条件，过滤两个表格的数据| [过滤组件选多表字段](<https://help.fanruan.com/finebi7.0/doc-view-527.html>)  
过滤组件求同期的值| [求同比和环比-表维度非日期](<https://help.fanruan.com/finebi7.0/doc-view-851.html>)  
过滤组件参数用法| [实时参数的过滤组件用法](<https://help.fanruan.com/finebi7.0/doc-view-381.html>)  
过滤组件不生效| 与组件需设置同一个表绑定字段  
没有关系的两个表，同一个日期过滤| [日期过滤组件不绑定字段](<https://help.fanruan.com/finebi7.0/doc-view-361.html>)  
1）过滤控件可以按照层级关系自动构建树2）过滤条件里面做下拉树| [树过滤组件](<https://help.fanruan.com/finebi7.0/doc-view-137.html>)  
1）怎么添加时间做过滤2）如何做动态日期筛选框  
3）显示当日数据4）日期过滤组件设置默认范围| [时间过滤组件](<https://help.fanruan.com/finebi7.0/doc-view-135.html>)  
如何添加下拉选择框| [文本过滤组件](<https://help.fanruan.com/finebi7.0/doc-view-136.html>)  
### 7.2 其他组件
其他组件包括，文本组件，Web组件和图片组件，可以根据需要添加在仪表板界面，常见问题如下表所示：  

问题| 方案  
---|---  
1）什么是文本组件2）文本组件添加字段3）文本组件悬浮（自由布局）| [文本组件](<https://help.fanruan.com/finebi7.0/doc-view-141.html>)  
文本组件里面能添加公式吗| 不能  
1）web组件怎用2）怎么嵌套报表和网页链接3）在仪表板中放视频| [Web组件](<https://help.fanruan.com/finebi7.0/doc-view-143.html>)  
### 7.3 常见问题
常见的仪表板问题如下表所示：  

问题| 方案  
---|---  
仪表板是自动保存吗| 是的  
仪表板可以进行合并吗| 不可以  
1）自定义仪表板样式2）怎么修改仪表板的背景图| [仪表板样式](<https://help.fanruan.com/finebi7.0/doc-view-156.html>)  
分享仪表板、分析主题给别人查看如何和别人一起制作仪表板| [协作](<https://help.fanruan.com/finebi7.0/doc-view-1895.html>)  
不需要登录 BI 直接访问仪表板| [公共链接分享仪表板](<https://help.fanruan.com/finebi7.0/doc-view-164.html>)  
1）怎样才能让设计好仪表板显示到目录下2）仪表板申请挂出流程说明3）已经挂出的仪表板撤回| [挂出仪表板](<https://help.fanruan.com/finebi7.0/doc-view-165.html>)  
怎么复制一个仪表板| [仪表板复制](<https://help.fanruan.com/finebi7.0/doc-view-160.html>)  
其他人编辑仪表板| [仪表板复制](<https://help.fanruan.com/finebi7.0/doc-view-160.html>)之后进行编辑  
仪表板导出| [仪表板导出](<https://help.fanruan.com/finebi7.0/doc-view-161.html>)  
怎么在移动端查看仪表板| [App 使用](<https://help.fanruan.com/finebi7.0/doc-view-342.html>)  
预览/导出仪表板报错| [图表大数据预览/导出报](<https://help.fanruan.com/finebi7.0/doc-view-476.html>)[错](<https://help.fanruan.com/finebi7.0/doc-view-476.html>)[导出Excel报错](<https://help.fanruan.com/finebi7.0/doc-view-578.html>)  
仪表板编辑界面数据显示不完整  
| [仪表板编辑与预览区别](<https://help.fanruan.com/finebi7.0/doc-view-457.html>)  
  
## 8\. 移动端
使用移动端 APP 的常见问题：  

问题  
| 方案  
---|---  
移动端应用介绍| [移动端简介](<https://help.fanruan.com/finebi7.0/doc-view-335.html>)  
手机查看仪表板| [App 使用](<https://help.fanruan.com/finebi7.0/doc-view-342.html>)  
怎么取消掉登录页，直接进到页面| [HTML5 端单点登录](<https://help.fanruan.com/finebi7.0/doc-view-534.html>)  
移动端的功能说明| [移动端功能点说明](<https://help.fanruan.com/finebi7.0/doc-view-552.html>)  
手机直接用链接访问，不登录 APP| [HTML5 端访问仪表板/工程](<https://help.fanruan.com/finebi7.0/doc-view-452.html>)  
调整移动端仪表板组件位置等页面布局设置| [移动端布局](<https://help.fanruan.com/finebi7.0/doc-view-445.html>)  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [业务员快速入门](<category-view-96>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：FineBI视频学习](<index.php?doc-view-1104.html>)
[下一篇：FineBI新手常见问题 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1003.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
