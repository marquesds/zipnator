import logging
from django.conf import settings
from django.http import Http404
from adresses import InvalidZipcodeException
from adresses.models import Address
from adresses.helpers import validate_zipcode
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
import requests


logger = logging.getLogger('zipnator')


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
        validate_zipcode(self.data['zipcode'])
        zipcode_url = settings.ZIPCODE_PROVIDER + self.data['zipcode']
        resp = requests.get(zipcode_url)
        if resp.status_code == 404:
            msg = 'Zipcode not found'
            logger.error(msg)
            raise Http404(msg)
        else:
            results = resp.json()
        data = {
            'street': results.get('logradouro'),
            'district': results.get('bairro'),
            'city': results.get('cidade'),
            'state': results.get('estado'),
            'zipcode': results.get('cep')
        }
        return Address.objects.create(**data)

    def delete(self, pk):
        validate_zipcode(pk)
        pk = pk.replace('-', '')
        Address.objects.get(zipcode=pk).delete()

    def list(self):
        limit = self.request.GET.get('limit', None)
        limit = int(limit) if limit else limit
        return Address.objects.all()[:limit]

    def detail(self, pk):
        validate_zipcode(pk)
        pk = pk.replace('-', '')
        return Address.objects.get(zipcode=pk)
