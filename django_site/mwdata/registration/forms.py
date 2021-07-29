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


class RegistrationAcceptedForm(forms.ModelForm):

    confirmed = forms.TypedChoiceField(
        coerce=lambda x: x == "True",
        choices=(
            (True, "CONFIRM my participation"),
            (False, "CANCEL my registration"),
        ),
        widget=forms.RadioSelect,
    )

    def save(self, *args, **kwargs):
        print(self.cleaned_data)
        raise
        registration = super().save(*args, **kwargs)
        if not self.cleaned_data["confirmed"]:
            registration.user_canceled = False
            registration.save()
        return registration

    class Meta:
        model = models.Registration
        fields = ("confirmed",)
