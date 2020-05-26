from django.db import models

from utils.model_manager import MyManager


class Ispdn(models.Model):
    objects = MyManager()

    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    prikaz = models.ManyToManyField('Prikaz', related_name='ispdns', blank=True)
    instruct = models.ManyToManyField('Instruct', related_name='ispdns', blank=True)
    rukovodstvo = models.ManyToManyField('Rukovodstvo', related_name='ispdns', blank=True)
    polozhenie = models.ManyToManyField('Polozhenie', related_name='ispdns', blank=True)
    po = models.ManyToManyField('ProgOb', related_name='ispdns', blank=True)
    raznoe = models.ManyToManyField('Raznoe', related_name='ispdns', blank=True)

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
    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    ovetstv = models.ForeignKey('Pdn.Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
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
    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Pdn.Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = "Инструкции"
        ordering = ['-id']


class Rukovodstvo(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('rukovodstva', Rukovodstvo, filename)

    objects = MyManager()
    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = "Руководства"
        ordering = ['-id']


class Polozhenie(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('polozhenia', Polozhenie, filename)

    objects = MyManager()
    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    ovetstv = models.ForeignKey('Pdn.Person', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'Положение'
        verbose_name_plural = "Положения"
        ordering = ['-id']


class ProgOb(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('progob', ProgOb, filename)

    objects = MyManager()
    nomer = models.CharField(max_length=32, verbose_name='Номер')
    name = models.CharField(max_length=256, verbose_name='Название')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return f'{self.nomer} {self.name}'

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = "ПО"
        ordering = ['-id']


class Raznoe(models.Model):
    def content_file_name(instance, filename):
        return ispdn_filename('raznoe', Raznoe, filename)

    objects = MyManager()
    name = models.CharField(max_length=256, verbose_name='Название')
    file = models.FileField(null=True, upload_to=content_file_name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разное'
        verbose_name_plural = "Разное"
        ordering = ['-id']