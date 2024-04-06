from django.db import models

from hitstore1.utils.base import BaseModel


class Subscriber(BaseModel):
    email = models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email
    