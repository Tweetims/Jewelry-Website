# Generated by Django 3.2.13 on 2022-11-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_design_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='stones',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Number of Stones'),
        ),
    ]
