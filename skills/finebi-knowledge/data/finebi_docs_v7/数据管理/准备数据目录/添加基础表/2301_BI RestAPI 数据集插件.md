---
title: BI RestAPI 数据集插件
doc_id: 2301
url: https://help.fanruan.com/finebi/doc-view-2301.html
source: FineBI 7.X 帮助文档
crawled_at: 2026-07-16 17:26:23
version: "7.X"
---

> 1. 概述1.1 版本FineBI 版本功能变更7.0新增动态Token认证说明1.2 功能场景BI Rest API数据集支持FineBI对接WEB API进行取数。对接第三方的WEB API进行取数

![](./view/finebi70_2025/images/info_fill.png) 您正在浏览的是 FineBI7.X 帮助文档，点击跳转至： [FineBI6.X帮助文档](<https://help.fanruan.com/finebi6.X/>)
# BI RestAPI 数据集插件
[__](<doc-edit-2301.html>)
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[小张好像不在线](<user-space-703598.html>)_
* 历史版本：[17](<edition-list-2301.html>)
* 最近更新：[Dejiang.Wang](<user-space-3447105.html>) 于 2026-05-28 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 版本
FineBI 版本| 功能变更  
---|---  
7.0| 新增动态Token认证说明  
### 1.2 功能场景
BI Rest API数据集支持FineBI对接WEB API进行取数。
  * 对接第三方的WEB API进行取数。
  * 通过JSON解析返回的数据。
  * **直连数据集支持直连传递参数调用第三方的WEB API。**


### 1.3 注意事项
Rest API 数据集不支持增量更新，仅支持全量覆盖。
## 2\. 插件介绍
### 2.1 插件安装
  * 插件获取：[BI Rest API数据集插件](<https://market.fanruan.com/plugin/0b642404-fc08-48c3-97bd-3ca2bf3998da>)
  * 设计器插件安装方法参照：[设计器插件管理](<https://help.fanruan.com/finereport/doc-view-2198.html>)
  * 服务器安装插件方法参照：[服务器插件管理](<https://help.fanruan.com/finereport/doc-view-2220.html>)


**插件安装、更新、禁用后重新启用，都需要重启FineBI才会生效。**
### 2.2 使用流程
1）安装插件后，公共数据的创建数据集中出现“Rest数据集”选项。
![](https://help.fanruan.com/core/style/lod.png)
2）点击进入创建数据集界面，完成相关配置后，点击保存。
![创建数据集界面截图](https://help.fanruan.com/core/style/lod.png)
3）在数据预览模块，可以预览添加的数据集，该数据集可以用于BI分析中。
![数据预览截图](https://help.fanruan.com/core/style/lod.png)
### 2.3 面板配置说明
![面板配置说明截图](https://help.fanruan.com/core/style/lod.png)
①：数据集名称，可重命名。
②：请求类型，支持GET和POST请求方式。
③：URL地址，填写接口完整地址即可。
![URL地址配置截图](https://help.fanruan.com/core/style/lod.png)
**URL参数：** Query参数会自动拼接到URL地址中。
![URL参数配置截图](https://help.fanruan.com/core/style/lod.png)
**API认证：** 支持的认证方式有：无认证、Basic Auth、Bearer Token、动态Token认证、其他认证（自定义Token）。
![API认证方式截图](https://help.fanruan.com/core/style/lod.png)
**请求头：** 添加请求头参数。
**请求体：** 只有在POST请求方式下，才需要配置Body。
表单方式支持：form-data 与 x-www-form-urlencoded。
文本方式支持：TEXT、JSON、XML。
**返回值处理：** 返回值处理支持JSON解析，通过使用JsonPath语句，查找节点、获取想要的数据。
**参数设置：** 支持配置参数，可以在API配置中引用参数，URL、Query参数值、认证参数、Header参数值、Body中均可使用。
引用形式：${参数名}。
在直连数据集里，此处参数支持实时传参调用。
### 2.4 全局配置
在“管理系统 > 系统管理 > 常规 > RestAPI全局配置”中可以进行全局配置，设置日志和连接池相关属性。
![RestAPI全局配置截图](https://help.fanruan.com/core/style/lod.png)
## 3\. 注意事项
当前默认都输出为文本字段。如需修改字段类型，点击如图所示的“编辑”按钮，进行字段类型转换。
![字段类型转换截图](https://help.fanruan.com/core/style/lod.png)
## 4\. 动态Token认证
### 4.1 功能说明
动态Token鉴权用于以下场景：
  * 业务接口调用前，需要先请求一个取Token接口。
  * Token不是固定值，而是需要按接口返回结果动态获取。
  * 正式业务请求中，需要在Header、Query、Body或URL中引用该Token。
  * Token存在有效期，希望在一定时间内复用，避免每次都重复获取。


整体执行流程如下：
  1. 先调用配置好的Token接口。
  2. 从Token接口响应中按JSON Path提取Token值。
  3. 将提取出的原始Token写入运行时变量 `${dynamic_token}`。
  4. 执行正式业务请求，并将 `${dynamic_token}` 替换到URL、Header、Query、Body中。


### 4.2 配置入口
在数据集配置页面中：
  1. 打开配置TAB。
  2. 找到认证方式。
  3. 选择 `动态Token`。
![](https://help.fanruan.com/core/style/lod.png)  



可用运行时变量：
  * `${dynamic_token}`：取Token接口返回并提取到的原始Token值。


### 4.3 字段说明
### 4.3.1 Token接口URL
填写获取Token的接口地址。
[code]
    https://api.example.com/auth/token
[/code]
说明：
  * 支持数据集参数替换。
  * 该地址用于插件先发起一次Token请求。


### 4.3.2 请求方式
当前支持：
  * GET
  * POST


说明：
  * 若选择POST，可以同时配置请求体。
  * 若不是GET，后端会按POST处理。


### 4.3.3 Token JSON路径
用于从Token接口响应中提取token字段，语法为JSON Path。
[code]
    $.token
    $.data.access_token
    $.result.token
[/code]
要求：
  * 该路径必须能提取到非空值。
  * 若提取结果为空，正式请求不会继续执行，并提示获取动态Token失败。


### 4.3.4 启用缓存
用于控制是否缓存Token。
  * 关闭：每次执行业务请求前都重新获取Token。
  * 开启：命中缓存时直接复用Token，不再重复调用Token接口。


### 4.3.5 缓存模式
启用缓存后可选两种模式：
  * 固定时长：手工指定缓存秒数。
  * 从响应提取过期时长：从Token接口响应里取TTL字段。


### 4.3.6 缓存时长(秒)
仅在固定时长模式下生效。
[code]
    3600
[/code]
说明：
  * 表示Token缓存1小时。
  * 小于等于0时，不会形成有效缓存。


### 4.3.7 过期时长JSON路径
仅在从响应提取过期时长模式下生效。
[code]
    $.expires_in
    $.data.expires
[/code]
说明：
  * 该字段应为数字，或可转换为数字的字符串。
  * 若取值失败或不是数字，会提示动态Token过期时长解析失败。


### 4.3.8 Token接口请求体
用于配置获取Token时发送的请求体。
[code]
    {
      "clientId": "demo_client",
      "clientSecret": "demo_secret"
    }
[/code]
说明：
  * 仅在Token请求方式为POST时生效。
  * 若未手工设置Content-Type，插件会默认补 application/json。
  * 支持数据集参数替换。


### 4.3.9 Token接口请求Header参数
用于配置获取Token接口时附带的请求头。
[code]
    Content-Type: application/json
    X-App-Id: demo-app
[/code]
说明：
  * 支持配置多个Header。
  * Header值支持数据集参数替换。


### 4.4 正式请求中如何使用Token
动态Token拿到后，会提供变量 `${dynamic_token}`，可用于以下位置：
  * 正式请求URL。
  * Query参数。
  * Header参数。
  * Body内容。


示例一：放在查询参数中。
[code]
    token=${dynamic_token}
[/code]
示例二：放在Header中。
[code]
    X-Access-Token: ${dynamic_token}
[/code]
示例三：放在JSON请求体中。
[code]
    {
      "token": "${dynamic_token}",
      "keyword": "${keyword}"
    }
[/code]
### 4.5 配置示例
### 4.5.1 场景示例
先调用登录接口：
[code]
    POST /auth/login
    Content-Type: application/json
    
    {
      "username": "demo",
      "password": "123456"
    }
[/code]
返回：
[code]
    {
      "code": 0,
      "data": {
        "access_token": "abc123xyz",
        "expires_in": 7200
      }
    }
[/code]
再调用业务接口：
[code]
    GET /orders/list
    X-Access-Token: abc123xyz
[/code]
### 4.5.2 动态Token配置示例
可按下面方式填写：
  * Token接口URL：`https://api.example.com/auth/login`
  * 请求方式：`POST`
  * Token JSON路径：`$.data.access_token`
  * 启用缓存：`是`
  * 缓存模式：`从响应提取过期时长`
  * 过期时长JSON路径：`$.data.expires_in`
  * Token接口请求Header参数：`Content-Type=application/json`


Token接口请求体：
[code]
    {
      "username": "demo",
      "password": "123456"
    }
[/code]
正式业务请求中可这样使用：
  * Header：`X-Access-Token = ${dynamic_token}`
  * Query：`access_token = ${dynamic_token}`
  * Body：`"token": "${dynamic_token}"`


### 4.6 预览调试建议
动态Token配置区自带预览按钮，建议先单独预览Token接口，确认以下几点：
  * Token接口URL可访问。
  * 请求方式正确。
  * 请求Header和请求体正确。
  * 返回结果中确实包含目标token字段。
  * JSON Path能正确提取到值。


如果Token接口预览通过，再配置正式业务请求里的 `${dynamic_token}` 引用。
### 4.7 注意事项
### 4.7.1 ${dynamic_token} 是保留运行时变量
不要把 `dynamic_token` 当作普通数据集参数使用。
说明：
  * 该变量由插件在运行时写入。
  * 它会保留到正式请求发起前再替换。
  * 即使存在同名用户参数，也不会覆盖运行时动态Token值。


### 4.7.2 Token接口参数替换范围
当前支持数据集参数替换的Token配置项包括：
  * Token接口URL。
  * Token接口请求体。
  * Token接口请求Header的值。


不建议把动态表达式放在以下配置项中：
  * Token JSON路径。
  * 缓存模式。
  * 缓存时长。
  * 过期时长JSON路径。


### 4.7.3 缓存键的组成
以下配置变化会影响缓存命中：
  * Token接口URL。
  * 请求方式。
  * 请求体。
  * Token JSON路径。
  * Token请求Header。
  * 缓存模式。
  * 缓存时长。
  * 过期时长JSON路径。


只要这些配置变化，插件会认为是另一份Token缓存。
### 4.8 常见问题
### 4.8.1 为什么提示获取动态Token失败？
请优先检查：
  * Token接口URL是否可访问。
  * 请求方式是否正确。
  * 请求Header和请求体是否正确。
  * Token JSON路径是否能提取到值。
  * Token接口是否返回了空token。


### 4.8.2 为什么缓存没生效？
请检查：
  * 是否已开启缓存。
  * 固定时长是否大于0。
  * 若按响应提取TTL，JSON路径是否正确。
  * TTL字段是否为数字。


### 4.8.3 为什么目标接口没有识别到Bearer Token？
因为动态Token只会提供运行时变量 `${dynamic_token}`，不会自动帮你组装：
[code]
    Authorization: Bearer <token>
[/code]
如果业务接口必须要求Bearer前缀，请在正式请求Header中手工配置：
[code]
    Authorization = Bearer ${dynamic_token}
[/code]
**补充：** 如果目标服务要求的是自定义Header，也可以直接把 `${dynamic_token}` 放到对应Header、Query或Body字段中。
### 4.8.4 为什么点击预览报错
暂时不支持配置项有参数的时候执行预览  

  

### 附件列表 
  
下载次数：：0
    
**主题：** [数据治理](<category-view-285>)
[![](https://help.fanruan.com/core/style/back.png)上一篇：添加表概述](<index.php?doc-view-43.html>)
[下一篇：添加数据库表 ![](https://help.fanruan.com/core/style/forward.png) ](<index.php?doc-view-887.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
