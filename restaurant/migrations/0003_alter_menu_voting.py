# Generated by Django 5.1.1 on 2024-09-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_rename_rating_menu_voting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="voting",
            field=models.IntegerField(default=0),
        ),
    ]
