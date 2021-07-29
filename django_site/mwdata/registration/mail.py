from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMessage
from django.template import loader

from . import models


class BaseEmail(EmailMessage):

    template = "registration/email/base.txt"
    default_subject = "SET SUBJECT HERE"

    def __init__(self, *args, **kwargs):
        self.context = kwargs.pop("context", {})
        self.request = kwargs.pop("request", {})
        self.recipient_name = kwargs.pop("recipient_name")
        kwargs.setdefault("subject", self.default_subject)

        super(BaseEmail, self).__init__(*args, **kwargs)
        self.body = self.get_body()

    def get_context_data(self):
        c = self.context
        site = get_current_site(self.request)
        c["request"] = self.request
        c["domain"] = site.domain
        c["site_name"] = site.name
        c["protocol"] = "https" if not settings.DEBUG else "http"
        c["recipient_name"] = self.recipient_name
        return c

    def get_body(self):
        return loader.render_to_string(self.template, self.get_context_data())

    def send(self, send_not_print=True):
        if send_not_print:
            super().send(fail_silently=False)
            for recipient in self.to:
                models.EmailLog.objects.create(
                    email_content=self.get_body(),
                    registration=getattr(self, "registration"),
                    recipient=recipient,
                )
        else:
            print(self.get_body())


class RegistrationAccepted(BaseEmail):

    template = "registration/email/accepted.txt"
    default_subject = "Accepted: Malawi Data Science Bootcamp 2021"

    def __init__(self, *args, **kwargs):
        self.registration = kwargs.pop("registration")
        super().__init__(*args, **kwargs)

    def get_context_data(self):
        c = super().get_context_data()
        c["registration"] = self.registration
        return c


class RegistrationNotAccepted(BaseEmail):

    template = "registration/email/rejected.txt"
    default_subject = "Not accepted: Malawi Data Science Bootcamp 2021"

    def __init__(self, *args, **kwargs):
        self.registration = kwargs.pop("registration")
        super().__init__(*args, **kwargs)

    def get_context_data(self):
        c = super().get_context_data()
        c["registration"] = self.registration
        return c


class RegistrationWaitingList(BaseEmail):

    template = "registration/email/waiting_list.txt"
    default_subject = "Waiting list: Malawi Data Science Bootcamp 2021"

    def __init__(self, *args, **kwargs):
        self.registration = kwargs.pop("registration")
        super().__init__(*args, **kwargs)

    def get_context_data(self):
        c = super().get_context_data()
        c["registration"] = self.registration
        return c
