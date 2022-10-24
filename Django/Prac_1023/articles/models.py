from django.db import models

from accounts.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField