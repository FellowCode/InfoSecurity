from django.contrib import admin

from .models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Pdn)
class PdnAdmin(admin.ModelAdmin):
    pass