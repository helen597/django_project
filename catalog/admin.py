from django.contrib import admin
from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name', 'description', )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'is_active', 'product',)
    list_filter = ('name', 'is_active', )
    search_fields = ('name', 'is_active', )
