import django.db.models
import django.conf

import users.models
import tasks.tools


class Subject(django.db.models.Model):
    title = django.db.models.CharField(
        max_length=40,
        verbose_name="название предмета"
    )


class Test(django.db.models.Model):
    creator = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
    )
    subject = django.db.models.ForeignKey(
        Subject,
        on_delete=django.db.models.CASCADE,
    )
    time = django.db.models.TimeField(
        verbose_name="время на прохождение теста",
    )
    tasks = django.db.models.FilePathField(
        path=tasks.tools.test_tasks_path,
        verbose_name="информация о заданиях",
    )
    many_solutions = django.db.models.BooleanField(
        default=False,
        verbose_name="можно ли пройти тест несколько раз?"
    )


class Solution(django.db.models.Model):
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
    )
    test = django.db.models.ForeignKey(
        Test,
        on_delete=django.db.models.CASCADE,
    )
    info = django.db.models.FilePathField(
        path=tasks.tools.solution_info_path,
        verbose_name="информация о решении",
    )


class Images(django.db.models.Model):
    test = django.db.models.ForeignKey(
        Test,
        on_delete=django.db.models.CASCADE,
        verbose_name="Тест",
        related_name="images",
        blank=True,
        null=True
    )
    task = django.db.models.SmallIntegerField(
        verbose_name="номер задания",
    )
    variant = django.db.models.SmallIntegerField(
        verbose_name="вариант задания",
    )
    image = django.db.models.ImageField(
        upload_to="test_images",
        verbose_name="фото",
    )
