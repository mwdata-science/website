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
            accepted=False,
            waiting_list=False,
            confirmed=False,
            rejection_list_email_sent=None,
        )
        waiting_list_registrations = models.Registration.objects.filter(
            accepted=False,
            waiting_list=True,
            confirmed=False,
            rejection_list_email_sent=None,
        )

        for registration in accepted_registrations:
            print("Sending to: {}".format(registration.email))
            email = mail.RegistrationAccepted(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=not options.get("dry"))
            if not options.get("dry"):
                registration.accepted_email_sent = timezone.now()
                registration.save()

        for registration in rejected_registrations:
            print("Sending to: {}".format(registration.email))
            email = mail.RegistrationNotAccepted(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=not options.get("dry"))
            if not options.get("dry"):
                registration.rejection_list_email_sent = timezone.now()
                registration.save()

        for registration in waiting_list_registrations:
            print("Sending to: {}".format(registration.email))
            email = mail.RegistrationWaitingList(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=not options.get("dry"))
            if not options.get("dry"):
                registration.waiting_list_email_sent = timezone.now()
                registration.save()

        print(
            "Accepted registrations: {}\n".format(accepted_registrations.count())
            + "Rejected registrations: {}\n".format(rejected_registrations.count())
            + "Waiting list registrations: {}\n".format(
                waiting_list_registrations.count()
            )
        )
