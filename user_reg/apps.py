from django.apps import AppConfig


class UserRegConfig(AppConfig):
    name = 'user_reg'

    def ready(self):
        import user_reg.signals
