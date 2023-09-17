from django.forms import inlineformset_factory
from django.shortcuts import render
from django.db.models import QuerySet
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Contacts, Version
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

COUNT_LATEST_PRODUCTS = 5


def contacts(request):
    context = {
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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.slug = slugify(new_entry.name)
            new_entry.save()
            return super().form_valid(form)

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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_entry = form.save(commit=False)
    #         new_entry.slug = slugify(new_entry.name)
    #         new_entry.save()
    #         return super().form_valid(form)
    #
    #     return super().form_valid(form)

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


def category(request):
    context = {
        # 'name': category.objects.get(object.pk),
        'title': 'category'
    }

    return render(request, 'catalog/category.html', context)
