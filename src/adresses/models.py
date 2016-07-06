import re
from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    street = models.CharField('Street', max_length=300)
    district = models.CharField('District', max_length=200)
    city = models.CharField('City', max_length=200)
    state = models.CharField('State', max_length=2)
    zipcode = models.CharField(
        'Zipcode',
        max_length=9,
        unique=True,
        validators=[RegexValidator(regex=re.compile(r'^\d{8}'), message='Invalid zipcode')]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.zipcode

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Adresses'
