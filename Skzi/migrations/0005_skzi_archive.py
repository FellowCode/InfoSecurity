# Generated by Django 3.0.6 on 2020-06-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skzi', '0004_auto_20200529_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='skzi',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
