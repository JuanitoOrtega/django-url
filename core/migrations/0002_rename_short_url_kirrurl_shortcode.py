# Generated by Django 4.2.4 on 2023-08-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kirrurl',
            old_name='short_url',
            new_name='shortcode',
        ),
    ]
