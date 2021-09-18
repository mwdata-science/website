# Generated by Django 3.2.2 on 2021-09-12 15:19
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0007_add_internal_notes"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="registration",
            options={
                "verbose_name": "Registration (Week 2)",
                "verbose_name_plural": "Registrations (Week 2)",
            },
        ),
        migrations.AlterModelOptions(
            name="registrationweek1",
            options={
                "verbose_name": "Registration (Week 1)",
                "verbose_name_plural": "Registrations (Week 1)",
            },
        ),
        migrations.CreateModel(
            name="MassMail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        default="Malawi Data Science Bootcamp 2021", max_length=512
                    ),
                ),
                (
                    "text_body",
                    models.TextField(
                        default="",
                        help_text="Allows to use template syntax like {{ registration.first_name }} and such.",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("modified", models.DateTimeField(auto_now_add=True)),
                (
                    "schedule_send",
                    models.DateTimeField(
                        blank=True,
                        help_text="Set a date in the future where the email should be sent",
                        null=True,
                    ),
                ),
                ("sent", models.BooleanField(default=False, editable=False)),
                ("sending", models.BooleanField(default=False, editable=False)),
                (
                    "registrations_week1",
                    models.ManyToManyField(
                        blank=True, to="registration.RegistrationWeek1"
                    ),
                ),
                (
                    "registrations_week2",
                    models.ManyToManyField(blank=True, to="registration.Registration"),
                ),
            ],
        ),
    ]