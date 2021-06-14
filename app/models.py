import datetime
from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    name = models.CharField(_('username'), max_length=254)
    email = models.EmailField(max_length = 254, unique=True)
    password = models.CharField(_('password'), max_length=128)
    like = models.ManyToManyField(Property, null=True, blank=True, on_delite=PROTECT) #models.ForeignKey(Question, on_delete=models.CASCADE)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    join_date = models.DateTimeField(_('date joined'), default=timezone.now)
    last_date = models.DateField(_('last login'), blank=True, null=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    prop_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=50)
    address =
    price =
    fee =
    after_fee =
    before_fee =
    madori =
    menseki =
    access1 =
    access2 =
    access3 =
    height =
    floor =
    age =
    detail_url =
    like = models.ManyToManyField(get_user_model(), on_delete=models.PROTECT)#良いねの数に変換
    def __str__(self):
        return self.question_text

