# Generated by Django 5.1.1 on 2024-09-28 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("western_cuisine", models.JSONField(default=dict)),
                ("arab_cuisine", models.JSONField(default=dict)),
                ("vegetarian_cuisine", models.JSONField(default=dict)),
                ("date", models.DateField()),
                ("rating", models.FloatField(default=0)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.restaurant",
                    ),
                ),
            ],
            options={
                "ordering": ("date",),
            },
        ),
    ]
