import django.db.models

import users.models


class FeedbackReason(django.db.models.Model):
    title = django.db.models.CharField(
        max_length=40, verbose_name="причина отзыва"
    )


class Feedback(django.db.models.Model):
    user = django.db.models.ForeignKey(
        users.models.User, on_delete=django.db.models.CASCADE
    )
    reason = django.db.models.ForeignKey(
        FeedbackReason,
        on_delete=django.db.models.CASCADE,
    )
    text = django.db.models.TextField(
        verbose_name="текст обращения",
    )
    email = django.db.models.EmailField(
        verbose_name="почта",
    )
    status = django.db.models.CharField(
        choices=[("На проверке", "На проверке"), ("Проверено", "Проверено")],
        max_length=20,
        default="На проверке",
        verbose_name="статус",
    )


class FeedbackStatusLog(django.db.models.Model):
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
    )
    from_status = django.db.models.CharField(
        max_length=20,
    )
    to_status = django.db.models.CharField(
        max_length=20,
    )
    time = django.db.models.DateTimeField(
        auto_now_add=True, verbose_name="дата создание"
    )
