from . import *


def test_add_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddGroup(
        "type",
        "group name",
        ["description1", "description2", "description3"],
        ["source group 1", "source group 2", "source group 3"],
        ["domain 1", "domain 2", "domain 3"],
        ["conversion group 1", "conversion group 2", "conversion group 3"],
    )
    client._get.assert_called_with(
        "AddGroup",
        params={
            "type": "type",
            "name": "group name",
            "description": ["description1", "description2", "description3"],
            "sourceGroupName": ["source group 1", "source group 2", "source group 3"],
            "domain": ["domain 1", "domain 2", "domain 3"],
            "conversionGroup": [
                "conversion group 1",
                "conversion group 2",
                "conversion group 3",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddQuota(
        "name",
        ["description1", "description2", "description3"],
        ["rid 1", "rid 2", "rid 3"],
        [1, 2, 3],
        [True, False, True],
    )
    client._get.assert_called_with(
        "AddQuota",
        params={
            "name": "name",
            "description": ["description1", "description2", "description3"],
            "referenceId": ["rid 1", "rid 2", "rid 3"],
            "defaultValue": [1, 2, 3],
            "assignToGroup": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.DeleteGroup("name")
    client._get.assert_called_with("DeleteGroup", params={"name": "name"})
    assert response == success_response


def test_edit_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditGroup(
        "name",
        ["new name 1", "new name 2", "new name 3"],
        ["description1", "description2", "description3"],
        ["group1", "group2", "group3"],
    )
    client._get.assert_called_with(
        "EditGroup",
        params={
            "name": "name",
            "newName": ["new name 1", "new name 2", "new name 3"],
            "description": ["description1", "description2", "description3"],
            "conversionGroup": ["group1", "group2", "group3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditQuota(
        "name",
        ["rid 1", "rid 2", "rid 3"],
        ["new rid 1", "new rid 2", "new rid 3"],
        ["description1", "description2", "description3"],
    )
    client._get.assert_called_with(
        "EditQuota",
        params={
            "name": "name",
            "referenceId": ["rid 1", "rid 2", "rid 3"],
            "newReferenceId": ["new rid 1", "new rid 2", "new rid 3"],
            "description": ["description1", "description2", "description3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_group_quotas(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroupQuotas(
        "name",
        ["quota 1", "quota 2", "quota 3"],
    )
    client._get.assert_called_with(
        "GetGroupQuotas",
        params={
            "name": "name",
            "quotasnames": ["quota 1", "quota 2", "quota 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroups()
    client._get.assert_called_with("GetGroups", params={})
    assert response == success_response


def test_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetPricingModels("name")
    client._get.assert_called_with("GetPricingModels", params={"groupName": "name"})
    assert response == success_response


def test_get_quotas_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetQuotas()
    client._get.assert_called_with("GetQuotas", params={})
    assert response == success_response


def test_is_domain_bound(client):
    client._get.return_value = success_response
    response = client.GroupQuota.IsDomainBound(
        ["checksum 1", "checksum 2", "checksum"],
    )
    client._get.assert_called_with(
        "IsDomainBound",
        params={"checksum": ["checksum 1", "checksum 2", "checksum"]},
        delimiter=",",
    )
    assert response == success_response


def test_remove_groupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveGroupQuota(
        "group name",
        "quota name",
    )
    client._get.assert_called_with(
        "RemoveGroupQuota",
        params={
            "groupName": "group name",
            "quotaName": "quota name",
        },
    )
    assert response == success_response


def test_remove_quota_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveQuota(
        "name",
        [True, False, True],
        ["rid 1", "rid 2", "rid 3"],
    )
    client._get.assert_called_with(
        "RemoveQuota",
        params={
            "name": "name",
            "force": [True, False, True],
            "referenceId": ["rid 1", "rid 2", "rid 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_collaboration_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetCollaborationGroup("name")
    client._get.assert_called_with("SetCollaborationGroup", params={"name": "name"})
    assert response == success_response


def test_set_default_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetDefaultGroup("name")
    client._get.assert_called_with("DefaultGroup", params={"name": "name"})
    assert response == success_response


def test_set_group_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetGroupQuota(
        "name",
        "quota name",
        1,
        ["rid 1", "rid 2", "rid 3"],
    )
    client._get.assert_called_with(
        "SetGroupQuota",
        params={
            "groupName": "name",
            "quotaName": "quota name",
            "value": 1,
            "referenceId": ["rid 1", "rid 2", "rid 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetPricingModels("name", "data")
    client._get.assert_called_with(
        "SetPricingModel", params={"groupName": "name", "data": "data"}
    )
    assert response == success_response


def test_set_win_domain(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetWinDomain("name", 1)
    client._get.assert_called_with(
        "SetWinDomain", params={"groupName": "name", "winDomainId": 1}
    )
    assert response == success_response


def test_unassign_hd_node_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.UnassignHdNodeGroup("group", "checksum")
    client._get.assert_called_with(
        "UnassignHdNodeGroup",
        params={
            "hardwareNodeGroup": "group",
            "checksum": "checksum",
        },
    )
    assert response == success_response


def test_set_signup_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetSignupGroup(
        "group",
    )
    client._get.assert_called_with(
        "SetSignupGroup",
        params={
            "name": "group",
        },
    )
    assert response == success_response
