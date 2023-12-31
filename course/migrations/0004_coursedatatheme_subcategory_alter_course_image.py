# Generated by Django 4.2.3 on 2023-07-17 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_manager_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedatatheme',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.coursedatasubcategory'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Courses/main'),
        ),
    ]
