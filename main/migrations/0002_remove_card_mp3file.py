# Generated by Django 5.1.3 on 2024-11-24 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='mp3file',
        ),
    ]