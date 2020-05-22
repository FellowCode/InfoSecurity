from django.db import models

from utils.model_manager import MyManager


class OtdelIR(models.Model):
    objects = MyManager()

    name = models.CharField(max_length=128, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел ИР"
        verbose_name_plural = "Отделы ИР"


class Skzi(models.Model):
    objects = MyManager()

    otdel = models.ForeignKey('OtdelIR', on_delete=models.CASCADE, related_name='skzis', verbose_name='Отдел')

    name = models.ForeignKey('SkziName', on_delete=models.CASCADE)
    serial_n = models.CharField(max_length=32)
    ekz_n = models.CharField(max_length=32)

    #Отметка о получении
    from_person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='skzis_from')
    date_and_n = models.CharField(max_length=64)

    #Отметка о рас.
    to_person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='skzis_to')
    date_sopr = models.DateField()
    date_podtv = models.DateField()
    podtv = models.BooleanField()
    vozvr_date_pisma = models.DateField()
    vozvr_date_podtv = models.DateField()
    date_vvod = models.DateField()
    date_vivod = models.DateField()
    date_unichtozh = models.DateField()

    nomer_acta = models.CharField(max_length=32)
    primechanie = models.CharField(max_length=1024)

    rassilka = models.ManyToManyField('FioRassilki')



class SkziName(models.Model):
    objects = MyManager()

    type = models.CharField(max_length=128, verbose_name='Тип')
    firma = models.CharField(max_length=256, verbose_name='Фирма')
    version = models.CharField(max_length=32, verbose_name='Версия')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Наименование СКЗИ'
        verbose_name_plural = 'Наименования СКЗИ'


class OrganCrypto(models.Model):
    objects = MyManager

    company = models.CharField(max_length=256, verbose_name='Компания')
    region = models.CharField(max_length=256, verbose_name='Регион')

    fio = models.CharField(max_length=256, verbose_name='ФИО', blank=True, null=True)

    def __str__(self):
        return f'{self.company} ({self.region})'

    class Meta:
        verbose_name = 'Орган криптозащиты'
        verbose_name_plural = 'Органы криптозащиты'


class FioRassilki(models.Model):
    objects = MyManager()

    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    surname = models.CharField(max_length=128, verbose_name='Отчество')
    dolzhnost = models.CharField(max_length=128, verbose_name='Должность')

    def get_fio(self):
        return f'{self.last_name} {self.first_name[0]}.{self.surname[0]}.'

    def __str__(self):
        return self.get_fio()

    class Meta:
        verbose_name = 'ФИО Рассылки'
        verbose_name_plural = 'ФИО Рассылки'

class Ispdn(models.Model):
    objects = MyManager()

    otdel = models.ForeignKey('OtdelIR', on_delete=models.CASCADE, related_name='ispdns', verbose_name='Отдел')

    nomer = models.IntegerField()
    name = models.CharField(max_length=256)
    start_date = models.DateField()
    end_date = models.DateField()

    prikaz = models.ForeignKey('Prikaz', on_delete=models.CASCADE)
    instruct = models.ForeignKey('Instruct', on_delete=models.CASCADE)
    rukovodstvo = models.ForeignKey('Rukovodstvo', on_delete=models.CASCADE)
    polozhenie = models.ForeignKey('Polozhenie', on_delete=models.CASCADE)
    po = models.ForeignKey('ProgOb', on_delete=models.CASCADE)

class Prikaz(models.Model):
    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Приказ'
        verbose_name_plural = "Приказы"


class Instruct(models.Model):
    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = "Инструкции"


class Rukovodstvo(models.Model):
    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = "Руководства"


class Polozhenie(models.Model):
    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Положение'
        verbose_name_plural = "Положения"


class ProgOb(models.Model):
    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = "ПО"


class Pdn(models.Model):
    objects = MyManager()

    otdel = models.ForeignKey('OtdelIR', on_delete=models.CASCADE, related_name='pdns', verbose_name='Отдел')

    preson = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='pdns')
    nalichie = models.BooleanField()


class Person(models.Model):
    objects = MyManager()
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    birth_date = models.DateField()
    fakultet = models.CharField(max_length=128)
    podrazd = models.CharField(max_length=128)

    def get_fio(self):
        return f'{self.last_name} {self.first_name[0]}.{self.surname[0]}.'

    def __str__(self):
        return self.get_fio()

    class Meta:
        verbose_name = 'Сотрудник/Студент'
        verbose_name_plural = 'Сотрудники/Студенты'
