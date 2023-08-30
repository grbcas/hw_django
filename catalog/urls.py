from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import contacts, category,\
    ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='index'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path("__debug__/", include("debug_toolbar.urls")),
]
