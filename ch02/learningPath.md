# Ch2. Hello World app

## 1. Start Django Project ( Helloworld example)

```bash
# Start the project> django-admin startproject helloworld_project .
```

***settings.py*** : project’s setting.

***urls.py*** : pages to build in response to a browser/ URL request.

***wsgi.py*** : Web Server Gateway Interface.

## 2. Create apps

```bash
# Create apps
> python manage.py startapp pages
> tree
└── pages
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

***admin.py*** : configuration file for the build-in Django Admin app.

***apps.py*** : configureation filre for app itself.

***migrations/*** : relate to **models.py** so our database and **models.py** stay in sync.

***model.py*** : define database models.

***test.py*** : app-specific tests.

***views.py*** : handle request/response logic for web app.

## 3. Link/Install APP to project

Although app exits, Django doesn’t “know” about it untill we explicitly add it.

```python
# hellowrold_project/setting.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig', # new
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## 4. Views and URLConfs

In pages apps, create a [urls.py](http://urls.py) in apps

The Django request work flow will like

> URL → View → Model → Temple
>

### Add pages views and pages urls

```python
# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, My Django!")
```

```python
# pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
```

### Create "Porject-Level" urls.py

> “Project-level” means the topmost, parent directory of an application. In this case where both the helloworld_project and pages app folders exist. Once we are inside a specific app we are “app-level.
>

```python
# hellowrold_project/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'))  # new
]
```

## Recall

1. Understand relation between Django **project** and **app**
2. Project and apps communicate by **settings.py**
3. Under stand Views, Under stand "Project-level" and "App-level" urls.py
