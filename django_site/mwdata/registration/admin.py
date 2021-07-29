from django.contrib import admin

from . import models


class RegistrationAbstractAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "email",
        "registration_total_score",
        "accepted",
        "confirmed",
        "waiting_list",
    )

    list_filter = ("accepted", "confirmed", "waiting_list")

    list_editable = (
        "registration_total_score",
        "accepted",
        "confirmed",
        "waiting_list",
    )

    def get_name(self, obj):
        return obj.name

    get_name.admin_order_field = "first_name"
    get_name.short_description = "Name"


class RegistrationAdmin(RegistrationAbstractAdmin):
    list_filter = ("accepted", "confirmed", "waiting_list", "scholarship")


class RegistrationWeek1Admin(RegistrationAbstractAdmin):
    pass


admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.RegistrationWeek1, RegistrationWeek1Admin)
