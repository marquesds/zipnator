from django.test import TestCase
from adresses.models import Address


class AddressTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_address(self):
        data = {
            'street': 'Rua Maria José de Souza',
            'district': 'Jardim Souza',
            'city': 'São Paulo',
            'state': 'SP',
            'zipcode': '04917080'
        }
        self.assertTrue(Address.objects.create(**data))
