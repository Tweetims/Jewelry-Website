# Generated by Django 3.2.16 on 2023-07-09 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_alter_design_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('64ae4c19-2810-461e-9e3a-04e13d56333f'), editable=False),
        ),
    ]
