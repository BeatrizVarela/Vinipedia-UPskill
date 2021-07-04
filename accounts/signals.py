# Signal
from django.db.models.signals import post_save
# Sender
from django.contrib.auth.models import User
# Receiver
from django.dispatch import receiver

# Model we will be creating
from .models import Profile

@receiver(post_save, sender=User)   # When user triggers a save
def create_profile(sender, instance, created, **kwargs):    # It passes all kwargs from post_save
    if created: # If user was created
        Profile.objects.create(user=instance)   # create a profile obj with user defined equal to the instance

# Update function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Both signals were imported to app.py