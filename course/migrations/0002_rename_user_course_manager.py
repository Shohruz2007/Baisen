# Generated by Django 4.2.3 on 2023-07-16 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='user',
            new_name='manager',
        ),
    ]
