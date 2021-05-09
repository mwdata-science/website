from django.shortcuts import render

from . import forms
from . import models
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls.base import reverse


class RegistrationCreateView(CreateView):
    model = models.Registration
    form_class = forms.RegistrationForm
    template_name = "registration/create.html"

    def get_success_url(self):
        return reverse("registration_confirm")


class RegistrationConfirm(TemplateView):
    template_name = "registration/created.html"
