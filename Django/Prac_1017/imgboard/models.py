from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Imgboard(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True,)
    thumbnail = ProcessedImageField(
        upload_to='images/',
        blank=True,
        processors=[Thumbnail(400,500)],
        format='JPEG',
        options={'quiality' : 90 },
    )