---
title: FineBI_Cli 安装
doc_id: 2774
url: https://help.fanruan.com/finebi/doc-view-2774.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:30:07
version: "7.X"
---

> 1. 功能概览FineBI_Cli 通过 AI 连接 FineBI，使业务人员可以用自然语言查询数据、导出仪表板、生成分析报告、同步数据到飞书多维表格，并结合飞书消息或任务完成自动化跟进。整体架构采用

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# FineBI_Cli 安装
[__](<doc-edit-2774.html>)
对此内容反馈
* _
__
  * 此方案由番薯贡献。  
若完全参照文档中场景与步骤操作，出现问题可咨询帆软技术支持团队，提供服务范围内的指导。（注：文档场景可能无法兼容所有客户场景）  
其他情况，可到帆软社区提问（问题响应快，解决率超80%），[立即提问](<https://bbs.fanruan.com/wenda>)。  
详情：[《关于帆软社区提问的相关说明》](<https://bbs.fanruan.com/thread-117166-1-1.html>)  
技术支持服务范围详见：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


社区级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[13](<edition-list-2774.html>)
* 最近更新：[dailer](<user-space-81512.html>) 于 2026-07-09 
[](<javascript:;>) [](<javascript:>)
## 1\. 功能概览
FineBI_Cli 通过 AI 连接 FineBI，使业务人员可以用自然语言查询数据、导出仪表板、生成分析报告、同步数据到飞书多维表格，并结合飞书消息或任务完成自动化跟进。
整体架构采用 FineBI Skill + FineBI_Cli + FineBI API
  * FineBI Skill：负责识别用户意图、提取参数、编排任务。
  * FineBI_Cli：负责 FineBI 鉴权、API 调用、文件导出、错误处理。
  * FineBI_API：提供数据集、仪表板、平台目录和组件数据等只读能力。


![](https://help.fanruan.com/core/style/lod.png)
## 2.方式一：自然语言安装（适用于 OpenClaw用户）
### 2.1 安装 FineBI Skill&Cli
可以在飞书小龙虾中直接完成 Skill & Cli 安装，可以发送：
[code]
    请帮我完成 FineBI Skill 的安装和依赖检查：  
      
    1. 从 ClawHub 安装 FineBI Skill：  
    https://clawhub.ai/zsmj1994/finebi-skills  
      
    2. 在 OpenClaw 运行环境中安装 finebi-cli：  
    npm install -g finebi-cli@latest --registry=https://registry.npmjs.org/  
      
    3. 安装完成后执行：  
    finebi-cli --help  
      
    完成后请把安装结果告诉我。  
    
[/code]
### 2.2 FineBI 服务端配置
获取 FineBI 的鉴权信息  

1）下载 Fine-Access-Token 插件：[fine-plugin-com.fr.plugin.access.token-1.0.0.zip](<doc-download-/finebi/uploads/file/20260522/fine-plugin-com.fr.plugin.access.token-1.0.0.zip> "下载资料")
2）安装插件，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）重启 FineBI 工程。
4）访问 FineBI 地址 +/url/access-key/create 。生成并妥善保存你的 FINE_ACCESS_TOKEN，用于后续接口鉴权，防止越权。
![](https://help.fanruan.com/core/style/lod.png)
### 2.3 配置 FineBI 环境信息
将 2.2 节获取的 FineBI 地址和 TOKEN 告诉飞书小龙虾，让它帮你更改配置文件。
需要在小龙虾的 .env 中修改 FINEBI_BASE_URL和 FINE_ACCESS_TOKEN 的参数值：
[code]
    请帮我配置 FineBI Skill 的环境变量。  
      
    请将以下配置写入 OpenClaw 默认 env 文件：  
      
    FINEBI_BASE_URL=**http://testcrmbi.com/webroot/decision**  
     FINE_ACCESS_TOKEN=**xxxxxx**  
      
     配置完成后，请检查 FineBI Skill 是否能正常读取这些环境变量。  
    
[/code]
完成安装。
## 3\. 方式二：命令行安装
如果你倾向于在终端（Terminal）中安装，请按照以下标准命令行流程进行部署。
1）安装 FineBI_Cli
[code]
    npm install -g finebi-cli@latest --registry=https://registry.npmjs.org/  
    
[/code]
2）安装 FineBI Skill
[code]
    # 使用 clawhub 命令行工具直接安装远端 Skill  
    clawhub install zsmj1994/finebi-skills  
    
[/code]
3）完成 FineBI 服务端配置，获取 FineBI 地址和生成的 FINE_ACCESS_TOKEN（用于后续接口鉴权，防止越权）。详情请参见本文 2.2 节。
4）配置环境变量
  * 若是小龙虾环境：修改当前小龙虾的 .env 文件


[code]
    FINEBI_BASE_URL=http://testcrmbi.com/webroot/decision  
    FINE_ACCESS_TOKEN=xxxxxx  
    
[/code]
  * 若脱离小龙虾环境，推荐使用 CLI 自带的交互式引导进行初始化。在终端执行：


[code]
    finebi-cli init  
    
[/code]
5）完成安装。
## 3\. 接口开放说明
  * 仅开放从 FineBI 读取数据或导出内容的能力。
  * 不开放写入、修改、删除 FineBI 资源的能力。


### 3.1 数据集接口
命令| 说明  
---|---  
get-publick-datasets-list| 分页获取公共数据的数据集列表(7.0)  
preview-dataset-data| 预览数据集数据，最多支持 10 万行  
get-dataset-info| 通过表名获取对应的数据集信息  
search-my-datasets| 搜索“我的分析”中的自助数据集  
search-public-dataset| 搜索公共数据目录中的数据集(7.0)  
### 3.2 仪表板与平台目录接口
命令| 说明  
---|---  
export-dashboard-excel| 将仪表板导出为 Excel 文件  
export-dashboard-pdf| 将仪表板导出为 PDF 文件  
export-dashboard-image| 将仪表板导出为 PNG 图片  
get-dashboard-user-info| 获取当前用户信息及其创建的仪表板  
search-my-dashboards| 搜索“我的分析”下的所有仪表板  
get-dashboards-by-subject| 获取特定主题下的仪表板列表  
get-dashboard-design-configure| 获取仪表板详细配置信息  
get-entry-tree| 获取平台目录树  
get-published-subject-resources| 根据平台目录节点挂出信息，查询对应挂出主题的资源  
get-widget-data| 根据仪表板 ID 和组件 ID 查询组件数据  
  

### 附件列表 
  
下载次数：：0
    
**主题：** [管理系统](<category-view-100>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：仪表板多语言切换](<index.php?doc-view-2447.html>)
[下一篇：FineBI_Cli 介绍及使用 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2776.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
