from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name', 'slug')}
    list_display = ('name', 'slug')
    search_fields = ['name', 'slug']


admin.site.register(Category, CategoryAdmin)
