from django.db import models

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(verbose_name="Name:",max_length=60)
    weight = models.FloatField(verbose_name="Weight With Kg:")
    price = models.FloatField(verbose_name="Price:")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name