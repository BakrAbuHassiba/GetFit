# Generated by Django 4.2.6 on 2024-06-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0028_alter_user_calories_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]