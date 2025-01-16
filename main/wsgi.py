import os
from django.core.wsgi import get_wsgi_application

# Replace 'pythonProject' with your project's name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
