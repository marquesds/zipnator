import re
from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    street = models.CharField('Street', max_length=300, blank=False, null=False)
    district = models.CharField('District', max_length=200, blank=False, null=False)
    city = models.CharField('City', max_length=200, blank=False, null=False)
    state = models.CharField('State', max_length=2, blank=False, null=False)
    zipcode = models.CharField(
        'Zipcode',
        max_length=9,
        blank=False,
        null=False,
        unique=True,
        validators=[RegexValidator(regex=re.compile('^\d{8}'), message='Invalid zipcode')]
    )

    def __str__(self):
        return self.zipcode

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Adresses'
