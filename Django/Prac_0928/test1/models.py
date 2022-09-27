from django.db import models

# Create your models here.
class Test1(models.Model):
    email = models.TextField()
    nickname = models.TextField()
    pw = models.TextField()
