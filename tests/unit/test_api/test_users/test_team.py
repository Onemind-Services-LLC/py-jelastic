from . import *


def test_create(client):
    client._get.return_value = success_response
    response = client.Team.Create( "displayName", 1)
    client._get.assert_called_with(
        "Create",
        params={
            "displayName": "displayName",
            "ownerUid": 1
        }
    )

    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Team.Delete(1, 1)
    client._get.assert_called_with(
        "Delete",
        params={
            "teamId": 1,
            "ownerUid": 1
        }
    )

    assert response == success_response


def test_delete_member_team(client):
    client._get.return_value = success_response
    response = client.Team.DeleteMember(1,1)
    client._get.assert_called_with(
        "DeleteMember",
        params={
            "memberId": 1,
            "ownerUid":1
        }
    )

    assert response == success_response


def test_edit(client):
    client._get.return_value = success_response
    response = client.Team.Edit(
        1, "displayName",  "externalId",1
    )
    client._get.assert_called_with(
        "Edit",
        params={
            "teamId": 1,
            "displayName": "displayName",
            "externalId": "externalId",
            "ownerUid": 1
        }
    )

    assert response == success_response


def test_get(client):
    client._get.return_value = success_response
    response = client.Team.Get(1)
    client._get.assert_called_with(
        "Get",
        params={
            "ownerUid":1
        }
    )

    assert response == success_response


def test_invite(client):
    client._get.return_value = success_response
    response = client.Team.Invite(
        "email", 1, "displayName", 1
    )
    client._get.assert_called_with(
        "Invite",
        params={
            "email": "email",
            "teamId": 1,
            "displayName":"displayName",
            "ownerUid": 1
        }
    )

    assert response == success_response


def test_resend_invite(client):
    client._get.return_value = success_response
    response = client.Team.ResendInvite(1, 1)
    client._get.assert_called_with(
        "ResendInvite",
        params={
            "memberId": 1,
            "ownerUid": 1
        }
    )

    assert response == success_response
