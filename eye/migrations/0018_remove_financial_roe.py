# Generated by Django 4.0.4 on 2022-06-22 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0017_shortfinancial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financial',
            name='roe',
        ),
    ]