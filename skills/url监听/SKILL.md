---
name: url监听
description: url监听技能
---

DrissionPage 网络请求监听技能使用说明
1. 功能概述
DrissionPage 网络请求监听工具是一个基于 DrissionPage 库的浏览器网络请求捕获工具，用于实时监听浏览器发出的特定 API 请求，并获取详细的请求信息。主要功能包括：

启动 Chromium 浏览器并打开指定页面

设置监听目标（URL、请求方法）

捕获匹配条件的网络请求数据包

提取请求的 URL、方法、请求头（Headers）和请求体（POST Data）

实时打印或保存捕获到的请求信息

该工具适用于接口调试、爬虫参数分析、自动化测试等场景。

2. 安装和配置
2.1 环境要求
Python 3.6 及以上版本

安装 DrissionPage 库：pip install DrissionPage

系统需安装 Chromium 或 Chrome 浏览器（DrissionPage 会自动查找，也可手动指定路径）

2.2 配置文件
本工具无需额外配置文件，所有设置均在代码中完成。

3. 使用方法
3.1 基本使用流程
导入 ChromiumPage 类

创建 ChromiumPage 对象，启动浏览器

获取监听器 page.listen

设置监听目标 listener.set_targets()

启动监听 listener.start()

循环等待捕获请求 listener.wait()

处理捕获到的数据包 packet

停止监听 listener.stop()

3.2 初始化监听器
python
from DrissionPage import ChromiumPage

# 创建浏览器对象（会自动打开一个浏览器窗口）
page = ChromiumPage()

# 获取监听器
listener = page.listen
3.3 设置监听目标并启动
python
# 设置监听目标：监听指定URL的POST请求，同时监听响应（可选）
listener.set_targets(
    targets='https://sys.kqgyl.com/v1/waybill/manage/selectList',
    method='POST',
    res_type=True  # 是否监听响应，默认为False
)

# 启动监听
listener.start()
print("监听器已启动，等待 API 请求...")
3.4 等待并处理请求
python
# 循环等待捕获请求
while True:
    packet = listener.wait(timeout=10)  # 等待10秒，若无请求则返回None
    if packet:
        print(f"\n=== 监听到目标API请求 ===")
        print(f"URL: {packet.url}")
        print(f"请求方法: {packet.method}")
        print(f"请求头:")
        for k, v in packet.request.headers.items():
            print(f"  {k}: {v}")
        
        # 打印请求体（POST数据）
        if packet.request.postData:
            print(f"请求体: {packet.request.postData}")
        
        # 如果需要响应内容（需开启res_type=True）
        if packet.response.body:
            print(f"响应体: {packet.response.body}")
        
        print(f"\n=== 请求信息结束 ===")
3.5 停止监听
python
listener.stop()
# 可选关闭浏览器
# page.close()
4. 参数说明
4.1 listener.set_targets() 参数
参数名	类型	默认值	说明
targets	str 或 list	必填	监听的URL，支持字符串或列表（可含通配符*）
method	str	None	监听的HTTP方法，如 'GET', 'POST'，None表示所有方法
res_type	bool	False	是否同时监听响应数据，开启后packet.response包含响应信息
4.2 listener.wait() 参数
参数名	类型	默认值	说明
timeout	float	None	等待超时时间（秒），若为None则一直等待直到捕获到请求
4.3 listener.stop() 参数
无参数。

5. 返回结果说明
listener.wait() 返回一个 DataPacket 对象，主要包含以下属性：

属性	类型	说明
url	str	请求的完整URL
method	str	HTTP方法（GET/POST等）
request	Request对象	请求相关信息
response	Response对象	响应相关信息（仅在res_type=True时有值）
5.1 request 对象属性
属性	类型	说明
headers	dict	请求头字典
postData	str	POST请求的请求体（字符串形式）
method	str	请求方法
url	str	请求URL
5.2 response 对象属性
属性	类型	说明
headers	dict	响应头字典
body	str	响应体（字符串形式）
status	int	HTTP状态码
url	str	响应URL
6. 错误处理
所有方法在遇到错误时会抛出异常，建议使用try-except块进行捕获和处理：

python
try:
    packet = listener.wait(timeout=10)
    if packet:
        # 处理请求
        pass
except Exception as e:
    print(f"监听异常: {e}")
finally:
    listener.stop()
7. 最佳实践
合理设置超时：根据网络状况和请求频率，设置合适的 timeout 值，避免无限等待。

使用通配符监听多个接口：targets 支持 * 通配符，可灵活匹配一组URL。

及时停止监听：在脚本结束或不再需要监听时，务必调用 listener.stop() 释放资源。

保存捕获数据：可将捕获到的请求头和请求体保存到文件或数据库，便于后续分析。

结合手动操作：脚本启动浏览器后，手动登录并触发请求，可捕获需要登录态的数据。

使用无头模式：如需后台运行，可在创建 ChromiumPage 时传入配置启用无头模式。

8. 示例脚本
8.1 基础监听脚本
python
# -*- coding:utf-8 -*-
from DrissionPage import ChromiumPage

def monitor_api():
    page = ChromiumPage()
    listener = page.listen
    listener.set_targets(
        targets='https://api.example.com/v1/data',
        method='POST',
        res_type=True
    )
    listener.start()
    print("监听已启动，请在浏览器中操作...")
    
    try:
        while True:
            packet = listener.wait(timeout=10)
            if packet:
                print(f"URL: {packet.url}")
                print(f"请求头: {packet.request.headers}")
                if packet.request.postData:
                    print(f"请求体: {packet.request.postData}")
                if packet.response.body:
                    print(f"响应体: {packet.response.body[:200]}...")  # 截取前200字符
    except KeyboardInterrupt:
        print("用户停止监听")
    finally:
        listener.stop()
        # page.close()

if __name__ == "__main__":
    monitor_api()
8.2 监听多个接口并保存到文件
python
from DrissionPage import ChromiumPage
import json
import time

def monitor_multiple():
    page = ChromiumPage()
    listener = page.listen
    listener.set_targets(
        targets=[
            'https://api.example.com/v1/*',   # 监听所有v1接口
            'https://api.example.com/v2/order'
        ],
        method='POST'
    )
    listener.start()
    
    captured_data = []
    try:
        while True:
            packet = listener.wait(timeout=5)
            if packet:
                record = {
                    'url': packet.url,
                    'method': packet.method,
                    'headers': dict(packet.request.headers),
                    'postData': packet.request.postData,
                    'timestamp': time.time()
                }
                captured_data.append(record)
                print(f"已捕获 {packet.url}")
    except KeyboardInterrupt:
        # 保存到文件
        with open('captured_requests.json', 'w', encoding='utf-8') as f:
            json.dump(captured_data, f, ensure_ascii=False, indent=2)
        print(f"已保存 {len(captured_data)} 条记录到 captured_requests.json")
    finally:
        listener.stop()

if __name__ == "__main__":
    monitor_multiple()
9. 常见问题
9.1 浏览器未自动打开
问题：运行脚本后浏览器窗口没有出现。

解决方案：

检查 DrissionPage 是否正确安装：pip show DrissionPage

手动指定浏览器路径：ChromiumPage(chromium_path='C:/Program Files/Google/Chrome/Application/chrome.exe')

确认系统环境变量中能找到 Chrome/Chromium

9.2 监听不到任何请求
问题：脚本运行后一直未捕获到请求。

解决方案：

确认目标 URL 是否正确，包括协议和路径。

确认请求方法是否匹配（GET/POST）。

在浏览器开发者工具中查看实际发出的请求，对比设置的目标。

检查是否在监听启动后才触发的请求（监听启动前的请求不会被捕获）。

尝试使用通配符扩大匹配范围，例如 '*selectList*'。

9.3 打印的请求头不全或没有请求体
问题：捕获到的请求信息缺少某些头字段或 POST Data 为空。

解决方案：

某些请求头可能由浏览器自动添加，但 DrissionPage 会捕获原始请求，理论上应包含全部。

检查请求方法：GET 请求通常没有请求体。

确认请求体是否为纯文本格式（如 JSON），DrissionPage 的 postData 会以字符串形式返回。

如果使用 res_type=False，则不会捕获响应信息，但不影响请求头。

9.4 如何保持登录状态
问题：监听需要登录态的接口时，每次重启脚本都需要重新登录。

解决方案：

脚本启动浏览器后，手动登录一次，后续监听会保持该会话。

使用 DrissionPage 的 cookies 功能保存和加载 cookies，避免重复登录。

10. 更新日志
v1.0.0 (2026-03-13)
初始版本

支持监听单个或多个 URL

支持捕获请求头、请求体、响应信息

提供基础的监听循环和异常处理

11. 监听数据包结构
DataPacket 对象的结构如下：

json
{
  "url": "https://api.example.com/v1/data",
  "method": "POST",
  "request": {
    "headers": {
      "Host": "api.example.com",
      "User-Agent": "Mozilla/5.0...",
      "Content-Type": "application/json"
    },
    "postData": "{\"key\":\"value\"}",
    "method": "POST",
    "url": "https://api.example.com/v1/data"
  },
  "response": {
    "headers": {
      "Content-Type": "application/json",
      "Status": "200 OK"
    },
    "body": "{\"result\":\"success\"}",
    "status": 200,
    "url": "https://api.example.com/v1/data"
  }
}
12. API请求数据结构与捕获字段映射
12.1 监听到的请求数据结构解析
API原始字段	捕获字段	说明
URL	packet.url	请求的完整URL
请求方法	packet.method	HTTP方法（GET/POST等）
请求头	packet.request.headers	字典形式，包含所有请求头
请求体	packet.request.postData	字符串形式，仅POST请求存在
响应头	packet.response.headers	字典形式，需开启res_type=True
响应体	packet.response.body	字符串形式，需开启res_type=True
响应状态码	packet.response.status	HTTP状态码，需开启res_type=True
12.2 常见字段提取示例
python
# 提取特定请求头
auth_token = packet.request.headers.get('Authorization')

# 解析JSON格式的请求体
import json
if packet.request.postData:
    data = json.loads(packet.request.postData)
    page_num = data.get('pageNum')

# 提取响应中的信息
if packet.response.body:
    resp_data = json.loads(packet.response.body)
    total_count = resp_data.get('totalCount')
13. 联系方式
如有问题或建议，请联系开发团队。