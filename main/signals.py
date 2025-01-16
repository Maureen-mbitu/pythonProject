from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment

@receiver(post_save, sender=Appointment)
def send_appointment_confirmation(sender, instance, created, **kwargs):
    if created:
        # Send an email notification
        subject = 'Appointment Confirmation'
        message = f'Dear {instance.user.username},\n\nYour appointment for {instance.service.name} on {instance.date} at {instance.time} has been confirmed.'
        recipient_list = [instance.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

        print(f'Email sent to {instance.user.email} for appointment {instance.id}')