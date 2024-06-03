from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group)


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(
        max_length=255, unique=True, db_index=True, blank=True, null=True)
    image = models.ImageField(default='default.jpg',
                              upload_to='images', blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    ideal_weight = models.FloatField(blank=True, null=True)
    calories = models.FloatField(blank=True, null=True)

    activity = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(Group, verbose_name=(
        'groups'), blank=True, related_name='authentication_users')
    user_permissions = models.ManyToManyField(
        'auth.Permission',  # or 'authentication.Permission' if you have a custom Permission model
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='authentication_users',
    )

    def __str__(self):
        return self.email


class Foods(models.Model):
    FoodName = models.CharField(max_length=200, unique=True)
    # LinkDrive = models.ImageField(upload_to='foods_images/')
    LinkDrive = models.CharField(max_length=500, default='Images/bagel.jpg')
    TheDescription = models.CharField(max_length=400, default=0)
    YoutubeLink = models.CharField(max_length=200, default=0)

    Calories = models.FloatField(blank=False, null=False, default=0)
    Protein = models.FloatField(blank=False, null=False, default=0)
    Fats = models.FloatField(blank=False, null=False, default=0)
    Carbs = models.FloatField(blank=False, null=False, default=0)
    likes = models.ManyToManyField(
        User, related_name='liked_foods', blank=True)  # New field for likes

    def __str__(self):
        return self.FoodName
