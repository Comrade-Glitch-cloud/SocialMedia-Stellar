from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template

register = template.Library()
User = get_user_model()

class StellarGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='StellarGroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('stellar_groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class StellarGroupMember(models.Model):
    group = models.ForeignKey(StellarGroup, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_stellar_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
