from django.apps import AppConfig
from sqlite3 import OperationalError


class HomeConfig(AppConfig):
    name = 'apps.home'

    def ready(self):
        # maybe try putting a sleep in an async process to delay the population of the table
        # or just make a button in the admin section that does this
        try:
            self.create_tag('Ring')
            self.create_tag('Earring')
            self.create_tag('Pendant')
            self.create_tag("Men's")
            self.create_tag("Women's")
            self.create_tag("White Gold")
            self.create_tag("Yellow Gold")
            self.create_tag("Silver")
            self.create_tag("Stones")

            from django.contrib.auth.models import Group
            Group.objects.get_or_create(name='customer')
        except Exception as e:
            pass

    @staticmethod
    def create_tag(name):
        from .models import Tag
        Tag.objects.get_or_create(name=name)
