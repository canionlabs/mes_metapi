from apps.boards.models import Board
from apps.organizations.models import Organization

import jwt
import pytest

import uuid
import random
from string import Template


ORG_NAME = str(uuid.uuid4().hex)
BOARD_KEY = str(uuid.uuid4().hex)
BOARD_NUMBER = random.randint(1, 100)
URL = '127.0.0.1:3000'

ADDRESS_TEMPLATE = Template("$url/embed/dashboard/$token#bordered=true&titled=true")


@pytest.mark.django_db
def test_create_board_model():
    org = Organization.objects.create(name=ORG_NAME)
    board = Board.objects.create(
        url=URL, key=BOARD_KEY, organization=org, board_number=BOARD_NUMBER)

    assert board.key == BOARD_KEY
    assert board.organization == org
    assert board.url == URL

    payload = {
        "resource": {"dashboard": board.board_number},
        "params": {}
    }
    token = jwt.encode(payload, board.key, algorithm="HS256")
    assert board.address == ADDRESS_TEMPLATE.substitute(
        url=board.url, token=token.decode("utf8"))


@pytest.mark.django_db
def test_delete_organization_from_board():
    org = Organization.objects.create(name=ORG_NAME)
    board = Board.objects.create(
        url=URL, key=BOARD_KEY, organization=org, board_number=BOARD_NUMBER)

    org.delete()
    board_id = board.id
    board = Board.objects.get(id=board_id)

    assert board.organization is None
