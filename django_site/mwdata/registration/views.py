from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.static import serve
from ratelimit.decorators import ratelimit

from . import forms
from . import models


@login_required
def protected_serve(request, path, file_root=None):
    return serve(request, path, file_root)


class RegistrationCreate(CreateView):
    model = models.Registration
    form_class = forms.RegistrationForm
    template_name = "registration/create.html"

    def get_success_url(self):
        return reverse("registration:confirmed")


class RegistrationConfirm(TemplateView):
    template_name = "registration/create_confirmed.html"


class RegistrationWeek1Create(CreateView):
    model = models.RegistrationWeek1
    form_class = forms.RegistrationWeek1Form
    template_name = "registration/week1_create.html"

    def get_success_url(self):
        return reverse("registration:confirmed-week1")


class RegistrationWeek1Confirm(TemplateView):
    template_name = "registration/week1_create_confirmed.html"


class RegistrationAccepted(UpdateView):
    template_name = "registration/accepted.html"
    model = models.Registration
    context_object_name = "registration"

    @method_decorator(ratelimit(key="ip", rate="100/h"))
    def dispatch(self, request, *args, **kwargs):
        self.access_code = kwargs["access_code"]
        return UpdateView.dispatch(self, request, *args, **kwargs)

    def get_object(self):
        return UpdateView.get_queryset(self).get(
            access_code=self.access_code,
            accepted=True,
        )

    def get_success_url(self):
        return reverse(
            "registration:confirmation-done",
            kwargs={"access_code": self.access_code},
        )

    def get_form_class(self):
        if self.object.scholarship and not self.object.scholarship_confirmed:
            return forms.RegistrationAcceptedScholarshipForm
        if self.object.scholarship_confirmed:
            return forms.RegistrationAcceptedScholarshipConfirmedForm
        if self.object.confirmed:
            return forms.RegistrationAcceptedConfirmedForm
        return forms.RegistrationAcceptedForm


class RegistrationAcceptedConfirm(DetailView):
    template_name = "registration/accepted_confirmed.html"
    model = models.Registration
    context_object_name = "registration"

    @method_decorator(ratelimit(key="ip", rate="100/h"))
    def dispatch(self, request, *args, **kwargs):
        self.access_code = kwargs["access_code"]
        return DetailView.dispatch(self, request, *args, **kwargs)

    def get_object(self):
        return UpdateView.get_queryset(self).get(access_code=self.access_code)


class RegistrationWeek1AcceptedConfirm(DetailView):
    template_name = "registration/week1_accepted_confirmed.html"
    model = models.RegistrationWeek1
    context_object_name = "registration"

    @method_decorator(ratelimit(key="ip", rate="100/h"))
    def dispatch(self, request, *args, **kwargs):
        self.access_code = kwargs["access_code"]
        return DetailView.dispatch(self, request, *args, **kwargs)

    def get_object(self):
        return UpdateView.get_queryset(self).get(access_code=self.access_code)


class RegistrationWeek1Accepted(UpdateView):
    template_name = "registration/week1_accepted.html"
    model = models.RegistrationWeek1
    context_object_name = "registration"

    @method_decorator(ratelimit(key="ip", rate="100/h"))
    def dispatch(self, request, *args, **kwargs):
        self.access_code = kwargs["access_code"]
        return UpdateView.dispatch(self, request, *args, **kwargs)

    def get_object(self):
        return UpdateView.get_queryset(self).get(
            access_code=self.access_code,
            accepted=True,
        )

    def get_success_url(self):
        return reverse(
            "registration:week1-confirmation-done",
            kwargs={"access_code": self.access_code},
        )

    def get_form_class(self):
        return forms.RegistrationWeek1AcceptedForm
