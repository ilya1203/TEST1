# Generated by Django 3.0.2 on 2021-02-10 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('hour', models.IntegerField(verbose_name='Часы')),
                ('minut', models.IntegerField(verbose_name='Минуты')),
                ('sec', models.IntegerField(verbose_name='Секунды')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('standp', models.CharField(max_length=50, verbose_name='StandartPlus')),
                ('term', models.IntegerField(verbose_name='Срок выполнения')),
                ('garant', models.IntegerField(verbose_name='Гарантия')),
                ('pers', models.IntegerField(verbose_name='Процент оплаты')),
                ('price', models.IntegerField(verbose_name='Цна')),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('lot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.Lot', verbose_name='Лот')),
            ],
        ),
    ]
