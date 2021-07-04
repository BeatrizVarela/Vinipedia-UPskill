# Signal
from django.db.models.signals import post_save
# Sender
from django.contrib.auth.models import User
# Receiver
from django.dispatch import receiver

# Model we will be creating
from .models import Quizz

@receiver(post_save, sender=User)   # When user triggers a save
def create_quizz(sender, instance, created, **kwargs):    # It passes all kwargs from post_save
    if created: # If user was created
        Quizz.objects.create(user=instance)   # create a quizz obj with user defined equal to the instance

# Update function
@receiver(post_save, sender=User)
def save_quizz(sender, instance, **kwargs):
    instance.quizz.save()

# Both signals were imported to app.py