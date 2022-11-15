from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'apps.home'

    def ready(self):
        from django.contrib.auth.models import Group
        from .models import WaxConversion
        Group.objects.get_or_create(name='customer')
        WaxConversion.objects.get_or_create(id='silver', value=10.36)
        WaxConversion.objects.get_or_create(id='y10', value=11.60)
        WaxConversion.objects.get_or_create(id='y14', value=13.08)
        WaxConversion.objects.get_or_create(id='y18', value=15.60)
        WaxConversion.objects.get_or_create(id='w10', value=11.20)
        WaxConversion.objects.get_or_create(id='w14', value=12.65)
        WaxConversion.objects.get_or_create(id='w18', value=14.65)
        WaxConversion.objects.get_or_create(id='pt950', value=21.45)
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
