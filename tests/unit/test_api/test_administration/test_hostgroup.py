from . import *


def test_add(client):
    client._get.return_value = success_response
    response = client.HostGroup.Add(
        {
            "add1": "val1",
            "add2": "val2",
            "add3": "val3",
            "add4": "val4",
        }
    )
    client._get.assert_called_with(
        "Add",
        params={
            "data": {
                "add1": "val1",
                "add2": "val2",
                "add3": "val3",
                "add4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.AddEndpoints(
        "host group",
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        },
    )
    client._get.assert_called_with(
        "AddEndpoints",
        params={
            "hostGroup": "host group",
            "endpoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit(client):
    client._get.return_value = success_response
    response = client.HostGroup.Edit(
        {
            "edit1": "data1",
            "edit2": "data2",
            "edit3": "data3",
            "edit4": "data4",
        }
    )
    client._get.assert_called_with(
        "Edit",
        params={
            "data": {
                "edit1": "data1",
                "edit2": "data2",
                "edit3": "data3",
                "edit4": "data4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.EditEndpoints(
        "host group",
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        },
    )
    client._get.assert_called_with(
        "EditEndpoints",
        params={
            "hostGroup": "host group",
            "endpoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.HostGroup.Get()
    client._get.assert_called_with("Get", params={})
    assert response == success_response


def test_get_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.GetEndpoints("host group")
    client._get.assert_called_with(
        "GetEndpoints",
        params={
            "hostGroup": "host group",
        },
    )
    assert response == success_response


def test_remove(client):
    client._get.return_value = success_response
    response = client.HostGroup.Remove(1)
    client._get.assert_called_with(
        "Remove",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_remove_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.RemoveEndpoints(1)
    client._get.assert_called_with(
        "RemoveEndpoints",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_rename_remote_user(client):
    client._get.return_value = success_response
    response = client.HostGroup.RenameRemoteUser(1, "remoteuser@.email.com")
    client._get.assert_called_with(
        "RenameRemoteUser",
        params={
            "uid": 1,
            "email": "remoteuser@.email.com",
        },
    )
    assert response == success_response


def test_test_end_points(client):
    client._get.return_value = success_response
    response = client.HostGroup.TestEndpoints(
        {
            "endpoint1": "val1",
            "endpoint2": "val2",
            "endpoint3": "val3",
            "endpoint4": "val4",
        }
    )
    client._get.assert_called_with(
        "TestEndpoints",
        params={
            "endPoints": {
                "endpoint1": "val1",
                "endpoint2": "val2",
                "endpoint3": "val3",
                "endpoint4": "val4",
            },
        },
        delimiter=",",
    )
    assert response == success_response
