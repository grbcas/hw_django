from django.contrib import admin
from catalog.models import Student, Product, Category


# Register your models here.
# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')
