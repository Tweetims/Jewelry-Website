# Generated by Django 3.2.13 on 2022-12-04 04:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_design_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetalPriceConversion',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name='Price per gram')),
            ],
        ),
        migrations.AlterField(
            model_name='coursesignup',
            name='metal_type',
            field=models.CharField(choices=[('silver', 'Silver'), ('y10', '10K Yellow Gold'), ('y14', '14K Yellow Gold'), ('y18', '18K Yellow Gold'), ('w10', '10K White Gold'), ('w14', '14K White Gold'), ('w18', '18K White Gold')], max_length=256, verbose_name='Metal Type'),
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d1fb6dd1-bca5-4791-b86e-bfbabaac7fc0'), editable=False),
        ),
    ]
