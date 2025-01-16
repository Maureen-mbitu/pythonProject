from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Main Application'

    def ready(self):
        # This method is called when the application is ready.
        # You can put initialization code here.
        import main.signals  # Import signals if you have any