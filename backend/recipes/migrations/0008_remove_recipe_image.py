# Generated by Django 2.2.19 on 2022-09-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20220923_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]
