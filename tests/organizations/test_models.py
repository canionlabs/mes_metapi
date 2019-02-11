from django.utils import timezone
from django.contrib.auth.models import User

from apps.organizations.models import Organization

import pytest
import uuid
from datetime import timedelta


ORG_NAME = str(uuid.uuid4().hex)


@pytest.mark.django_db
def test_organization_creation():
    org = Organization(name=ORG_NAME)
    org.save()

    assert org.name == ORG_NAME
    assert (
        org.created_at <= timezone.now() and
        org.created_at >= timezone.now() - timedelta(seconds=5)
    )


@pytest.mark.django_db
def test_organization_creation_with_related_user(isolated_users):
    org = Organization(name=ORG_NAME)
    org.save()

    user = User.objects.order_by('?').first()
    org.members.add(user)

    assert org.members.filter(id=user.id).exists()
    assert org.members.get(id=user.id) == user
