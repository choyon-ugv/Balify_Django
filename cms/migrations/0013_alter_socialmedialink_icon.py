# Generated by Django 5.1.7 on 2025-03-16 07:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_landingpage_card_landingpage_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialink',
            name='icon',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='icon'),
        ),
    ]
