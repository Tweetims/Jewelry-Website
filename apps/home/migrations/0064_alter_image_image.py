# Generated by Django 3.2.16 on 2023-08-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_auto_20230802_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='no_image.jpg', null=True, upload_to='', verbose_name='Design Image'),
        ),
    ]
