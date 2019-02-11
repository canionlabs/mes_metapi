from django.db import models
from django.contrib.auth.models import User

from apps.common.models import DefaultModel


class Organization(DefaultModel):
    name = models.CharField(max_length=75)
    members = models.ManyToManyField(User, related_name='organizations')

    def __str__(self):
        return f'{self.name}'
