from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT, CASCADE
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils import timezone
import datetime

class Property(models.Model):
    title= models.CharField(max_length=50, default="sample")
    area = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    access1 = models.CharField(max_length=60)
    access2 = models.CharField(max_length=60)
    access3 = models.CharField(max_length=60)
    age = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    floor = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    fee = models.CharField(max_length=10)
    after_fee = models.CharField(max_length=10)
    before_fee = models.CharField(max_length=10)
    madori = models.CharField(max_length=10)
    menseki = models.CharField(max_length=10)
    detail = models.URLField()
    createted_at = models.DateTimeField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # pred_price = models.IntegerField(max_length=10, default=0, blank=True)


    def __str__(self):
        return self.prop_name
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True,)
    like = models.ManyToManyField(Property, blank=True)
    join_date = models.DateTimeField('date joined', default=timezone.now)
    last_date = models.DateField('last login', default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
