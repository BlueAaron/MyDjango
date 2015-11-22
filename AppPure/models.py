from django.db import models

# Create your models here.
class Usr(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
    def __unicode__(self):
        return self.username
