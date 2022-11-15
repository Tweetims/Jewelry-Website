# Generated by Django 3.2.13 on 2022-09-28 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteuser',
            name='account',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]