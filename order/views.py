from rest_framework import viewsets, permissions
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from api.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Order.objects.all()
        return queryset


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = OrderItem.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrdersTodayViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        today = timezone.datetime.today()  # Get current day

        queryset = Order.objects.filter(
            created__year=today.year,
            created__month=today.month,
            created__day=today.day)
        return queryset


class OrdersThisMonthViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        today = timezone.datetime.today()  # Get current day

        queryset = Order.objects.filter(
            created__year=today.year,
            created__month=today.month)
        return queryset


@api_view(['GET'])
def orders_last_month(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        sql = """
                SELECT COUNT(id)
                FROM api_order
                WHERE created >= date_trunc('month', current_date - interval '1' month)
                AND created < date_trunc('month', current_date)
              """
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        keys = ('count',)

        for row in rows:
            result.append(dict(zip(keys, row)))

        return Response(result)


@api_view(['GET'])
def orders_plot(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        orders_sql = """
                        SELECT
                        MAX(id) as id,
                        COUNT(id) AS value,
                        to_char(created, 'yyyy-mm-dd') AS date
                        FROM api_order
                        GROUP BY date ORDER BY date ASC
                     """

        cursor.execute(orders_sql)
        rows = cursor.fetchall()
        result = []
        keys = ('id', 'value', 'date')
        if rows:
            for row in rows:
                result.append(dict(zip(keys, row)))
            return Response(result)
        else:
            return Response([{"detail": "No results"}])
