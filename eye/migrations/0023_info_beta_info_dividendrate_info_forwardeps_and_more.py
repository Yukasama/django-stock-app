# Generated by Django 4.0.4 on 2022-06-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eye', '0022_rename_summary_info_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='beta',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='dividendRate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='forwardEPS',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pegRatio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='recommendationMean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='sharesOutstanding',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='shortRatio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='targetMeanPrice',
            field=models.FloatField(blank=True, null=True),
        ),
    ]