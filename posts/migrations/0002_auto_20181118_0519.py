# Generated by Django 2.0.2 on 2018-11-17 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='follower',
            new_name='hunter',
        ),
    ]