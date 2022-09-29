from django.db import models

# Create your models here.
class Board(models.Model):
    board = models.TextField(default="null")
    title = models.CharField(max_length=80)
    content = models.TextField(default="null")
    created_at = models.DateField(auto_now_add=True)
