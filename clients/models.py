from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length = 200)
    cpfcnpj = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name