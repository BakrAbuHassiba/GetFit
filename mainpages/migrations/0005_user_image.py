# Generated by Django 5.0.3 on 2024-05-29 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0004_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]