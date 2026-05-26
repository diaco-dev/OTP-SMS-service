from datetime import datetime
from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, mobile=None, email=None, password=None):
        if not mobile and not email:
            raise ValueError('User must have a mobile or email.')
        if not password:
            raise ValueError('User must have a password.')
        user = self.model(
            mobile=mobile
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile=None, password=None):
        if not mobile:
            raise ValueError('User must have an mobile.')
        if not password:
            raise ValueError('User must have a password.')

        user = self.model(
            mobile=mobile
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    id = models.UUIDField(
        "unique id",
        primary_key=True,
        unique=True,
        null=False,
        default=uuid4,
        editable=False
    )
    first_name = models.CharField(
        'first name',
        max_length=50,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'last name',
        max_length=100,
        null=True,
        blank=True
    )
    email = models.EmailField(
    'email',
    unique=True
    )
    mobile = models.CharField(
        'mobile',
        max_length=11,
        unique=True
    )
    mobile_verified = models.BooleanField(
        'mobile verified',
        default=False
    )
    mobile2 = models.CharField(
        "mobile2",
        max_length=11,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name=('created at'),
        default=timezone.now
    )
    username = None

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    objects = UserManager()
    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
        db_table = 'core_user'
        indexes = (
            models.Index(fields=['id'], name='user_id_idx'),
            models.Index(fields=['email'], name='user_email_idx'),
        )

    @property
    def full_name(self):
        return self.get_full_name() or self.mobile

    def __str__(self):
        return self.full_name

    @property
    def created_at(self):
        return datetime(self.created_at)
