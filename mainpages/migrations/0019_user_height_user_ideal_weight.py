# Generated by Django 4.2.6 on 2024-06-02 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0018_foods_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ideal_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]