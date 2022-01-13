# Generated by Django 2.2.16 on 2022-01-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20220112_2029'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique'),
        ),
    ]