# Generated by Django 5.0.4 on 2024-05-20 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_alter_patient_bed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="patient",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="main_app.patient",
            ),
        ),
    ]