from django.contrib.auth import get_user_model

import pytest
from model_mommy import mommy


UserModel = get_user_model()


@pytest.fixture
def isolated_users():
    iso_users = mommy.make(UserModel, _quantity=3)
    return iso_users
