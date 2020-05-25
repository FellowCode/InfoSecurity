from django.contrib import admin

from .models import *




@admin.register(SkziName)
class SkziNameAdmin(admin.ModelAdmin):
    pass


@admin.register(FioRassilki)
class FioRassilkiAdmin(admin.ModelAdmin):
    pass





@admin.register(OrganCrypto)
class OrganCrypto(admin.ModelAdmin):
    list_display = ['company', 'region']


@admin.register(Skzi)
class Skzi(admin.ModelAdmin):
    pass



