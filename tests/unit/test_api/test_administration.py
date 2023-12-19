import pytest
import datetime
from unittest.mock import patch, Mock
from jelastic.api import Administration

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


def test_add_statistics(client):
    client._get.return_value = success_response
    response = client.Resource.AddStatistics(
        "resource 1",
        1,
        1234,
        [datetime.date.today(), datetime.date.today()],
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
            "startDate": [datetime.date.today(), datetime.date.today()],
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
