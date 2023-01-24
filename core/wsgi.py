# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='./static')
application.add_files("./static/assets/css")
application.add_files("./static/assets/fonts")
application.add_files("./static/assets/img")
application.add_files("./static/assets/js")
application.add_files("./static/assets/scss")



