# Generated by Django 4.2.6 on 2024-05-31 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0014_user_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ideal_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
