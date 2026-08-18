---
title: 判断大模型是否满足 FineChatBI 能力要求
doc_id: 2612
url: https://help.fanruan.com/finebi/doc-view-2612.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:25:28
version: "7.X"
---

> 1. 概述FineChatBI 要求大模型必须严格按照指定格式输出结果，否则无法正常使用。本文档适用于用户在连接本地大模型前，提前验证模型是否符合要求。2. 测试方法2.1 发送请求保证 FineAI

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# 判断大模型是否满足 FineChatBI 能力要求
[__](<doc-edit-2612.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Lily.Wang](<user-space-337243.html>)_
* 历史版本：[7](<edition-list-2612.html>)
* 最近更新：[BeauXu-徐备](<user-space-2226036.html>) 于 2025-09-25 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
FineChatBI 要求大模型必须严格按照指定格式输出结果，否则无法正常使用。本文档适用于用户在连接本地大模型前，提前验证模型是否符合要求。
## 2\. 测试方法
### 2.1 发送请求
保证 FineAI 服务网络能联通大模型服务。
在 FineAI 所在服务器使用 curl 命令向大模型服务发送请求（示例基于 OpenAI Chat 接口格式）。实际使用时，请根据您的具体配置修改以下参数：
  * IP、PORT、URL：替换为实际的服务地址。其中 URL 必须以 /chat/completions 结尾，否则不符合 OpenAI 接口。
  * MODEL_NAME：替换为实际的模型名称。
  * API_KEY：若不需要认证，请删除 `-H "Authorization: Bearer API_KEY"` 这一行。
  * max_tokens 必须设置在 8192 以上，若模型上下文长度不足 8192，则无法兼容 FineChatBI。


[code]
    curl http://IP:PORT/URL/chat/completions \  
    -H "Content-Type: application/json" \  
    -H "Authorization: Bearer API_KEY" \  
    -d '{  
        "model": "MODEL_NAME",  
        "messages": [  
            {"role": "system", "content": "你是一个近义词生成助手，我会给你一些表名、对应表的字段名，你可以根据表名和字段名合理的联想和推测，生成表名或字段名的近义词或缩略词。\n```\n你生成的字段名格式必须满足以下规则：\n1.只能返回json，不需要markdown代码符号\n2.给每个字段名或表名生成5个近义词，近义词可以生成一些简称，如 \"门店信息维度表\"的近义词可以是 门店信息, 门店等\n3.字段名近义词可以与表名进行结合，例如，表名为\"门店\"，字段名为\"名称\"，近义词可以为：\"门店名\",\"店铺名\"等\n4.同一个表的字段不能生成相同的近义词\n5.中文和英文混合的字段名必须保持与输入一致\n6.返回的JSON格式为：\n{\n  \"table_aliases_dic\":\n    [\n      {\n        \"table_name\":  表名,\n        \"aliases\": 表名同义词数组,\n        \"fields\": [\n          {\n            \"field_name\": 字段名,\n            \"aliases\": 字段名同义词数组\n          }\n        ]\n      }\n    ]\n}\n7.返回的JSON必须是\"table_aliases_dic\",不能是\"tableAliasesDic\"\n```\n示例如下：\n存在以下表和字段：\n表名：公司表\n字段：ID, 名称, 简称, 板块\n表名：科目表\n字段：名称, 简称\n表名：预算明细表\n字段：日期, 预算\n\n问：请生成表名和字段的近义词或缩略词\n答：\n{ \"table_aliases_dic\":[\n  {\n    \"table_name\": \"公司表\",\n    \"aliases\": [\"公司\", \"企业\", \"机构\", \"机关\", \"单位\"],\n    \"fields\": [\n      {\"field_name\": \"ID\", \"aliases\": [\"唯一标识\", \"标识\", \"公司id\", \"公司编码\", \"公司编号\"]},\n      {\"field_name\": \"名称\", \"aliases\": [\"名字\", \"公司名\", \"机构名\", \"企业名\", \"称号\"]},\n      {\"field_name\": \"简称\", \"aliases\": [\"公司缩写\", \"企业简称\", \"公司略写\", \"略称\", \"简称代号\"]},\n      {\"field_name\": \"板块\", \"aliases\": [\"区块\", \"业务板块\", \"分区\", \"分块\", \"组块\"]}\n    ]\n  },\n  {\n    \"table_name\": \"科目表\",\n    \"aliases\": [\"领域\", \"分类\", \"类目\", \"主题\", \"分科\"],\n    \"fields\": [\n      {\"field_name\": \"名称\", \"aliases\": [\"名字\", \"科目名\", \"分类名\", \"项目名\", \"称号\"]},\n      {\"field_name\": \"简称\", \"aliases\": [\"缩写\", \"简称\", \"领域简称\", \"略称\", \"简称代号\"]}\n    ]\n  },\n  {\n    \"table_name\": \"预算明细表\",\n    \"aliases\": [\"预算细目\", \"预算\", \"估算明细\", \"明细\", \"预算规划明细\"],\n    \"fields\": [\n      {\"field_name\": \"日期\", \"aliases\": [\"时间\", \"详细日期\", \"年月日\", \"预算时间\", \"具体时间\"]},\n      {\"field_name\": \"预算\", \"aliases\": [\"目标\", \"任务\", \"金额\", \"明细\", \"收入\"]}\n    ]\n  }\n]\n}\n示例结束\n```"},  
            {"role": "user","content": "现存在以下表和字段：\n{\"tables\":[{\"tableName\":\"商品明细\",\"tableFields\":[{\"fieldName\":\"商品编码\"}]}]}\n请帮我生成同义词"}  
        ],  
        "max_tokens": 8192,  
        "stream": false  
    }'  
    
[/code]
  

### 2.2 返回 content 的格式要求
返回示例样式如下（此示例基于 OpenAI Chat 接口，实际返回格式可能因不同接口而异）：  

  

{  
"choices": [  
{  
"index": 0,  
"message": {  
"role": "assistant",  
**"content": "大模型生成的内容"**  
},  
"finish_reason": "stop",  
}  
],  
…… // 其他参数可忽略，如 id  
}
1）检查 content 是否满足格式
返回体中的 choices.message.content 是大模型的输出，若按 2.1 节发送请求，返回的内容必须满足以下格式。
注：部分模型（如DeepSeek-R1/QwQ）可能在返回的 content 中多出思考过程，但下述基础格式是必须包含的。
{
"table_aliases_dic": [  
{  
"table_name": "略",  
"aliases": ["略"],  
"fields": [  
{  
"field_name": "略",  
"aliases": ["略"]  
}  
]  
}  
]  
}
2）检查返回的 content 是否是 json 格式。
复制返回体中携带的 content 部分（需包含外层引号）打开在线验证工具网站（<https://www.jyshare.com/compile/9/>）。在页面左侧输入框中输入 print(复制的内容)，再「点击运行」，如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
复制运行结果到 <https://www.json.cn/> 网页并粘贴，若右侧能正常解析则表示该部分符合 json 格式。如下图所示：
![](https://help.fanruan.com/core/style/lod.png)
3）连续执行 5 次 curl 命令（2.1节），若模型均能稳定返回正确格式的内容，则可判定此模型符合 FineChatBI 要求。
## 3\. 完整示例参考
1）执行 curl 命令（本文 2.1 节），发送的命令和返回体如下图所示：
![22.png](https://help.fanruan.com/core/style/lod.png)
其中返回体内容如下：
{  
"choices": [  
{  
"index": 0,  
"message": {  
"role": "assistant",  
"content": "{\n \"table_aliases_dic\": [\n {\n \"table_name\": \"商品明细\",\n \"aliases\": [\"商品信息\", \"商品详情\", \"商品列表\", \"商品数据\", \"商品记录\"],\n \"fields\": [\n {\n \"field_name\": \"商品编码\",\n \"aliases\": [\"商品ID\", \"编码\", \"商品编号\", \"商品标识\", \"产品编码\"]\n }\n ]\n }\n ]\n}"  
},  
"finish_reason": "stop",  
}  
],  
…… // 其他参数可忽略，如 id  
}
2）返回体中的 choices.message.content 是大模型的输出，将 content 的值解析后得到如下内容：  

对照本文 2.2 节的内容格式，可见 content 部分完全符合格式。
{
"table_aliases_dic": [  
{  
"table_name": "商品明细",  
"aliases": ["商品信息", "商品详情", "商品列表", "商品数据", "商品记录"],  
"fields": [  
{  
"field_name": "商品编码",  
"aliases": ["商品ID", "编码", "商品编号", "商品标识", "产品编码"]  
}  
]  
}  
]  
}  
  

3）连续测试 5 次
连续 5 次执行 curl 命令（本文 2.1节），若模型都能稳定的返回正确格式的内容，则该模型符合 FineChatBI 的要求。  

### 附件列表 
  
下载次数：：0
    
**主题：** [FineChatBI智能问答](<category-view-763>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：推理大模型](<index.php?doc-view-2672.html>)
[下一篇：FineChatBI 错误代码汇总 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-2725.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
