from django.shortcuts import render
from django.db.models import QuerySet
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

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

    def from_valid(self, form):
        if form.is_valid():
            _object = form.save()
            _object.slug = slugify(_object.name)
            _object.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price', 'modify_date', 'is_published', )
    success_url = reverse_lazy('catalog:index')

    def from_valid(self, form):
        if form.is_valid():
            _object = form.save()
            _object.slug = slugify(_object.name)
            _object.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def category(request):
    context = {
        'name': category.objects.get(pk=1),
        'title': 'category'
    }

    return render(request, 'catalog/category.html', context)
