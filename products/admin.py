from django.contrib import admin
from .models import Product, Category, Product, Outfit, OutfitProduct, OutfitCategory

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

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Outfit)
admin.site.register(OutfitProduct)
admin.site.register(OutfitCategory)