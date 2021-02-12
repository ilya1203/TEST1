from django.contrib import admin
from .models import Client, Lot, ClientLK

# Register your models here.
admin.site.register(Lot)
admin.site.register(ClientLK)
admin.site.register(Client)
