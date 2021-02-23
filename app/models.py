from django.db import models

# Create your models here.
class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
