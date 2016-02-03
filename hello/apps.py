from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'hello'

    def ready(self):
    	import hello.signals