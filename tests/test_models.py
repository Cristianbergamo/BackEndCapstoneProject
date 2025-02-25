from django.test import TestCase
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
django.setup()

from restaurant.models import Menu


class TestMenu(TestCase):
    def test_instance(self):
        item = Menu.objects.create(Title="Prova", Price=10, Inventory=1)
        self.assertEqual(str(item), "Prova : 10")
