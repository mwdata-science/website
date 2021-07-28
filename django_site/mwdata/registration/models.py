from django.db import models
from django_countries.fields import CountryField
from django.core.validators import FileExtensionValidator


class Registration(models.Model):
    """
    This is the model for people registering for Week 2.
    """

    registration_total_score = models.PositiveSmallIntegerField(
        default=0,
    )

    accepted = models.BooleanField(
        default=False,
        help_text="Organizers have accepted the registration"
    )
    confirmed = models.BooleanField(
        default=False,
        help_text="User has confirmed their acceptance"
    )
    waiting_list = models.BooleanField(
        default=False,
        help_text="A non-accepted registration is on the waiting list in case there is space",
    )
    user_canceled = models.BooleanField(
        default=False,
        help_text="User has canceled their registration",
    )

    access_code = models.CharField(
        null=True,
        blank=True,
        editable=False,
        help_text="A short random code used to process an application in the URL.",
        max_length=16,
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    accepted_email_sent = models.DateTimeField(null=True)
    waiting_list_email_sent = models.DateTimeField(null=True)
    rejection_list_email_sent = models.DateTimeField(null=True)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    date_of_bith = models.DateField()

    gender = models.CharField(choices=[("f", "Female"), ("m", "Male")], max_length=3)

    email = models.EmailField()

    phone = models.CharField(
        max_length=256, help_text="Please remember country-code if different from +265."
    )

    occupation = models.CharField(
        max_length=32,
        choices=[
            ("phd", "Student (PhD)"),
            ("masters", "Student (masters)"),
            ("undergrad", "Student (undergrad)"),
            ("employed", "Employed"),
            ("other", "Other (please fill in)"),
        ],
    )
    occupation_other = models.CharField(
        max_length=255,
        help_text="Occupation, if other than listed",
        null=True,
        blank=True,
    )

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
        ],
    )
    speciality_other = models.CharField(
        max_length=255,
        help_text="Speciality, if other than listed",
        null=True,
        blank=True,
    )

    highest_qualification = models.CharField(
        max_length=32,
        choices=[
            ("phd", "PhD"),
            ("masters", "MSc"),
            ("undergrad", "BSc"),
            ("other", "Other (please fill in)"),
        ],
    )
    highest_qualification_other = models.CharField(
        max_length=255,
        help_text="Highest qualification, if other than listed",
        null=True,
        blank=True,
    )

    country = CountryField(help_text="Country of your current residence.")

    motivation = models.TextField(
        help_text="What motivates you to participate in this Bootcamp?"
    )

    benefits = models.TextField(
        help_text="How do you think that your participation in this event will be beneficial for you?"
    )

    scholarship = models.BooleanField(
        verbose_name="I will apply for a scholarship",
        help_text="Please check this field if you intend to apply for a scholarship. This option will open later.",
    )
    scholarship_conditioned = models.BooleanField(
        verbose_name="Participation conditioned by scholarship",
        help_text="Is your participation in this event reliant on the Scholarship?",
    )

    cv = models.FileField(
        verbose_name="Curriculum Vitae",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx", "odt", "txt"]
            )
        ],
        upload_to="cv",
    )

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)


class EmailLog(models.Model):
    
    registration = models.ForeignKey(Registration, null=True, blank=True, on_delete=models.SET_NULL)
    recipient = models.CharField(max_length=32)
    email_content = models.TextField()
    
    sent = models.DateTimeField(auto_now_add=True)
