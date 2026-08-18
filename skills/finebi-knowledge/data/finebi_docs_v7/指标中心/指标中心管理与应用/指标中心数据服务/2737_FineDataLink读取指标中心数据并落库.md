---
title: FineDataLink读取指标中心数据并落库
doc_id: 2737
url: https://help.fanruan.com/finebi/doc-view-2737.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:27:20
version: "7.X"
---

> 1. 概述1.1 应用场景用户希望能将指标中心中的指标/维度数据取出，给外部自由的使用。1.2 实现思路使用 FineDataLInk 将接口中的指标维度数据取出，并写入指定的数据库。其他系统即可直接使

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineDataLink读取指标中心数据并落库
[__](<doc-edit-2737.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Roxy](<user-space-233328.html>)_
* 历史版本：[4](<edition-list-2737.html>)
* 最近更新：[Roxy](<user-space-233328.html>) 于 2026-01-21 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 应用场景
用户希望能将指标中心中的指标/维度数据取出，给外部自由的使用。
### 1.2 实现思路
使用 FineDataLInk 将接口中的指标维度数据取出，并写入指定的数据库。  

其他系统即可直接使用指标中心的数据。
![2026-01-21_16-21-55.jpg](https://help.fanruan.com/core/style/lod.png)
## 2\. 操作步骤
接口取数时，通常不会一次性取出全量数据，因此使用参数，分批从接口中取出全量数据。
从接口中获取 pageNum 和 pageSize 返回值，并使用 SparkSQL 计算出数据总页数 total_pages，将其作为参数，也就是需要执行的次数；
使用分页取数，翻页方式选择「页码」，并设置 ${pageNum}页数参数，首次执行 pageIndex 页码数为 1 ，然后增长间隔为1，递增执行取出每一页的数据，当页数pageNum<=totalpages 继续执行，当页数pageNum>totalpages 时，停止执行。
### 2.1 设置 API 基本信息
获取 [数据查询接口](<https://help.fanruan.com/finebi/doc-view-2734.html#151341f6a37feca9>) 信息。  

新建一个定时任务，由于需要将 API 数据解析计算后获取总页数值作为参数，因此需要使用「数据转换」节点。
在数据转换中，选择「API输入」并选择POST请求方式，输入复制的API链接，如下图所示：
![2026-01-21_16-02-07.jpg](https://help.fanruan.com/core/style/lod.png)
设置认证方式：[认证方式](<https://help.fanruan.com/finebi/doc-view-2720.html#530fa4fec185b6df>)  

然后在Body 中输入 json 数据，如下图所示：  

示例 pageSize 设置为 100，也就是每页数据限制为 100 条，从第一个开始取数。
[code]
    {  
      "dimensions": [  
        "8db3f282-3da0-4443-8f41-6d223908ec07",  
        "62cde1be-cb29-4377-ba54-7de1244d3ffb",  
        "b69615a3-6530-41c0-935e-7d2cb10c383b"  
      ],  
      "metrics": [  
        "a2594100-58bf-4d4d-af00-839722e86a43"  
      ],  
      "source": {  
        "8db3f282-3da0-4443-8f41-6d223908ec07": {  
          "id": "8db3f282-3da0-4443-8f41-6d223908ec07",  
          "fieldId": "8db3f282-3da0-4443-8f41-6d223908ec07",  
          "name": "商品编码",  
          "transferName": "商品编码",  
          "type": 16,  
          "resourceType": 66  
        },  
        "62cde1be-cb29-4377-ba54-7de1244d3ffb": {  
          "id": "62cde1be-cb29-4377-ba54-7de1244d3ffb",  
          "fieldId": "62cde1be-cb29-4377-ba54-7de1244d3ffb",  
          "name": "门店编码",  
          "transferName": "门店编码",  
          "type": 16,  
          "resourceType": 66  
        },  
        "b69615a3-6530-41c0-935e-7d2cb10c383b": {  
          "id": "b69615a3-6530-41c0-935e-7d2cb10c383b",  
          "fieldId": "b69615a3-6530-41c0-935e-7d2cb10c383b",  
          "name": "日期",  
          "transferName": "日期",  
          "type": 48,  
          "resourceType": 66  
        },  
        "a2594100-58bf-4d4d-af00-839722e86a43": {  
          "id": "a2594100-58bf-4d4d-af00-839722e86a43",  
          "fieldId": "a2594100-58bf-4d4d-af00-839722e86a43",  
          "name": "毛利率",  
          "transferName": "毛利率",  
          "type": 32,  
          "resourceType": 65,  
          "current": true  
        }  
      },  
      "filters": [],  
      "orders": [  
        "8db3f282-3da0-4443-8f41-6d223908ec07",  
        "62cde1be-cb29-4377-ba54-7de1244d3ffb",  
        "b69615a3-6530-41c0-935e-7d2cb10c383b",  
        "a2594100-58bf-4d4d-af00-839722e86a43"  
      ],  
      "engineType": "spider",  
      "limit": {  
        "rowCount": 5000,  
        "pageSize": 100,  
        "pageIndex": 1  
      }  
    }  
    
[/code]
解析后的返回值如下图所示：
![2026-01-21_16-07-22.jpg](https://help.fanruan.com/core/style/lod.png)
### 2.2 获取数据总页数
使用获取到的 rowCount（总数据条数）和 pageSize（每页数据条数）进行计算，获取总页数。
使用 SparkSQL 输入如下公式：
[code]
    select CEILING($[API输入].`data.pageInfo.rowCount`/$[API输入].`data.pageInfo.pageSize`) from $[API输入]  
    
[/code]
注：字段都需要在输入时选择自动识别出的字段，不能手动输入。
在数据预览界面就可以看到计算出的总页数，如下图所示：
![2026-01-21_16-08-04.jpg](https://help.fanruan.com/core/style/lod.png)
使用参数输出，将总页数设置为参数 total_pages ，如下图所示：
![2026-01-21_16-10-08.jpg](https://help.fanruan.com/core/style/lod.png)
### 2.3 分批取数
新增数据转换节点，选择 API 输入后，输入API配置信息，勾选「分页取数」，设置取数逻辑，分页方式选择「页码」，更新策略为初始值 1 ，增长间隔 1，即按照设置的更新策略从第一页开始递增 ${pageNum}页数参数，从接口取数。该参数即可实现按照页数递增取出所有的数据。如下图所示：
![2026-01-21_16-11-48.jpg](https://help.fanruan.com/core/style/lod.png)
当页数参数 ${pageNum} 递增到大于等于总页数参数，则${total_pages}，则分页结束，如下图所示：
![11.jpg](https://help.fanruan.com/core/style/lod.png)
写入 API 配置，并设置参数名：pageSize，参数值：100，pageNum 使用分页参数 ${pageNum} ，也就是按照每页 100 条数据，从第一页开始递增从接口取数，如下图所示：
注：此处为了保证总页数一致，设置的 pageSize 需要与 2.2 节相同。
![2026-01-21_16-10-48.jpg](https://help.fanruan.com/core/style/lod.png)
可以使用 JSON 解析，设置取出指定的数据，如下图所示：
![2026-01-21_16-13-36.jpg](https://help.fanruan.com/core/style/lod.png)
在数据去向中设置指定的输出数据库以及数据表，如下图所示：
![2026-01-21_16-14-15.jpg](https://help.fanruan.com/core/style/lod.png)
### 2.4 效果查看
保存并运行任务后，此时在数据库中即可取出全部工单数据，如下图所示：
![2026-01-21_16-20-47.jpg](https://help.fanruan.com/core/style/lod.png)
### 附件列表 
  
下载次数：：0
    
**主题：** [指标中心](<category-view-760>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：指标数据查询/校验接口](<index.php?doc-view-2734.html>)
[下一篇：管理系统简介 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-168.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
