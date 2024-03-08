from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    student_id = models.ForeignKey(User, verbose_name="студент", on_delete=models.CASCADE, blank=True)
    information = models.TextField(blank=True)
    about = models.TextField(blank=True)
    iam = models.TextField(blank=True)
    resume_send = models.BooleanField(null=True, blank=True)
    resume_accept = models.BooleanField(null=True, blank=True)
