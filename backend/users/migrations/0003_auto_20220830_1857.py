# Generated by Django 2.2.19 on 2022-08-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_subscribed',
            field=models.BooleanField(),
        ),
    ]
