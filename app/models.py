import datetime
from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    name = models.CharField(_('username'), max_length=254)
    email = models.EmailField(max_length = 254, unique=True, null=False, blank=False)
    password = models.CharField(_('password'), max_length=128)
    like = models.ManyToManyField(Property, null=True, blank=True, on_delite=PROTECT) #models.ForeignKey(Question, on_delete=models.CASCADE)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    join_date = models.DateTimeField(_('date joined'), default=timezone.now)
    last_date = models.DateField(_('last login'), blank=True, null=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    prop_name = models.CharField(max_length=254)
    area = models.CharField(max_length=10)
    address = models.CharField(max_length=254)
    price = models.CharField(max_length=10)
    fee = models.CharField(max_length=10)
    after_fee = models.CharField(max_length=10)
    before_fee = models.CharField(max_length=10)
    madori = models.CharField(max_length=10)
    menseki = models.CharField(max_length=10)
    access1 = models.CharField(max_length=100)
    access2 = models.CharField(max_length=100)
    access3 = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    detail_url = models.URLField()
    like = models.ManyToManyField(get_user_model(), on_delete=models.PROTECT)#良いねの数に変換
    pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField(_("date published"),auto_now_add=True)

    def __str__(self):
        return self.prop_name

