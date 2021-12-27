# Ch05 MVT practice and Front-end

## Blog app

make a blog app allows users to create, edit, and delete posts. Home page will show lists of post, with link to each individual post.  Code CSS in static files.

## 1. Initial Set Up

- create Django project ‘blog_project’
- create app ‘blog’
- perform a migrate to set up the database
- update setting.py

Same steps as previewers chapter

## 2. Database Models

Learning more about [django.db.models.Models](https://docs.djangoproject.com/en/4.0/topics/db/models/).

the following code do something like

- title with limiting length to 200
- author with [ForeignKey](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/) which allows for a many-to-one relationship. [on_delete](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete) is specify option to use.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
```

Create migration record for database

```bash
> python manage.py makemigration blog
> python manage.py migrate blog
```

## 3. Admin

Same as before, create superuser with python manage.py  

- modify blog/admin.py to register Post ( class in models.py)

## 4. URLs

add urls in “app-level” and link “blog.urls” to “project level”

## 5. Views and Template

- in Views: create the old ListView and link to model Post
- in Template: same as before, create ‘base.html’ and ‘home.html’

## 6. Static files

static files contain something doesn’t change like CSS, JavaScript and images.

- link static to file path in setting.py

```python
# blog_project/setting.py
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

- create base.css in static/css/base.css

## 7. Create Individual blog pages

- In Views add class with DetailViews

```python
# blog/views.py
from django.views.generic import ListView, DetailView

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
```

- We can use [context_object_name](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#making-friendly-template-contexts) to make code better
- Create templates/post_detail.html, this part use “object” to replace “post” which remove the confusing.

```html
<!--template/post_detail.html-->
{% extends 'base.html' %}

{% block content%}
    <div class="post-entry">
        <h2>{{ object.title }}</h2>
        <p>{{ object.body }}</p>
    </div>
{% endblock content %}
```

- write path in blog/urls

```python
urlpatterns = [
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]
```

<int:pk> use int as primary key.

- Last, use {% url ‘post_detail’ post.pk%} to link our home page with individual one.

## 8. Test

Start with set up, which import get_user_model to reference active user.

Than, use Client() to set testing data.

We also need to test both “list_views” and “detail_view”

## Recall

1. Basic MVT home page build with Django admin
2. A little taste of CSS and HTML
3. Add extra class to Views, add link in templates
4. Write more detail test case
