# Generated by Django 3.2.13 on 2022-06-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_event_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default='12:00', verbose_name='Event Time'),
        ),
    ]