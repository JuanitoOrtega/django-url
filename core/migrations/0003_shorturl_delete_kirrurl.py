# Generated by Django 4.2.4 on 2023-08-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_short_url_kirrurl_shortcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, verbose_name='URL')),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True, verbose_name='Shortcode')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
        migrations.DeleteModel(
            name='KirrURL',
        ),
    ]