# Generated by Django 3.2.16 on 2023-07-08 16:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20230708_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='URL',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='design',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9fad0244-11de-47f6-8cab-6b6ea2639ed3'), editable=False),
        ),
    ]
