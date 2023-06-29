# email_app/views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .models import ScheduledEmail

def send_email(request):
    if request.method == 'POST':
        recipients = request.POST['recipients']
        subject = request.POST['subject']
        message = request.POST['message']
        send_at = request.POST['send_at']

        email = ScheduledEmail.objects.create(
            recipients=recipients,
            subject=subject,
            message=message,
            send_at=send_at
        )

        return HttpResponse('Email scheduled successfully.')

    return render(request, 'email_app/send_email.html')
