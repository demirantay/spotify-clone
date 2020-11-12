# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports


# Basic User Profile
# -------------
# This model holds the basis user profile such as email, username .. etc
# more complicated settigns such as privacy, sms ... etc. Basic profile is
# used and created for basic users.
class BasicUserProfile(models.Model):
    # O2One relationship with django's user model
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)

    # Edit Profile -- settings
    profile_photo = models.ImageField(
        upload_to="profile_photo/", blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "Settings id: " + str(self.id) + " | User: " + str(self.user)
