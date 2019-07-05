# 编写第一个django应用程序，第1部分

## 查看版本： 

```
$ python -m django --version
```

## 我可以在django中使用什么python版本？

| Django版本 | Python版本                                 |
| ---------- | ------------------------------------------ |
| 1.11       | 2.7、3.4、3.5、3.6、3.7（在1.11.17中增加） |
| 2.0        | 3.4、3.5、3.6、3.7                         |
| 2.1，2.2   | 3.5、3.6、3.7                              |

## 创建项目

建立Django [project](https://www.osgeo.cn/django/glossary.html#term-project) --Django实例的设置集合

```
$ django-admin startproject mysite
```

让我们看看 [`startproject`](https://www.osgeo.cn/django/ref/django-admin.html#django-admin-startproject) 创建：

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

- 外部 `mysite/` 根目录只是项目的容器。它的名字对Django来说无关紧要；你可以把它改名为任何你喜欢的名字。
- `manage.py` ：一个命令行实用程序，允许您以各种方式与Django项目进行交互。你可以阅读有关 `manage.py` 在里面 [django-admin and manage.py](https://www.osgeo.cn/django/ref/django-admin.html) .
- 内部 `mysite/` 目录是项目的实际python包。它的名称是python包的名称，您需要使用它来导入其中的任何内容（例如 `mysite.urls` ）
- `mysite/__init__.py` ：一个空文件，告诉python应该将此目录视为python包。如果你是一个 Python 初学者，请阅读 [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) 在官方的python文档中。
- `mysite/settings.py` ：此Django项目的设置/配置。 [Django设置](https://www.osgeo.cn/django/topics/settings.html) 将告诉您有关设置如何工作的所有信息。
- `mysite/urls.py` ：此django项目的URL声明；django支持的站点的“目录”。您可以在中阅读有关URL的更多信息 [URL调度器](https://www.osgeo.cn/django/topics/http/urls.html) .
- `mysite/wsgi.py` ：与wsgi兼容的Web服务器为您的项目提供服务的入口点。见 [如何使用wsgi部署](https://www.osgeo.cn/django/howto/deployment/wsgi/index.html) 了解更多详细信息。



## django-admin and manage.py

## 使用

```
$ django-admin <command> [options]
$ manage.py <command> [options]
$ python -m django <command> [options]
```

获取运行时帮助

运行 django-admin help 显示使用信息和每个应用程序提供的命令列表。

运行 django-admin help --commands 显示所有可用命令的列表。

运行 django-admin help <command> 显示给定命令的描述及其可用选项列表。





## 开发服务器

让我们验证一下您的Django项目的工作

```
$ python manage.py runserver
```
- 更改端口

  默认情况下， [`runserver`](https://www.osgeo.cn/django/ref/django-admin.html#django-admin-runserver) 命令在端口8000的内部IP上启动开发服务器。

  ```
  $ python manage.py runserver 8080  # 此命令在端口8080上启动服务器：
  $ python manage.py runserver 0:8000 # 更改为本地IP
  
  ```

## 创建投票应用程序

```
$ python manage.py startapp polls
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## 写下你的第一个视图

创建视图函数

polls/views.py

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

将视图函数映射到一个URL，新建urls.py

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

polls/urls.py

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

将根urlconf指向 `polls.urls` 模块

mysite/urls.py

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```



## django.urls 用于urlconfs的函数

**path()**
path(route, view, kwargs=None, name=None)

```
from django.urls import include, path

urlpatterns = [
    path('index/', views.index, name='main-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('articles/<slug:title>/', views.article, name='article-detail'),
    path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    path('weblog/', include('blog.urls')),
    ...
]
```

这个 path() 函数传递四个参数，需要两个参数： route 和 view 和两个可选： kwargs 和 name . 

path() argument: route
route 是包含URL模式的字符串。处理请求时，django从中的第一个模式开始 urlpatterns 并沿着列表向下移动，将请求的URL与每个模式进行比较，直到找到匹配的URL。模式不搜索get和post参数，也不搜索域名。例如，在请求中 https://www.example.com/myapp/ ，URLCONF将查找 myapp/ . 在请求中 https://www.example.com/myapp/?page=3 ，urlconf也将查找 myapp/ .

path() argument: view
这个 view 参数是视图函数或 as_view() 用于基于类的视图。它也可以是 django.urls.include() 。当Django找到匹配的模式时，它使用 HttpRequest 对象作为第一个参数，并将路由中的任何“捕获”值作为关键字参数。

path() argument: kwargs
可以在字典中将任意关键字参数传递给目标视图。

path() argument: name
命名URL可以让您明确地从Django的其他地方引用它，特别是在模板中。这个强大的功能允许您在只访问单个文件的同时对项目的URL模式进行全局更改。