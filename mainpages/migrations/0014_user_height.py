# Generated by Django 4.2.6 on 2024-05-31 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0013_foods_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
