# Generated by Django 3.0.6 on 2020-05-23 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Security', '0002_auto_20200523_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='ispdn',
            name='instruct',
            field=models.ManyToManyField(related_name='ispdns', to='Security.Instruct'),
        ),
        migrations.AddField(
            model_name='ispdn',
            name='po',
            field=models.ManyToManyField(related_name='ispdns', to='Security.ProgOb'),
        ),
        migrations.AddField(
            model_name='ispdn',
            name='polozhenie',
            field=models.ManyToManyField(related_name='ispdns', to='Security.Polozhenie'),
        ),
        migrations.AddField(
            model_name='ispdn',
            name='prikaz',
            field=models.ManyToManyField(related_name='ispdns', to='Security.Prikaz'),
        ),
        migrations.AddField(
            model_name='ispdn',
            name='rukovodstvo',
            field=models.ManyToManyField(related_name='ispdns', to='Security.Rukovodstvo'),
        ),
    ]
