from django.db import models

# Create your models here.
class Chathistory(models.Model):
    message = models.CharField()
    response = models.CharField()
    