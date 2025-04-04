# Generated by Django 5.1.7 on 2025-03-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_moderator",
            field=models.BooleanField(
                default=False,
                help_text="Пользователь является модератором",
                verbose_name="Модератор",
            ),
        ),
    ]
