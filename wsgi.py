"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

python_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace("/app","")
sys.path.insert(0, python_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.pepperdine")

from helpers.utility import set_environment_var_from_file
set_environment_var_from_file('/var/www/dashboards/vars.env')

application = get_wsgi_application()

