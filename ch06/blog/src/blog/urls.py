from django.urls import path

from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(),
        name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    # use pk(primary key) as int for path
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]