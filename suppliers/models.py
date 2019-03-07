from django.db import models

class Type(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length = 200)
    cpfcnpj = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

