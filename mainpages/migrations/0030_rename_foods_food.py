# Generated by Django 4.2.6 on 2024-06-06 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpages', '0029_alter_user_activity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foods',
            new_name='Food',
        ),
    ]