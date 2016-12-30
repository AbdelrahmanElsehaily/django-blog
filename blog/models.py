from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    puplished_date=models.DateTimeField(blank=True,null=True)

    def puplish(self):
        self.puplished_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title()