# Generated by Django 4.0.4 on 2022-05-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0002_alter_cashflow_netincome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='logo',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='info',
            name='website',
            field=models.URLField(max_length=300),
        ),
    ]