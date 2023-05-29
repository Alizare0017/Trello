from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, email="", **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(username, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex=settings.USERNAME_REGEX)])

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email','first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name
