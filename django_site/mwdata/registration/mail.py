from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMessage
from django.template import Context
from django.template import loader
from django.template import Template

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
                registration = getattr(self, "registration")
                if isinstance(registration, models.RegistrationWeek1):
                    registration_week1 = registration
                    registration = None
                models.EmailLog.objects.create(
                    email_content=self.get_body(),
                    registration=registration,
                    registration_week1=registration_week1,
                    recipient=recipient,
                )
        else:
            print(self.get_body())


class BaseRegistrationEmail(BaseEmail):
    def __init__(self, *args, **kwargs):
        self.registration = kwargs.pop("registration")
        super().__init__(*args, **kwargs)

    def get_context_data(self):
        c = super().get_context_data()
        c["registration"] = self.registration
        return c


class RegistrationAccepted(BaseRegistrationEmail):

    template = "registration/email/accepted.txt"
    default_subject = "Accepted: Malawi Data Science Bootcamp 2021"


class RegistrationWaitingListAccepted(BaseRegistrationEmail):

    template = "registration/email/accepted_waiting_list.txt"
    default_subject = "Accepted: Malawi Data Science Bootcamp 2021"


class RegistrationNotAccepted(BaseRegistrationEmail):

    template = "registration/email/rejected.txt"
    default_subject = "Not accepted: Malawi Data Science Bootcamp 2021"


class RegistrationWaitingList(BaseRegistrationEmail):

    template = "registration/email/waiting_list.txt"
    default_subject = "Waiting list: Malawi Data Science Bootcamp 2021"


class RegistrationWeek1Accepted(BaseRegistrationEmail):

    template = "registration/email/week1/accepted.txt"
    default_subject = "Accepted: Python Week of Code Malawi 2021"


class RegistrationWeek1WaitingListAccepted(BaseRegistrationEmail):

    template = "registration/email/week1/accepted_waiting_list.txt"
    default_subject = "Accepted: Python Week of Code Malawi 2021"


class RegistrationWeek1NotAccepted(BaseRegistrationEmail):

    template = "registration/email/week1/rejected.txt"
    default_subject = "Not accepted: Python Week of Code Malawi 2021"


class RegistrationWeek1WaitingList(BaseRegistrationEmail):

    template = "registration/email/week1/waiting_list.txt"
    default_subject = "Waiting list: Python Week of Code Malawi 2021"


class RegistrationMassmail(BaseRegistrationEmail):

    template = "registration/email/massmail.txt"

    def __init__(self, *args, **kwargs):
        self.massmail = kwargs.pop("massmail")
        kwargs.setdefault("subject", self.massmail.subject)
        super().__init__(*args, **kwargs)

    def get_body(self):
        t = Template(self.massmail.text_body)
        return t.render(Context(self.get_context_data()))
