from django.conf import settings
from adresses.models import Address
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
import requests


class AddressResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'street': 'street',
        'district': 'district',
        'city': 'city',
        'state': 'state',
        'zipcode': 'zipcode',
    })

    def is_authenticated(self):
        return True

    def create(self):
        zipcode_url = settings.ZIPCODE_PROVIDER + self.data['zipcode']
        results = requests.get(zipcode_url).json()
        data = {
            'street': results.get('logradouro'),
            'district': results.get('bairro'),
            'city': results.get('cidade'),
            'state': results.get('estado'),
            'zipcode': results.get('cep')
        }
        return Address.objects.create(**data)

    def list(self):
        return Address.objects.all()

    def detail(self, pk):
        return Address.objects.get(zipcode=pk)
