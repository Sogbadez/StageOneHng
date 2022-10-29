from django.db import models

# Create your models here.


class Me (models.Model):
    slackUsername=models.CharField(max_length=50)
    backend=models.BooleanField()
    age=models.IntegerField()
    bio=models.TextField(max_length=250)

    def __str__(self):
        return self.slackUsername