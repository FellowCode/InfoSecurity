# Generated by Django 3.0.6 on 2020-05-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pdn', '0007_delete_pdn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Podrazdelenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='fakultet',
        ),
        migrations.RemoveField(
            model_name='person',
            name='podrazd',
        ),
    ]
