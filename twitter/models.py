from django.db import models

# Create your models here.

class RawTweet(models.Model):
    text = models.CharField(max_length=140)
    p_date = models.DateTimeField()

#syncdb v dgango 1.7