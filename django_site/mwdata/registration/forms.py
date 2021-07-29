from django import forms

from . import models


BIRTH_YEAR_CHOICES = range(1900, 2010)


class RegistrationForm(forms.ModelForm):
    date_of_bith = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "dob"})
    )

    def clean(self):
        raise forms.ValidationError("Registration is closed :/")

    class Meta:
        model = models.Registration
        fields = "__all__"


class RegistrationWeek1Form(forms.ModelForm):
    date_of_bith = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "dob"})
    )

    class Meta:
        model = models.RegistrationWeek1
        fields = (
            "first_name",
            "last_name",
            "date_of_bith",
            "gender",
            "email",
            "phone",
            "occupation",
            "occupation_other",
            "speciality",
            "speciality_other",
            "highest_qualification",
            "highest_qualification_other",
            "country",
            "motivation",
            "benefits",
            "cv",
            "week_2_registration",
            "motivation",
            "python_level",
            "python_knowledge",
            "programming_level",
            "programming_knowledge",
        )


class RegistrationAcceptedForm(forms.ModelForm):

    confirmed_choice = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=(
            (True, "CONFIRM my participation"),
            (False, "CANCEL my registration"),
        ),
        widget=forms.RadioSelect,
        initial=None,
        label="Confirmation",
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        participation_fields = [
            "tshirt_size",
            "tshirt_fit",
            "tshirt_color",
            "dietary_restrictions",
        ]

        if not cleaned_data["confirmed_choice"]:
            if any(cleaned_data[k] for k in participation_fields):
                raise forms.ValidationError(
                    "You have chosen to cancel your participation, please leave all other fields blank."
                )
        else:
            if not all(cleaned_data[k] for k in participation_fields):
                raise forms.ValidationError("You have to fill in all the fields.")
        return cleaned_data

    def save(self, *args, **kwargs):
        registration = super().save(*args, **kwargs)
        registration.confirmed = self.cleaned_data["confirmed_choice"]
        registration.user_canceled = not self.cleaned_data["confirmed_choice"]
        registration.save()
        return registration

    class Meta:
        model = models.Registration
        fields = [
            "confirmed_choice",
            "tshirt_size",
            "tshirt_fit",
            "tshirt_color",
            "dietary_restrictions",
        ]


class RegistrationAcceptedScholarshipForm(RegistrationAcceptedForm):
    class Meta:
        model = models.Registration
        fields = RegistrationAcceptedForm.Meta.fields + [
            "scholarship_accomodation",
            "scholarship_transportation",
            "scholarship_transportation_departure",
            "scholarship_other_needs",
        ]
