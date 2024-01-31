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
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_add_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.AddQuota("name", "description", "rid", 1, True, "ruk")
    client._get.assert_called_with(
        "AddQuota",
        params={
            "name": "name",
            "description": "description",
            "referenceId": "rid",
            "defaultValue": 1,
            "assignToGroup": True,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.DeleteGroup("name", "ruk")
    client._get.assert_called_with("DeleteGroup", params={"name": "name", "ruk": "ruk"})
    assert response == success_response


def test_edit_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditGroup(
        "name", "new_name", "description", "group", "ruk"
    )
    client._get.assert_called_with(
        "EditGroup",
        params={
            "name": "name",
            "newName": "new_name",
            "description": "description",
            "conversionGroup": "group",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_edit_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.EditQuota(
        "name", "rid", "new rid", "description", "ruk"
    )
    client._get.assert_called_with(
        "EditQuota",
        params={
            "name": "name",
            "referenceId": "rid",
            "newReferenceId": "new rid",
            "description": "description",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_group_quotas(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroupQuotas("name", "quota", "ruk")
    client._get.assert_called_with(
        "GetGroupQuotas", params={"name": "name", "quotasnames": "quota", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_groups(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetGroups("ruk")
    client._get.assert_called_with("GetGroups", params={"ruk": "ruk"})
    assert response == success_response


def test_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetPricingModels("name", "ruk")
    client._get.assert_called_with(
        "GetPricingModels", params={"groupName": "name", "ruk": "ruk"}
    )
    assert response == success_response


def test_get_quotas_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.GetQuotas("ruk")
    client._get.assert_called_with("GetQuotas", params={"ruk": "ruk"})
    assert response == success_response


def test_is_domain_bound(client):
    client._get.return_value = success_response
    response = client.GroupQuota.IsDomainBound("checksum", "ruk")
    client._get.assert_called_with(
        "IsDomainBound", params={"checksum": "checksum", "ruk": "ruk"}
    )
    assert response == success_response


def test_remove_groupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveGroupQuota("group name", "quota name", "ruk")
    client._get.assert_called_with(
        "RemoveGroupQuota",
        params={"groupName": "group name", "quotaName": "quota name", "ruk": "ruk"},
    )
    assert response == success_response


def test_remove_quota_GroupQuota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.RemoveQuota("name", True, "rid", "ruk")
    client._get.assert_called_with(
        "RemoveQuota",
        params={"name": "name", "force": True, "referenceId": "rid", "ruk": "ruk"},
    )
    assert response == success_response


def test_collaboration_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetCollaborationGroup("name", "ruk")
    client._get.assert_called_with(
        "SetCollaborationGroup", params={"name": "name", "ruk": "ruk"}
    )
    assert response == success_response


def test_set_default_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetDefaultGroup("name", "ruk")
    client._get.assert_called_with(
        "DefaultGroup", params={"name": "name", "ruk": "ruk"}
    )
    assert response == success_response


def test_set_group_quota(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetGroupQuota("name", "quota name", 1, "rid", "ruk")
    client._get.assert_called_with(
        "SetGroupQuota",
        params={
            "groupName": "name",
            "quotaName": "quota name",
            "value": 1,
            "referenceId": "rid",
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_pricing_models(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetPricingModels("name", "data", "ruk")
    client._get.assert_called_with(
        "SetPricingModel", params={"groupName": "name", "data": "data", "ruk": "ruk"}
    )
    assert response == success_response


def test_set_win_domain(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetWinDomain("name", 1, "ruk")
    client._get.assert_called_with(
        "SetWinDomain", params={"groupName": "name", "winDomainId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_unassign_hd_node_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.UnassignHdNodeGroup("group", "checksum", "ruk")
    client._get.assert_called_with(
        "UnassignHdNodeGroup",
        params={"hardwareNodeGroup": "group", "checksum": "checksum", "ruk": "ruk"},
    )
    assert response == success_response


def test_set_signup_group(client):
    client._get.return_value = success_response
    response = client.GroupQuota.SetSignupGroup("group", "ruk")
    client._get.assert_called_with(
        "SetSignupGroup",
        params={"name": "group", "ruk": "ruk"},
    )
    assert response == success_response
