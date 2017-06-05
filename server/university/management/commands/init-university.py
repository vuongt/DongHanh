import sys
import os
import json
import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from university.models import University

logger = logging.getLogger(__name__)

BASE_DIR = getattr(settings, 'BASE_DIR')

def _get_fixtures_path(filename):
    return os.path.join(BASE_DIR, 'fixtures', filename)

class Command(BaseCommand):
    def handle(self, *args, **options):
        admin = User.objects.first()
        path = _get_fixtures_path('university.json')
        with open(path) as infile:
            data = json.load(infile)
        if data:
            for u in data:
                if University.objects.filter(code=u['code']).count() > 0:
                    University.objects.filter(code=u['code']).update(name=u['name'])
                    logger.info("Updating University model to {}: {}".format(u['code'], u['name']))
                else:
                    University.objects.create(name=u['name'], code=u['code'], created_by=admin)
                    logger.info("Creating University model for {}: {}".format(u['code'], u['name']))