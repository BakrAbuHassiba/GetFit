# Generated by Django 4.2.6 on 2024-06-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0026_alter_user_activity_alter_user_calories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
