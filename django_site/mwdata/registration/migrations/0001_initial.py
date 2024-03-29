# Generated by Django 3.2.2 on 2021-05-09 23:24
import django.core.validators
import django_countries.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_bith", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("f", "Female"), ("m", "Male")], max_length=3
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone",
                    models.CharField(
                        help_text="Please remember country-code if different from +265.",
                        max_length=256,
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        choices=[
                            ("phd", "Student (PhD)"),
                            ("masters", "Student (masters)"),
                            ("undergrad", "Student (undergrad)"),
                            ("employed", "Employed"),
                            ("other", "Other (please fill in)"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "occupation_other",
                    models.CharField(
                        blank=True,
                        help_text="Occupation, if other than listed",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "speciality",
                    models.CharField(
                        choices=[
                            ("it", "Information Technology"),
                            ("cs", "Computer Science"),
                            ("statistics", "Statistics"),
                            ("mathematics", "Mathematics"),
                            ("health", "Health"),
                            ("agriculture", "Agriculture"),
                            ("other", "Other (please fill in)"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "speciality_other",
                    models.CharField(
                        blank=True,
                        help_text="Speciality, if other than listed",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "highest_qualification",
                    models.CharField(
                        choices=[
                            ("phd", "PhD"),
                            ("masters", "MSc"),
                            ("undergrad", "BSc"),
                            ("other", "Other (please fill in)"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "highest_qualification_other",
                    models.CharField(
                        blank=True,
                        help_text="Highest qualification, if other than listed",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        help_text="Country of your current residence.", max_length=2
                    ),
                ),
                (
                    "motivation",
                    models.TextField(
                        help_text="What motivates you to participate in this Bootcamp?"
                    ),
                ),
                (
                    "benefits",
                    models.TextField(
                        help_text="How do you think that your participation in this event will be beneficial for you?"
                    ),
                ),
                (
                    "scholarship",
                    models.BooleanField(
                        help_text="Please check this field if you intend to apply for a scholarship. This option will open later.",
                        verbose_name="I will apply for a scholarship",
                    ),
                ),
                (
                    "scholarship_conditioned",
                    models.BooleanField(
                        help_text="Is your participation in this event reliant on the Scholarship?",
                        verbose_name="Participation conditioned by scholarship",
                    ),
                ),
                (
                    "cv",
                    models.FileField(
                        upload_to="cv",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "doc", "docx", "odt", "txt"]
                            )
                        ],
                        verbose_name="Curriculum Vitae",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("modified", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
