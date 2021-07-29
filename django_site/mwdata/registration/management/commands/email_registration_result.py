"""
For development purposes: Create a bunch of random events at random times.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from mwdata.registration import mail
from mwdata.registration import models


class Command(BaseCommand):
    help = "Send emails to participants about their registration"

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry",
            action="store_true",
            help="Do not send emails, just print",
        )

    def handle(self, *args, **options):

        accepted_registrations = models.Registration.objects.filter(
            accepted=True, confirmed=False
        )
        rejected_registrations = models.Registration.objects.filter(
            accepted=True, waiting_list=False, confirmed=False
        )
        waiting_list_registrations = models.Registration.objects.filter(
            accepted=True, waiting_list=True, confirmed=False
        )

        for registration in accepted_registrations:
            print("Sending to: {}".format(registration.email))
            email = mail.RegistrationAccepted(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=options.get("dry"))
            registration.accepted_email_sent = timezone.now()
            registration.save()

        for registration in rejected_registrations:
            pass

        for registration in waiting_list_registrations:
            pass
