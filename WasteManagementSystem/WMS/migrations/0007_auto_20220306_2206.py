# Generated by Django 3.1 on 2022-03-06 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WMS', '0006_contact_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
