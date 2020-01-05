from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""


    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        """Return a string reporesentative of rhe models"""

        return self.text

class Entry(models.Model):
    """Something specific learn about a Topic"""
    topic = models.ForeignKey(Topic,on_delete= models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entrie'

    def __str__(self):
        """Return a String representative of the model"""
        return f"{self.text[:50]}"