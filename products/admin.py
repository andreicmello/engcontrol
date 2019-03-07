from django.contrib import admin
from .models import Product, Type, Composition

admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Composition)