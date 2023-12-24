from . import *


def test_attach_env(client):
    client._get.return_value = success_response
    response = client.Group.AttachEnv(
        "env_name",
        "env_group",
        ["target_appid1", "target_appid2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "AttachEnv",
        params={
            "envName": "env_name",
            "envGroup": "env_group",
            "targetAppid": ["target_appid1", "target_appid2"],
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_create_group(client):
    client._get.return_value = success_response
    response = client.Group.CreateGroup(
        "env_name",
        "env_group",
        {"data1": "data1", "data2": "data2"},
        [1, 1],
    )
    client._get.assert_called_with(
        "CreateGroup",
        params={
            "envName": "env_name",
            "envGroup": "env_group",
            "data": {"data1": "data1", "data2": "data2"},
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_detach_env(client):
    client._get.return_value = success_response
    response = client.Group.DetachEnv(
        "env_name",
        "env_group",
        ["target_appid1", "target_appid2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "DetachEnv",
        params={
            "envName": "env_name",
            "envGroup": "env_group",
            "targetAppid": ["target_appid1", "target_appid2"],
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_group(client):
    client._get.return_value = success_response
    response = client.Group.EditGroup(
        "env_name",
        "src_group_name",
        ["dst_group_name1", "dst_group_name2"],
        {"data1": "data1", "data2": "data2"},
        [1, 1],
    )
    client._get.assert_called_with(
        "EditGroup",
        params={
            "envName": "env_name",
            "srcGroupName": "src_group_name",
            "dstGroupName": ["dst_group_name1", "dst_group_name2"],
            "data": {"data1": "data1", "data2": "data2"},
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.Group.GetGroups(
        "env_name",
        ["target_appid1", "target_appid2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "GetGroups",
        params={
            "envName": "env_name",
            "targetAppid": ["target_appid1", "target_appid2"],
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_group(client):
    client._get.return_value = success_response
    response = client.Group.RemoveGroup(
        "env_name",
        "env_group",
        [1, 1],
    )
    client._get.assert_called_with(
        "RemoveGroup",
        params={
            "envName": "env_name",
            "envGroup": "env_group",
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_env(client):
    client._get.return_value = success_response
    response = client.Group.SetEnv(
        "env_name", "env_group", ["target_appid1", "target_appid2"]
    )
    client._get.assert_called_with(
        "SetEnv",
        params={
            "envName": "env_name",
            "envGroup": "env_group",
            "targetAppid": ["target_appid1", "target_appid2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_isolation_enabled(client):
    client._get.return_value = success_response
    response = client.Group.SetIsolationEnabled(
        "env_name",
        "group_name",
        True,
        [1, 1],
    )
    client._get.assert_called_with(
        "SetIsolationEnabled",
        params={
            "envName": "env_name",
            "groupName": "group_name",
            "enabled": True,
            "ownerUid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response
