# Generated by Django 5.0.4 on 2024-05-20 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="bed",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patients",
                to="main_app.bed",
            ),
        ),
    ]
