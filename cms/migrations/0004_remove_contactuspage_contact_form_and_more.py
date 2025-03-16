# Generated by Django 5.1.7 on 2025-03-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_alter_socialmedialink_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuspage',
            name='contact_form',
        ),
        migrations.RemoveField(
            model_name='contactuspage',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='contact_form',
            field=models.ManyToManyField(related_name='contact', to='cms.customcontactform'),
        ),
        migrations.AddField(
            model_name='contactuspage',
            name='contact_info',
            field=models.ManyToManyField(related_name='contact', to='cms.contact'),
        ),
    ]
