import django.db.models
import django.contrib.auth.models
import django.conf

import users.validators


class User(django.contrib.auth.models.AbstractUser):
    first_name = django.db.models.CharField(
        max_length=20,
        verbose_name="имя",
    )
    last_name = django.db.models.CharField(
        max_length=30,
        verbose_name="фамилия",
    )
    patronomyc = django.db.models.CharField(
        max_length=20,
        verbose_name="отчество",
    )
    role = django.db.models.CharField(
        max_length=20,
        choices=[
            ("Ученик", "Ученик"),
            ("Учитель", "Учитель"),
            ("Учитель платформы", "Учитель платформы"),
            ("Администратор", "Администратор"),
        ],
        verbose_name="Статус",
    )
    grade = django.db.models.CharField(
        max_length=3,
        validators=[
            users.validators.school_class_validator,
            ],
    )
