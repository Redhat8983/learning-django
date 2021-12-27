from django.urls import path

from .views import BlogDetailView, BlogListView

urlpatterns = [
    # use pk(primary key) as int for path
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]