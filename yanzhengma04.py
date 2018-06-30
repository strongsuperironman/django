#在templates中配置
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户登录</title>
    <script type="text/javascript" src="https://cdn.bootcss.com/jquery/1.10.2/jquery.js"></script><!--jQuery 的点击事件-->
    <script type="text/javascript">
        $(function () {
            $("img").click(function () {
                console.log("我要换验证码");
                $(this).attr("src","/app/get_verity_code/"+Math.random());{# 路径后面添加随机数可以在每次刷新后改变路径,符合浏览器的缓存机制 #}
                
            })
            
        })
    </script><!--function()表示页面主备好了,$("img").click()(添加的是点击事件的对象)添加点击,console.log在控制台上打印,$(this).attr()找到点击的图片-->
</head>
<body>
<form action="#" method="post">
    {% csrf_token %}
    <span></span><input type="text" name="username" placeholder="请输入用户名">
    <br>
    <span>验证码</span><input type="text" name="verifycode" placeholder="请输入验证码">
    <br>
    <img height="50px" src="{% url 'app:get_verity_code' %}"alt="验证码">
    <br>
    <input type="submit">
</form>>
</body>
</html>
#url:
url中配置name和namespace

