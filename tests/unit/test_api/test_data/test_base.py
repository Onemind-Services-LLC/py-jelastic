from . import *


def test_add_field(client):
    client._get.return_value = success_response
    response = client.Base.AddField(
        "type",
        "field",
        "fieldType",
        "ruk",
    )
    client._get.assert_called_with(
        "AddField",
        params={
            "type": "type",
            "field": "field",
            "fieldType": "fieldType",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_create_object(client):
    client._get.return_value = success_response
    response = client.Base.CreateObject(
        "type",
        "data",
        "ruk",
    )
    client._get.assert_called_with(
        "CreateObject",
        params={
            "type": "type",
            "data": "data",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_create_objects(client):
    client._get.return_value = success_response
    response = client.Base.CreateObjects(
        "type",
        "data",
        "ruk",
    )
    client._get.assert_called_with(
        "CreateObjects",
        params={
            "type": "type",
            "data": "data",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_define_type(client):
    client._get.return_value = success_response
    response = client.Base.DefineType(
        "type",
        "fields",
        "unique",
        "ruk",
    )
    client._get.assert_called_with(
        "DefineType",
        params={
            "type": "type",
            "fields": "fields",
            "unique": "unique",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_define_type_by_uid(client):
    client._get.return_value = success_response
    response = client.Base.DefineTypeByUid(
        1,
        "type",
        "fields",
        "unique",
        "ruk",
    )
    client._get.assert_called_with(
        "DefineTypeByUid",
        params={
            "uid": 1,
            "type": "type",
            "fields": "fields",
            "unique": "unique",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_delete_object(client):
    client._get.return_value = success_response
    response = client.Base.DeleteObject(
        "type",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteObject",
        params={
            "type": "type",
            "id": 1,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_delete_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.DeleteObjectsByCriteria(
        "type",
        "criteria",
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteObjectsByCriteria",
        params={
            "type": "type",
            "criteria": "criteria",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_not_empty_type(client):
    client._get.return_value = success_response
    response = client.Base.GetNotEmptyType(
        "type_like",
        True,
        "ruk",
    )
    client._get.assert_called_with(
        "GetNotEmptyType",
        params={
            "typeLike": "type_like",
            "asc": True,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_object(client):
    client._get.return_value = success_response
    response = client.Base.GetObject(
        "type",
        1,
        "join",
        "ruk",
    )
    client._get.assert_called_with(
        "GetObject",
        params={
            "type": "type",
            "id": 1,
            "join": "join",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_objects(client):
    client._get.return_value = success_response
    response = client.Base.GetObjects(
        "type",
        1,
        1,
        "join",
        "ruk",
    )
    client._get.assert_called_with(
        "GetObjects",
        params={
            "type": "type",
            "froms": 1,
            "count": 1,
            "join": "join",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByCriteria(
        "type",
        "criteria",
        1,
        1,
        "join",
        "projection",
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_objects_by_role(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsByRole(
        "type",
        "role",
        "criteria",
        1,
        1,
        "join",
        "projection",
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_objects_count(client):
    client._get.return_value = success_response
    response = client.Base.GetObjectsCount(
        "type",
        "criteria",
        "ruk",
    )
    client._get.assert_called_with(
        "GetObjectsCount",
        params={
            "type": "type",
            "criteria": "criteria",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_property(client):
    client._get.return_value = success_response
    response = client.Base.GetProperty(
        "type",
        1,
        "property",
        "join",
        "ruk",
    )
    client._get.assert_called_with(
        "GetProperty",
        params={
            "type": "type",
            "id": 1,
            "property": "property",
            "join": "join",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_type(client):
    client._get.return_value = success_response
    response = client.Base.GetType(
        "type",
        "ruk",
    )
    client._get.assert_called_with(
        "GetType",
        params={
            "type": "type",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_types(client):
    client._get.return_value = success_response
    response = client.Base.GetTypes(
        1,
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetTypes",
        params={
            "froms": 1,
            "count": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_type_count(client):
    client._get.return_value = success_response
    response = client.Base.GetTypesCount(
        "ruk",
    )
    client._get.assert_called_with(
        "GetTypesCount",
        params={
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_get_unique_fields(client):
    client._get.return_value = success_response
    response = client.Base.GetUniqueFields(
        "type",
        "ruk",
    )
    client._get.assert_called_with(
        "GetUniqueFields",
        params={
            "type": "type",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_remove_field(client):
    client._get.return_value = success_response
    response = client.Base.RemoveField(
        "type",
        "field",
        "ruk",
    )
    client._get.assert_called_with(
        "RemoveField",
        params={
            "type": "type",
            "field": "field",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_rename_field(client):
    client._get.return_value = success_response
    response = client.Base.RenameField(
        "type",
        "old_field",
        "new_field",
        "ruk",
    )
    client._get.assert_called_with(
        "RenameField",
        params={
            "type": "type",
            "oldField": "old_field",
            "newField": "new_field",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_rename_type(client):
    client._get.return_value = success_response
    response = client.Base.RenameType(
        "type",
        "old_type",
        "new_type",
        "ruk",
    )
    client._get.assert_called_with(
        "RenameType",
        params={
            "type": "type",
            "oldType": "old_type",
            "newTyoe": "new_type",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_set_object(client):
    client._get.return_value = success_response
    response = client.Base.SetObject(
        "type",
        1,
        "data",
        "ruk",
    )
    client._get.assert_called_with(
        "SetObject",
        params={
            "type": "type",
            "id": 1,
            "data": "data",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_set_objects(client):
    client._get.return_value = success_response
    response = client.Base.SetObjects(
        "type",
        "data",
        "ruk",
    )
    client._get.assert_called_with(
        "SetObjects",
        params={
            "type": "type",
            "data": "data",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_set_property(client):
    client._get.return_value = success_response
    response = client.Base.SetProperty(
        "type",
        1,
        "property",
        None,
        "ruk",
    )
    client._get.assert_called_with(
        "SetProperty",
        params={
            "type": "type",
            "id": 1,
            "property": "property",
            "value": None,
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_set_objects_by_criteria(client):
    client._get.return_value = success_response
    response = client.Base.SetObjectsByCriteria(
        "type",
        "property",
        None,
        "criteria",
        1,
        1,
        "join",
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_unique_fields(client):
    client._get.return_value = success_response
    response = client.Base.SetUniqueFields(
        "type",
        "unique",
        "ruk",
    )
    client._get.assert_called_with(
        "SetUniqueFields",
        params={
            "type": "type",
            "unique": "unique",
            "ruk": "ruk",
        },
    )

    assert response == success_response


def test_undefine_type(client):
    client._get.return_value = success_response
    response = client.Base.UndefineType(
        "type",
        "ruk",
    )
    client._get.assert_called_with(
        "UndefineType",
        params={
            "type": "type",
            "ruk": "ruk",
        },
    )

    assert response == success_response
