# Generated by Django 3.2.2 on 2021-09-26 15:33
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0010_registration_scholarship_confirmed"),
    ]

    operations = [
        migrations.AddField(
            model_name="registrationweek1",
            name="scholarship_transportation_departure",
            field=models.CharField(
                blank=True,
                help_text="Tell us where you are traveling from. Please indicate city/district (if Lilongwe), country",
                max_length=1024,
                null=True,
                verbose_name="Departure place",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="scholarship_confirmed",
            field=models.BooleanField(
                default=False,
                help_text="Scholarship is confirmed",
                verbose_name="Scholarship confirmed",
            ),
        ),
    ]
