# Generated by Django 4.2.1 on 2023-06-01 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_contact_emial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="emial",
            new_name="email",
        ),
    ]
