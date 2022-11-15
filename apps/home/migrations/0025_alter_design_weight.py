# Generated by Django 3.2.13 on 2022-11-12 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_design_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=2, verbose_name='Wax Weight'),
        ),
    ]
