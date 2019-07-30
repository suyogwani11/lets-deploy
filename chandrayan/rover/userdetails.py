from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accdata(models.Model):
    usernamee = models.CharField(max_length=50,unique=True)
    emailid = models.EmailField()

    def __str__(self):
        return self.usernamee


class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
