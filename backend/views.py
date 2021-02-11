from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from time import gmtime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Client, Lot
from .serializers import *

@api_view(['GET', 'POST'])
def index(request, name):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Client.objects.all().filter(lot=name)
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        serializer = ClientSer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        retr = int(str(Lot.objects.get(pk=name).createdAt).split()[1].split(':')[0])*3600 + int(str(Lot.objects.get(pk=name).createdAt).split()[1].split(':')[1])*60+int(str(Lot.objects.get(pk=name).createdAt).split()[1].split(':')[2].split('.')[0])
        retr += int(Lot.objects.get(pk=name).hour)*3600+int(Lot.objects.get(pk=name).minut)*60+int(Lot.objects.get(pk=name).sec)
        retr += 24*3600*(int(str(Lot.objects.get(pk=name).createdAt).split()[0].split('-')[-1])-int(gmtime().tm_mday))
        retr -= int(gmtime().tm_hour)*3600+int(gmtime().tm_min)*60+int(gmtime().tm_sec)
        if retr <= 0:
            retr = 0
        print(retr)
        print(str(Lot.objects.get(pk=name).createdAt).split()[0])
        dLot = {'pk':name, 'nameOfLot': Lot.objects.get(pk=name).name,
                'hour': retr // 3600,
                'minute': retr % 3600 // 60,
                'sec': retr%60}
        print(dLot)
        return Response({'LotInfo':dLot,'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})
