# Generated by Django 3.2.13 on 2022-09-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220911_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=2048, verbose_name='Course Description'),
        ),
    ]