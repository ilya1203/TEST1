from django.db import models


    

class Client(models.Model):
    cli = models.ForeignKey('ClientLk', null=True, on_delete=models.PROTECT, verbose_name='Клиент')
    
    standp  = models.CharField(max_length=50, verbose_name='StandartPlus')
    term = models.IntegerField(verbose_name='Срок выполнения')
    garant = models.IntegerField(verbose_name='Гарантия')
    pers = models.IntegerField(verbose_name='Процент оплаты')
    price = models.IntegerField(verbose_name='Цена')
    createdAt = models.DateTimeField("Добавлен в", auto_now_add=True, db_index=True)
    lot = models.ForeignKey('Lot', null=True, on_delete=models.PROTECT, verbose_name='Лот')
    
    def __str__(self):
        try:
            return self.cli.name
        except:
            pass
    class Meta:
            verbose_name_plural = 'Участие в лоте'
            verbose_name = 'Участие в лоте'
            

class ClientLK(models.Model):
    login = models.CharField(max_length=50, verbose_name='Login')
    password = models.CharField(max_length=50, verbose_name='Password')
    name = models.CharField(max_length=50, verbose_name='Имя')
    works = models.CharField(max_length=255, verbose_name='Область деятельности')
    ava = models.CharField(max_length=255, verbose_name='Src Аватарка')

    def __str__(self):
        return self.name
    class Meta:
            verbose_name_plural = 'Пользователи'
            verbose_name = 'Пользователь'
            ordering = ['name']

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
    
