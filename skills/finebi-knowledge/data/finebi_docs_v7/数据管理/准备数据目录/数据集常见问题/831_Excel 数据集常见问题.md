---
title: Excel 数据集常见问题
doc_id: 831
url: https://help.fanruan.com/finebi/doc-view-831.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:57
version: "7.X"
---

> 1. Excel制作自助数据集失败现象描述添加 Excel 数据集，制作自助数据集，不能添加字段，如下图所示：原因分析可能是 lib下的 JAR 包冲突导致。解决方法可以删除有冲突的 JAR 包，在文件

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# Excel 数据集常见问题
[__](<doc-edit-831.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[15](<edition-list-831.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-07-07 
[](<javascript:;>) [](<javascript:>)
## 1\. Excel制作自助数据集失败
**现象描述**
添加 Excel 数据集，制作自助数据集，不能添加字段，如下图所示：
![image.png](https://help.fanruan.com/core/style/lod.png)
**原因分析**
可能是 lib下的 JAR 包冲突导致。
**解决方法**
可以删除有冲突的 JAR 包，在文件目录%FineBI5.1%\webapps\webroot\WEB-INF\lib下，找到并删除 clickhouse.jar
## 2\. 出现空白值和空白字段
**现象描述**
导入 Excel (.xls文件) 时，出现空白的数据，整列或者最后几行。如下图所示：
![130.png](https://help.fanruan.com/core/style/lod.png)
**原因分析**
Excel 里的的空白格没有被删除干净。
**解决方法**
之前添加过内容的单元格清除内容后是没办法去掉空白格的，只有通过 Excel 删除单元格的功能去除。
## 3\. 重新上传，字段值为空
**现象描述  
**
上传表 1 保存。删除表 1 的「总金额」字段，点击更新excel，重新上传表 1 后，「总金额」字段显示为空值。如下图所示：
![image.png](https://help.fanruan.com/core/style/lod.png)
**原因分析**
Excel 重新上传的规则：
当 Excel 中新增了字段，重新上传时会增加该字段。
当 Excel 中删除了某字段，重新上传时该字段不会消失，会显示字段值为空。 
**解决方法**
不影响 Excel 数据集的使用情况下忽略该空值，或者新增 Excel 数据集，上传删除字段后的 Excel。  

## 4\. 后缀为xls的excel数据集不能成功上传
**问题现象**
后缀为 xls 的 excel 数据集上传提示上传失败
**原因分析**
我们支持03、07版本的后缀为xls、xlsx的Excel文件，并且不支持Excel 5.0/95 后缀为 xls 的 Excel 文件。
## 5\. 查看上传的 Excel 是否更新
当页面左侧栏显示所上传的表格，只能说明已经将数据上传到服务器了，并且在更新队列中排队更新，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
若是需要查看 Excel 表是否已经将最新上传的数据更新到 BI，需要在数据集下方或「更新信息」里查看最新更新时间，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
## 6\. csv文件导入失败
**问题现象  
**
添加excel数据集，选择csv文件，上传失败，如下图所示：
![2021-04-07_23-05-52.jpg](https://help.fanruan.com/core/style/lod.png)
**原因分析**
csv文件会有信息泄露的风险，所以做了一定的限制。  

**解决方法**
关闭「安全管理>文件校验」。
## 7\. 数值识别成文本
Excel识别字段规律：
1）数值长度超过15位时，就会识别成文本，eg:1234567891234567 会识别成文本类型；
2）0开头的数字不识别为数字。
## 8\. 导入数值和日期识别问题
参考文档：[上传 Excel 能被正确识别的字段类型](<https://help.fanruan.com/finebi7.0/doc-view-628.html>)
## 9\. 集群环境下导入大数据量excel数据集失败
**问题现象**
集群环境下，导入excel时出现上传失败弹窗，如下图所示：
![复现.gif](https://help.fanruan.com/core/style/lod.png)
**解决方法**
先找到 nginx.conf 文件，更改 nginx 配置。nginx.conf 文件参考位置：/usr/nginx/conf/nginx.conf
**![1617809044433353.png](https://help.fanruan.com/core/style/lod.png)**
****
## 10\. 在更新excel界面修改字段类型不生效
**问题及原因分析**  

1）在编辑Excel页面，修改了字段类型。
2）在更新Excel的地方，再次修改字段类型，此时不生效。
**原因分析**
再次进入编辑Excel页面，修改字段类型即可。
## 11\. 重新上传不一样的excel时，上传界面与数据准备预览界面不一样的
**问题现象**
添加一个excel1，进编辑保存后，再重新上传一个不一样的excel2,上传界面的数据预览和数据准备界面的预览数据会不一样。
**原因分析**
首次上传后去做了编辑，因此这张表变成了带有operator的ConfAnalysisEntryInfo
在保存的时候，字段生成会先拿childEntryInfo生成全部字段，然后根据operator再过滤一次，因此保存下来没有重新上传新增的字段。
**解决方法**
去数据集编辑界面将新增的字段勾选上。
## 12\. csv文件上传乱码
**问题现象**
上传csv文件，预览中文乱码。
**原因分析**
由于该csv文件遭到了破坏，导致文件的编码出现了问题。
**解决方法**
将该csv文件另存为新的csv文件，上传。
  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：Excel 上传失败](<index.php?doc-view-830.html>)
[下一篇：限制数据集抽取数量 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1355.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
