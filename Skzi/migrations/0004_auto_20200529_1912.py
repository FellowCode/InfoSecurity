# Generated by Django 3.0.6 on 2020-05-29 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skzi', '0003_auto_20200525_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skzi',
            name='nomer_acta',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='skzi',
            name='primechanie',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='skzi',
            name='vozvr_nomer_podtv',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='skzi',
            name='vozvr_nomer_sopr',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
