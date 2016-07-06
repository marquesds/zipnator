import re
import logging
from adresses import InvalidZipcodeException


logger = logging.getLogger('zipnator')


def validate_zipcode(zipcode):
    pattern = re.compile(r'^\d{5}-?\d{3}')
    if not re.match(pattern, zipcode):
        message = '{} is invalid.'.format(zipcode)
        logger.error(message)
        raise InvalidZipcodeException('{} is invalid.'.format(zipcode))
    else:
        return zipcode
