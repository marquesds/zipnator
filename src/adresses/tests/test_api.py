from django.test import TestCase
from django.test import RequestFactory
from adresses.api import AddressResource


class AddressResourceServerTest(TestCase):
    fixtures = ['adresses_fixtures.json']

    def setUp(self):
        self.req_factory = RequestFactory()
        self.resource = AddressResource()

    def test_save_address(self):
        pass

    def test_save_address_with_invalid_zipcode(self):
        pass

    def test_save_address_with_nonexistent_zipcode(self):
        pass

    def test_save_existing_address(self):
        pass

    def test_delete_address(self):
        pass

    def test_delete_address_with_invalid_zipcode(self):
        pass

    def test_delete_nonexisting_address(self):
        pass

    def test_get_address_by_zipcode(self):
        pass

    def test_get_address_by_invalid_zipcode(self):
        pass

    def test_get_address_by_nonexistent_zipcode(self):
        pass

    def test_list_all_adresses(self):
        req = self.req_factory.get('/api/adresses/')
        self.resource.request = req
        results = self.resource.list()
        self.assertEqual(5, len(results))
