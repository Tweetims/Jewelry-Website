# Generated by Django 3.2.16 on 2023-07-10 01:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20230709_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('dfdf18e8-1d31-4cda-a2f8-73b0d0c30b08'), editable=False),
        ),
    ]
