# Generated by Django 4.1.7 on 2023-04-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='notes',
            field=models.TextField(default='No notes', max_length=250),
        ),
        migrations.AddField(
            model_name='destination',
            name='notes',
            field=models.TextField(default='No notes', max_length=250),
        ),
    ]
