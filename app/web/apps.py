from django.apps import AppConfig

# Compare this snippet from web/apps.py:
class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    
