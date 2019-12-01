import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lufeiapi.settings.dev")

django.setup()

from django.conf import settings
print(settings)

from utils.logging import logger
logger.info('info')
