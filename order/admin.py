from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_total', 'created', 'updated', 'is_site_order', 'is_app_order')


admin.site.register(Order, OrderAdmin)

