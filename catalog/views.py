from django.shortcuts import render
from django.db.models import QuerySet
from catalog.models import Product, Category, Contacts
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.

COUNT_LATEST_PRODUCTS = 5


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'home'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'contacts': Contacts.objects.get(pk=1),
        'title': 'contacts'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)
