from django.db import models

from utils.model_manager import MyManager


class Skzi(models.Model):
    objects = MyManager()

    name = models.ForeignKey('SkziName', on_delete=models.CASCADE)
    serial_n = models.CharField(max_length=32)
    ekz_n = models.CharField(max_length=32, blank=True)

    #Отметка о получении
    from_organ = models.ForeignKey('OrganCrypto', on_delete=models.CASCADE, related_name='skzis_from')
    date_poluch = models.DateField(null=True, blank=True)
    nomer_poluch = models.CharField(max_length=64, blank=True)

    #Отметка о рас.
    to_person = models.ForeignKey('FioRassilki', on_delete=models.CASCADE, related_name='skzis_to')
    date_sopr = models.DateField(null=True, blank=True)
    nomer_sopr = models.CharField(max_length=32, blank=True)
    date_podtv = models.DateField(null=True, blank=True)
    nomer_podtv = models.CharField(max_length=32, blank=True)
    podtv = models.BooleanField(default=False)

    #Отметка о возврате
    vozvr_date_sopr = models.DateField(null=True, blank=True)
    vozvr_nomer_sopr = models.CharField(max_length=32, blank=True)
    vozvr_date_podtv = models.DateField(null=True, blank=True)
    vozvr_nomer_podtv = models.CharField(max_length=32, blank=True)

    date_vvod = models.DateField(null=True, blank=True)
    date_vivod = models.DateField(null=True, blank=True)

    #Отметка о уничтожении
    date_unichtozh = models.DateField(null=True, blank=True)
    nomer_acta = models.CharField(max_length=32, blank=True)
    act_podtv = models.BooleanField(default=False)

    primechanie = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.name.type

    class Meta:
        verbose_name = 'Запись СКЗИ'
        verbose_name_plural = 'Записи СКЗИ'


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
