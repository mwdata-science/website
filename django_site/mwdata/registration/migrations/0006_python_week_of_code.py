# Generated by Django 3.2.2 on 2021-07-29 21:23
import django.core.validators
import django_countries.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0005_registration_confirmation"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegistrationWeek1",
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
                    "registration_total_score",
                    models.PositiveSmallIntegerField(default=0),
                ),
                (
                    "accepted",
                    models.BooleanField(
                        default=False,
                        help_text="Organizers have accepted the registration",
                    ),
                ),
                (
                    "confirmed",
                    models.BooleanField(
                        default=False, help_text="User has confirmed their acceptance"
                    ),
                ),
                (
                    "waiting_list",
                    models.BooleanField(
                        default=False,
                        help_text="A non-accepted registration is on the waiting list in case there is space",
                    ),
                ),
                (
                    "user_canceled",
                    models.BooleanField(
                        default=False, help_text="User has canceled their registration"
                    ),
                ),
                (
                    "access_code",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="A short random code used to process an application in the URL.",
                        max_length=16,
                        null=True,
                        unique=True,
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "accepted_email_sent",
                    models.DateTimeField(editable=False, null=True),
                ),
                (
                    "waiting_list_email_sent",
                    models.DateTimeField(editable=False, null=True),
                ),
                (
                    "rejection_list_email_sent",
                    models.DateTimeField(editable=False, null=True),
                ),
                (
                    "tshirt_size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("xs", "XS"),
                            ("s", "S"),
                            ("m", "M"),
                            ("l", "L"),
                            ("xl", "XL"),
                            ("2xl", "2xl"),
                            ("3xl", "3xl"),
                        ],
                        max_length=3,
                        null=True,
                        verbose_name="T-shirt sizes",
                    ),
                ),
                (
                    "tshirt_fit",
                    models.CharField(
                        blank=True,
                        choices=[("women", "Women's fit"), ("men", "Men's fit")],
                        max_length=16,
                        null=True,
                        verbose_name="T-shirt sizes",
                    ),
                ),
                (
                    "tshirt_color",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("black", "Black"),
                            ("blue", "Blue (event's theme color)"),
                            ("white", "White"),
                            ("grey", "Grey"),
                        ],
                        max_length=32,
                        null=True,
                        verbose_name="T-shirt color preference",
                    ),
                ),
                (
                    "dietary_restrictions",
                    models.TextField(blank=True, verbose_name="Dietary restrictions"),
                ),
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
                    "benefits",
                    models.TextField(
                        help_text="How do you think that your participation in this event will be beneficial for you?"
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
                (
                    "week_2_registration",
                    models.BooleanField(
                        default=False,
                        help_text="Indicate whether you registered -- whether you were accepted or not doesn't matter.",
                        verbose_name="Registered for Week 2",
                    ),
                ),
                (
                    "motivation",
                    models.TextField(
                        help_text="For example, how do you use Python in your everyday life; how will you be using Data Science; anything else that you find motivating about this event?"
                    ),
                ),
                (
                    "python_level",
                    models.CharField(
                        choices=[
                            ("none", "None"),
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        max_length=32,
                        verbose_name="Python level",
                    ),
                ),
                (
                    "python_knowledge",
                    models.TextField(
                        help_text="If you have existing Python experiences, you can indicate them here (300 characters max)",
                        max_length=300,
                        verbose_name="Python experience",
                    ),
                ),
                (
                    "programming_level",
                    models.CharField(
                        choices=[
                            ("none", "None"),
                            ("beginner", "Beginner"),
                            ("intermediate", "Intermediate"),
                            ("advanced", "Advanced"),
                        ],
                        max_length=32,
                        verbose_name="programming skills",
                    ),
                ),
                (
                    "programming_knowledge",
                    models.TextField(
                        help_text="If you have existing experiences with general programming, you can indicate them here (300 characters max)",
                        max_length=300,
                        verbose_name="Programming experience",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="registration",
            name="accepted_email_sent",
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="registration",
            name="rejection_list_email_sent",
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="registration",
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
            name="tshirt_color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("black", "Black"),
                    ("blue", "Blue (event's theme color)"),
                    ("white", "White"),
                    ("grey", "Grey"),
                ],
                max_length=32,
                null=True,
                verbose_name="T-shirt color preference",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="tshirt_fit",
            field=models.CharField(
                blank=True,
                choices=[("women", "Women's fit"), ("men", "Men's fit")],
                max_length=16,
                null=True,
                verbose_name="T-shirt sizes",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="tshirt_size",
            field=models.CharField(
                blank=True,
                choices=[
                    ("xs", "XS"),
                    ("s", "S"),
                    ("m", "M"),
                    ("l", "L"),
                    ("xl", "XL"),
                    ("2xl", "2xl"),
                    ("3xl", "3xl"),
                ],
                max_length=3,
                null=True,
                verbose_name="T-shirt sizes",
            ),
        ),
        migrations.AlterField(
            model_name="registration",
            name="waiting_list_email_sent",
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]