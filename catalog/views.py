from django.shortcuts import render
from django.db.models import QuerySet
from django.urls import reverse_lazy

from catalog.models import Product, Category, Contacts
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

COUNT_LATEST_PRODUCTS = 5


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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price', 'create_date', 'is_published',)
    success_url = reverse_lazy('catalog:index')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price', 'modify_date', 'is_published', )
    success_url = reverse_lazy('catalog:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def category(request):
    context = {
        'name': category.objects.get(pk=1),
        'title': 'category'
    }

    return render(request, 'catalog/category.html', context)
