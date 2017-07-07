在指定文件下，创建虚拟环境，
$ virtualenv venv
在此文件夹下生成与虚拟环境相关子文件夹venv
虚拟环境激活 , win7下:
$venv\Scripts\activate

1. Flask 类的对象
客户端---->WSGI---->Flask对象
2. request对象
封装客户端发送的HTTP请求
避免将request对象作为视图函数作为参数，使用context临时将其变为全局可访问
改对象只对当前线程全局可访问有效
3. Flask两种context； application context and request context
application context global variables有current_app and g
4. Requests Hook
函数在请求被分发到视图函数之前或后调用.
用修饰器实现.
4种钩子:
before_first_request  注册一个函数，在处理第一个请求之前运行.
before_request 注册一个函数，在每次请求之前运行.
after_request 注册一个函数，如果没有未处理的异常抛出，每次请求之后运行.
teardown_request  注册一个函数，即使有未处理的异常抛出，每次请求之后运行.

在HOOK函数和视图函数之间，共享数据，使用application context global variable g.
g 处理请求时用作临时存储的对象。每次请求都会重设这个变量.

5.响应
Flask会将视图函数返回值作为响应内容
返回一个字符串
返回一个元组，一般不这么做
返回Response对象，使用make_response()
返回特殊的响应类型--重定向（告诉浏览器一个新地址），
		重定向常用302状态码，使用函数redirect(url)
返回特殊的响应类型--abort函数生成，用于处理错误。
		发生异常，abort将控制权交给服务器。

6. 模板渲染
使用函数render_template()--第一个参数模板文件名，后面参数为关键字参数
7. Jinja2变量
{{name}}表示变量，Jinja2识别所有类型的变量
8. 过滤器修饰Jinja2变量
{{name|过滤器}}
过滤器:
	safe	渲染值时不转义
	完整的过滤器列表  http://jinja.pocoo.org/docs/templates/#builtin-filters
9. 控制结构，Jinja2渲染流程
条件:
{% if user %}
	Hello, {{ user }}!
{% else %}
	Hello, Stranger!
{% endif %}

for:
<ul>
	{% for comment in comments %}
		<li>{{ comment }}</li>
	{% endfor %}
</ul>

Jinja2 还支持宏:
宏类似于 Python 代码中的函数
{% macro render_comment(comment) %}
	<li>{{ comment }}<li>
{% endmacro %}

<ul>
	{% for comment in comments %}
		{{render_comment(comment)}}
	{% endfor%}
</ul>

单独文件中保存宏，使用时，import
{% import 'macros.html' as macros %}
<ul>
	{% for comment in comments %}
		{{macros.render_comment(comment)}}
	{% endfor %}
</ul>

10. 包含模板代码片段:
{% include 'common.html' %}
11. 模板继承
12. Flask Bootstrap
使用pip安装：pip install flask-bootstrap
初始化Flask-Bootstrap
	from flask.ext.bootstrap import Bootstrap
	bootstrap=Bootstrap(app)

13. 
