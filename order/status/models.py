from django.db import models
from core.models import AbstractDateModel


class OrderStatus(AbstractDateModel, models.Model):

    __tablename__ = 'order_statuses'

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('-created',)
        db_table = 'order_statuses'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
