# Generated by Django 2.0.9 on 2018-12-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("games", "0010_gamesession_report_time")]

    operations = [
        migrations.AlterField(
            model_name="adventure",
            name="type",
            field=models.IntegerField(
                choices=[
                    (10, "AL"),
                    (1, "EN"),
                    (2, "EP"),
                    (3, "EX"),
                    (4, "HC"),
                    (5, "IA"),
                    (6, "LE"),
                    (7, "CCC"),
                    (8, "AO"),
                    (9, "Other"),
                ],
                default=3,
                verbose_name="Type",
            ),
        )
    ]