from django.contrib import admin

from . import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
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
