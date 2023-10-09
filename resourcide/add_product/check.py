# from django.db import models
from models import Product

all = Product.object.all()

for product in all:
    print(product.name, product.description)