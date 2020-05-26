from django.db import models

from utils.model_manager import MyManager


class Zametka(models.Model):
    objects = MyManager()

    name = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-id']
