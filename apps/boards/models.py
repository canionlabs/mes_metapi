from django.db import models

from apps.organizations.models import Organization

import jwt


class Board(models.Model):
    organization = models.ForeignKey(
        Organization, related_name="boards",
        on_delete=models.SET_NULL, null=True, blank=True)
    key = models.CharField(max_length=275)
    board_number = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return f'[{self.id}] {self.key}'

    @property
    def address(self):
        payload = {
            "resource": {"dashboard": self.board_number},
            "params": {}
        }
        token = jwt.encode(payload, self.key, algorithm="HS256")
        return self.url + "/embed/dashboard/" + token.decode("utf8") + "#bordered=true&titled=true"
