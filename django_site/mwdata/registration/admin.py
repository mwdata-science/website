from django.contrib import admin

from . import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name", "email")
