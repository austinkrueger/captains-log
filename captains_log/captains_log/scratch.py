import os
import sys

# needed for Sublime Text 3
# sys.path.append('PATHTOPROJECT/captains_log')
# set the Django settings module before initializing Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "captains_log.settings"
)
import django

django.setup()
