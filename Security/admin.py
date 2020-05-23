from django.contrib import admin

from .models import *




@admin.register(SkziName)
class SkziNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(FioRassilki)
class FioRassilkiAdmin(admin.ModelAdmin):
    pass


@admin.register(Prikaz)
class PrikazAdmin(admin.ModelAdmin):
    list_display = ['nomer', 'name', 'date']


@admin.register(Instruct)
class InstructAdmin(admin.ModelAdmin):
    list_display = ['nomer', 'name']


@admin.register(Rukovodstvo)
class RukovodstvoAdmin(admin.ModelAdmin):
    list_display = ['nomer', 'name']


@admin.register(Polozhenie)
class PolozhenieAdmin(admin.ModelAdmin):
    list_display = ['nomer', 'name']


@admin.register(ProgOb)
class ProgObAdmin(admin.ModelAdmin):
    list_display = ['nomer', 'name']


@admin.register(OrganCrypto)
class OrganCrypto(admin.ModelAdmin):
    list_display = ['company', 'region']


@admin.register(Skzi)
class Skzi(admin.ModelAdmin):
    pass


@admin.register(Ispdn)
class IspdnAdmin(admin.ModelAdmin):
    pass
