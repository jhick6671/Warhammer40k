from django.db import models

class WoundCounter(models.Model):
    dice = models.CharField(max_length=3)
    hit = models.CharField(max_length=3)
    wound = models.CharField(max_length=3)
    saves = models.CharField(max_length=3)

    def __unicode__(self):
        return "{}-{}-{}-{}".format(self.dice,
                                    self.hit,
                                    self.wound,
                                    self.saves)

    def get_absolute_url(self):
        return '/woundcounter/results/{}'.format(self.pk)

class Army(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=None)
    units = models.URLField()
    symbols = models.ImageField(upload_to='symbols')

    def __unicode__(self):
        return "{} - {} - {} - {}".format(self.name,
                                          self.description,
                                          self.units,
                                          self.symbols)
