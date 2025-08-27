from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for use profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        # normalizing email address: second half in lower case
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # Never hard code. Hashes passwords. Best practice.
        user.save(using=self._db) # Best practice to add this line, standard django.

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # user profile activated or not
    is_staff = models.BooleanField(default=False) # staff user has access to django admin etc...

    # specify model manager
    # Django needs a custom model manager for the user so it knows how to create users.
    objects = UserProfileManager()

    # To work with django admin and authentication system
    # we override the default
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
    

