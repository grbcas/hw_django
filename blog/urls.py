from django.urls import path, include

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    # path('', BlogListView.as_view(), name='index'),
    # path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    # path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
