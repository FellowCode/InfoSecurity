# Generated by Django 3.0.6 on 2020-05-25 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Отчество')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('dolzhnost', models.CharField(default='', max_length=64, verbose_name='Должность')),
                ('gr_key', models.CharField(blank=True, default=None, max_length=16, null=True, verbose_name='Графический ключ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
    ]
