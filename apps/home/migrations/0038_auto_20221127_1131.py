# Generated by Django 3.2.13 on 2022-11-27 18:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20221122_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='designs',
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('47ef1c6c-e3ee-4829-a15a-aa43a9dc8e73'), editable=False),
        ),
    ]
