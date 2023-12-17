from unittest.mock import patch, Mock

import pytest

from jelastic.api import Migration

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        migration = Migration(session=Mock(), token="token")
        migration._get = mock_get
        yield migration


def test_get_migration_operations(client):
    client._get.return_value = success_response
    response = client.Migration.GetMigrationOperations(
        'docker',
    )
    client._get.assert_called_with(
        'GetMigrationOperations',
        params={
            'search': 'docker'
        }
    )
    assert response == success_response


def test_migrate(client):
    client._get.return_value = success_response
    response = client.Migration.Migrate()
    client._get.assert_called_with(
        'Migrate'
    )
    assert response == success_response
