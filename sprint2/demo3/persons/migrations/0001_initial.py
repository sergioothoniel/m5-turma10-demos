# Generated by Django 4.1 on 2022-08-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("birthdate", models.DateField(blank=True, null=True)),
                ("married", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "account_balance",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
