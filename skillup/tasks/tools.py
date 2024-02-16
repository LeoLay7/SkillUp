import django.conf


def solution_info_path():
    return django.conf.settings.LOCAL_FILES_DIR / "solutions"


def test_tasks_path():
    return django.conf.settings.LOCAL_FILES_DIR / "tasks"
