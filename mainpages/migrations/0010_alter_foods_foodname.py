# Generated by Django 4.2.6 on 2024-05-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0009_alter_foods_foodname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='FoodName',
            field=models.CharField(max_length=200),
        ),
    ]
