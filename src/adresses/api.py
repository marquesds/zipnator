import logging
from django.conf import settings
from adresses.models import Address
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
        try:
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
        except Exception as e:
            logger.error(e)

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
