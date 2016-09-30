from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'personal_app'

    def ready(self):
        import personal_app.signals # NoQA
