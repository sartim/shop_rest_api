from django.contrib import admin
from order.item.models import OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')


admin.site.register(OrderItem, OrderItemAdmin)
