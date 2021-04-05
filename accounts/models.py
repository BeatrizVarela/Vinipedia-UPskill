from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='images/profiles/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        pass
