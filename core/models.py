
# import uuid
# from datetime import datetime, timedelta
# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, blank=True)
#     address = models.TextField(blank=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']  # keep username as display name

#     def __str__(self):
#         return self.email
# User = settings.AUTH_USER_MODEL

# class PasswordResetRequest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_verified = models.BooleanField(default=False)

#     def is_expired(self):
#         return datetime.now() > self.created_at + timedelta(hours=1)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'   # Login with email
    REQUIRED_FIELDS = ['username']  # Required for createsuperuser
