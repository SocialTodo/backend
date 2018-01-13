# Generated by Django 2.0.1 on 2018-01-13 19:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('facebook_user_id', models.CharField(db_index=True, max_length=300, primary_key=True, serialize=False, unique=True)),
                ('facebook_token', models.CharField(max_length=700)),
                ('name', models.CharField(max_length=255)),
                ('facebook_friends', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
