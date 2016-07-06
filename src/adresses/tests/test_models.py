from django.test import TestCase
from django.db.utils import IntegrityError
from adresses.models import Address


class AddressTest(TestCase):
    def test_save_address(self):
        data = {
            'street': 'Rua Maria José de Souza',
            'district': 'Jardim Souza',
            'city': 'São Paulo',
            'state': 'SP',
            'zipcode': '04917080'
        }
        Address.objects.create(**data)
        adresses = Address.objects.all()
        self.assertTrue(len(adresses) > 0)

    def test_save_not_unique_zipcode(self):
        Address.objects.create(zipcode='04917080')
        with self.assertRaises(IntegrityError):
            Address.objects.create(zipcode='04917080')

    def test_address_str(self):
        address = Address.objects.create(zipcode='04917080')
        self.assertEqual(str(address), '04917080')
