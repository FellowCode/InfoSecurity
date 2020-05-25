from django.contrib import admin

from .models import *

@admin.register(Ispdn)
class IspdnAdmin(admin.ModelAdmin):
    fields = ['nomer', 'name']

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


@admin.register(Raznoe)
class RaznoeAdmin(admin.ModelAdmin):
    pass