# Generated by Django 4.2.6 on 2024-05-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0008_foods_carbs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='FoodName',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
