from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RawTweet(models.Model):
    text = models.CharField(max_length=140)
    p_date = models.DateTimeField()

    # syncdb v dgango 1.7


class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=140)
    p_date = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars')