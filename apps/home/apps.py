from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'apps.home'

    def ready(self):
        from django.contrib.auth.models import Group

        Group.objects.get_or_create(name='customer')

        self.create_tag('Ring')
        self.create_tag('Earring')
        self.create_tag('Pendant')
        self.create_tag("Men's")
        self.create_tag("Women's")
        self.create_tag("White Gold")
        self.create_tag("Yellow Gold")
        self.create_tag("Silver")
        self.create_tag("Stones")

    @staticmethod
    def create_tag(name):
        from .models import Tag
        Tag.objects.get_or_create(name=name)
