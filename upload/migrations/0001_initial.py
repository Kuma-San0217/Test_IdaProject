# Generated by Django 2.1 on 2018-08-10 12:34

import django.core.validators
from django.db import migrations, models
import upload.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(blank=True, upload_to=upload.helpers.RandomFileName('raw_images'), validators=[django.core.validators.validate_image_file_extension])),
                ('image_url', models.URLField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]