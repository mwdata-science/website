from django.db import models
from django_countries.fields import CountryField
from django.core.validators import FileExtensionValidator


class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    date_of_bith = models.DateField()
    
    gender = models.CharField(choices=[("f", "Female"), ("m", "Male")], max_length=3)
    
    email = models.EmailField()
    
    phone = models.CharField(max_length=256, help_text="Please remember country-code if different from +265.")
    
    occupation = models.CharField(
        max_length=32,
        choices=[
            ("phd", "Student (PhD)"),
            ("masters", "Student (masters)"),
            ("undergrad", "Student (undergrad)"),
            ("employed", "Employed"),
            ("other", "Other (please fill in)"),
        ]
    )
    occupation_other = models.CharField(max_length=255, help_text="Occupation, if other than listed", null=True, blank=True)


    speciality = models.CharField(
        max_length=32,
        choices=[
            ("it", "Information Technology"),
            ("cs", "Computer Science"),
            ("statistics", "Statistics"),
            ("mathematics", "Mathematics"),
            ("health", "Health"),
            ("agriculture", "Agriculture"),
            ("other", "Other (please fill in)"),
        ]
    )
    speciality_other = models.CharField(max_length=255, help_text="Speciality, if other than listed", null=True, blank=True)

    highest_qualification = models.CharField(
        max_length=32,
        choices=[
            ("phd", "PhD"),
            ("masters", "MSc"),
            ("undergrad", "BSc"),
            ("other", "Other (please fill in)"),
        ]
    )
    highest_qualification_other = models.CharField(max_length=255, help_text="Highest qualification, if other than listed", null=True, blank=True)

    country = CountryField(help_text="Country of your current residence.")

    motivation = models.TextField(help_text="What motivates you to participate in this Bootcamp?")

    benefits = models.TextField(help_text="How do you think that your participation in this event will be beneficial for you?")

    scholarship = models.BooleanField(verbose_name="I will apply for a scholarship", help_text="This option will open later.")
    scholarship_conditioned = models.BooleanField(verbose_name="Participation conditioned by scholarship", help_text="Is your participation in this event reliant on the Scholarship?")

    cv = models.FileField(verbose_name="Curriculum Vitae", validators=[FileExtensionValidator(allowed_extensions=['pdf', "doc", "docx", "odt", "txt"])])
