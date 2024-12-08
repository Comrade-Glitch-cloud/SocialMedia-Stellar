from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import misaka
from stellar_groups.models import StellarGroup

User = get_user_model()

class StellarPost(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(StellarGroup, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.message)

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
