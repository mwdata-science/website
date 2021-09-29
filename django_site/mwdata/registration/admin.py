from csvexport.actions import csvexport
from django.contrib import admin
from django.shortcuts import redirect
from django.template import loader

from . import models


class RegistrationAbstractAdmin(admin.ModelAdmin):
    list_display = [
        "get_name",
        "email",
        "registration_total_score",
        "accepted",
        "confirmed",
        "waiting_list",
        "user_canceled",
    ]

    list_filter = ("accepted", "confirmed", "waiting_list")

    list_editable = [
        "registration_total_score",
        "accepted",
        "confirmed",
        "waiting_list",
        "user_canceled",
    ]

    def get_name(self, obj):
        return obj.name

    get_name.admin_order_field = "first_name"
    get_name.short_description = "Name"


class RegistrationAdmin(RegistrationAbstractAdmin):
    list_display = RegistrationAbstractAdmin.list_display + ["scholarship_confirmed"]
    list_editable = RegistrationAbstractAdmin.list_editable + ["scholarship_confirmed"]
    list_filter = (
        "accepted",
        "confirmed",
        "waiting_list",
        "scholarship",
        "user_canceled",
        "scholarship_confirmed",
        "scholarship_transportation",
    )
    actions = ("create_massmail", csvexport)

    def create_massmail(self, request, queryset):
        template_string = loader.render_to_string(
            "registration/email/massmail.txt",
            {"recipient_name": "{{ registration.first_name }}"},
        )
        massmail = models.MassMail.objects.create(text_body=template_string)
        for registration in queryset:
            massmail.registrations_week2.add(registration)
        return redirect("admin:registration_massmail_change", object_id=massmail.id)

    create_massmail.short_description = (
        "Create a new mass email for selected recipients"
    )


class RegistrationWeek1Admin(RegistrationAbstractAdmin):
    actions = ("create_massmail",)

    def create_massmail(self, request, queryset):
        template_string = loader.render_to_string(
            "registration/email/massmail.txt",
            {"recipient_name": "{{ registration.first_name }}"},
        )
        massmail = models.MassMail.objects.create(text_body=template_string)
        for registration in queryset:
            massmail.registrations_week1.add(registration)
        return redirect(
            "admin:registration_massmail_change", kwargs={"object_id": massmail.id}
        )

    create_massmail.short_description = (
        "Create a new mass email for selected recipients"
    )


class MassMailAdmin(admin.ModelAdmin):
    list_display = ("subject", "created", "schedule_send", "sent", "sending")


admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.RegistrationWeek1, RegistrationWeek1Admin)
admin.site.register(models.MassMail, MassMailAdmin)
