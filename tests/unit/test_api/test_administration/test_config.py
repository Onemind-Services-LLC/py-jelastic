from . import *


def test_apply_config(client):
    client._get.return_value = success_response
    response = client.Config.ApplyConfig("type", "password")
    client._get.assert_called_with(
        "ApplyConfig",
        params={
            "type": "type",
            "password": "password",
        },
    )
    assert response == success_response


def test_apply_defaults(client):
    client._get.return_value = success_response
    response = client.Config.ApplyDefaults(
        "edition",
    )
    client._get.assert_called_with(
        "ApplyDefaults",
        params={
            "edition": "edition",
        },
    )
    assert response == success_response


def test_apply_reseller_config(client):
    client._get.return_value = success_response
    response = client.Config.ApplyResellerConfig("type", "password", "id_1")
    client._get.assert_called_with(
        "ApplyResellerConfig",
        params={
            "type": "type",
            "password": "password",
            "resellerId": "id_1",
        },
    )
    assert response == success_response


def test_change_config_key(client):
    client._get.return_value = success_response
    response = client.Config.ChangeConfigKey("type", "key", ["value1", "value2"])
    client._get.assert_called_with(
        "ChangeConfigKey",
        params={
            "type": "type",
            "key": "key",
            "value": ["value1", "value2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_change_properties_for_reseller(client):
    client._get.return_value = success_response
    response = client.Config.ChangePropertiesForReseller(
        "rid_1",
    )
    client._get.assert_called_with(
        "ChangePropertiesForReseller",
        params={
            "resellerId": "rid_1",
        },
    )
    assert response == success_response


def test_creating_config_type(client):
    client._get.return_value = success_response
    response = client.Config.CreatingConfigType(
        "type",
        "description",
    )
    client._get.assert_called_with(
        "CreatingConfigType",
        params={"type": "type", "description": "description"},
    )
    assert response == success_response


def test_creating_key_config(client):
    client._get.return_value = success_response
    response = client.Config.CreatingKeyConfig(
        "type", "key", "value", "default value", "expert", "description", "key type"
    )
    client._get.assert_called_with(
        "CreatingKeyConfig",
        params={
            "type": "type",
            "key": "key",
            "value": "value",
            "default_value": "default value",
            "expert": "expert",
            "description": "description",
            "keyType": "key type",
        },
    )
    assert response == success_response


def test_find_config_key(client):
    client._get.return_value = success_response
    response = client.Config.FindConfigKey(
        "value",
    )
    client._get.assert_called_with(
        "FindConfigKey",
        params={
            "value": "value",
        },
    )
    assert response == success_response


def test_get_all_config_type(client):
    client._get.return_value = success_response
    response = client.Config.GetAllConfigType(
        "expert",
    )
    client._get.assert_called_with(
        "GetAllConfigType",
        params={
            "expert": "expert",
        },
    )
    assert response == success_response


def test_get_all_key_config_by_type(client):
    client._get.return_value = success_response
    response = client.Config.GetAllKeyConfigByType("type", "expert")
    client._get.assert_called_with(
        "GetAllKeyConfigByType",
        params={
            "type": "type",
            "expert": "expert",
        },
    )
    assert response == success_response


def test_get_congif_key(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKey(
        "type",
        "key",
    )
    client._get.assert_called_with(
        "GetConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_get_config_key_by_seller_id(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKeyByResellerId(
        "type",
        "key",
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "GetConfigKeyByResellerId",
        params={
            "type": "type",
            "key": "key",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_config_keys(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKeys(
        ["type1", "type2", "type3"], ["key1", "key2", "key3"]
    )
    client._get.assert_called_with(
        "GetConfigKeys",
        params={
            "type": ["type1", "type2", "type3"],
            "key": ["key1", "key2", "key3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_config_key(client):
    client._get.return_value = success_response
    response = client.Config.RemoveConfigKey("type", "key")
    client._get.assert_called_with(
        "RemoveConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_remove_config_type(client):
    client._get.return_value = success_response
    response = client.Config.RemoveConfigType(
        "type",
    )
    client._get.assert_called_with(
        "RemoveConfigType",
        params={
            "type": "type",
        },
    )
    assert response == success_response


def test_remove_reseller_properties(client):
    client._get.return_value = success_response
    response = client.Config.RemoveResellerProperties(
        1,
    )
    client._get.assert_called_with(
        "RemoveResellerProperties",
        params={
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_revert_config_key(client):
    client._get.return_value = success_response
    response = client.Config.RevertConfigKey("type", "key")
    client._get.assert_called_with(
        "RevertConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_set_reseller_config_key(client):
    client._get.return_value = success_response
    response = client.Config.SetResellerConfigKey("type", "key", "value", 1)
    client._get.assert_called_with(
        "SetResellerConfigKey",
        params={
            "type": "type",
            "key": "key",
            "value": "value",
            "resellerId": 1,
        },
    )
    assert response == success_response
