# Generated by Django 4.1.7 on 2023-04-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_activities_img_activities_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='city',
            new_name='destination',
        ),
    ]
