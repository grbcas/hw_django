from django.urls import path, include

from catalog.apps import CatalogConfig
from catalog.views import index, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path("__debug__/", include("debug_toolbar.urls")),
]
