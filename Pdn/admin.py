from django.contrib import admin

from .models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    pass


@admin.register(Podrazdelenie)
class PodrazdelenieAdmin(admin.ModelAdmin):
    pass