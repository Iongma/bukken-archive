# Generated by Django 3.2.4 on 2021-07-06 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='sample', max_length=254)),
                ('area', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=254)),
                ('access1', models.CharField(max_length=100)),
                ('access2', models.CharField(max_length=100)),
                ('access3', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('fee', models.CharField(max_length=10)),
                ('after_fee', models.CharField(max_length=10)),
                ('before_fee', models.CharField(max_length=10)),
                ('madori', models.CharField(max_length=10)),
                ('menseki', models.CharField(max_length=10)),
                ('detail', models.URLField()),
                ('createted_at', models.DateTimeField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
