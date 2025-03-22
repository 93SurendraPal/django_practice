import os
from celery import Celery

# Set default settings for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')

# Create Celery instance
app = Celery('practice')

# Load configuration from Django settings, using CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in installed apps
app.autodiscover_tasks()
