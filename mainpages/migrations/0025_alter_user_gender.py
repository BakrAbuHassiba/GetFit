# Generated by Django 4.2.6 on 2024-06-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0024_alter_foods_linkdrive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, default='...', max_length=6, null=True),
        ),
    ]
