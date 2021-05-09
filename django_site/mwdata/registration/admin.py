from django.contrib import admin

from . import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
