from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from ratelimit.decorators import ratelimit

from . import forms
from . import models


class RegistrationCreate(CreateView):
    model = models.Registration
    form_class = forms.RegistrationForm
    template_name = "registration/create.html"

    def get_success_url(self):
        return reverse("registration:confirmed")


class RegistrationConfirm(TemplateView):
    template_name = "registration/created.html"


class RegistrationAccepted(UpdateView):
    template_name = "registration/accepted.html"
    model = models.Registration
    form_class = forms.RegistrationAcceptedForm

    @method_decorator(ratelimit(key="ip", rate="100/h"))
    def dispatch(self, request, *args, **kwargs):
        self.access_code = kwargs["access_code"]
        return UpdateView.dispatch(self, request, *args, **kwargs)

    def get_object(self):
        return UpdateView.get_queryset(self).get(access_code=self.access_code)
