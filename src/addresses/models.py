from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    street = models.CharField(max_length=300, blank=False, null=False)
    district = models.CharField(max_length=200, blank=False, null=False)
    city = models.CharField(max_length=200, blank=False, null=False)
    state = models.CharField(max_length=200, blank=False, null=False)
    zipcode = models.CharField(
        max_length=9,
        blank=False,
        null=False,
        validators=[RegexValidator(regex='^[0-9]{5}-?[0-9]{3}', message='Invalid zipcode'),]
    )
