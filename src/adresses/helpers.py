import re
from adresses import InvalidZipcodeException


def validate_zipcode(zipcode):
    pattern = re.compile(r'^\d{5}-?\d{3}')
    if not re.match(pattern, zipcode):
        raise InvalidZipcodeException('{} is invalid.'.format(zipcode))
