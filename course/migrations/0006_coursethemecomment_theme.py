# Generated by Django 4.2.3 on 2023-07-17 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_registercourseuser_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursethemecomment',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.coursedatatheme'),
            preserve_default=False,
        ),
    ]
