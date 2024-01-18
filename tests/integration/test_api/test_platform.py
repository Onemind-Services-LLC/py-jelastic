import os

import pytest

from jelastic import Jelastic

JELASTIC_URL = os.environ.get("JELASTIC_URL", "https://app.xapp.cloudmydc.com/")
JELASTIC_TOKEN = os.environ.get("JELASTIC_TOKEN")

if not JELASTIC_TOKEN:
    raise Exception("JELASTIC_TOKEN must be set as environment variables")


@pytest.fixture
def client():
    client = Jelastic(base_url=JELASTIC_URL, token=JELASTIC_TOKEN)
    return client.platform


def test_get(client):
    response = client.Engine.Get()
    assert isinstance(response, dict)
