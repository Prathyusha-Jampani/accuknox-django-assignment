import os
import django
# Setup Django before importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()  # Initialize Django
from django.db import transaction
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Signal handler
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print("Signal received! Processing...")
        instance.first_name = "UpdatedName"
        instance.save()  # Modify instance within signal
        print("Signal processing completed!")
try:
    with transaction.atomic():  # Ensures database transaction handling
        print("Saving user...")
        user = User.objects.create(username="test_user3")
        print("User saved! Raising exception now...")
        raise Exception("Simulating an error after user save")
except Exception as e:
    print(f"Exception occurred: {e}")
# Check if user is actually saved in DB
user_exists = User.objects.filter(username="test_user3").exists()
print(f"Was user saved in DB? {'Yes' if user_exists else 'No'}")
