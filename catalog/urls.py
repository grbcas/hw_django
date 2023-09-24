from django.urls import path, include
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contacts, category,\
    ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('', cache_page(60)(ProductListView.as_view()), name='index'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='delete'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path("__debug__/", include("debug_toolbar.urls")),
]
