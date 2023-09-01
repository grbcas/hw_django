from django.urls import path, include

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create_blog/', BlogCreateView.as_view(), name='create'),
    path('list_blog/', BlogListView.as_view(), name='list'),
    path('view_blog/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit_blog/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    # path("__debug__/", include("debug_toolbar.urls")),
]
