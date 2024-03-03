from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView
from blog import apps


app_name = apps.BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create')
]
