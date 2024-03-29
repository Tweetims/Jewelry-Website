# Generated by Django 3.2.13 on 2022-12-04 05:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_alter_design_uuid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MetalPriceConversion',
        ),
        migrations.RemoveField(
            model_name='design',
            name='metal_types',
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8d81b5bf-f6cc-4bbc-8a6e-454462803581'), editable=False),
        ),
        migrations.DeleteModel(
            name='WaxConversion',
        ),
    ]
