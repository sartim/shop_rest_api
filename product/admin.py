from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name', 'slug')}
    list_display = ('category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created',
                    'updated')
    search_fields = ['name', 'slug']


admin.site.register(Product, ProductAdmin)
