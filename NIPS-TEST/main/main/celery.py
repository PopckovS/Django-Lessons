import os

from celery import Celery

# Запуск сервера:  ./manage.py runserver
# Flower:          celery -A main flower --address = 127.0.0.1 --port = 5566
# Celery:          celery -A main worker -l info
# Celery beat:     celery - A main beat


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# ля временных задач
app.conf.beat_schedule = {
    'create_new_object': {
        'task': 'app.tasks.create_new_object',
        'schedule': 15.0,
    }
}


