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
    return client.pricing


def test_option_get(client):
    response = client.Option.Get()
    assert isinstance(response, dict)


def test_tariff_get_grids(client):
    response = client.Tariff.GetGrids()
    assert isinstance(response, dict)
