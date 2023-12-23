from datetime import datetime
from unittest.mock import patch, Mock

import jelastic
import pytest
from jelastic.api import Data

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        data = Data(session=Mock(), token="token")
        data._get = mock_get
        yield data


def test_add_field(client):
    client._get.return_value = success_response
    response = client.Base.AddField(
        "type",
        "field",
        ["field_type1", "field_type2"],
    )
    client._get.assert_called_with(
        "AddField",
        params={
            "type": "type",
            "field": "field",
            "fieldType": ["field_type1", "field_type2"],
        },
    )

    assert response == success_response


def test_create_object(client):
    client._get.return_value = success_response
    response = client.Base.CreateObject("type", ["data1", "data2"])
    client._get.assert_called_with(
        "CreateObject",
        params={
            "type": "type",
            "data": ["data1", "data2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_create_objects(client):
    client._get.return_value = success_response
    response = client.Base.CreateObjects("type", "data")
    client._get.assert_called_with(
        "CreateObjects",
        params={"type": "type", "data": "data"},
        delimiter=",",
    )

    assert response == success_response


def test_define_type(client):
    client._get.return_value = success_response
    response = client.Base.DefineType(
        "type", ["fields1", "fields2"], ["unique1", "unique2"]
    )
    client._get.assert_called_with(
        "DefineType",
        params={
            "type": "type",
            "fields": ["fields1", "fields2"],
            "unique": ["unique1", "unique2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_define_type_by_uid(client):
    client._get.return_value = success_response
    response = client.Base.DefineTypeByUid(
        1, "type", ["fields1", "fields2"], ["unique1", "unique2"]
    )
    client._get.assert_called_with(
        "DefineTypeByUid",
        params={
            "uid": 1,
            "type": "type",
            "fields": ["fields1", "fields2"],
            "unique": ["unique1", "unique2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_delete_object(client):
    client._get.return_value = success_response
    response = client.Base.DeleteObject("type", 1)
    client._get.assert_called_with(
        "DeleteObject",
        params={"type": "type", "id": 1},
    )

    assert response == success_response


def test_delete_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.DeleteObjectsByCriteria("type", ["criteria1", "criteria2"])
    client._get.assert_called_with(
        "DeleteObjectsByCriteria",
        params={
            "type": "type",
            "criteria": ["criteria1", "criteria2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_not_empty_type(client):
    client._get.return_value = success_response
    response = client.Base.GetNotEmptyType("type_like", ["asc1", "asc2"])
    client._get.assert_called_with(
        "GetNotEmptyType",
        params={
            "typeLike": "type_like",
            "asc": ["asc1", "asc2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_object(client):
    client._get.return_value = success_response
    response = client.Base.GetObject("type", 1, ["join1", "join2"])
    client._get.assert_called_with(
        "GetObject",
        params={"type": "type", "id": 1, "join": ["join1", "join2"]},
        delimiter=",",
    )

    assert response == success_response


def test_get_objects(client):
    client._get.return_value = success_response
    response = client.Base.GetObjects("type", [1, 1], [1, 1], ["join1", "join2"])
    client._get.assert_called_with(
        "GetObjects",
        params={
            "type": "type",
            "froms": [1, 1],
            "count": [1, 1],
            "join": ["join1", "join2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByCriteria(
        "type",
        ["criteria1", "criteria2"],
        [1, 1],
        [1, 1],
        ["join1", "join2"],
        ["projection1", "projection2"],
    )
    client._get.assert_called_with(
        "GetObjectsByCriteria",
        params={
            "type": "type",
            "criteria": ["criteria1", "criteria2"],
            "froms": [1, 1],
            "count": [1, 1],
            "join": ["join1", "join2"],
            "projection": ["projection1", "projection2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_objects_by_role(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByRole(
        "type",
        "role",
        ["criteria1", "criteria2"],
        [1, 1],
        [1, 1],
        ["join1", "join2"],
        ["projection1", "projection2"],
    )
    client._get.assert_called_with(
        "GetObjectsByRole",
        params={
            "type": "type",
            "role": "role",
            "criteria": ["criteria1", "criteria2"],
            "froms": [1, 1],
            "count": [1, 1],
            "join": ["join1", "join2"],
            "projection": ["projection1", "projection2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_objects_count(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsCount("type", ["criteria1", "criteria2"])
    client._get.assert_called_with(
        "GetObjectsCount",
        params={
            "type": "type",
            "criteria": ["criteria1", "criteria2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_property(client):
    client._get.return_value = success_response
    response = client.Base.GetProperty("type", 1, "property", ["join1", "join2"])
    client._get.assert_called_with(
        "GetProperty",
        params={
            "type": "type",
            "id": 1,
            "property": "property",
            "join": ["join1", "join2"],
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_type(client):
    client._get.return_value = success_response
    response = client.Base.GetType("type")
    client._get.assert_called_with(
        "GetType",
        params={
            "type": "type",
        },
    )

    assert response == success_response


def test_get_types(client):
    client._get.return_value = success_response
    response = client.Base.GetTypes([1, 1], [1, 1])
    client._get.assert_called_with(
        "GetTypes",
        params={
            "froms": [1, 1],
            "count": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_type_count(client):
    client._get.return_value = success_response
    response = client.Base.GetTypesCount()
    client._get.assert_called_with("GetTypesCount", params={})

    assert response == success_response


def test_get_unique_fields(client):
    client._get.return_value = success_response
    response = client.Base.GetUniqueFields("type")
    client._get.assert_called_with(
        "GetUniqueFields",
        params={
            "type": "type",
        },
    )

    assert response == success_response


def test_remove_field(client):
    client._get.return_value = success_response
    response = client.Base.RemoveField("type", "field")
    client._get.assert_called_with(
        "RemoveField", params={"type": "type", "field": "field"}
    )

    assert response == success_response


def test_rename_field(client):
    client._get.return_value = success_response
    response = client.Base.RenameField("type", "old_field", "new_field")
    client._get.assert_called_with(
        "RenameField",
        params={"type": "type", "oldField": "old_field", "newField": "new_field"},
    )

    assert response == success_response


def test_rename_type(client):
    client._get.return_value = success_response
    response = client.Base.RenameType("type", "old_type", "new_type")
    client._get.assert_called_with(
        "RenameType",
        params={"type": "type", "oldType": "old_type", "newTyoe": "new_type"},
    )

    assert response == success_response


def test_set_object(client):
    client._get.return_value = success_response
    response = client.Base.SetObject("type", 1, "data")
    client._get.assert_called_with(
        "SetObject", params={"type": "type", "id": 1, "data": "data"}
    )

    assert response == success_response


def test_set_objects(client):
    client._get.return_value = success_response
    response = client.Base.SetObjects("type", "data")
    client._get.assert_called_with(
        "SetObjects", params={"type": "type", "data": "data"}
    )

    assert response == success_response


def test_set_property(client):
    client._get.return_value = success_response
    response = client.Base.SetProperty("type", 1, "property", ["value1", "value2"])
    client._get.assert_called_with(
        "SetProperty",
        params={
            "type": "type",
            "id": 1,
            "property": "property",
            "value": ["value1", "value2"],
        },
    )

    assert response == success_response


def test_set_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.SetObjectsByCriteria(
        "type",
        "property",
        ["criteria1", "criteria2"],
        [1, 1],
        [1, 1],
        ["join1", "join2"],
        ["projection1", "projection2"],
    )
    client._get.assert_called_with(
        "SetObjectsByCriteria",
        params={
            "type": "type",
            "property": "property",
            "criteria": ["criteria1", "criteria2"],
            "froms": [1, 1],
            "count": [1, 1],
            "join": ["join1", "join2"],
            "projection": ["projection1", "projection2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_unique_fields(client):
    client._get.return_value = success_response
    response = client.Base.SetUniqueFields("type", ["unique1", "unique2"])
    client._get.assert_called_with(
        "SetUniqueFields",
        params={"type": "type", "unique": ["unique1", "unique2"]},
        delimiter=",",
    )

    assert response == success_response


def test_undefine_type(client):
    client._get.return_value = success_response
    response = client.Base.UndefineType("type")
    client._get.assert_called_with(
        "UndefineType",
        params={
            "type": "type",
        },
    )

    assert response == success_response
    assert response == success_response
