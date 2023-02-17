# Generated by Django 4.1.7 on 2023-02-17 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=1000000)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]