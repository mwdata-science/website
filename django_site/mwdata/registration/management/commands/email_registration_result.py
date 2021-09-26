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
        self.handle_generalized(
            "Week 1, Python Week of Code Malawi 2021",
            models.RegistrationWeek1,
            mail.RegistrationWeek1Accepted,
            mail.RegistrationWeek1NotAccepted,
            mail.RegistrationWeek1WaitingList,
            mail.RegistrationWeek1WaitingListAccepted,
            *args,
            **options,
        )
        self.handle_generalized(
            "Week 2, Malawi Data Science Bootcamp",
            models.Registration,
            mail.RegistrationAccepted,
            mail.RegistrationNotAccepted,
            mail.RegistrationWaitingList,
            mail.RegistrationWaitingListAccepted,
            *args,
            **options,
        )

    def handle_generalized(
        self,
        verbose_type_name,
        Registration,
        RegistrationAccepted,
        RegistrationNotAccepted,
        RegistrationWaitingList,
        RegistrationWaitingListAccepted,
        *args,
        **options,
    ):

        accepted_registrations = Registration.objects.filter(
            accepted=True,
            confirmed=False,
            waiting_list=False,
            user_canceled=False,
            accepted_email_sent=None,
        )
        rejected_registrations = Registration.objects.filter(
            accepted=False,
            waiting_list=False,
            confirmed=False,
            rejection_list_email_sent=None,
            user_canceled=False,
        )
        waiting_list_registrations = Registration.objects.filter(
            accepted=False,
            waiting_list=True,
            confirmed=False,
            waiting_list_email_sent=None,
            user_canceled=False,
        )
        waiting_list_accepted = Registration.objects.filter(
            accepted=True,
            waiting_list=True,
            confirmed=False,
            accepted_email_sent=None,
            user_canceled=False,
        )

        for registration in accepted_registrations:
            print("Sending to: {}".format(registration.email))
            email = RegistrationAccepted(
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
            email = RegistrationNotAccepted(
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
            email = RegistrationWaitingList(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=not options.get("dry"))
            if not options.get("dry"):
                registration.waiting_list_email_sent = timezone.now()
                registration.save()

        for registration in waiting_list_accepted:
            print("Sending to: {}".format(registration.email))
            email = RegistrationWaitingListAccepted(
                registration=registration,
                recipient_name=registration.name,
                from_email="info@mwdata.science",
                to=[f"{registration.name} <{registration.email}>"],
            )
            email.send(send_not_print=not options.get("dry"))
            if not options.get("dry"):
                registration.accepted_email_sent = timezone.now()
                registration.save()

        print(
            f"{verbose_type_name}\n\n"
            + "Accepted registrations: {}\n".format(accepted_registrations.count())
            + "Rejected registrations: {}\n".format(rejected_registrations.count())
            + "Informed waiting list registrations: {}\n".format(
                waiting_list_accepted.count()
            )
            + "Accepted waiting list registrations: {}\n".format(
                waiting_list_registrations.count()
            )
        )
