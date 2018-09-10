from django.db import models
from django.conf import settings

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    degree = models.CharField(max_length=20)


    def __str__(self):
        return self.user.username
