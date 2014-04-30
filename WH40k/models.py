from django.db import models

class WoundCounter(models.Model):
    dice = models.CharField(max_length=3)
    hit = models.CharField(max_length=3)
    wound = models.CharField(max_length=3)
    save = models.CharField(max_length=3)
