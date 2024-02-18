import django.conf


def group_solutions_path():
    return django.conf.settings.LOCAL_FILES_DIR / "group_marks"
