from django.db import models
from django.conf import settings
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    category = models.TextField()
    title = models.CharField(max_length=20)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    image = ProcessedImageField(
        upload_to = 'images/',
        blank = True,
        processors = [Thumbnail(400,500)],
        format = 'JPEG',
        options = {'quality' : 90},
    )