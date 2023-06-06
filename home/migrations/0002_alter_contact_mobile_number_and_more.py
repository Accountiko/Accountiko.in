# Generated by Django 4.2.1 on 2023-05-31 04:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Mobile_number",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MaxValueValidator(9999999999)]
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="Whatsapp_number",
            field=models.PositiveBigIntegerField(),
        ),
    ]