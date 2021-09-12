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
        dry = options.get("dry")
        while True:

            massmail = models.MassMail.objects.filter(
                sending=False,
                sent=False,
                schedule_send__lte=timezone.now(),
            ).first()
            if not massmail:
                break

            if not dry:
                # Yes, this can have race conditions but we are not anticipating
                # overlaps here
                massmail.sending = True
                massmail.save()

            registrations = list(massmail.registrations_week1.all()) + list(
                massmail.registrations_week2.all()
            )

            for registration in registrations:
                mail_to_send = mail.RegistrationMassmail(
                    registration=registration,
                    massmail=massmail,
                    from_email="Malawi Data Science Bootcamp 2021 <info@mwdata.science>",
                    recipient_name=registration.name,
                    to=[f"{registration.name} <{registration.email}>"],
                )
                mail_to_send.send(send_not_print=not dry)

            if not dry:
                massmail.sent = True
                massmail.sending = False
                massmail.save()
            else:
                print("This is a dry-run, so we cannot keep looping")
                break
