from . import *


def test_add_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddGroup(
        "type",
        "group name",
        "description",
        "sourceGroupName",
        "domain",
        "conversionGroup",
    )
    client._get.assert_called_with(
        "AddGroup",
        params={
            "type": "type",
            "name": "group name",
            "description": "description",
            "sourceGroupName": "sourceGroupName",
            "domain": "domain",
            "conversionGroup": "conversionGroup",
        },
    )
    assert response == success_response


def test_add_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddQuota(
        "name",
        "description",
        "rid",
        1,
        True,
    )
    client._get.assert_called_with(
        "AddQuota",
        params={
            "name": "name",
            "description": "description",
            "referenceId": "rid",
            "defaultValue": 1,
            "assignToGroup": True,
        },
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
        "new_name",
        "description",
        "group",
    )
    client._get.assert_called_with(
        "EditGroup",
        params={
            "name": "name",
            "newName": "new_name",
            "description": "description",
            "conversionGroup": "group",
        },
    )
    assert response == success_response


def test_edit_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditQuota("name", "rid", "new rid", "description")
    client._get.assert_called_with(
        "EditQuota",
        params={
            "name": "name",
            "referenceId": "rid",
            "newReferenceId": "new rid",
            "description": "description",
        },
    )
    assert response == success_response


def test_get_group_quotas(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroupQuotas("name", "quota")
    client._get.assert_called_with(
        "GetGroupQuotas", params={"name": "name", "quotasnames": "quota"}
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
    response = client.GroupQuota.IsDomainBound("checksum")
    client._get.assert_called_with("IsDomainBound", params={"checksum": "checksum"})
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
    response = client.GroupQuota.RemoveQuota("name", True, "rid")
    client._get.assert_called_with(
        "RemoveQuota", params={"name": "name", "force": True, "referenceId": "rid"}
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
    response = client.GroupQuota.SetGroupQuota("name", "quota name", 1, "rid")
    client._get.assert_called_with(
        "SetGroupQuota",
        params={
            "groupName": "name",
            "quotaName": "quota name",
            "value": 1,
            "referenceId": "rid",
        },
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
