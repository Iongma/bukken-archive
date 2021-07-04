from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT, CASCADE
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
import datetime

class Property(models.Model):
    title= models.CharField(max_length=254, default="sample")
    area = models.CharField(max_length=10)
    address = models.CharField(max_length=254)
    access1 = models.CharField(max_length=100)
    access2 = models.CharField(max_length=100)
    access3 = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    height = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    fee = models.CharField(max_length=10)
    after_fee = models.CharField(max_length=10)
    before_fee = models.CharField(max_length=10)
    madori = models.CharField(max_length=10)
    menseki = models.CharField(max_length=10)
    detail = models.URLField()
    createted_at = models.DateTimeField()
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL)
    # pred_price = models.IntegerField(max_length=10, default=0, blank=True)


    def __str__(self):
        return self.prop_name

class User(AbstractUser):
    name = models.CharField('username', max_length=254, default="yourName")
    email = models.EmailField(max_length = 254, unique=True, null=False, blank=False)
    password = models.CharField('password', max_length=128)
    like = models.ManyToManyField(Property, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('superuser status', default=False)
    join_date = models.DateTimeField('date joined', default=timezone.now)
    last_date = models.DateField('last login', blank=True)

    def __str__(self):
        return self.name
