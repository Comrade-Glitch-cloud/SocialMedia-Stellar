from django.apps import AppConfig

class StarAccountsHubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'star_accounts_hub'

    def ready(self):
        import star_accounts_hub.signals
