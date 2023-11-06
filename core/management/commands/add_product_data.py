import csv
import random
import time

from django.core.management.base import BaseCommand

from product.category.models import ProductCategory
from helpers.utils import slugify
from product.models import Product


class Command(BaseCommand):
    help = 'Adds product data from electronic products dataset'

    def handle(self, *args, **options):
        with open('electronic_products_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                price = row[1]
                brand = row[12]
                image_urls = row[17]
                name = row[21]
                category = row[22]
                stock = random.randint(5, 50)
                product = Product(name=name, slug='{}-{}'.format(slugify(name), time.time()))
                product.price = price
                product.brand = brand
                product.image_urls = image_urls
                category = ProductCategory(name=category, slug='{}-{}'.format(slugify(name), time.time()))
                category.save()
                product.category_id = category.id
                product.stock = stock
                product.available = True
                product.save()
        self.stdout.write(self.style.SUCCESS('Successfully finished adding data'))
