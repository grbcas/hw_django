from django.contrib import admin
from catalog.models import Contacts, Product, Category, Version
from blog.models import Blog


# Register your models here.
# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'slug')
    list_filter = ('title',)
    search_fields = ('title', 'body')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'version_sing')
    list_filter = ('version_number',)
    search_fields = ('product', 'version_number', )
