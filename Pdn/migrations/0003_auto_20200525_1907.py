# Generated by Django 3.0.6 on 2020-05-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdn', '0002_auto_20200525_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='fakultet',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='podrazd',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=128, verbose_name='Отчество'),
        ),
    ]
