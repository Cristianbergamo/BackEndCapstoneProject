from django.test import TestCase
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")
django.setup()

from restaurant.serializers import menuSerializer


from restaurant.models import Menu


class TestMenu(TestCase):

    def setUp(self):
        Menu.objects.create(Title="Prova1", Price=10, Inventory=1)
        Menu.objects.create(Title="Prova2", Price=20, Inventory=1)
        Menu.objects.create(Title="Prova3", Price=30, Inventory=1)
        return

    def test_create_instance(self):
        item = Menu.objects.create(Title="Prova", Price=10, Inventory=1)
        self.assertEqual(str(item), "Prova : 10")

    def test_getall(self):
        # Recupera tutti gli oggetti e ordina per id per avere un ordine deterministico
        all_items = Menu.objects.all().order_by("id")
        serialized_items = menuSerializer(all_items, many=True)

        # Costruisci il risultato atteso in base agli oggetti presenti nel database
        expected_data = []
        for item in all_items:
            expected_data.append(
                {
                    "id": item.id,
                    "Title": item.Title,
                    # Se il campo Price è un Decimal, formatta a 2 decimali
                    "Price": "{:.2f}".format(item.Price),
                    "Inventory": item.Inventory,
                }
            )

        self.assertEqual(serialized_items.data, expected_data)
