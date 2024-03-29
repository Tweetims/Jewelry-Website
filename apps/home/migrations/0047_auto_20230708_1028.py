# Generated by Django 3.2.16 on 2023-07-08 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_alter_design_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='URL',
            field=models.URLField(default='', verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1e2217a3-5cb0-4dd4-985e-63137ad8b76b'), editable=False),
        ),
    ]
