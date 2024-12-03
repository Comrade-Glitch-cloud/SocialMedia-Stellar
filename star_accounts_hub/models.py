from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class CadetProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cadet')
    stellarname = models.CharField(max_length=30, unique=True)
    cadet_picture = models.ImageField(upload_to='cadet_pics/', blank=True, null=True)
    cadet_picture_thumbnail = ImageSpecField(
        source='cadet_picture',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
