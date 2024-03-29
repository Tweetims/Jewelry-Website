# Generated by Django 3.2.16 on 2023-07-29 04:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_alter_design_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesignup',
            name='purity',
            field=models.CharField(choices=[('925s', 'Sterling Silver'), ('10k', '10K Gold'), ('14k', '14K Gold'), ('18k', '18K Gold')], max_length=128, verbose_name='Purity'),
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6b1bad5c-ac32-45f2-b689-70a6eeb44512'), editable=False),
        ),
    ]
