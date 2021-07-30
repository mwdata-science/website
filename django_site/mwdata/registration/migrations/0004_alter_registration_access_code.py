# Generated by Django 3.2.2 on 2021-07-29 13:43
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0003_access_codes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="access_code",
            field=models.CharField(
                blank=True,
                editable=False,
                help_text="A short random code used to process an application in the URL.",
                max_length=16,
                null=True,
                unique=True,
            ),
        ),
    ]