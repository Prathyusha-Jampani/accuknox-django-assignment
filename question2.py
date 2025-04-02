import django
import threading
from django.conf import settings

# Django Setup
settings.configure(
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
    ],
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}},
)

django.setup()  # Initialize Django properly before imports

from django.contrib.auth.models import User  # Import after setup

# Function to create a user and trigger a signal
def create_user():
    print(f"Running in thread: {threading.get_ident()}")

    # Check if user exists before creating
    if not User.objects.filter(username="test_user").exists():
        User.objects.create(username="test_user")
        print("User created successfully!")
    else:
        print("User already exists!")

# Main thread
print(f"Main program running in thread: {threading.get_ident()}")
create_user()
