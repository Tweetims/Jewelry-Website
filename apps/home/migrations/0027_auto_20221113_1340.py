# Generated by Django 3.2.13 on 2022-11-13 20:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_design_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('305a93c7-fd93-44f2-8a52-c7a8762dc8c0'), editable=False),
        ),
        migrations.AlterField(
            model_name='design',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name='Wax Weight'),
        ),
    ]
