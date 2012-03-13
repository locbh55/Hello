from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title