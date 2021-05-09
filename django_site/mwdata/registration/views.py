from django.shortcuts import render

from . import forms
from . import models
from django.views.generic.edit import CreateView

class RegistrationCreateView(CreateView):
    model = models.Registration
    form_class = forms.RegistrationForm
    template_name = "registration/create.html"