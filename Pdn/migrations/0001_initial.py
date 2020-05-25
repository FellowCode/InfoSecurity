# Generated by Django 3.0.6 on 2020-05-25 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
                ('fakultet', models.CharField(max_length=128)),
                ('podrazd', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Сотрудник/Студент',
                'verbose_name_plural': 'Сотрудники/Студенты',
            },
        ),
        migrations.CreateModel(
            name='Pdn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nalichie', models.BooleanField()),
                ('preson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdns', to='Pdn.Person')),
            ],
        ),
    ]
