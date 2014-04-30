from django.db import models

# Create your models here.
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