# Generated by Django 4.2.1 on 2023-05-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_pages_definition_alter_pages_how_to_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
