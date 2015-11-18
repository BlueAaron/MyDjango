from django.db import models

# Create your models here.
class Usr(models.Model):
    username = models.CharField(max_length=30)
    passwd = models.IntegerField()
    def __unicode__(self):
        return self.username
