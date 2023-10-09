from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    images = models.ManyToManyField('ProductImage')
    
class ProductImage(models.Model):
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
