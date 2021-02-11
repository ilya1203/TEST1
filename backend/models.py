from django.db import models


    

class Client(models.Model):
    name  = models.CharField(max_length=50, verbose_name='Имя')
    standp  = models.CharField(max_length=50, verbose_name='StandartPlus')
    term = models.IntegerField(verbose_name='Срок выполнения')
    garant = models.IntegerField(verbose_name='Гарантия')
    pers = models.IntegerField(verbose_name='Процент оплаты')
    price = models.IntegerField(verbose_name='Цна')
    createdAt = models.DateTimeField("Created At", auto_now_add=True, db_index=True)
    lot = models.ForeignKey('Lot', null=True, on_delete=models.PROTECT, verbose_name='Лот')
    
    def __str__(self):
        return self.name

class Lot(models.Model):
    name = models.CharField(max_length=50, db_index=True,
    verbose_name = 'Название')
    hour = models.IntegerField(verbose_name='Часы')
    minut = models.IntegerField(verbose_name='Минуты')
    sec = models.IntegerField(verbose_name='Секунды')
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
   
    def __str__(self):
        return self.name

    class Meta:
            verbose_name_plural = 'Лоты'
            verbose_name = 'Лот'
            ordering = ['name']
    
