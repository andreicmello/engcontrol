from django.contrib import admin
from .models import Product, Type, Composition, CompositionItem, ReferenceEntity

admin.site.register(Product)
admin.site.register(Type)
admin.site.register(CompositionItem)
admin.site.register(Composition)
admin.site.register(ReferenceEntity)