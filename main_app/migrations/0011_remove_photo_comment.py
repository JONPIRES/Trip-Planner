# Generated by Django 4.1.7 on 2023-04-07 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_activities_notes_alter_destination_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='comment',
        ),
    ]
