from django.db import models

class Type(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    unit = models.CharField(max_length = 20)
    unit_value = models.DecimalField(max_digits = 8, decimal_places=2)
    is_service = models.BooleanField(default=False)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
         
class Composition(models.Model):
    name = models.CharField(max_length = 200)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


