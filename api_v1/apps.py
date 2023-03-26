from django.apps import AppConfig
from django.db.models import BigAutoField


class ApiV1Config(AppConfig):
    default_auto_field = BigAutoField

    name = 'api_v1'

    def ready(self):
        import api_v1.signals
