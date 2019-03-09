from django.db import models

class Type(models.Model):
    name = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Product(models.Model):
    name = models.CharField(max_length = 500)
    unit = models.CharField(max_length = 20)
    unit_value = models.DecimalField(max_digits = 8, decimal_places=2)
    is_service = models.BooleanField(default=False)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
         
class ReferenceEntity(models.Model):
    name = models.CharField(max_length = 500)

class CompositionItem(models.Model):
    composition_id = models.CharField(max_length = 20)
    product_reference_id = models.CharField(max_length = 20)
    entity = models.ForeignKey(ReferenceEntity, on_delete = models.CASCADE)
    name = models.CharField(max_length = 500)
    unit = models.CharField(max_length = 20)
    products = models.ManyToManyField(Product)
    coeficient = models.DecimalField(max_digits = 8, decimal_places=4)
    unit_value = Product.unit_value

    def _get_total(self):
        return self.unit_value * self.coeficient

    total_value = property(_get_total)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Composition(models.Model):
    name = models.CharField(max_length = 500)
    composition = models.ManyToManyField(CompositionItem)




