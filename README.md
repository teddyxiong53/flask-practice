# flask-practice

这个仓库用来练习各种flask插件的用法。

按照学习的顺序进行编号。

## 准备

创建一个python3的venv环境并激活。

```
virtualenv flask-practice-venv
source flask-practivce-venv/bin/activate
```

所有的运行，都用Python app.py的方式来运行。

文件尽量简单。

有配置的话，都写在app.py里。

然后用下面方式来使用配置。

```
app.config.from_object(__name__)
```



基本的运行方法是：

```
cd 0x-xx #进入到对应的目录
python app.py
```



总的学习策略是：

先看github里readme的。如果没有详细说明，那再看对应的官方文档。



## 01-flask-wtf

练习flask-wtf的用法。

有2个测试：

### 1、测试基本的文本字段输入

执行下面代码，启动服务端

```
cd 01-flask-wtf
python app.py
```

浏览器打开：http://localhost:5000

### 测试文件上传

服务端仍然保持运行。

浏览器访问：http://localhost:5000/upload

## 02-flask-nav  

这个是生成bootstrap风格的导航栏的。

但是默认只有靠左对齐的风格的。

一般会把登陆注册这些放在右侧。有没有办法进行定制呢？

这里有个讨论：

https://github.com/mbr/flask-bootstrap/issues/126

这个gist是一个实现。

https://gist.github.com/thedod/eafad9458190755ce943e7aa58355934#file-readme-md

我加上测试了一下，的确是可以的。

另外一个问题，就是怎么动态添加或者去掉元素呢？

例如根据登陆状态来确定靠右的显示的是登陆还是退出。

flask-nav的确是很久没有更新了。2017年后就没有提交了。

https://pythonhosted.org/flask-nav/advanced-topics.html#dynamic-construction

其实flask-nav本身已经支持这个特性的。

所以这个文档还是需要仔细看一下。

动态的创建和去除，就很简单，就是register_element的第二个参数，传递一个函数对象过来。

任何函数里，根据判断创建不同的Navbar对象返回。

```
def top_nav():
	# 如果登陆了。返回一个不同的。
    return ExtendedNavbar(
    title=View('hanliang', 'index'),
    root_class = 'navbar navbar-inverse',
    items = (
        View('aa', 'index'),
        View('bb', 'about'),
        Subgroup(
            'Product',
            View('cc', 'products', product='cc'),
            Separator(),
            Text("hhhhhhh"),
            View('dd', 'products', product='dd')
        ),
        Link('tech support', dest='http://www.baidu.com'),
    ),
    right_items=(
            View('Signup', 'index'),
    )
)
# 下面这个top，是id。
# 在html里，会通过nav.top这样来引用到这个变量。
nav.register_element('top', top_nav)
```



## 03-flask-bootstrap-single 

这个实际是把这部分代码写了一遍。把里面的错误解决掉。

是只有一个简单文件的flask-bootstrap模板。

如果有简单的需求，可以在这个基础上改。

`https://github.com/mbr/flask-bootstrap/blob/master/sample_application/__init__.py`

## 03-flask-bootstrap-multi

这个是多文件版本的。

代码来自：`https://github.com/mbr/flask-bootstrap/blob/master/sample_app/__init__.py`

可以正常运行。

## 04-flask-admin

这个就属于比较复杂的部分了。

所以要通过多个例子来做。

### 01-basic

这个就是最基础的代码。用最少的代码跑起来。

```
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='teddy', template_mode='bootstrap3')

app.run(host='0.0.0.0', debug=True)
```

这几行就够了。

访问地址需要ip:5000/admin。

### 02-add-custom-page

增加一些自定义界面。

来自：https://github.com/flask-admin/flask-admin/blob/master/examples/simple/app.py

### 03-peewee

使用peewee来做orm。非常好用。

https://github.com/flask-admin/flask-admin/blob/master/examples/peewee/app.py

### 04-auth

https://github.com/flask-admin/flask-admin/blob/master/examples/auth/README.rst



## 05-flask-sqlalchemy

尽管我不太喜欢sqlalchemy。比较喜欢peewee。

但是sqlalchemy还是更加强大。用的人也更多。

所以我必须把sqlalchemy学习掌握。

### 01-basic

这个直接执行就好了。会生成数据库，插入一条数据。

### 02-todo

这个是用一个todo的例子来演示。

https://github.com/pallets-eco/flask-sqlalchemy/blob/main/examples/todo/app.py

看了2个例子，基本动了sqlalchemy的操作逻辑了。



## 06-flask-security

这个插件官方不再维护。我也不深入学习了。

了解一下即可。

### 01-basic

https://flask-security.readthedocs.io/en/3.0.0/quickstart.html

照着这个写了基础的。用login_required来要求登陆。

会自动跳转到登陆界面，而不需要自己写这个登陆界面。

## 07-flask-login

登陆功能就用这个就够了。

https://flask-login.readthedocs.io/en/latest/