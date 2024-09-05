from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Please provide Email')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, email, password):
#         user = self.create_user(email=email, password=password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, blank=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # objects = CustomUserManager()
    
    def __str__(self):
        return self.email
