import django.db.models

import tasks.models
import users.models
import groups.tools


class Group(django.db.models.Model):
    creator = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        related_name="created_groups",
    )
    title = django.db.models.CharField(
        max_length=20,
        verbose_name="Название группы",
    )
    users = django.db.models.ManyToManyField(
        users.models.User,
        related_name="user_groups",
    )
    tests = django.db.models.ManyToManyField(
        tasks.models.Test,
    )
    solutions = django.db.models.FilePathField(
        path=groups.tools.group_solutions_path,
        verbose_name="Оценки учащихся",
    )
