# Generated by Django 4.1 on 2022-08-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=10)),
                ("last_name", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                (
                    "favorite_season",
                    models.CharField(
                        choices=[
                            ("Verão", "Summer"),
                            ("Outono", "Autumn"),
                            ("Inverno", "Winter"),
                            ("Primavera", "Spring"),
                            ("Não especificado", "Default"),
                        ],
                        default="Não especificado",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
