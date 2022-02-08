# Ch 14 Permissions and Authorization

First, we will build authorization. So, the user can only edit article they create.

With Django framework, it has a built-in function for authorization that we can use. In this chapter we will limit access to various pages only to logged-in users.

## 1. New Article

Improve the CreateView, so the new article page will use the log in user as create new article.

We will set by overwrite `form_valid` method

```python
class ArticleCreateView( LoginRequiredMixin ,CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title', 'body') # edit, remove author
    login_url = 'login'

    def form_valid(self, form):  # new, overwirte the method
        form.instance.author = self.request.user
        return super().form_valid(form)
```

Try to create new article with logged-in user.

## 2. Authorization

There still problem when use new article page without user log in. As we click save bottom, there will be an error. Because our model **expects** an *author* field which we do not have.

Next will introduce Mixins to fix this problems

## 3. Mixins

*mixin*, which is a special kind of multiple inheritance that Django uses to avoid duplicate code and still allows customization.

For example, the built-in generic ListView needs a way to return a template. But so does DetailView and in fact almost every other view. Rather than repeat the same code in each big generic view.

Django breaks out this functionality into a “mixin” known as TemplateRespon

seMixin. Both ListView and DetailView use this mixin to render the proper template

link of [TempateResonsseMixin](https://docs.djangoproject.com/en/4.0/ref/class-based-views/mixins-simple/#templateresponsemixin) and [Using mixins with class-based views](https://docs.djangoproject.com/en/4.0/topics/class-based-views/mixins/)

### Login Restrict

To restrict view access to only logged in users, Django has LoginRequired mixin we can use.

Add LoginRequiredMixin to our ArticleCreateView. Make sure that the mixin is to the left of ListView so it will be read first.

```python
# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article

...
class ArticleCreateView( LoginRequiredMixin ,CreateView): # new
...
```

Then try [http://localhost](http://localhost):8000/articles/new/ which show 404. Because the default redirect use `/account/login` as route, however we are using `users/` as route. We will add redirect parameter for CreateView

```python
# articles/views.py
...
class ArticleCreateView( LoginRequiredMixin ,CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title', 'body')
    login_url = 'login'  # new : here.

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

## 3. LoginRequiredMixin

Now we see how restricting view does. We add `LoginRequiredMixin` and `login_url` to rest of Views.

Such that, all Login restrict page will redirect to login page without user log in.

## 4. UpdateView and DeleteView

In our Update and Delete page, we will restrict only author can edit and delete there own post.

The base View class use in Django has an internal `dispatch()` method. In articles/views.py file add a import `PermissionDenied`, then add `dispatch()` method for both `ArticleUpdateView` and `ArticleDeleteView`.

```python
# articles/views.py
...
from django.core.exceptions import PermissionDenied # new
...

class ArticleUpdateView( LoginRequiredMixin ,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)
```

## Conclusion

- Use LoginRequiredMixin to implement authorization
- Use LoginRequiredMixin with dispatch and PermissionDeny to restrict user with behavior
- Idea of Mixins.
