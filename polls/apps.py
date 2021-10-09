"""This is app files for configure."""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """This is class for configure the polls."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
