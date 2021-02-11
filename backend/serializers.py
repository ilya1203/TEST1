from rest_framework import serializers
from .models import Client, Lot

class LotSer(serializers.ModelSerializer):

    class Meta:
        model = Lot
        fields = ('pk','name', 'hour', 'minut', 'sec')


class ClientSer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('pk','name', 'standp','garant', 'term', 'pers','price')
