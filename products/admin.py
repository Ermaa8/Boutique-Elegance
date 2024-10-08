from django.contrib import admin
from .models import Product, Category, OutfitCategory, Outfit

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class OutfitCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class OutfitAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OutfitCategory, OutfitCategoryAdmin)
admin.site.register(Outfit, OutfitAdmin)