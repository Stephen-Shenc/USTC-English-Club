# Generated by Django 4.1 on 2024-05-09 13:27

from django.db import migrations, models
import django.utils.timezone


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
                ("name", models.CharField(max_length=64, verbose_name="name")),
                (
                    "sex",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="sex"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                ("password", models.CharField(max_length=64, verbose_name="password")),
                (
                    "birthdate",
                    models.DateField(blank=True, null=True, verbose_name="birthdate"),
                ),
                (
                    "register_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="register_date"
                    ),
                ),
            ],
        ),
    ]
