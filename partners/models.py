from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Offers(models.Model):
    company = models.ForeignKey(User, verbose_name="компания", on_delete=models.CASCADE, related_name="company")
    student = models.ForeignKey(User, verbose_name="студент", on_delete=models.CASCADE, related_name="student")
    send = models.BooleanField()
    offer_send = models.BooleanField(null=True, blank=True)
