# email_app/models.py

from django.db import models

class ScheduledEmail(models.Model):
    recipients = models.TextField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    send_at = models.DateTimeField()
