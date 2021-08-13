from django.db import models

class productinfoModel(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/')
