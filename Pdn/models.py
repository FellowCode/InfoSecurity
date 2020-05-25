from django.db import models

from utils.model_manager import MyManager


class Pdn(models.Model):
    objects = MyManager()

    preson = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='pdns')
    nalichie = models.BooleanField()

    class Meta:
        verbose_name = 'ПДн'
        verbose_name_plural = 'ПДн'

class Person(models.Model):
    objects = MyManager()
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    surname = models.CharField(max_length=128, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    fakultet = models.CharField(max_length=128, null=True, blank=True, verbose_name='Факультет')
    podrazd = models.CharField(max_length=128, null=True, blank=True, verbose_name='Подразделение')

    def get_fio(self):
        return f'{self.last_name} {self.first_name[0]}.{self.surname[0]}.'

    def __str__(self):
        return self.get_fio()

    class Meta:
        verbose_name = 'Сотрудник/Студент'
        verbose_name_plural = 'Сотрудники/Студенты'