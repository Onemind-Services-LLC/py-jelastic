import os

import pytest

from jelastic import Jelastic

JELASTIC_URL = os.environ.get("JELASTIC_URL", "https://jca.xapp.cloudmydc.com/")
JELASTIC_TOKEN = os.environ.get("JELASTIC_TOKEN")

if not JELASTIC_TOKEN:
    raise Exception("JELASTIC_TOKEN must be set as environment variables")


@pytest.fixture
def client():
    client = Jelastic(base_url=JELASTIC_URL, token=JELASTIC_TOKEN)
    return client.utils


def test_get_tasks(client):
    response = client.Scheduler.GetTasks()
    assert isinstance(response, dict)
