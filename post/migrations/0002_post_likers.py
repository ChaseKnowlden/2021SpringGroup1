# Generated by Django 3.2.3 on 2021-05-30 10:22

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.TextField(default=[], max_length=builtins.max),
            preserve_default=False,
        ),
    ]