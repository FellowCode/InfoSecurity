# Generated by Django 3.0.6 on 2020-05-26 00:09

import Ispdn.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ispdn', '0003_auto_20200525_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raznoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('file', models.FileField(null=True, upload_to=Ispdn.models.Raznoe.content_file_name)),
            ],
            options={
                'verbose_name': 'Разное',
                'verbose_name_plural': 'Разное',
            },
        ),
        migrations.AlterField(
            model_name='instruct',
            name='nomer',
            field=models.CharField(max_length=32, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='polozhenie',
            name='nomer',
            field=models.CharField(max_length=32, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='prikaz',
            name='nomer',
            field=models.CharField(max_length=32, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='progob',
            name='nomer',
            field=models.CharField(max_length=32, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='rukovodstvo',
            name='nomer',
            field=models.CharField(max_length=32, verbose_name='Номер'),
        ),
    ]
