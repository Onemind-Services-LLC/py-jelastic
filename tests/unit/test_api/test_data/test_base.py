from . import *


def test_add_field(client):
    client._get.return_value = success_response
    response = client.Base.AddField("type", "field", "fieldType")
    client._get.assert_called_with(
        "AddField",
        params={"type": "type", "field": "field", "fieldType": "fieldType"},
    )

    assert response == success_response


def test_create_object(client):
    client._get.return_value = success_response
    response = client.Base.CreateObject("type", "data")
    client._get.assert_called_with(
        "CreateObject", params={"type": "type", "data": "data"}
    )

    assert response == success_response


def test_create_objects(client):
    client._get.return_value = success_response
    response = client.Base.CreateObjects("type", "data")
    client._get.assert_called_with(
        "CreateObjects", params={"type": "type", "data": "data"}
    )

    assert response == success_response


def test_define_type(client):
    client._get.return_value = success_response
    response = client.Base.DefineType("type", "fields", "unique")
    client._get.assert_called_with(
        "DefineType", params={"type": "type", "fields": "fields", "unique": "unique"}
    )

    assert response == success_response


def test_define_type_by_uid(client):
    client._get.return_value = success_response
    response = client.Base.DefineTypeByUid(1, "type", "fields", "unique")
    client._get.assert_called_with(
        "DefineTypeByUid",
        params={"uid": 1, "type": "type", "fields": "fields", "unique": "unique"},
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
    response = client.Base.DeleteObjectsByCriteria("type", "criteria")
    client._get.assert_called_with(
        "DeleteObjectsByCriteria", params={"type": "type", "criteria": "criteria"}
    )

    assert response == success_response


def test_get_not_empty_type(client):
    client._get.return_value = success_response
    response = client.Base.GetNotEmptyType("type_like", True)
    client._get.assert_called_with(
        "GetNotEmptyType",
        params={
            "typeLike": "type_like",
            "asc": True,
        },
    )

    assert response == success_response


def test_get_object(client):
    client._get.return_value = success_response
    response = client.Base.GetObject("type", 1, "join")
    client._get.assert_called_with(
        "GetObject", params={"type": "type", "id": 1, "join": "join"}
    )

    assert response == success_response


def test_get_objects(client):
    client._get.return_value = success_response
    response = client.Base.GetObjects("type", 1, 1, "join")
    client._get.assert_called_with(
        "GetObjects", params={"type": "type", "froms": 1, "count": 1, "join": "join"}
    )

    assert response == success_response


def test_get_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByCriteria(
        "type", "criteria", 1, 1, "join", "projection"
    )
    client._get.assert_called_with(
        "GetObjectsByCriteria",
        params={
            "type": "type",
            "criteria": "criteria",
            "froms": 1,
            "count": 1,
            "join": "join",
            "projection": "projection",
        },
    )
    assert response == success_response


def test_get_objects_by_role(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByRole(
        "type", "role", "criteria", 1, 1, "join", "projection"
    )
    client._get.assert_called_with(
        "GetObjectsByRole",
        params={
            "type": "type",
            "role": "role",
            "criteria": "criteria",
            "froms": 1,
            "count": 1,
            "join": "join",
            "projection": "projection",
        },
    )
    assert response == success_response


def test_get_objects_count(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsCount("type", "criteria")
    client._get.assert_called_with(
        "GetObjectsCount", params={"type": "type", "criteria": "criteria"}
    )

    assert response == success_response


def test_get_property(client):
    client._get.return_value = success_response
    response = client.Base.GetProperty("type", 1, "property", "join")
    client._get.assert_called_with(
        "GetProperty",
        params={"type": "type", "id": 1, "property": "property", "join": "join"},
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
    response = client.Base.GetTypes(1, 1)
    client._get.assert_called_with(
        "GetTypes",
        params={
            "froms": 1,
            "count": 1,
        },
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
    response = client.Base.SetProperty("type", 1, "property", None)
    client._get.assert_called_with(
        "SetProperty",
        params={"type": "type", "id": 1, "property": "property", "value": None},
    )

    assert response == success_response


def test_set_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.SetObjectsByCriteria(
        "type", "property", None, "criteria", 1, 1, "join"
    )
    client._get.assert_called_with(
        "SetObjectsByCriteria",
        params={
            "type": "type",
            "property": "property",
            "value": None,
            "criteria": "criteria",
            "froms": 1,
            "count": 1,
            "join": "join",
        },
    )
    assert response == success_response


def test_set_unique_fields(client):
    client._get.return_value = success_response
    response = client.Base.SetUniqueFields("type", "unique")
    client._get.assert_called_with(
        "SetUniqueFields", params={"type": "type", "unique": "unique"}
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
