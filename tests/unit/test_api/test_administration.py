import pytest
import datetime
from unittest.mock import patch, Mock
from jelastic.api import Administration

CURRENT_DATETIME = datetime.datetime.now()
success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        admin = Administration(session=Mock(), token="token")
        admin._get = mock_get
        yield admin


def test_get_nodes_affinity_suggestion(client):
    client._get.return_value = success_response
    response = client.Analytics.GetNodesAffinitySuggestion(
        ["app_id1", "app_id2"], ["node_group1", "node_group2"], ["uid1", "uid2"], 10
    )
    client._get.assert_called_with(
        "GetNodesAffinitySuggestion",
        params={
            "targetAppIds": ["app_id1", "app_id2"],
            "nodeGroups": ["node_group1", "node_group2"],
            "uids": ["uid1", "uid2"],
            "threadCount": 10,
        },
        delimiter=",",
    )

    assert response == success_response


def test_get_nodes_anti_affinity_suggestion(client):
    client._get.return_value = success_response
    response = client.Analytics.GetNodesAntiAffinitySuggestion(
        ["app_id1", "app_id2"],
        "STRONG",
        ["node_group1", "node_group2"],
        ["uid1", "uid2"],
        10,
    )
    client._get.assert_called_with(
        "GetNodesAntiAffinitySuggestion",
        params={
            "targetAppIds": ["app_id1", "app_id2"],
            "mode": "STRONG",
            "nodeGroups": ["node_group1", "node_group2"],
            "uids": ["uid1", "uid2"],
            "threadCount": 10,
        },
        delimiter=",",
    )
    assert response == success_response


def test_apply_config(client):
    client._get.return_value = success_response
    response = client.Config.ApplyConfig("type", "password")
    client._get.assert_called_with(
        "ApplyConfig",
        params={
            "type": "type",
            "password": "password",
        },
    )
    assert response == success_response


def test_apply_defaults(client):
    client._get.return_value = success_response
    response = client.Config.ApplyDefaults(
        "edition",
    )
    client._get.assert_called_with(
        "ApplyDefaults",
        params={
            "edition": "edition",
        },
    )
    assert response == success_response


def test_apply_reseller_config(client):
    client._get.return_value = success_response
    response = client.Config.ApplyResellerConfig("type", "password", "id_1")
    client._get.assert_called_with(
        "ApplyResellerConfig",
        params={
            "type": "type",
            "password": "password",
            "resellerId": "id_1",
        },
    )
    assert response == success_response


def test_change_config_key(client):
    client._get.return_value = success_response
    response = client.Config.ChangeConfigKey("type", "key", ["value1", "value2"])
    client._get.assert_called_with(
        "ChangeConfigKey",
        params={
            "type": "type",
            "key": "key",
            "value": ["value1", "value2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_change_properties_for_reseller(client):
    client._get.return_value = success_response
    response = client.Config.ChangePropertiesForReseller(
        "rid_1",
    )
    client._get.assert_called_with(
        "ChangePropertiesForReseller",
        params={
            "resellerId": "rid_1",
        },
    )
    assert response == success_response


def test_creating_config_type(client):
    client._get.return_value = success_response
    response = client.Config.CreatingConfigType(
        "type",
        "description",
    )
    client._get.assert_called_with(
        "CreatingConfigType",
        params={"type": "type", "description": "description"},
    )
    assert response == success_response


def test_creating_key_config(client):
    client._get.return_value = success_response
    response = client.Config.CreatingKeyConfig(
        "type", "key", "value", "default value", "expert", "description", "key type"
    )
    client._get.assert_called_with(
        "CreatingKeyConfig",
        params={
            "type": "type",
            "key": "key",
            "value": "value",
            "default_value": "default value",
            "expert": "expert",
            "description": "description",
            "keyType": "key type",
        },
    )
    assert response == success_response


def test_find_config_key(client):
    client._get.return_value = success_response
    response = client.Config.FindConfigKey(
        "value",
    )
    client._get.assert_called_with(
        "FindConfigKey",
        params={
            "value": "value",
        },
    )
    assert response == success_response


def test_get_all_config_type(client):
    client._get.return_value = success_response
    response = client.Config.GetAllConfigType(
        "expert",
    )
    client._get.assert_called_with(
        "GetAllConfigType",
        params={
            "expert": "expert",
        },
    )
    assert response == success_response


def test_get_all_key_config_by_type(client):
    client._get.return_value = success_response
    response = client.Config.GetAllKeyConfigByType("type", "expert")
    client._get.assert_called_with(
        "GetAllKeyConfigByType",
        params={
            "type": "type",
            "expert": "expert",
        },
    )
    assert response == success_response


def test_get_congif_key(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKey(
        "type",
        "key",
    )
    client._get.assert_called_with(
        "GetConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_get_config_key_by_seller_id(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKeyByResellerId(
        "type",
        "key",
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "GetConfigKeyByResellerId",
        params={
            "type": "type",
            "key": "key",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_config_keys(client):
    client._get.return_value = success_response
    response = client.Config.GetConfigKeys(
        ["type1", "type2", "type3"], ["key1", "key2", "key3"]
    )
    client._get.assert_called_with(
        "GetConfigKeys",
        params={
            "type": ["type1", "type2", "type3"],
            "key": ["key1", "key2", "key3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_config_key(client):
    client._get.return_value = success_response
    response = client.Config.RemoveConfigKey("type", "key")
    client._get.assert_called_with(
        "RemoveConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_remove_config_type(client):
    client._get.return_value = success_response
    response = client.Config.RemoveConfigType(
        "type",
    )
    client._get.assert_called_with(
        "RemoveConfigType",
        params={
            "type": "type",
        },
    )
    assert response == success_response


def test_remove_reseller_properties(client):
    client._get.return_value = success_response
    response = client.Config.RemoveResellerProperties(
        1,
    )
    client._get.assert_called_with(
        "RemoveResellerProperties",
        params={
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_revert_config_key(client):
    client._get.return_value = success_response
    response = client.Config.RevertConfigKey("type", "key")
    client._get.assert_called_with(
        "RevertConfigKey",
        params={
            "type": "type",
            "key": "key",
        },
    )
    assert response == success_response


def test_set_reseller_config_key(client):
    client._get.return_value = success_response
    response = client.Config.SetResellerConfigKey("type", "key", "value", 1)
    client._get.assert_called_with(
        "SetResellerConfigKey",
        params={
            "type": "type",
            "key": "key",
            "value": "value",
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_add_statistics(client):
    client._get.return_value = success_response
    response = client.Resource.AddStatistics(
        "resource 1",
        1,
        1234,
        [CURRENT_DATETIME.date().today(), CURRENT_DATETIME.date().today()],
        [datetime.date(2025, 11, 11), datetime.date(2025, 11, 12)],
        ["env 1", "env 2", "env 3"],
        [1, 2, 3],
        ["note 1", "note 2", "note 3"],
        ["value 1", "value 2", "value 3"],
    )
    client._get.assert_called_with(
        "AddStatistics",
        params={
            "resourceName": "resource 1",
            "uid": 1,
            "value": 1234,
            "startDate": [CURRENT_DATETIME.date().today(), CURRENT_DATETIME.date().today()],
            "endDate": [datetime.date(2025, 11, 11), datetime.date(2025, 11, 12)],
            "envName": ["env 1", "env 2", "env 3"],
            "nodeId": [1, 2, 3],
            "note": ["note 1", "note 2", "note 3"],
            "valueGroup": ["value 1", "value 2", "value 3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_category(client):
    client._get.return_value = success_response
    response = client.Subscription.AddCategory(
        {
            "category1": "val1",
            "category2": "val2",
            "category3": "val3",
            "category4": "val4",
            "category5": "val5",
        },
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "AddCategory",
        params={
            "category": {
                "category1": "val1",
                "category2": "val2",
                "category3": "val3",
                "category4": "val4",
                "category5": "val5",
            },
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_product(client):
    client._get.return_value = success_response
    response = client.Subscription.AddProduct(
        {
            "product1": "val1",
            "product2": "val2",
            "product3": "val3",
            "product4": "val4",
            "product5": "val5",
        },
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "AddProduct",
        params={
            "product": {
                "product1": "val1",
                "product2": "val2",
                "product3": "val3",
                "product4": "val4",
                "product5": "val5",
            },
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.AddServicePlan(
        {
            "servicePlan1": "val1",
            "servicePlan2": "val2",
            "servicePlan3": "val3",
            "servicePlan4": "val4",
        },
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
    )
    client._get.assert_called_with(
        "AddServicePlan",
        params={
            "servicePlan": {
                "servicePlan1": "val1",
                "servicePlan2": "val2",
                "servicePlan3": "val3",
                "servicePlan4": "val4",
            },
            "resellerId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_subscription_item_resource(client):
    client._get.return_value = success_response
    response = client.Subscription.AddSubscriptionItemResource(
        1,
        1,
        1,
        {
            "resource1": "val1",
            "resource2": "val2",
            "resource3": "val3",
            "resource4": "val4",
            "resource5": "val5",
        },
    )
    client._get.assert_called_with(
        "AddSubscriptionItemResource",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "itemResourceId": 1,
            "resources": {
                "resource1": "val1",
                "resource2": "val2",
                "resource3": "val3",
                "resource4": "val4",
                "resource5": "val5",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_adjust_product(client):
    client._get.return_value = success_response
    response = client.Subscription.AdjustProduct(1, 1, 1)
    client._get.assert_called_with(
        "AdjustProduct",
        params={
            "subscriptionId": 1,
            "itemId": 1,
            "itemResourceId": 1,
        },
    )
    assert response == success_response


def test_delete_category(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteCategory(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteCategory",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_product(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteProduct(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteProduct",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.DeleteServicePlan(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "DeleteServicePlan",
        params={
            "id": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_category(client):
    client._get.return_value = success_response
    response = client.Subscription.EditCategory(1, [1, 2, 3, 4])
    client._get.assert_called_with(
        "EditCategory",
        params={
            "category": 1,
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_product(client):
    client._get.return_value = success_response
    response = client.Subscription.EditProduct(
        {
            "category1": "val1",
            "category2": "val2",
            "category3": "val3",
            "category4": "val4",
            "category5": "val5",
        },
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "EditProduct",
        params={
            "category": {
                "category1": "val1",
                "category2": "val2",
                "category3": "val3",
                "category4": "val4",
                "category5": "val5",
            },
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.EditServicePlan(
        {
            "service_plan1": "val1",
            "service_plan2": "val2",
            "service_plan3": "val3",
            "service_plan4": "val4",
            "service_plan5": "val5",
        },
        [1, 2, 3, 4, 5],
        ["exp1", "exp2", "exp3", "exp4", "exp5"],
    )
    client._get.assert_called_with(
        "EditServicePlan",
        params={
            "servicePlan": {
                "service_plan1": "val1",
                "service_plan2": "val2",
                "service_plan3": "val3",
                "service_plan4": "val4",
                "service_plan5": "val5",
            },
            "resellerId": [1, 2, 3, 4, 5],
            "expendFields": ["exp1", "exp2", "exp3", "exp4", "exp5"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_categories(client):
    client._get.return_value = success_response
    response = client.Subscription.GetCategories(
        [1, 2, 3, 4], ["exp1", "exp2", "exp3", "exp4"]
    )
    client._get.assert_called_with(
        "GetCategories",
        params={
            "resellerId": [1, 2, 3, 4],
            "expendFields": ["exp1", "exp2", "exp3", "exp4"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_products(client):
    client._get.return_value = success_response
    response = client.Subscription.GetProducts(
        [1, 2, 3, 4, 5],
        ["status1", "status2", "status3", "status4", "status5"],
        [1, 2, 3, 4, 5],
        ["sub1", "sub2", "sub3", "sub4", "sub5"],
        ["exp1", "exp2", "exp3", "exp4"],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ["order1", "order2", "order3", "order4", "order5"],
        ["direction1", "direction2", "direction3", "direction4", "direction5"],
    )
    client._get.assert_called_with(
        "GetProduct",
        params={
            "id": [1, 2, 3, 4, 5],
            "status": ["status1", "status2", "status3", "status4", "status5"],
            "resellerId": [1, 2, 3, 4, 5],
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4", "sub5"],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
            "startRow": [1, 2, 3, 4, 5],
            "resultCount": [1, 2, 3, 4, 5],
            "orderField": ["order1", "order2", "order3", "order4", "order5"],
            "orderDirection": [
                "direction1",
                "direction2",
                "direction3",
                "direction4",
                "direction5",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_service_plan(client):
    client._get.return_value = success_response
    response = client.Subscription.GetServicePlans(
        [1, 2, 3, 4],
        [True, False, True, False],
        ["sub1", "sub2", "sub3", "sub4"],
        [1, 2, 3, 4],
        ["exp1", "exp2", "exp3", "exp4"],
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetServicePlans",
        params={
            "id": [1, 2, 3, 4],
            "hasProducts": [True, False, True, False],
            "subscriptionStatus": ["sub1", "sub2", "sub3", "sub4"],
            "productId": [1, 2, 3, 4],
            "expandFields": ["exp1", "exp2", "exp3", "exp4"],
            "resellerId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_subscriptions(client):
    client._get.return_value = success_response
    response = client.Subscription.GetSubscriptions(
        [1, 2, 3],
        [1, 2, 3],
        ["status1", "status2", "status3"],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        ["exp1", "exp2", "exp3"],
        [1, 2, 3],
        [1, 2, 3],
        ["field1", "field2", "field3"],
        ["direction1", "direction2", "direction3"],
    )
    client._get.assert_called_with(
        "GetSubscriptions",
        params={
            "id": [1, 2, 3],
            "uid": [1, 2, 3],
            "status": ["status1", "status2", "status3"],
            "resellerId": [1, 2, 3],
            "productId": [1, 2, 3],
            "servicePlanId": [1, 2, 3],
            "expandFields": ["exp1", "exp2", "exp3"],
            "startRow": [1, 2, 3],
            "resultCount": [1, 2, 3],
            "orderField": ["field1", "field2", "field3"],
            "orderDirection": ["direction1", "direction2", "direction3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_category_published(client):
    client._get.return_value = success_response
    response = client.Subscription.SetCategoryPublished(1, True, [1, 2, 3])
    client._get.assert_called_with(
        "SetCategoryPublished",
        params={
            "id": 1,
            "published": True,
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_product_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetProductStatus(1, "status", [1, 2, 3])
    client._get.assert_called_with(
        "SetProductStatus",
        params={
            "id": 1,
            "status": "status",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_service_plan_status(client):
    client._get.return_value = success_response
    response = client.Subscription.SetServicePlanStatus(1, "status", [1, 2, 3])
    client._get.assert_called_with(
        "SetServicePlanStatus",
        params={
            "id": 1,
            "status": "status",
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_terminate_subscription(client):
    client._get.return_value = success_response
    response = client.Subscription.TerminateSubscription(
        1,
        "password",
    )
    client._get.assert_called_with(
        "TerminateSubscription",
        params={
            "subscriptionId": 1,
            "password": "password",
        },
    )
    assert response == success_response


def test_update_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Update.FixExtDns(
        [1, 2, 3, 4],
        ["target_app_id1", "target_app_id2", "target_app_id3"],
    )
    client._get.assert_called_with(
        "FixExtDns",
        params={
            "uid": [1, 2, 3, 4],
            "targetAppIds": ["target_app_id1", "target_app_id2", "target_app_id3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_restore_env(client):
    client._get.return_value = success_response
    response = client.Update.RestoreEnv(
        ["env1", "env2", "env3"],
        [1, 2, 3],
        ["region1", "region2", "region3"],
    )
    client._get.assert_called_with(
        "RestoreEnv",
        params={
            "envName": ["env1", "env2", "env3"],
            "uid": [1, 2, 3],
            "region": ["region1", "region2", "region3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_sync_infra_env(client):
    client._get.return_value = success_response
    response = client.Update.SyncInfraEnv(
        ["domain1", "domain2", "domain3"],
        ["registry1", "registry2", "registry3"],
    )
    client._get.assert_called_with(
        "SyncInfraEnv",
        params={
            "domain": ["domain1", "domain2", "domain3"],
            "registry": ["registry1", "registry2", "registry3"],
        },
        delimiter=",",
    )


def test_get_docker_pull_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetDockerPullStatus()
    client._get.assert_called_with("GetDockerPullStatus", params={})
    assert response == success_response


def test_get_host_firewall_status(client):
    client._get.return_value = success_response
    response = client.Monitoring.GetHostFirewallStatus()
    client._get.assert_called_with("GetHostFirewallStatus", params={})
    assert response == success_response


def test_set_default_registry(client):
    client._get.return_value = success_response
    response = client.Template.SetDefaultRegistry(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "SetDefaultRegistry",
        params={
            "id": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_distribution(client):
    client._get.return_value = success_response
    response = client.Template.SetDistribution(
        "node type",
        ["distribution1", "distribution2"],
    )
    client._get.assert_called_with(
        "SetDistribution",
        params={
            "nodeTypes": "node type",
            "distribution": ["distribution1", "distribution2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.AddSystemExternalDNSRecord(
        "record1",
        "name1",
        1,
        "data type 1",
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_with(
        "AddSystemExternalDNSRecord",
        params={
            "recordData": "record1",
            "name": "name1",
            "ttl": 1,
            "recordDataType": "data type 1",
            "sslEnabled": [True, False, True],
            "enabled": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_analize_env(client):
    client._get.return_value = success_response
    response = client.Utils.AnalizeEnv(
        "domain",
    )
    client._get.assert_called_with(
        "AnalizeEnv",
        params={
            "domain": "domain",
        },
    )
    assert response == success_response


def test_balance_resources(client):
    client._get.return_value = success_response
    response = client.Utils.BalanceResources(
        1,
    )
    client._get.assert_called_with("BalanceResources", params={"domain": 1})
    assert response == success_response


def test_clear_envs(client):
    client._get.return_value = success_response
    response = client.Utils.ClearEnvs()
    client._get.assert_called_with("ClearEnvs", params={})
    assert response == success_response


def test_delete_broken_envs(client):
    client._get.return_value = success_response
    response = client.Utils.DeleteBrokenEnvs(
        ["app1", "app2", "app3"],
    )
    client._get.assert_called_with(
        "DeleteBrokenEnvs",
        params={
            "targetAppIds": ["app1", "app2", "app3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.EditSystemExternalDNSRecord(
        1,
        ["record1", "record2", "record2"],
        ["name1", "name2", "name3"],
        [1, 2, 3],
        ["datatype1", "datatype2", "datatype3"],
        [True, False, True],
        [True, False, True],
    )
    client._get.assert_called_with(
        "EditSystemExternalDNSRecord",
        params={
            "id": 1,
            "recordData": ["record1", "record2", "record2"],
            "name": ["name1", "name2", "name3"],
            "ttl": [1, 2, 3],
            "recordDataType": ["datatype1", "datatype2", "datatype3"],
            "sslEnabled": [True, False, True],
            "enabled": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_export_env(client):
    client._get.return_value = success_response
    response = client.Utils.ExportEnv(
        "app id 1",
    )
    client._get.assert_called_with(
        "ExportEnv",
        params={
            "targetAppId": "app id 1",
        },
    )
    assert response == success_response


def test_utils_fix_ext_dns(client):
    client._get.return_value = success_response
    response = client.Utils.FixExtDns(
        [1, 2, 3],
        ["app id 1", "app id 2", "app id"],
    )
    client._get.assert_called_with(
        "FixExtDns",
        params={
            "uid": [1, 2, 3],
            "targetAppId": ["app id 1", "app id 2", "app id"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_fix_launching(client):
    client._get.return_value = success_response
    response = client.Utils.FixLaunching()
    client._get.assert_called_with("FixLaunching", params={})
    assert response == success_response


def test_generate_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GenerateZone(
        True,
    )
    client._get.assert_called_with(
        "GenerateZone",
        params={
            "generateSlept": True,
        },
    )
    assert response == success_response


def test_get_avgs(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs()
    client._get.assert_called_with("GetAvgs", params={})
    assert response == success_response


def test_get_avgs2(client):
    client._get.return_value = success_response
    response = client.Utils.GetAvgs2()
    client._get.assert_called_with("GetAvgs2", params={})
    assert response == success_response


def test_get_balance_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetBalancerStat(
        "2022-11-11",
        "2024-11-11",
    )
    client._get.assert_called_with(
        "GetBalancerStat",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
        },
    )
    assert response == success_response


def test_get_cloud_lets_usage(client):
    client._get.return_value = success_response
    response = client.Utils.GetCloudletsUsage()
    client._get.assert_called_with("GetCloudletsUsage", params={})
    assert response == success_response


def test_get_db_creation_stat(client):
    client._get.return_value = success_response
    response = client.Utils.GetDBCreationStat(
        "2022-11-11",
        "2024-11-11",
    )
    client._get.assert_called_with(
        "GetDBCreationStat",
        params={
            "startTime": "2022-11-11",
            "endTime": "2024-11-11",
        },
    )
    assert response == success_response


def test_get_errors(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrors(
        "2022-11-11",
        "2024-11-11",
        1,
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GerErrors",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
            "startrow": 1,
            "resultCount": 1,
            "filter": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_errors_by_date(client):
    client._get.return_value = success_response
    response = client.Utils.GetErrorsByDate(
        "2022-11-11",
        "2024-11-11",
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetErrorsByDate",
        params={
            "starttime": "2022-11-11",
            "endtime": "2024-11-11",
            "interval": 1,
            "filter": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_system_external_dns_records(client):
    client._get.return_value = success_response
    response = client.Utils.GetSystemExternalDNSRecords()
    client._get.assert_called_with("GetSystemExternalDNSRecords", params={})
    assert response == success_response


def test_get_zone(client):
    client._get.return_value = success_response
    response = client.Utils.GetZone()
    client._get.assert_called_with("GetZone", params={})
    assert response == success_response


def test_import_env(client):
    client._get.return_value = success_response
    response = client.Utils.ImportEnv(
        "env1",
        ["name1", "name2", "name3"],
        [True, False, True],
    )
    client._get.assert_called_with(
        "ImportEnv",
        params={
            "envInfo": "env1",
            "envName": ["name1", "name2", "name3"],
            "enableFirewall": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_inspect_envs(client):
    client._get.return_value = success_response
    response = client.Utils.InspectEnvs(
        [True, False, True],
    )
    client._get.assert_called_with(
        "InspectEnvs",
        params={
            "remove": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_manage_service(client):
    client._get.return_value = success_response
    response = client.Utils.ManageService(
        1,
        "command",
        "service 1",
    )
    client._get.assert_called_with(
        "ManageServices",
        params={
            "nodeid": 1,
            "command": "command",
            "servicename": "service 1",
        },
    )
    assert response == success_response


def test_remove_system_external_dns_record(client):
    client._get.return_value = success_response
    response = client.Utils.RemoveSystemExternalDNSRecord(1)
    client._get.assert_called_with(
        "RemoveSystemExternalDNSRecord",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_update_env(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnv("app 1")
    client._get.assert_called_with(
        "UpdateEnv",
        params={
            "targetAppId": "app 1",
        },
    )
    assert response == success_response


def test_update_inv_in_thread(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateEnvInThread(
        "thread app 1",
    )
    client._get.assert_called_with(
        "UpdateEnvInThread",
        params={
            "targetAppId": "thread app 1",
        },
    )
    assert response == success_response


def test_update_nodes(client):
    client._get.return_value = success_response
    response = client.Utils.UpdateNodes()
    client._get.assert_called_with("UpdateNodes", params={})
    assert response == success_response


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


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


def test_add_labels(client):
    client._get.return_value = success_response
    response = client.Host.AddLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "AddLabels",
        params={
            "ids": "app_id1",
            "labels": "app_label1",
        },
    )
    assert response == success_response


def test_check_host_connection(client):
    client._get.return_value = success_response
    response = client.Host.CheckHostConnection(
        "host_id1", [8000, 8001, 8002], [True, False, True]
    )
    client._get.assert_called_with(
        "CheckHostConnection",
        params={
            "hostId": "host_id1",
            "port": [8000, 8001, 8002],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_host_firewall_sets(client):
    client._get.return_value = success_response
    response = client.Host.GetHostFirewallSets()
    client._get.assert_called_with("GetHostFirewallSets", params={})
    assert response == success_response


def test_remove_labels(client):
    client._get.return_value = success_response
    response = client.Host.RemoveLabels("app_id1", "app_label1")
    client._get.assert_called_with(
        "RemoveLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_set_label(client):
    client._get.return_value = success_response
    response = client.Host.SetLabels(
        "app_id1",
        "app_label1",
    )
    client._get.assert_called_with(
        "SetLabels", params={"ids": "app_id1", "labels": "app_label1"}
    )
    assert response == success_response


def test_update_host_firewall(client):
    client._get.return_value = success_response
    response = client.Host.UpdateHostFirewall(
        [1, 2, 3], [True, False, True], [True, False, True]
    )
    client._get.assert_called_with(
        "UpdateHostFirewall",
        params={
            "hostId": [1, 2, 3],
            "force": [True, False, True],
            "checkExternalIp": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_action_to_isolation_queue(client):
    client._get.return_value = success_response
    response = client.Cluster.AddActionToIsolationQueue(
        [1, 2],
        [1, 2],
    )
    client._get.assert_called_with(
        "AddActionToIsolationQueue",
        params={
            "count": [1, 2],
            "delay": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_cartridge(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCartridge("manifest_url")
    client._get.assert_called_with(
        "AddCartridge",
        params={"manifestUrl": "manifest_url"},
    )
    assert response == success_response


def test_add_certified_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.AddCertifiedTemplates("manifest_url", [True, False])
    client._get.assert_called_with(
        "AddCertifiedTemplates",
        params={
            "repositories": "manifest_url",
            "publish": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddExtIps("ipfrom", "ipto", "regions")
    client._get.assert_called_with(
        "AddExtIps",
        params={
            "ipfrom": "ipfrom",
            "ipto": "ipto",
            "regions": "regions",
        },
    )
    assert response == success_response


def test_add_hard_ware_node_message(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHardWareNodeMessage(
        "hn_id",
        "message_type",
        "process_response_code",
        "percentage",
        "message",
        "custom_data",
    )
    client._get.assert_called_with(
        "AddHardWareNodeMessage",
        params={
            "hnId": "hn_id",
            "messageType": "message_type",
            "processResponseCode": "process_response_code",
            "percentage": "percentage",
            "message": "message",
            "customData": "custom_data",
        },
    )
    assert response == success_response


def test_add_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNode(
        {"hd_node1": "hd_node1", "hd_node2": "hd_node2"}, [True, False], [True, False]
    )
    client._get.assert_called_with(
        "AddHdNode",
        params={
            "hdnode": {"hd_node1": "hd_node1", "hd_node2": "hd_node2"},
            "setAsDockerHost": [True, False],
            "setAsDockerHost": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.AddHdNodeGroup({"data1": "data1", "data2": "data2"})
    client._get.assert_called_with(
        "AddHdNodeGroup",
        params={"data": {"data1": "data1", "data2": "data2"}},
        delimiter=",",
    )
    assert response == success_response


def test_add_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.AddIps("ipfrom", "ipto", "regions")
    client._get.assert_called_with(
        "AddIps",
        params={
            "ipfrom": "ipfrom",
            "ipto": "ipto",
            "region": "regions",
        },
    )
    assert response == success_response


def test_add_ipv6_network(client):
    client._get.return_value = success_response
    response = client.Cluster.AddIpv6Network("region", ["network1", "network2"])
    client._get.assert_called_with(
        "AddIpv6Network",
        params={"region": "region", "network": ["network1", "network2"]},
        delimiter=",",
    )
    assert response == success_response


def test_add_nameserver(client):
    client._get.return_value = success_response
    response = client.Cluster.AddNameserver(1, "nameserver")
    client._get.assert_called_with(
        "AddNameserver",
        params={
            "nodeId": 1,
            "nameserver": "nameserver",
        },
    )
    assert response == success_response


def test_add_region(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegion(
        {"data1": "data1", "data2": "data2"}, [True, False]
    )
    client._get.assert_called_with(
        "AddRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": [True, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionDomain(1, "domain", [True, False])
    client._get.assert_called_with(
        "AddRegionDomain",
        params={"regionId": 1, "domain": "domain", "primary": [True, False]},
        delimiter=",",
    )
    assert response == success_response


def test_add_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionReseller(
        1,
        "domain",
        "type",
        True,
        ["ssl_type1", "ssl_type2"],
        [1, 2],
        ["key1", "key2"],
        ["intermediate1", "intermediate2"],
        ["cert1", "cert2"],
        ["source5021", "source5022"],
    )
    client._get.assert_called_with(
        "AddRegionReseller",
        params={
            "resellerId": 1,
            "domain": "domain",
            "type": "type",
            "generateDns": True,
            "sslType": ["ssl_type1", "ssl_type2"],
            "regionId": [1, 2],
            "key": ["key1", "key2"],
            "intermediate": ["intermediate1", "intermediate2"],
            "cert": ["cert1", "cert2"],
            "source502": ["source5021", "source5022"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.AddRegionSsl(
        1,
        "ssl_type",
        [1, 2],
        ["cert_key1", "cert_keyt2"],
        ["intermediate1", "intermediate2"],
        ["cert1", "cert2"],
    )
    client._get.assert_called_with(
        "AddRegionSsl",
        params={
            "regionId": 1,
            "sslType": "ssl_type",
            "domainId": [1, 2],
            "cert_key": ["cert_key1", "cert_keyt2"],
            "intermediate": ["intermediate1", "intermediate2"],
            "cert": ["cert1", "cert2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_template(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplate(
        1,
        "repository",
        "tags",
        "nodeType",
        "nodeMission",
        "displayName",
        ["engine_type1", "engine_type2"],
        ["images_data1", "images_data2"],
        ["auto_update1", "auto_update2"],
        [True, False],
        [True, False],
        ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"],
    )
    client._get.assert_called_with(
        "AddTemplate",
        params={
            "registryId": 1,
            "repository": "repository",
            "tags": "tags",
            "nodeType": "nodeType",
            "nodeMission": "nodeMission",
            "displayName": "displayName",
            "engineType": ["engine_type1", "engine_type2"],
            "imagesData": ["images_data1", "images_data2"],
            "autoUpdate": ["auto_update1", "auto_update2"],
            "keepSelectedTags": [True, False],
            "updateDefaultTag": [True, False],
            "skipTagsFromAutoUpdate": [
                "skip_tags_from_auto_update1",
                "skip_tags_from_auto_update2",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.AddTemplateRegistry("data")
    client._get.assert_called_with(
        "AddTemplateRegistry",
        params={"data": "data"},
        delimiter=",",
    )
    assert response == success_response


def test_add_user_to_container(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUserToContainer(
        ["node_id1", "node_id2"], ["container_id1", "container_id2"], [True, True]
    )
    client._get.assert_called_with(
        "AddUserToContainer",
        params={
            "nodeId": ["node_id1", "node_id2"],
            "containerId": ["container_id1", "container_id2"],
            "regenerateKeys": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_users_to_gate(client):
    client._get.return_value = success_response
    response = client.Cluster.AddUsersToGate()
    client._get.assert_called_with(
        "AddUsersToGate",
        params={},
    )
    assert response == success_response


def test_apply_firewall_rules(client):
    client._get.return_value = success_response
    response = client.Cluster.ApplyFirewallRules()
    client._get.assert_called_with(
        "ApplyFirewallRules",
        params={},
    )
    assert response == success_response


def test_check_migration_env_possibility(client):
    client._get.return_value = success_response
    response = client.Cluster.CheckMigrationEnvPossibility(
        ["target_appid1", "target_appid2"],
        ["hardware_node_group1", "hardware_node_group2"],
    )
    client._get.assert_called_with(
        "CheckMigrationEnvPossibility",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "hardwareNodeGroup": ["hardware_node_group1", "hardware_node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_clean_template_manifest_cache(client):
    client._get.return_value = success_response
    response = client.Cluster.CleanTemplateManifestCache()
    client._get.assert_called_with(
        "CleanTemplateManifestCache",
        params={},
    )
    assert response == success_response


def test_clear_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.ClearPool([1, 2])
    client._get.assert_called_with(
        "ClearPool",
        params={"hnid": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_convert_passwords(client):
    client._get.return_value = success_response
    response = client.Cluster.ConvertPasswords()
    client._get.assert_called_with(
        "ConvertPasswords",
        params={},
    )
    assert response == success_response


def test_deactivate_region_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.DeactivateRegionDomain(1, 2)
    client._get.assert_called_with(
        "DeactivateRegionDomain",
        params={"regionId": 1, "domainId": 2},
    )
    assert response == success_response


def test_delete_env(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnv("target_appid", "password")
    client._get.assert_called_with(
        "DeleteEnv",
        params={"targetAppid": "target_appid", "password": "password"},
    )
    assert response == success_response


def test_delete_envs_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByChecksum(1, "target_appid")
    client._get.assert_called_with(
        "DeleteEnvsByChecksum",
        params={
            "uid": 1,
            "targetAppid": "target_appid",
        },
    )
    assert response == success_response


def test_delete_envs_by_uid_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteEnvsByUidByChecksum(1)
    client._get.assert_called_with(
        "DeleteEnvsByUidByChecksum",
        params={
            "uid": 1,
        },
    )
    assert response == success_response


def test_delete_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.DeleteHDNode(1, [True, True])
    client._get.assert_called_with(
        "DeleteHDNode",
        params={"hdnodeid": 1, "force": [True, True]},
        delimiter=",",
    )
    assert response == success_response


def test_edit_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNode(
        {"hdnode1": "hdnode1", "hdnode2": "hdnode2"}, [True, True]
    )
    client._get.assert_called_with(
        "EditHdNode",
        params={
            "hdnode": {"hdnode1": "hdnode1", "hdnode2": "hdnode2"},
            "set_as_docker_host": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.EditHdNodeGroup({"data1": "data1", "data2": "data2"})
    client._get.assert_called_with(
        "EditHdNodeGroup",
        params={"data": {"data1": "data1", "data2": "data2"}},
        delimiter=",",
    )
    assert response == success_response


def test_edit_region(client):
    client._get.return_value = success_response
    response = client.Cluster.EditRegion(
        {"data1": "data1", "data2": "data2"}, [True, True]
    )
    client._get.assert_called_with(
        "EditRegion",
        params={
            "data": {"data1": "data1", "data2": "data2"},
            "testAuthentication": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_template(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplate(
        "node_type",
        ["tags1", "tags2"],
        ["display_name1", "display_name2"],
        ["engine_type1", "engine_type2"],
        ["images_data1", "images_data2"],
        [True, True],
        [True, True],
        [False, False],
        ["skip_tags_from_auto_update1", "skip_tags_from_auto_update2"],
    )
    client._get.assert_called_with(
        "EditTemplate",
        params={
            "nodeType": "node_type",
            "tags": ["tags1", "tags2"],
            "displayName": ["display_name1", "display_name2"],
            "engineType": ["engine_type1", "engine_type2"],
            "imagesData": ["images_data1", "images_data2"],
            "autoUpdate": [True, True],
            "keepSelectedTags": [True, True],
            "updateDefaultTag": [False, False],
            "skipTagsFromAutoUpdate": [
                "skip_tags_from_auto_update1",
                "skip_tags_from_auto_update2",
            ],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.EditTemplateRegistry("data")
    client._get.assert_called_with(
        "EditTemplateRegistry",
        params={"data": "data"},
    )
    assert response == success_response


def test_evacuate_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.EvacuateContainers(
        "source_hn_id",
        ["possible_target_node_id1", "possible_target_node_id2"],
        [True, True],
    )
    client._get.assert_called_with(
        "EvacuateContainers",
        params={
            "sourceHnId": "source_hn_id",
            "possibleTargetNodeIds": [
                "possible_target_node_id1",
                "possible_target_node_id2",
            ],
            "isOnline": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_hn_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHnCMD(
        "cmd",
        ["hn_id1", "hn_id2"],
        [True, True],
        [True, True],
        ["vz_version1", "vz_version2"],
        [True, True],
    )
    client._get.assert_called_with(
        "ExecHnCMD",
        params={
            "cmd": "cmd",
            "hnId": ["hn_id1", "hn_id2"],
            "infraOnly": [True, True],
            "runOnBroken": [True, True],
            "vzVersion": ["vz_version1", "vz_version2"],
            "dockerHostOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_exec_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.ExecHostCmd(
        "cmd",
        [1, 2],
        [True, True],
        [True, True],
        ["vz_version1", "vz_version2"],
        [True, True],
    )
    client._get.assert_called_with(
        "ExecHostCmd",
        params={
            "cmd": "cmd",
            "hostId": [1, 2],
            "infraOnly": [True, True],
            "runOnBroken": [True, True],
            "vzVersion": ["vz_version1", "vz_version2"],
            "dockerHostOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_generate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.GeneratePool(
        ["node_type1", "node_type2"],
        [1, 1],
    )
    client._get.assert_called_with(
        "GeneratePool",
        params={
            "nodeType": ["node_type1", "node_type2"],
            "hnId": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_add_hd_node_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHdNodeCmd(["hard_node_group1", "hard_node_group2"])
    client._get.assert_called_with(
        "GetAddHdNodeCmd",
        params={"hardNodeGroup": ["hard_node_group1", "hard_node_group2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_add_host_cmd(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAddHostCmd(["hostGroup1", "hostGroup2"])
    client._get.assert_called_with(
        "GetAddHostCmd",
        params={"hostGroup": ["hostGroup1", "hostGroup2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_all_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllContainers()
    client._get.assert_called_with(
        "GetAllContainers",
        params={},
    )
    assert response == success_response


def test_get_all_resellers(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllRegionReseller()
    client._get.assert_called_with(
        "GetAllRegionReseller",
        params={},
    )
    assert response == success_response


def test_get_all_sum_stat_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAllSumStatByUid(
        [1, 2], [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()], [1, 1]
    )
    client._get.assert_called_with(
        "GetAllSumStatByUid",
        params={
            "duration": [1, 2],
            "endtime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "uid": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_appid_by_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.GetAppidByDomain(["domain1", "domain2"])
    client._get.assert_called_with(
        "GetAppidByDomain",
        params={"domain": ["domain1", "domain2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_billable_items(client):
    client._get.return_value = success_response
    response = client.Cluster.GetBillableItems()
    client._get.assert_called_with(
        "GetBillableItems",
        params={},
    )
    assert response == success_response


def test_get_cluster_load_history(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadHistory(
        [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        [
            CURRENT_DATETIME.date(),
            CURRENT_DATETIME.date(),
        ],
    )
    client._get.assert_called_with(
        "GetClusterLoadHistory",
        params={
            "starttime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "endtime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        },
    )
    assert response == success_response


def test_get_cluster_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadInfo()
    client._get.assert_called_with(
        "GetClusterLoadInfo",
        params={},
    )
    assert response == success_response


def test_get_cluster_load_percent(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterLoadPercent("checksum")
    client._get.assert_called_with(
        "GetClusterLoadPercent",
        params={"checksum": "checksum"},
    )
    assert response == success_response


def test_get_cluster_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterStatus([True, True], [False, False])
    client._get.assert_called_with(
        "GetClusterStatus",
        params={"checkSMTP": [True, True], "cached": [False, False]},
        delimiter=",",
    )
    assert response == success_response


def test_get_cluster_usage(client):
    client._get.return_value = success_response
    response = client.Cluster.GetClusterUsage()
    client._get.assert_called_with(
        "GetClusterUsage",
        params={},
    )
    assert response == success_response


def test_get_container_config(client):
    client._get.return_value = success_response
    response = client.Cluster.GetContainerConfig(10)
    client._get.assert_called_with(
        "GetContainerConfig",
        params={"nodeId": 10},
    )
    assert response == success_response


def test_get_default_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultRegion()
    client._get.assert_called_with(
        "GetDefaultRegion",
        params={},
    )
    assert response == success_response


def test_get_default_tag_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDefaultTagInfo("node_type", ["engine1", "engine2"])
    client._get.assert_called_with(
        "GetDefaultTagInfo",
        params={"nodeType": "node_type", "engine": ["engine1", "engine2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_default_tag_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetDomainByIp("ips")
    client._get.assert_called_with(
        "GetDomainByIp",
        params={
            "ips": "ips",
        },
    )
    assert response == success_response


def test_get_engine_types(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEngineTypes()
    client._get.assert_called_with(
        "GetEngineTypes",
        params={},
    )
    assert response == success_response


def test_get_env_groups_by_uid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvGroupsByUid(1)
    client._get.assert_called_with(
        "GetEnvGroupsByUid",
        params={"uid": 1},
    )
    assert response == success_response


def test_get_env_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvInfo("target_appid")
    client._get.assert_called_with(
        "GetEnvInfo",
        params={"targetAppid": "target_appid"},
    )
    assert response == success_response


def test_get_env_stat(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvStat(
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
    )
    client._get.assert_called_with(
        "GetEnvStat",
        params={
            "starttime": CURRENT_DATETIME.date(),
            "endtime": CURRENT_DATETIME.date(),
        },
    )
    assert response == success_response


def test_get_environment_group_populations(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvironmentGroupPopulations(
        CURRENT_DATETIME.date(), CURRENT_DATETIME.date()
    )
    client._get.assert_called_with(
        "GetEnvironmentGroupPopulations",
        params={"start": CURRENT_DATETIME.date(), "end": CURRENT_DATETIME.date()},
    )
    assert response == success_response


def test_get_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEnvs(
        1, ["rights1", "rights2"], [True, True], [1, 2], [True, True]
    )
    client._get.assert_called_with(
        "GetEnvs",
        params={
            "uid": 1,
            "rights": ["rights1", "rights2"],
            "lazy": [True, True],
            "ownerUid": [1, 2],
            "sshAccessOnly": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_evacuation_state(client):
    client._get.return_value = success_response
    response = client.Cluster.GetEvacuationState(1)
    client._get.assert_called_with(
        "GetEvacuationState",
        params={"hardNodeId": 1},
    )
    assert response == success_response


def test_get_ext_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetExtIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetExtIpPoolInfo",
        params={"search": {"search1": "search1", "search2": "search2"}},
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_node_groups(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeGroups()
    client._get.assert_called_with(
        "GetHdNodeGroups",
        params={},
    )
    assert response == success_response


def test_get_hd_node_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodeStatus()
    client._get.assert_called_with(
        "GetHdNodeStatus",
        params={},
    )
    assert response == success_response


def test_get_hd_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodes(["id1", "id2"])
    client._get.assert_called_with(
        "GetHdNodes",
        params={"ids": ["id1", "id2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_nodes_load(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoad(1, ["hdnodes1", "hdnodes2"])
    client._get.assert_called_with(
        "GetHdNodesLoad",
        params={"duration": 1, "hdnodes": ["hdnodes1", "hdnodes2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_hd_load_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHdNodesLoadInfo(["id1", "id2"])
    client._get.assert_called_with(
        "GetHdNodesLoadInfo",
        params={"ids": ["id1", "id2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_hosts(client):
    client._get.return_value = success_response
    response = client.Cluster.GetHosts(["id1", "id2"])
    client._get.assert_called_with(
        "GetHosts",
        params={"ids": ["id1", "id2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_ip_pool_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpPoolInfo(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetIpPoolInfo",
        params={"search": {"search1": "search1", "search2": "search2"}},
        delimiter=",",
    )
    assert response == success_response


def test_get_ipv6_networks(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6Networks()
    client._get.assert_called_with(
        "GetIpv6Networks",
        params={},
    )
    assert response == success_response


def test_get_ipv6_subnets_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetIpv6SubnetsInfo(["search1", "search2"])
    client._get.assert_called_with(
        "GetIpv6SubnetsInfo",
        params={"search": ["search1", "search2"]},
        delimiter=",",
    )
    assert response == success_response


def test_get_jelastic_appid(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJelasticAppid()
    client._get.assert_called_with(
        "GetJelasticAppid",
        params={},
    )
    assert response == success_response


def test_get_job_names(client):
    client._get.return_value = success_response
    response = client.Cluster.GetJobNames()
    client._get.assert_called_with(
        "GetJobNames",
        params={},
    )
    assert response == success_response


def test_get_last_hard_ware_node_message(client):
    client._get.return_value = success_response
    response = client.Cluster.GetLastHardWareNodeMessage(1)
    client._get.assert_called_with(
        "GetLastHardWareNodeMessage",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodeInfo("target_appid", 1)
    client._get.assert_called_with(
        "GetNodeInfo",
        params={
            "targetAppid": "target_appid",
            "nodeId": 1,
        },
    )
    assert response == success_response


def test_get_node_missions(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodeMissions()
    client._get.assert_called_with(
        "GetNodeMissions",
        params={},
    )
    assert response == success_response


def test_get_node_password(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodePassword([1, 2])
    client._get.assert_called_with(
        "GetNodePassword",
        params={"nodeid": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_get_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetNodes(1, ["name1", "name2"], [1, 2], [1, 1])
    client._get.assert_called_with(
        "GetNodes",
        params={
            "hdnodeid": 1,
            "name": ["name1", "name2"],
            "startRow": [1, 2],
            "resultCount": [1, 1],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_oom_killed_processes(client):
    client._get.return_value = success_response
    response = client.Cluster.GetOOMKilledProcesses(
        {"search1": "search1", "search2": "search2"}
    )
    client._get.assert_called_with(
        "GetOOMKilledProcesses",
        params={"search": {"search1": "search1", "search2": "search2"}},
        delimiter=",",
    )
    assert response == success_response


def test_get_pcs_cluster_list(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPcsClusterList()
    client._get.assert_called_with(
        "GetPcsClusterList",
        params={},
    )
    assert response == success_response


def test_get_pool_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetPoolStatus()
    client._get.assert_called_with(
        "GetPoolStatus",
        params={},
    )
    assert response == success_response


def test_get_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegion(1)
    client._get.assert_called_with(
        "GetRegion",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_dns_records(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDnsRecords(1)
    client._get.assert_called_with(
        "GetRegionDnsRecords",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region_domains(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionDomains([1, 2])
    client._get.assert_called_with(
        "GetRegionDomains",
        params={"regionId": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_get_region_reseller_by_reseller_id(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegionResellerByResellerId(1)
    client._get.assert_called_with(
        "GetRegionResellerByResellerId",
        params={
            "id": 1,
        },
    )
    assert response == success_response


def test_get_region(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRegions()
    client._get.assert_called_with(
        "GetRegions",
        params={},
    )
    assert response == success_response


def test_get_repository_tags(client):
    client._get.return_value = success_response
    response = client.Cluster.GetRepositoryTags([1, 2], ["repository1", "repository2"])
    client._get.assert_called_with(
        "GetRepositoryTags",
        params={
            "registryId": [1, 2],
            "repository": ["repository1", "repository2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_soft_node_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSoftNodeInfo(1)
    client._get.assert_called_with(
        "GetSoftNodeInfo",
        params={"nodeId": 1},
    )
    assert response == success_response


def test_get_stand_by_status(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStandByStatus()
    client._get.assert_called_with(
        "GetStandByStatus",
        params={},
    )
    assert response == success_response


def test_get_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetStats(
        1,
        1,
        "target_appid",
        [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        [1, 2],
        ["nodetype1", "nodetype2"],
        ["node_group1", "node_group2"],
    )
    client._get.assert_called_with(
        "GetStats",
        params={
            "duration": 1,
            "interval": 1,
            "targetAppid": "target_appid",
            "endtime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "nodeid": [1, 2],
            "nodetype": ["nodetype1", "nodetype2"],
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_sum_stats(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSumStat(
        [1, 2],
        [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        ["target_appid1", "target_appid2"],
    )
    client._get.assert_called_with(
        "GetSumStat",
        params={
            "duration": [1, 2],
            "endtime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "targetAppid": ["target_appid1", "target_appid2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_system_log(client):
    client._get.return_value = success_response
    response = client.Cluster.GetSystemLog("search")
    client._get.assert_called_with(
        "GetSystemLog",
        params={"search": "search"},
    )
    assert response == success_response


def test_get_template_info(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateInfo("node_type")
    client._get.assert_called_with(
        "GetTemplateInfo",
        params={"nodeType": "node_type"},
    )
    assert response == success_response


def test_get_template_labels(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateLabels("repository", [1, 2], ["tag1", "tag2"])
    client._get.assert_called_with(
        "GetTemplateLabels",
        params={
            "repository": "repository",
            "registryId": [1, 2],
            "tag": ["tag1", "tag2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_template_registries(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplateRegistries()
    client._get.assert_called_with(
        "GetTemplateRegistries",
        params={},
    )
    assert response == success_response


def test_get_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.GetTemplates(
        ["type1", "type2"], [True, True], [False, False]
    )
    client._get.assert_called_with(
        "GetTemplates",
        params={
            "type": ["type1", "type2"],
            "published": [True, True],
            "lazy": [False, False],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_user_activity(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUserActivity(
        1,
        CURRENT_DATETIME.date(),
        CURRENT_DATETIME.date(),
        ["target_appid1", "target_appid2"],
        ["start_row1", "start_row2"],
        [1, 2],
        ["service_name1", "service_name2"],
        ["search_text1", "search_text2"],
        ["action_types1", "action_types2"],
        ["order_field1", "order_field2"],
        ["order_direction1", "order_direction2"],
    )
    client._get.assert_called_with(
        "GetUserActivity",
        params={
            "uid": 1,
            "starttime": CURRENT_DATETIME.date(),
            "endtime": CURRENT_DATETIME.date(),
            "targetAppid": ["target_appid1", "target_appid2"],
            "startRow": ["start_row1", "start_row2"],
            "resultCount": [1, 2],
            "serviceName": ["service_name1", "service_name2"],
            "searchText": ["search_text1", "search_text2"],
            "actionTypes": ["action_types1", "action_types2"],
            "orderField": ["order_field1", "order_field2"],
            "orderDirection": ["order_direction1", "order_direction2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_user_activities(client):
    client._get.return_value = success_response
    response = client.Cluster.GetUsersActivities(
        CURRENT_DATETIME.date(), CURRENT_DATETIME.date(), [1, 2], [1, 2]
    )
    client._get.assert_called_with(
        "GetUsersActivities",
        params={
            "starttime": CURRENT_DATETIME.date(),
            "endtime": CURRENT_DATETIME.date(),
            "startRow": [1, 2],
            "resultCount": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_l2_update(client):
    client._get.return_value = success_response
    response = client.Cluster.L2Update(1)
    client._get.assert_called_with(
        "L2Update",
        params={
            "hnId": 1,
        },
    )
    assert response == success_response


def test_migrate_env(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateEnv(
        ["target_appid1", "target_appid2"],
        ["hardware_node_group1", "hardware_node_group2"],
        [True, True],
    )
    client._get.assert_called_with(
        "MigrateEnv",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "hardwareNodeGroup": ["hardware_node_group1", "hardware_node_group2"],
            "isOnline": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_migrate_node(client):
    client._get.return_value = success_response
    response = client.Cluster.MigrateNode(1, 1, [True, True], [True, True])
    client._get.assert_called_with(
        "MigrateNode",
        params={
            "nodeid": 1,
            "hdnodeid": 1,
            "isOnline": [True, True],
            "manageDNSState": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_redeploy_containers(client):
    client._get.return_value = success_response
    response = client.Cluster.RedeployContainers(
        "target_env_name",
        "tag",
        ["node_group1", "node_group2"],
        [1, 2],
        [True, True],
        ["login1", "login2"],
        ["password1", "password2"],
        [True, True],
    )
    client._get.assert_called_with(
        "RedeployContainers",
        params={
            "targetEnvName": "target_env_name",
            "tag": "tag",
            "nodeGroup": ["node_group1", "node_group2"],
            "nodeId": [1, 2],
            "useExistingVolumes": [True, True],
            "login": ["login1", "login2"],
            "password": ["password1", "password2"],
            "skipReinstall": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_refresh_email_templates(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshEmailTemplates("modules")
    client._get.assert_called_with(
        "RefreshEmailTemplates",
        params={"modules": "modules"},
    )
    assert response == success_response


def test_refresh_user(client):
    client._get.return_value = success_response
    response = client.Cluster.RefreshUser(["language1", "language2"])
    client._get.assert_called_with(
        "RefreshUser",
        params={"language": ["language1", "language2"]},
        delimiter=",",
    )
    assert response == success_response


def test_regenerate_pool(client):
    client._get.return_value = success_response
    response = client.Cluster.RegeneratePool("node_type", ["exclude1", "exclude2"])
    client._get.assert_called_with(
        "RegeneratePool",
        params={"nodeType": "node_type", "exclude": ["exclude1", "exclude2"]},
        delimiter=",",
    )
    assert response == success_response


def test_register_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.RegisterInfaModule(
        ["module1", "module2"], ["dst_env_name1", "dst_env_name2"], [True, True]
    )
    client._get.assert_called_with(
        "RegisterInfaModule",
        params={
            "module": ["module1", "module2"],
            "dstEnvName": ["dst_env_name1", "dst_env_name2"],
            "dryRun": [True, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_ext_ips(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveExtIps(["ips1", "ips2"])
    client._get.assert_called_with(
        "RemoveExtIps",
        params={"ips": ["ips1", "ips2"]},
        delimiter=",",
    )
    assert response == success_response


def test_remove_hd_node_group(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveHdNodeGroup(1)
    client._get.assert_called_with(
        "RemoveHdNodeGroup",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_ipv6_network(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveIpv6Network(1)
    client._get.assert_called_with(
        "RemoveIpv6Network",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_region(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegion(1)
    client._get.assert_called_with(
        "RemoveRegion",
        params={"id": 1},
    )
    assert response == success_response


def test_remove_region_reseller(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionReseller(1, True, [1, 2])
    client._get.assert_called_with(
        "RemoveRegionReseller",
        params={"resellerId": 1, "dstEnvName": True, "regionId": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_remove_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveRegionSsl([1, 2], [1, 2], 1)
    client._get.assert_called_with(
        "RemoveRegionSsl",
        params={
            "regionId": [1, 2],
            "domainId": [1, 2],
            "resellerId": 1,
        },
        delimiter=",",
    )
    assert response == success_response


def test_remove_region(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplate("node_type")
    client._get.assert_called_with(
        "RemoveTemplate",
        params={"nodeType": "node_type"},
    )
    assert response == success_response


def test_remove_template_registry(client):
    client._get.return_value = success_response
    response = client.Cluster.RemoveTemplateRegistry(1)
    client._get.assert_called_with(
        "RemoveTemplateRegistry",
        params={"id": 1},
    )
    assert response == success_response


def test_replace_node_in_env(client):
    client._get.return_value = success_response
    response = client.Cluster.ReplaceNodeInEnv(
        ["dst_env_name1", "dst_env_name2"],
        [1, 2],
        ["src_env_id1", "src_env_id2"],
        [1, 2],
    )
    client._get.assert_called_with(
        "ReplaceNodeInEnv",
        params={
            "dstEnvName": ["dst_env_name1", "dst_env_name2"],
            "dstNodeId": [1, 2],
            "srcEnvId": ["src_env_id1", "src_env_id2"],
            "srcHnId": [1, 2],
        },
        delimiter=",",
    )
    assert response == success_response


def test_revive_install_hd_node(client):
    client._get.return_value = success_response
    response = client.Cluster.ReviveInstallHdNode(1)
    client._get.assert_called_with(
        "ReviveInstallHdNode",
        params={"id": 1},
    )
    assert response == success_response


def test_search_envs(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchEnvs({"search1": "search1", "search2": "search2"})
    client._get.assert_called_with(
        "SearchEnvs",
        params={"search": {"search1": "search1", "search2": "search2"}},
        delimiter=",",
    )
    assert response == success_response


def test_search_nodes(client):
    client._get.return_value = success_response
    response = client.Cluster.SearchNodes({"search1": "search1", "search2": "search2"})
    client._get.assert_called_with(
        "SearchNodes",
        params={"search": {"search1": "search1", "search2": "search2"}},
        delimiter=",",
    )
    assert response == success_response


def test_set_default_template_tag(client):
    client._get.return_value = success_response
    response = client.Cluster.SetDefaultTemplateTag("node_type", "tag")
    client._get.assert_called_with(
        "SetDefaultTemplateTag",
        params={"nodeType": "node_type", "tag": "tag"},
    )
    assert response == success_response


def test_set_env_note(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvNote(
        ["target_appid1", "target_appid2"], ["note1", "note2"]
    )
    client._get.assert_called_with(
        "SetEnvNote",
        params={
            "targetAppid": ["target_appid1", "target_appid2"],
            "note": ["note1", "note2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvStatus("target_appid", 1)
    client._get.assert_called_with(
        "SetEnvStatus",
        params={"targetAppid": "target_appid", "status": 1},
    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatus("target_appid", 1)
    client._get.assert_called_with(
        "SetEnvsStatus",
        params={"targetAppid": "target_appid", "status": 1},
    )
    assert response == success_response


def test_set_env_status(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatusByUid(1, 1)
    client._get.assert_called_with(
        "SetEnvsStatusByUid",
        params={
            "uid": 1,
            "status": 1,
        },
    )
    assert response == success_response


def test_set_envs_status_by_uid_by_checksum(client):
    client._get.return_value = success_response
    response = client.Cluster.SetEnvsStatusByUidByChecksum(1, 1)
    client._get.assert_called_with(
        "SetEnvsStatusByUidByChecksum",
        params={
            "uid": 1,
            "status": 1,
        },
    )
    assert response == success_response


def test_set_region_dns_records(client):
    client._get.return_value = success_response
    response = client.Cluster.SetRegionDnsRecords(
        1,
        1,
    )
    client._get.assert_called_with(
        "SetRegionDnsRecords",
        params={
            "id": 1,
            "data": 1,
        },
    )
    assert response == success_response


def test_set_region_primary_domain(client):
    client._get.return_value = success_response
    response = client.Cluster.SetRegionPrimaryDomain(1, 1)
    client._get.assert_called_with(
        "SetRegionPrimaryDomain",
        params={
            "regionId": 1,
            "domainId": 1,
        },
    )
    assert response == success_response


def test_set_stand_by_mode(client):
    client._get.return_value = success_response
    response = client.Cluster.SetStandbyMode(True)
    client._get.assert_called_with(
        "SetStandbyMode",
        params={
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_template_published(client):
    client._get.return_value = success_response
    response = client.Cluster.SetTemplatePublished("node type", True)
    client._get.assert_called_with(
        "SetTemplatePublished",
        params={"nodeType": "node type", "published": True},
    )
    assert response == success_response


def test_sleep(client):
    client._get.return_value = success_response
    response = client.Cluster.Sleep(
        [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "Sleep",
        params={
            "starttime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "endtime": [CURRENT_DATETIME.date(), CURRENT_DATETIME.date()],
            "deactivateAfter": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response


def test_start_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StartEnv("target")
    client._get.assert_called_with(
        "StartEnv(",
        params={
            "targetAppid": "target",
        },
    )
    assert response == success_response


def test_stop_balance_resources(client):
    client._get.return_value = success_response
    response = client.Cluster.StopBalanceResources()
    client._get.assert_called_with(
        "StopBalanceResources(",
        params={},
    )
    assert response == success_response


def test_stop_env(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEnv("target")
    client._get.assert_called_with(
        "StopEnv(",
        params={
            "targetAppid": "target",
        },
    )
    assert response == success_response


def test_stop_evacuation(client):
    client._get.return_value = success_response
    response = client.Cluster.StopEvacuation("hard node")
    client._get.assert_called_with(
        "StopEvacuation",
        params={
            "hardNodeId": "hard node",
        },
    )
    assert response == success_response


def test_sync_cloud_lets(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncCloudlets(
        CURRENT_DATETIME.date(),
        [True, False, True],
    )
    client._get.assert_called_with(
        "SyncCloudlets(",
        params={
            "starttime": CURRENT_DATETIME.date(),
            "debug": [True, False, True],
        },
    )
    assert response == success_response


def test_sync_infa_module(client):
    client._get.return_value = success_response
    response = client.Cluster.SyncInfaModule(
        "node group",
        "dst env",
        "components",
        ["tag1", "tag2", "tag3"],
    )
    client._get.assert_called_with(
        "SyncInfaModule",
        params={
            "nodeGroup": "node group",
            "dstEnvName": "dst env",
            "components": "components",
            "targetTag": ["tag1", "tag2", "tag3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_update_region_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateRegionSsl(
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "UpdateRegionSsl",
        params={
            "regionId": 1,
            "domainId": [1, 2, 3, 4],
        },
    )
    assert response == success_response


def test_update_reseller_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateResellerSsl(1, 1)
    client._get.assert_called_with(
        "UpdateResellerSsl",
        params={
            "regionId": 1,
            "resellerId": 1,
        },
    )
    assert response == success_response


def test_update_template(client):
    client._get.return_value = success_response
    response = client.Cluster.UpdateTemplate(
        1,
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "UpdateTemplate",
        params={
            "nodeType": 1,
            "iconsOnly": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_validate(client):
    client._get.return_value = success_response
    response = client.Cluster.Validate()
    client._get.assert_called_with(
        "Validate",
        params={},
    )
    assert response == success_response


def test_velidate_all(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateAll()
    client._get.assert_called_with(
        "ValidateAll",
        params={},
    )
    assert response == success_response


def test_validate_ssl(client):
    client._get.return_value = success_response
    response = client.Cluster.ValidateSsl(
        "domain",
        ["key1", "key2", "key3"],
        ["intermediate1", "intermediate2", "intermediate3"],
        ["certificate1", "certificate2", "certificate3"],
    )
    client._get.assert_called_with(
        "ValidateSsl",
        params={
            "domain": "domain",
            "key": ["key1", "key2", "key3"],
            "intermediate": ["intermediate1", "intermediate2", "intermediate3"],
            "cert": ["certificate1", "certificate2", "certificate3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_virtual_network(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.AddVirtualNetwork(
        {
            "networkName1": "name1",
            "networkName2": "name2",
            "networkName3": "name3",
            "networkName4": "name4",
            "networkName5": "name5",
        },
    )
    client._get.assert_called_with(
        "AddVirtualNetwork",
        params={
            "virtualNetwork": {
                "networkName1": "name1",
                "networkName2": "name2",
                "networkName3": "name3",
                "networkName4": "name4",
                "networkName5": "name5",
            },
        },
        delimiter=",",
    )
    assert response == success_response


def test_apply_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.ApplyVirtualNetworks(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "ApplyVirtualNetworks",
        params={
            "hostId": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_delete_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.DeleteVirtualNetworks(1)
    client._get.assert_called_with(
        "DeleteVirtualNetworks",
        params={
            "ids": 1,
        },
    )
    assert response == success_response


def test_get_virtual_networks(client):
    client._get.return_value = success_response
    response = client.VirtualNetwork.GetVirtualNetworks(
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "GetVirtualNetworks",
        params={
            "ids": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response
