# Generated by Django 4.2.6 on 2024-05-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0010_alter_foods_foodname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='FoodName',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images'),
        ),
    ]
