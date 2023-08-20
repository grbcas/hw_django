from django.urls import path, include

from catalog.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path("__debug__/", include("debug_toolbar.urls")),
]
