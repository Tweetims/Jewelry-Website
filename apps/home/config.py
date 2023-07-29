# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.apps import AppConfig


class MyConfig(AppConfig):
    name = 'apps.home'
    label = 'apps_home'

    METAL_PRICES = {
        '10k': 55.43,
        '14k': 75.62,
        '18k': 95.11,
    }

    MELEE_PRICES = {
        'natural': 1800.00,
        'lab': 600.00,
    }
