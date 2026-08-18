---
title: FineChatBI 配置项字段说明
doc_id: 2718
url: https://help.fanruan.com/finebi6.X/doc-view-2718.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:06:29
---

> 1. 概述本文汇总了 FineChatBI 的相关信息存储位置，以及对应的配置项字段说明。2. 管理员监管fine_ai_query_record 查询记录表存储用户的查询历史记录。字段名类型描述idv

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# FineChatBI 配置项字段说明
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[2](<edition-list-2718.html>)
* 最近更新：[Lily.Wang](<user-space-337243.html>) 于 2026-02-02 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
本文汇总了 FineChatBI 的相关信息存储位置，以及对应的配置项字段说明。
## 2\. 管理员监管
### fine_ai_query_record 查询记录表
存储用户的查询历史记录。
字段名  
| 类型| 描述|   
  
---|---|---|---  
id| varchar(255)| 主键ID|   
  
error_code| varchar(255)| 错误码|   
  
error_detail| varchar(255)| 错误详情|   
  
hasDisambiguation| bit(1)| 是否有歧义字段（0=否，1=是）|   
  
hasFeedback| bit(1)| 是否有反馈（0=否，1=是）|   
  
hasMissingWord| bit(1)| 是否有丢失词（0=否，1=是）|   
  
intention| longtext| 查询意图|   
  
intention_status| varchar(255)| 意图状态|   
  
multiple_turn| bit(1)| 是否多轮对话（0=否，1=是）|   
  
query| varchar(4000)| 查询语句|   
  
query_id| varchar(255)| 查询ID|   
  
query_time| bigint| 查询时间（时间戳）|   
  
query_type| varchar(255)| 查询类型|   
  
remark| varchar(255)| 备注|   
  
sentence| longtext| 解析后的语句|   
  
subject_id| varchar(255)| 主题ID|   
  
is_success| bit(1)| 是否成功（0=否，1=是）|   
  
tag_id| varchar(255)| 标签ID|   
  
user_id| varchar(255)| 用户ID|   
  
### fine_ai_feedback_record 反馈记录表
存储用户对查询结果的反馈。
字段名  
| 类型| 描述  
---|---|---  
id| varchar(255)| 主键 ID  
dislike_detail| varchar(255)| 不满意详情  
dislike_type| varchar(255)| 不满意类型  
feedback_type| varchar(255)| 反馈类型（满意/不满意）  
operate_time| bigint| 操作时间（时间戳）  
operator_status| varchar(255)| 操作状态  
query_id| varchar(255)| 查询ID  
subject_id| varchar(255)| 主题ID  
### fine_ai_word_confirm_record 歧义词/丢失词确认记录表
存储用户对歧义词和丢失词的确认记录。
字段名  
| 类型| 描述|   
  
---|---|---|---  
id| varchar(255)| 主键 ID|   
  
field_name| varchar(255)| 字段名称|   
  
ignored| bit(1)| 是否忽略（0=否，1=是）|   
  
model_id| varchar(255)| 模型 ID|   
  
operate_time| bigint| 操作时间（时间戳）|   
  
operator_status| varchar(255)| 操作状态|   
  
query_id| varchar(255)| 查询 ID|   
  
subject_id| varchar(255)| 主题 ID|   
  
table_id| varchar(255)| 表 ID|   
  
user_id| varchar(255)| 用户ID|   
  
word| varchar(255)| 词内容|   
  
word_confirm_type| varchar(255)| 词确认类型|   
  
word_type| varchar(255)| 词类型：Disambiguation - 歧义词  
Missing - 丢失词|   
  
## 3\. 预加载
### fine_ai_preload_subject 预加载分析主题表
存储分析主题的预加载信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
creator_id| varchar(255)| 创建者 ID  
error_message| varchar(4000)| 错误信息  
last_update_time| bigint| 最后更新时间（时间戳）  
loaded| bit(1)| 是否已加载（0=否，1=是）  
subject_desc| varchar(2000)| 主题描述  
subject_id| varchar(255)| 主题 ID  
update_success| bit(1)| 更新是否成功（0=否，1=是）  
### fine_ai_preload_field_config 字段预加载配置表
配置字段的预加载规则。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
data_format| varchar(255)| 数据格式
[code]
    {  
        "formatStyle":"PERCENTAGE",  
        "precision":2,  
        "suffix": "元",  
        "numberUnit":"THOUSAND",  
        "thousandSeparator":false,  
        "showHeaderPercent":false  
    }  
    
[/code]
formatStyle:
  * AUTO：自动  

  * PERCENTAGE：百分比
  * DIGIT：数字

precision：小数位数suffix：单位后缀numberUnit:
  * NONE：无
  * THOUSAND：千
  * TEN_THOUSAND：万
  * MILLION：百万
  * HUNDRED_MILLION：亿

thousandSeparator：千分符showHeaderPercent：表格表头单位  
data_length_limit| int| 数据长度限制  
field_id| varchar(255)| 字段 ID  
field_preload_type| varchar(255)| 字段预加载类型
  * ALL：全量学习
  * LIMIT：基础学习
  * IGNORE：不学习

  
fuzz_match| bit(1)| 是否模糊匹配（0=否，1=是）  
load_enum| bit(1)| 是否加载枚举值（0=否，1=是）  
subject_id| varchar(255)| 主题 ID  
table_id| varchar(255)| 表 ID  
case_sensitive| bit(1)| 是否大小写敏感（0=否，1=是）  
### fine_ai_preload_node 预加载节点表
存储预加载的节点信息，主要是「数据中心」的指标和维度信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
node_id| varchar(255)| 节点 ID  
node_type| varchar(255)| 节点类型：Metric - 指标；Dimension - 维度；Package - 文件夹  
## 4\. 标签
### fine_ai_data_tag 标签表
存储分类标签信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
tag_desc| varchar(255)| 标签描述  
tag_id| varchar(255)| 标签 ID  
tag_name| varchar(255)| 标签名称  
## 5\. 知识配置
### fine_ai_table_aliases 表别名表
存储数据表的别名（业务用语）。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
aliases| varchar(4000)| 别名列表  
global| bit(1)| 是否全局  
subject_id| varchar(255)| 主题 ID  
table_id| varchar(255)| 表 ID  
### fine_ai_field_aliases 字段别名表
存储数据表字段的别名（业务用语）。
字段名| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
aliases| varchar(4000)| 别名列表  
field_id| varchar(255)| 字段 ID  
global| bit(1)| 是否全局  
subject_id| varchar(255)| 主题 ID  
table_id| varchar(255)| 表 ID  
### fine_ai_enum_aliases 维度枚举别名表
存储维度枚举值的别名（业务用语）。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
aliases| varchar(4000)| 别名列表  
dimension_enum| varchar(255)| 维度枚举值  
field_id| varchar(255)| 字段 ID  
global| bit(1)| 是否全局  
subject_id| varchar(255)| 主题 ID  
table_id| varchar(255)| 表 ID  
### fine_ai_custom_aliases 自定义别名表
存储用户自定义语的别名（业务用语）。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
aliases| varchar(4000)| 用户输入的词  
global| bit(1)| 是否全局  
sentence| varchar(4000)| 标准词  
subject_id| varchar(255)| 主题 ID  
### fine_ai_params 参数表
存储用户的参数。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
aliases| varchar(4000)| 用户输入的词  
fields| varchar(4000)| 字段  
global| bit(1)| 是否全局  
param_key| varchar(255)| 参数  
subject_id| varchar(255)| 主题 ID  
### fine_ai_business_rule 业务规则
存储业务规则相关信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
business_type| varchar(255)| 业务规则类型  
description| varchar(4000)| 业务规则描述  
global| bit(1)| 是否是全局业务规则  
key_word| varchar(4000)| 关键词  
range_type| varchar(255)| 生效范围（个人还是全员）  
subject_id| varchar(255)| 主题 ID  
user_id| varchar(255)| 创建者 ID  
  

## 6\. 推荐问题配置
### fine_ai_recommend_card 推荐问题分类表
存储推荐问题的分类信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
card_type| varchar(255)| 卡片类型  
icon_index| int| 图标索引（用来确定展示的图标）  
card_index| int| 卡片索引（排序）  
card_name| varchar(255)| 推荐问题分类名称  
### fine_ai_card_question (推荐问题表)
存储推荐卡片的问题。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
card_id| varchar(255)| 卡片 ID  
question_index| int| 问题索引（排序）  
question| longtext| 问题内容  
subject_id| varchar(255)| 主题 ID  
## 7\. 用户偏好
### fine_ai_word_confirm_record 确认记录表
存储消歧确认记录。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
field_name| varchar(255)| 字段名称  
ignord| bit(1)| 是否忽略  
operate_time| Long| 操作时间  
operator_status| varchar(255)| 操作状态  
query_id| varchar(255)| queryID  
subject_id| varchar(255)| 主题 ID  
table_id| varchar(255)| 表 ID  
user_id| varchar(255)| 用户 ID  
word| varchar(255)| 歧义词  
word_confirm_type| varchar(255)| 歧义类型  
word_type| varchar(255)| 字段类型  
model_id| varchar(255)| modelID  
transfer_name| varchar(255)| 字段别名  
dimension_enus| varchar(255)| 维度枚举值  
### fine_ai_subject_disam
存储主题消歧的相关信息。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
subject_id| varchar(255)| 主题 ID  
text| varchar(255)| 歧义问题  
user_id| varchar(255)| 用户 ID  
is_word| varchar(255)| 歧义词还是歧义问题  
## 8\. 历史会话
### fine_ai_conv_history 历史会话记录表
存储历史会话记录。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
session_id| varchar(255)| 会话 ID  
user_id| varchar(255)| 用户 ID  
subject_id| varchar(255)| 主题 ID  
tag_id| varchar(255)| 标签 ID  
available_subject_ids| varchar(4000)| 标签对应的分析主题 ID 列表  
conversation_mode| varchar(255)| 问答模式  
is_favorite| bit(1)| 是否收藏  
title| varchar(255)| 标题  
update_time| bigint| 更新时间  
last_query_id| varchar(255)| 最新的问题 ID  
ai_rank_subject_result| longtext| 主题排序结果  
history_subject_ids| varchar(4000)| 历史问答过的所有主题ID列表  
### fine_ai_conv_query_history 历史会话记录明细表
存储历史会话记录明细。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
query_id| varchar(255)| 问题 ID  
session_id| varchar(255)| 会话 ID  
origin_query| longtext| 原始问题  
response_strategy| varchar(255)| 响应策略  
query_time| bigint| 提问时间  
update_time| bigint| 更新时间  
conversation_mode| varchar(255)| 问答模式  
tag_id| varchar(255)| 标签ID  
subject_id| varchar(255)| 主题ID  
error_code| varchar(255)| 报错码  
error_msg| varchar(255)| 报错信息  
query_status| varchar(255)| 查询状态  
intention_status| varchar(255)| 意图类型  
round_result_type| varchar(255)| 问答结果类型  
query_data_result| longtext| 问数据结果  
attribution_result| longtext| 归因分析结果  
analysis_plan_result| longtext| 分析思路结果  
analysis_break_result| longtext| 问思路结果  
resolved_charts| longtext| 图表结果  
report| longtext| 分析报告  
### fine_ai_conv_read_status 历史会话已读状态管理表
存储历史会话记录。
字段名  
| 类型| 说明  
---|---|---  
id| varchar(255)| 主键 ID  
session_id| varchar(255)| 会话 ID  
last_query_id| varchar(255)| 最新 Query 的 ID  
last_query_status| varchar(255)| 最新 Query 的查询状态  
is_read| bit(1)| 是否已读  
user_id| varchar(255)| 用户 ID  
update_time| bigint| 更新时间  
## 9\. 其他配置
其他配置中的内容，基本上都存储在 fine_conf_entity 表中，具体的对应关系如下：
参数名| 参数描述  
| 说明  
---|---|---  
AIConversationConfig.host| 语义解析小模型-主机| OPS 部署环境下，此字段不生效  
AIConversationConfig.port| 语义解析小模型-端口| OPS 部署环境下，此字段不生效  
ConversationCopilotConfig.llmEnable.modelEnabled| 大模型配置开关|   
  
ConversationCopilotConfig.aiCloudIp| FineAI-主机| OPS 部署环境下，此字段不生效  
ConversationCopilotConfig.aiCloudPort| FineAI-端口| OPS 部署环境下，此字段不生效  
ConversationCopilotConfig.llmModelName| 大模型配置-服务商名称|   
  
ConversationCopilotConfig.llmApiKey| 大模型配置-APIKey|   
  
ConversationCopilotConfig.llmParams.endPoint| 大模型配置-endPoint|   
  
ConversationCopilotConfig.llmParams.deploymentName| 大模型配置-部署模型名称|   
  
ConversationCopilotConfig.defaultConversationMode| 默认问答模式| smart：智能模式；speed：极速模式  
ConversationCopilotConfig.llmEnable.rewriteEnabled| 智能改写开关|   
  
ConversationCopilotConfig.llmEnable.analysisBreakEnabled| 分析思路开关|   
  
ConversationCopilotConfig.llmEnable.resultAnalysisEnabled| 智能解读开关|   
  
ConversationCopilotConfig.alternativeLlmModelName| 数据解读-服务商名称|   
  
ConversationCopilotConfig.alternativeLlmApiKey| 数据解读-APIKey|   
  
ConversationCopilotConfig.alternativeLlmParams.endPoint| 数据解读-endPoint|   
  
ConversationCopilotConfig.alternativeLlmParams.deploymentName| 数据解读-部署模型名称|   
  
ConversationCopilotConfig.llmEnable.analysisSummaryEnabled| 归因分析建议开关|   
  
ConversationCopilotConfig.llmEnable.autoConfigEnabled| 一键配置开关|   
  
ConversationCopilotConfig.llmEnable.autoSubjectDescEnabled| 智能简介开关|   
  
ConversationCopilotConfig.llmEnable.chatDashboardEnabled| 找报表开关|   
  
PredictConfig.enable| 预测配置开关|   
  
KnowledgeConfig.enable| 知识库问答配置开关|   
  
KnowledgeConfig.url| 知识库问答配置-请求地址|   
  
KnowledgeConfig.stream| 知识库问答配置-流式输出|   
  
KnowledgeConfig.name| 知识库问答配置-问法名称|   
  
KnowledgeConfig.description| 知识库问答配置-提示内容|   
  
PreChatConfig.enable| 预处理配置开关|   
  
PreChatConfig.url| 预处理配置-请求地址|   
  
ConversationVoiceConfig.enable| 语音集成设置开关|   
  
ConversationVoiceConfig.url| 语音集成设置-接口地址|   
  
ConversationLanguageConfig.enableUserCustom| 语音集成设置-是否允许不同用户自定义语言|   
  
ConversationLanguageConfig.defaultLanguage| 语音集成设置-系统默认语言|   
  
ConversationLanguageConfig.userCustomLanguage| 语音集成设置-用户自定义语言|   
  
ReportTemplateConfig.globalTemplates| 仪表板报告配置-全局模板配置|   
  
ReportTemplateConfig.userTemplates| 仪表板报告配置-用户自定义模板|   
  
HistoryConfig.maxSessionRound| 历史会话-单个会话最大问答轮次| 默认100，不提供前端修改参数接口  
HistoryConfig.maxSessionItem| 历史会话-单个用户最大问答会话个数| 默认100，不提供前端修改参数接口  
HistoryConfig.maxActiveSession| 历史会话-单个用户最大活跃会话个数| 默认 3 ，不提供前端修改参数接口  
  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-760>)
[![](/core/style/back.png)上一篇：FineChatBI 错误代码汇总](<index.php?doc-view-2717.html>)
[下一篇：集成指南下架说明 ![](/core/style/forward.png) ](<index.php?doc-view-2725.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
