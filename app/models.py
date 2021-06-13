import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    like = models.IntegerField()
    password
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# class Like(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

# class Property(models.Model):
#     prop_name = models.CharField(max_length=100)
#     pub_date = models.DateTimeField('date published')
#     area = models.CharField(max_length=50)
#     address =
#     price =
#     fee =
#     after_fee =
#     before_fee =
#     madori =
#     menseki =
#     access1 =
#     access2 =
#     access3 =
#     height =
#     floor =
#     age =
#     detail_url =
#     like =
#     def __str__(self):
#         return self.question_text

