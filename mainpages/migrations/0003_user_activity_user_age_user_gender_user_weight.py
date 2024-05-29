# Generated by Django 4.2.6 on 2024-05-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activity',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
