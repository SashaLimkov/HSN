# Generated by Django 5.0.1 on 2024-01-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HSNData", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="research",
            name="organs",
            field=models.ManyToManyField(
                to="HSNData.organ", verbose_name="Список огранов"
            ),
        ),
    ]