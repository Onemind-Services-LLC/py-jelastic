from . import *


def test_create(client):
    client._get.return_value = success_response
    response = client.Team.Create(["display_name1", "display_name2"], [1, 1])
    client._get.assert_called_with(
        "Create",
        params={
            "displayName": ["display_name1", "display_name2"],
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Team.Delete(1, [1, 1])
    client._get.assert_called_with(
        "Delete",
        params={
            "teamId": 1,
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_delete_member_team(client):
    client._get.return_value = success_response
    response = client.Team.DeleteMember(1, [1, 1])
    client._get.assert_called_with(
        "DeleteMember",
        params={
            "memberId": 1,
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_edit(client):
    client._get.return_value = success_response
    response = client.Team.Edit(
        1, ["display_name1", "display_name2"], ["external_id1", "external_id2"], [1, 1]
    )
    client._get.assert_called_with(
        "Edit",
        params={
            "teamId": 1,
            "displayName": ["display_name1", "display_name2"],
            "externalId": ["external_id1", "external_id2"],
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.Team.Get([1, 1])
    client._get.assert_called_with(
        "Get",
        params={
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_invite(client):
    client._get.return_value = success_response
    response = client.Team.Invite(
        "email", 1, ["display_name1", "display_name2"], [1, 1]
    )
    client._get.assert_called_with(
        "Invite",
        params={
            "email": "email",
            "teamId": 1,
            "displayName": ["display_name1", "display_name2"],
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response


def test_resend_invite(client):
    client._get.return_value = success_response
    response = client.Team.ResendInvite(1, [1, 1])
    client._get.assert_called_with(
        "ResendInvite",
        params={
            "memberId": 1,
            "ownerUid": [1, 1],
        },
        delimeter=",",
    )

    assert response == success_response
