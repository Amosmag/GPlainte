from django.contrib import admin
from .models import Operateur, Canal, Categorie, Plainte
# Register your models here.

admin.site.register(Operateur)
admin.site.register(Canal)
admin.site.register(Categorie)
admin.site.register(Plainte)