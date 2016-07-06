from django.test import TestCase
from django.test import RequestFactory
from django.http import Http404
from django.db.utils import IntegrityError
from adresses.api import AddressResource
from adresses.models import Address
from adresses import InvalidZipcodeException


class AddressResourceServerTest(TestCase):
    fixtures = ['adresses_fixtures.json']

    def setUp(self):
        self.req_factory = RequestFactory()
        self.resource = AddressResource()

    def test_save_address(self):
        data = {'zipcode': '04917080'}
        req = self.req_factory.post('/api/adresses/', data)
        self.resource.request = req
        self.resource.data = data
        address = self.resource.create()
        self.assertEqual(Address.objects.get(zipcode='04917080'), address)

    def test_save_address_with_invalid_zipcode(self):
        with self.assertRaises(InvalidZipcodeException):
            data = {'zipcode': '04917-80'}
            req = self.req_factory.post('/api/adresses/', data)
            self.resource.request = req
            self.resource.data = data
            self.resource.create()

        with self.assertRaises(InvalidZipcodeException):
            data = {'zipcode': '0491-080'}
            req = self.req_factory.post('/api/adresses/', data)
            self.resource.request = req
            self.resource.data = data
            self.resource.create()

        with self.assertRaises(InvalidZipcodeException):
            data = {'zipcode': '0491780'}
            req = self.req_factory.post('/api/adresses/', data)
            self.resource.request = req
            self.resource.data = data
            self.resource.create()

    def test_save_address_with_nonexistent_zipcode(self):
        with self.assertRaises(Http404):
            data = {'zipcode': '00000000'}
            req = self.req_factory.post('/api/adresses/', data)
            self.resource.request = req
            self.resource.data = data
            self.resource.create()

    def test_save_existing_address(self):
        with self.assertRaises(IntegrityError):
            data = {'zipcode': '04917080'}
            req = self.req_factory.post('/api/adresses/', data)
            self.resource.request = req
            self.resource.data = data
            self.resource.create()
            self.resource.create()

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

    def test_list_all_adresses_with_limit(self):
        req = self.req_factory.get('/api/adresses/?limit=2')
        self.resource.request = req
        results = self.resource.list()
        self.assertEqual(2, len(results))


class APIClientTest(TestCase):
    fixtures = ['adresses_fixtures.json']

    def setUp(self):
        pass

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
        pass

    def test_list_all_adresses_with_limit(self):
        pass
