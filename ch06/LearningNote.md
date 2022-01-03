# Ch 06 Form

## Forms

In Django “[Django’s build-in Form](https://docs.djangoproject.com/en/4.0/topics/forms/)” which handle a lot. Like accepting user input there are security concerns, proper error handling and UI considerations and situations.

## 1. Add New Post Form

### 1.1 Edit the Templates (T)

First Form we implement is “New Post” Form, start with add URL in base template which like code bellow

```html
<!-- base.html-->
...
<header>
  <div class="nav-left">
    <h1><a href="{% url 'home' %}">Django blog</a></h1>
  </div>
  <div class="nav-right">
    <a href="{% url 'post_new' %}">+ New Blog Post</a>
  </div>
</header>
...
```

### 1.2 Update urls in app (url)

Direct post/new/ and link to post_new

```python
# blog/urls.py
from .views import ( 
    BlogDetailView,
    BlogListView,
    BlogCreateView # new

)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),  # new
]
```

### 1.3 Edit [Add Class] in Views (V)

Add CreateView Class in views

```python
# blog/views.py
from django.views.generic.edit import CreateView # new
...
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'
...
```

In our case ‘__all__’ will only show 2 fields ‘title’ and ‘author’.

### 1.4 Create add post template (T)

```html
<!-- post_new.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>New post</h1>
    <form action="" method="post">{% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Save" />
    </form>

{% endblock content %}
```

- Use HTML **form** tags with POST method to SENDING data. If receiving data from a form use GET.
- Add {% csrf_token %} which provide protect form from cross-site scripting attacks. **Which should use it for all your Django forms**.
- To output our form data, use {{ form.as_p }} which renders to {p} tags
- Use {input} tags with “submit” and “Save”

### Extra: Direct page after form submit (M)

Django suggestion use “get_absolute_url” to our model.

In short, we should add a “get_absolute_url” and “__str__()” method.

```python
# blog/models.py
from django.urls import reverse

class Post(models.Model):
    ...
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id]
```

with code

```python
path('post/<int:pk>/', BlogDetailViews.as_view(), name='post_detail'),
```

In order for route to work, we must pass an argument with pk of object. In this case, we use id as pk as an argument.

## 2. Add Update Form

Follow the same steps.

### 2.1 Add “post_edit.html” temlate (T)

```html
<!-- post_edit.html -->
...
{% block content %}
    <h1>Edit post</h1>
    <form action="" method="post">{% csrf_token%}
        {{form.as_p}}
        <input type="submit" value="Update" />
    </form>
{% endblock content %}
...
```

### 2.2 Edit “post_detail.html” to include link to “post_edit.html” (T)

```html
<!-- post_detail.html-->
<p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
```

### 2.3 Add Update class in [views.py](http://views.py) (V)

```python
# blog/views.py
from django.views.generic.edit import UpdateView # Add import

class BlogUpdaeView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title','body']
```

base on our logic, change post will not change author. so, only set fields wit ‘title’ and ‘body’

### 2.4 Update url (url)

```python
# blog/urls.py

urlpatterns = [
...
    path('post/<int:pk/edit', BlogUpdateView.as_view(), name='post_edit')
...
]
```

## 3. Delete View

### 3.1 link “post_delete” to “post_delete” (T)

### 3.2 Create “post_delete.html” (T)

```html
<!-- template/post_delete -->
{% block content %}
    <h1>Delete post</h1>
    <form action="" method="post">{% csrf_token %}
        <p>Are you sure you want Delete "{{ post.title }}"?</p>
        <input type="submit" value="Confirm" />
    </form>
{% endblock content %}
```

use “{{ post.title }}” to display the title of blog post

### 3.3 Add Delete class (V)

```python
...
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
...
```

use reverse_lazy to direct to home after post deleted.

### 3.4 Updae urls (urls)

The final urls look like something bellow

```python
# blog/urls.py
from django.urls import path

from .views import ( 
    BlogDetailView,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', 
        BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',
        BlogDeleteView.as_view(), name='post_delete'),
]
```

## Tests

We will test four new methods

- def test_get_absolute_url
- def test_post_create_view
- def test_post_update_view
- def test_post_delete_view

Check blog/tests for detail

## Recall

We set a CRUD solution for our blogs.

We can use multiple ways to achieve same thin.
