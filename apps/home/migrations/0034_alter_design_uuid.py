# Generated by Django 3.2.13 on 2022-11-15 02:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_design_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('987e13f4-2e7a-4846-8eaa-a6af19811e5c'), editable=False),
        ),
    ]