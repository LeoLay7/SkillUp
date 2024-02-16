# Generated by Django 5.0.2 on 2024-02-13 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tasks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="solution",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.subject"
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="test_images",
            field=models.ManyToManyField(
                to="tasks.images", verbose_name="фото заданий"
            ),
        ),
        migrations.AddField(
            model_name="solution",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.test"
            ),
        ),
        migrations.AddField(
            model_name="images",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tasks.test",
                verbose_name="Тест",
            ),
        ),
    ]
