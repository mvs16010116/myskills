---
title: BI Echarts图表集成插件
doc_id: 2303
url: https://help.fanruan.com/finebi/doc-view-2303.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:19:07
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本FineBI JAR 包版本7.02023-09-041.2 功能场景安装BI Echarts图表集成插件后，FineBI可以对接Echarts图表，图表组件类型

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# BI Echarts图表集成插件
[__](<doc-edit-2303.html>)
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[小张好像不在线](<user-space-703598.html>)_
* 历史版本：[4](<edition-list-2303.html>)
* 最近更新：[TW](<user-space-1900999.html>) 于 2025-09-24 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| FineBI JAR 包版本  
---|---  
7.0| 2023-09-04  
### 1.2 功能场景
安装BI Echarts图表集成插件后，FineBI可以对接Echarts图表，图表组件类型支持Echarts图表
![](https://help.fanruan.com/core/style/lod.png)
## 2\. 插件介绍
### 2.1 插件安装
  * 插件获取：[BI echarts图表集成插件](<https://market.fanruan.com/plugin/567da0e2-54be-4e0a-9178-661456fc33a8>)
  * 设计器插件安装方法参照：[设计器插件管理](<https://help.fanruan.com/finereport/doc-view-2198.html>)
  * 服务器安装插件方法参照：[服务器插件管理](<https://help.fanruan.com/finereport/doc-view-2220.html>)


### 2.2 插件使用
#### 2.2.1 创建图表组件
在分析主题界面，添加组件，进入组件编辑界面，图表类型选择Echarts图表
![](https://help.fanruan.com/core/style/lod.png)
#### 2.2.2 编辑图表组件
1）拖入数据字段
将数据集中需要使用的字段拖入图表编辑区
![](https://help.fanruan.com/core/style/lod.png)
2） 编辑数据算子
数据算子，支持对原始图表数据（主要的内容有字段配置（fileds）和按列存储的二维表数据（colData））进行进一步处理
![](https://help.fanruan.com/core/style/lod.png)
  

旭日图数据算子示例  
---
[code]
    function dataCal(originData) {
        var dataModels = originData.dataModels;
        var colData = dataModels[0].colData;
        var data;
        var map = {};
        var arr = [];
        for (var i = 0; i < colData[0].length; i++) {
            var id = colData[0][i];
            var pid = colData[1][i];
            var name = colData[2][i];
            var value = colData[3][i];
            if (map[id]) {
                map[id].name = name;
                map[id].value = value;
            } else {
                map[id] = {
                    name: name,
                    value: value,
                    children: []
                }
            }
            if (pid && pid.length > 0) {
                if (!map[pid]) {
                    map[pid] = {
                        children: []
                    }
                }
                map[pid].children.push(map[id]);
            }
            if (!pid || pid.length === 0) {
                data = map[id];
            }
        }
        return data.children;
    }
[/code]  
参数说明：| originData.dataModels| 存放列信息（fields）和列数据（colData）  
---|---  
  
  
  

3 ）编辑配置算子
配置算子，基于上一步处理的数据，输出图表配置（对应Echarts的属性配置）
![](https://help.fanruan.com/core/style/lod.png)
旭日图配置算子示例  
---
[code]
    // 同步调用
    function optionCal(data, chartConfig) {
        var option = {
            series: {
                type: 'sunburst',
                // emphasis: {
                //     focus: 'ancestor'
                // },
                data: data,
                radius: [0, '90%'],
                label: {
                    rotate: 'radial'
                }
            }
        };
        return option;
    }
    // 异步调用，需要控制好加载逻辑，比如有些异步资源只能加载一次
    function optionCal(data, chartConfig, callbackFun) {
    var option = {
            series: {
                type: 'sunburst',
                // emphasis: {
                //     focus: 'ancestor'
                // },
                data: data,
                radius: [0, '90%'],
                label: {
                    rotate: 'radial'
                }
            }
        };
        callbackFun({
        option: option,
       chartContainerCb: function(myChart) {
          console.log(myChart);
        }
      });
    }
[/code]  
说明：| data| 上一步配置算子处理完数据返回的数据  
---|---  
chartConfig| 图表配置的相关信息，一般较少用到  
callbackFun| 可缺省。支持异步回调，如果是同步调用，直接return option即可。option传入echarts配置。chartContainerCb可以获取到echarts实例。调用示例： callbackFun({  
option: option,  
chartContainerCb: function(myChart) {  
console.log(myChart);  
}  
});  
  
  
4）预览图表  

数据算子和配置算子编辑完成后，点击运行，可以在右侧预览图表样式，如果此时开启了后端计算，则配置算子需要保存后才可生效
![](https://help.fanruan.com/core/style/lod.png)
5）高级配置  

数据后端计算：默认关闭，此时数据算子走前端计算；开启后，数据算子将在后端执行
![](https://help.fanruan.com/core/style/lod.png)
#### 2.2.3 模版管理  

1）另存模版
点击另存模板，弹窗编辑名称、描述、公共模板等配置信息，点击确定保存。可以选择新增模版或者更新已有模版。
开启公共模板后，其他用户可以在引用模板中看到并引用。
保存成功后，可在模板引用弹窗中选择对应模板。
![](https://help.fanruan.com/core/style/lod.png)
2）引用模版  

点击引用模板按钮，弹窗中可选择个人和公共模板进行引用
![](https://help.fanruan.com/core/style/lod.png)
模板引用成功后，支持继续设置算子同步（默认开启同步，关闭同步后，可以自行编辑配置）或者关闭模板引用
![](https://help.fanruan.com/core/style/lod.png)
3）删除模版
删除模板，当前支持删除个人下的非公共模板
![](https://help.fanruan.com/core/style/lod.png)
2.2.4 图表组件应用
仪表板编辑页面添加组件，即可预览
![](https://help.fanruan.com/core/style/lod.png)
#### 2.2.4 全局配置
![2025-09-24_10-02-10.png](https://help.fanruan.com/core/style/lod.png)
JS引擎：后端计算相关，默认调用J2V8（需工程支持J2V8），如不支持，尝试调用NASHORN
## 3\. 注意事项
3.1 数据格式转换相关：数值格式当前不支持，仅传递原始图表数据；前端计算模式下，日期字段支持格式转化（后端计算开启时不支持）
3.2 不支持移动端
3.3 不支持后台导出
3.4 暂不支持跳转和联动其他组件（其他组件可单向联动echarts图表组件）
### 附件列表 
  
下载次数：：0
    
**主题：** [制作可视化组件](<category-view-569>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：热力区域图](<index.php?doc-view-196.html>)
[下一篇：日历图-全年 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-1009.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
