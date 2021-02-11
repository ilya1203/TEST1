from django.contrib import admin
from .models import Client, Lot

# Register your models here.
admin.site.register(Lot)
admin.site.register(Client)
