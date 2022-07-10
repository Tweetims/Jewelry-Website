# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='./apps/static')
application.add_files("./apps/static/assets/css")
application.add_files("./apps/static/assets/fonts")
application.add_files("./apps/static/assets/img")
application.add_files("./apps/static/assets/js")
application.add_files("./apps/static/assets/scss")



