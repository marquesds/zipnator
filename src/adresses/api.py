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
        try:
            Address.objects.get(zipcode=pk).delete()
        except Exception as e:
            logger.error(e)

    def list(self):
        limit = self.request.GET.get('limit', None)
        limit = int(limit) if limit else limit
        try:
            return Address.objects.all()[:limit]
        except Exception as e:
            logger.error(e)

    def detail(self, pk):
        try:
            return Address.objects.get(zipcode=pk)
        except Exception as e:
            logger.error(e)
