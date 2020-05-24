from django.db import models

from utils.model_manager import MyManager

from utils.shortcuts import transliterate


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

    name = models.ForeignKey('SkziName', on_delete=models.CASCADE)
    serial_n = models.CharField(max_length=32)
    ekz_n = models.CharField(max_length=32, blank=True)

    #Отметка о получении
    from_organ = models.ForeignKey('OrganCrypto', on_delete=models.CASCADE, related_name='skzis_from')
    date_poluch = models.DateField(null=True, blank=True)
    nomer_poluch = models.CharField(max_length=64)

    #Отметка о рас.
    to_person = models.ForeignKey('FioRassilki', on_delete=models.CASCADE, related_name='skzis_to')
    date_sopr = models.DateField()
    nomer_sopr = models.CharField(max_length=32, default='')
    date_podtv = models.DateField()
    nomer_podtv = models.CharField(max_length=32, default='')
    podtv = models.BooleanField(default=False)

    #Отметка о возврате
    vozvr_date_sopr = models.DateField(null=True, blank=True)
    vozvr_nomer_sopr = models.CharField(max_length=32, default='', blank=True)
    vozvr_date_podtv = models.DateField(null=True, blank=True)
    vozvr_nomer_podtv = models.CharField(max_length=32, default='', blank=True)

    date_vvod = models.DateField()
    date_vivod = models.DateField(null=True, blank=True)

    #Отметка о уничтожении
    date_unichtozh = models.DateField(null=True, blank=True)
    nomer_acta = models.CharField(max_length=32)
    act_podtv = models.BooleanField(default=False)

    primechanie = models.CharField(max_length=1024)



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

    nomer = models.IntegerField()
    name = models.CharField(max_length=256)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    prikaz = models.ManyToManyField('Prikaz', related_name='ispdns', blank=True)
    instruct = models.ManyToManyField('Instruct', related_name='ispdns', blank=True)
    rukovodstvo = models.ManyToManyField('Rukovodstvo', related_name='ispdns', blank=True)
    polozhenie = models.ManyToManyField('Polozhenie', related_name='ispdns', blank=True)
    po = models.ManyToManyField('ProgOb', related_name='ispdns', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ИСПДн'
        verbose_name_plural = 'ИСПДн'


def ispdn_filename(dir, model, filename):
    try:
        obj = model.objects.latest('id')
        return '/'.join(['ispdn', dir, f"{obj.id + 1}-{filename}"])
    except:
        return '/'.join(['ispdn', dir, f"0-{filename}"])




class Prikaz(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('prikazi', Prikaz, filename)

    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    def get_filename(self):
        return self.file.name.split('/')[-1]

    class Meta:
        verbose_name = 'Приказ'
        verbose_name_plural = "Приказы"
        ordering = ['-id']


class Instruct(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('istructs', Instruct, filename)

    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = "Инструкции"


class Rukovodstvo(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('rukovodstva', Rukovodstvo, filename)

    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = "Руководства"


class Polozhenie(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('polozhenia', Polozhenie, filename)

    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Положение'
        verbose_name_plural = "Положения"


class ProgOb(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('progob', ProgOb, filename)

    objects = MyManager()
    nomer = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = "ПО"


class Pdn(models.Model):
    objects = MyManager()

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
