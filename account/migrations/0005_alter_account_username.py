# Generated by Django 4.0.5 on 2022-07-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]