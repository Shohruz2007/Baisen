# Generated by Django 4.2.3 on 2023-07-16 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_user_course_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='manager',
            new_name='user',
        ),
    ]
