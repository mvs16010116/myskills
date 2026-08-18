---
title: iframe跨域单点登录
doc_id: 1224
url: https://help.fanruan.com/finebi6.X/doc-view-1224.html
source: FineBI 帮助文档
crawled_at: 2026-07-02 15:11:27
---

> 1.&nbsp;概述1.1&nbsp;问题描述企业往往会有多个 BI 平台或多个相关的平台，用户希望只登录一次就可以访问其他的系统，例如登录 OA 系统的同时登录 BI 系统，即将输入的用户名密码也发送

![](./view/2022finebi6/images/info_fill.png) 您正在浏览的是 FineBI6.X 帮助文档，点击跳转至： [FineBI7.X帮助文档](<https://help.fanruan.com/finebi/>)
# iframe跨域单点登录
对此内容反馈
* _
__
  * 使用此篇文档遇到问题，可寻求帆软技术支持协助定位原因，若为帆软产品本身缺陷则对应给出解决方案。  
详情：[《帆软技术支持基础服务范围》](<https://bbs.fanruan.com/thread-135893-1-1.html>)


产品级协助_
* * 文档创建者： _[Wendy123456](<user-space-240644.html>)_
* 历史版本：[7](<edition-list-1224.html>)
* 最近更新：[Carly](<user-space-222366.html>) 于 2022-11-27 
[](<javascript:;>) [](<javascript:>)
## 1\. 概述
### 1.1 问题描述
企业往往会有多个 BI 平台或多个相关的平台，用户希望只登录一次就可以访问其他的系统，例如登录 OA 系统的同时登录 BI 系统，即将输入的用户名密码也发送到 BI 系统中进行认证，从而访问 BI 系统时不需要再次登录。
在上一节介绍了 [Ajax 跨域异步单点登录](<https://help.fanruan.com/finebi6.0/doc-view-1070.html>) ，那么如何通过 iframe 方式实现 OA 系统和 BI 系统的跨域单点登录呢？  

### 1.2 解决思路
在 OA 系统登录界面中，BI 先把权限验证地址以 iframe 的方式嵌入，解决跨域问题，然后再在 iframe 中触发表单登录事件，实现登录页面的跳转。
## 2\. 示例
启动两个工程，端口号分别为 37799 和 8080，将新建 HTML 文件 iframe.html 放到端口号为 37799 的工程下，访问http://localhost:37799/webroot/iframe.html，输入 8080 工程的用户名和密码，成功访问 8080 工程。
在登录成功的浏览器上新开标签页，访问http://localhost:37799/webroot/decision/logout/cross/domain，切换到之前登录成功的 8080 工程页面，刷新该页面，用户被踢出登录。
### 2.1 环境准备
1）本文示例准备的两个工程分别为：  

注：这两个工程需要有相同的用户名和密码。
  * 本地工程，端口号为 37799
  * 部署到 Tomcat 上的工程，端口号为 8080


Tomcat 服务器部署请参见：[Tomcat服务器部署](<https://help.fanruan.com/finebi6.0/doc-view-45.html>)   

2）启动两个工程。
### 2.2 新建登录页面
新建 HTML 文件，命名为「iframe.html」，代码如下所示：
注：根据实际情况修改代码中的访问路径或端口号。
[code]
    <!DOCTYPE html>  
    <html>  
      <head>   
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  
      <meta http-equiv="X-UA-Compatible" content="IE=10" />  
      <script type="text/javascript">  
        function doSubmit() {        
            var username = document.getElementById("username").value; //获取输入的用户名  
            var password = document.getElementById("password").value;  //获取输入的参数  
            var scr = document.createElement("iframe");      //创建iframe      
            scr.src = "http://localhost:8080/webroot/decision/login/cross/domain?fine_username=" + encodeURIComponent(username) + "&fine_password=" + encodeURIComponent(password) + "&validity=" + -1 + "&callback=callback";   //将报表验证用户名密码的地址指向此iframe  
            if (scr.attachEvent)  
          {       //判断是否为ie浏览器    
                   scr.attachEvent("onload", function(){                    //如果为ie浏览器则页面加载完成后立即执行    
                       window.location="http://localhost:8080/webroot/decision"; //直接跳转到数据决策系统  
                   });    
                } else {    
                   scr.onload = function(){              //其他浏览器则重新加载onload事件    
                       /*跳转到指定登录成功页面,index.jsp    
                        var f = document.getElementById("login");    
                        f.submit();  */  
                    window.location="http://localhost:8080/webroot/decision"; //直接跳转到数据决策系统  
                };    
             }    
             
         document.getElementsByTagName("head")[0].appendChild(scr);   //将iframe标签嵌入到head中      
        }     
     </script>        
    </head>        
    <body>        
      <p>请登录</p>        
      <form id="login" name="login" method="POST"  action="" >  
        <p>用户名:<input id="username" type="text" name="username" /></p>        
        <p>密 码:<input id="password" type="password" name="password"/></p>          
        <input type="button" value="登录" onClick="doSubmit()" />        
      </form>        
     </body>        
    </html>  
    
[/code]
代码说明：  

用户输入用户名密码后点击提交或登录按钮时，执行函数 doSubmit() ，该函数先创建一个 iframe，然后将 BI 验证用户名密码的认证地址指向此 iframe 的 src，并对使用的浏览器进行判断（因为每个浏览器注册写法不太一样），然后将此 iframe 标签加入到 head 标签中。
注：用户名密码表单中使用 button 来触发 doSubmit()，您只要将 doSubmit() 加入到您的 OA 的登录页面中即可，为了简化操作，完整代码中没有跳转到指定页面，直接跳转到平台页面。
### 2.3 将 HTML 文件放到指定位置
将 HTML 文件命名为iframe.html，放到端口号为 37799 工程的%BI_HOME%/webapps/webroot文件夹下，如下图所示：
![3.png](/core/style/lod.png)
### 2.4 效果查看
1）访问http://localhost:37799/webroot/iframe.html，输入 8080 工程的账号和密码，成功访问 8080 工程。如下图所示：
注：若出现无法访问的情况，请在两个工程中尝试关闭 [安全防护](<https://help.fanruan.com/finebi6.0/doc-view-781.html#11>) 中的「点击劫持攻击防护」按钮和「内容嗅探攻击防护」按钮。
![6.gif](/core/style/lod.png)
2）在登录成功的浏览器上新开标签页，访问http://localhost:37799/webroot/decision/logout/cross/domain，切换到之前登录成功的 8080 工程页面，刷新该页面，用户被踢出登录。如下图所示：
![9.gif](/core/style/lod.png)
  

### 附件列表 
  
下载次数：：0
    
**主题：** [部署集成](<category-view-101>)
[![](/core/style/back.png)上一篇：Ajax 跨域异步单点登录](<index.php?doc-view-1070.html>)
[下一篇：后台单点登录插件 ![](/core/style/forward.png) ](<index.php?doc-view-1625.html>)
  * 有帮助
  * 没帮助
  * 只是浏览


[中文（繁體）](<https://help.fanruan.com/finebi-tw/>) [English](<https://help.fanruan.com/finebi-en/>) [日本語](<https://help.fanruan.com/finebi-jp/>)
中文（简体）


__
[](<javascript:void\(0\)>)
提交页面反馈
仅适用于当前网页的意见收集，帆软产品问题请在 [问答板块提问](<https://bbs.fanruan.com/wenda>) 或 [前往服务平台](<https://service.fanruan.com/>) 获取技术支持 
