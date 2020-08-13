from django.apps import AppConfig
from django.conf import settings
import os


class CommunityConfig(AppConfig):
    name = 'community'

    def ready(self):
        print('ready 실행!')
        from community import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
