# Generated by Django 5.1.7 on 2025-03-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_alter_footer_location_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedialink',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/social/'),
        ),
    ]
