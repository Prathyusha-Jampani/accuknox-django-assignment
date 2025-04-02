import os
import django
import time
import threading
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

# ✅ Properly setup Django before importing models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# ✅ Use get_user_model() instead of direct User import
User = get_user_model()

# Print the main thread ID
print(f"Main program running in thread: {threading.get_ident()}")

# Define the signal
@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received in thread: {threading.get_ident()}")
        time.sleep(3)  # Simulate delay
        print("Signal processing completed!")

# ✅ Ensure a unique username before creating a user
username = f"test_user_{int(time.time())}"  # Generate a unique username using timestamp
print(f"Saving user with username: {username}...")

user = User.objects.create(username=username)
print(f"User '{user.username}' saved successfully!")
