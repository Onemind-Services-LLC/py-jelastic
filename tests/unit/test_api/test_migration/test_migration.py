from . import *


def test_get_migration_operations(client):
    client._get.return_value = success_response
    response = client.Migration.GetMigrationOperations(
        "docker",
        "ruk"
    )
    client._get.assert_called_with(
        "GetMigrationOperations", params={"search": "docker", "ruk":"ruk"}
    )
    assert response == success_response


def test_migrate(client):
    client._get.return_value = success_response
    response = client.Migration.Migrate("ruk")
    client._get.assert_called_with("Migrate", params={"ruk":"ruk"})
    assert response == success_response
