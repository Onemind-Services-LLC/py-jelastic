from . import *


def test_add_rule(client):
    client._get.return_value = success_response
    response = client.Security.AddRule(
        "env_name", {"rule1": "rule1", "rule2": "rule2"}, ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "AddRule",
        params={
            "envName": "env_name",
            "rule": {"rule1": "rule1", "rule2": "rule2"},
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_add_rules(client):
    client._get.return_value = success_response
    response = client.Security.AddRules(
        "env_name", "rule", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "AddRules",
        params={
            "envName": "env_name",
            "rules": "rule",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_edit_rule(client):
    client._get.return_value = success_response
    response = client.Security.EditRule(
        "env_name", {"rule1": "rule1", "rule2": "rule2"}
    )
    client._get.assert_called_with(
        "EditRule",
        params={
            "envName": "env_name",
            "rule": {"rule1": "rule1", "rule2": "rule2"},
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_rules(client):
    client._get.return_value = success_response
    response = client.Security.GetRules(
        "env_name", ["node_group1", "node_group2"], ["direction1", "direction2"]
    )
    client._get.assert_called_with(
        "GetRules",
        params={
            "envName": "env_name",
            "nodeGroup": ["node_group1", "node_group2"],
            "direction": ["direction1", "direction2"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_regenerate_isolation_sets(client):
    client._get.return_value = success_response
    response = client.Security.RegenerateIsolationSets()
    client._get.assert_called_with(
        "RegenerateIsolationSets",
        params={},
    )
    assert response == success_response


def test_remove_rule(client):
    client._get.return_value = success_response
    response = client.Security.RemoveRule("env_name", 1)
    client._get.assert_called_with(
        "RemoveRule",
        params={"envName": "env_name", "id": 1},
    )
    assert response == success_response


def test_remove_rules(client):
    client._get.return_value = success_response
    response = client.Security.RemoveRules("env_name", [1, 2])
    client._get.assert_called_with(
        "RemoveRules",
        params={"envName": "env_name", "ids": [1, 2]},
        delimiter=",",
    )
    assert response == success_response


def test_set_firewall_enabled(client):
    client._get.return_value = success_response
    response = client.Security.SetFirewallEnabled("env_name", True)
    client._get.assert_called_with(
        "SetFirewallEnabled",
        params={
            "envName": "env_name",
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_rule_enabled(client):
    client._get.return_value = success_response
    response = client.Security.SetRuleEnabled("env_name", 1, True)
    client._get.assert_called_with(
        "SetRuleEnabled",
        params={
            "envName": "env_name",
            "id": 1,
            "enabled": True,
        },
    )
    assert response == success_response


def test_set_rules(client):
    client._get.return_value = success_response
    response = client.Security.SetRules(
        "env_name", "rule", ["node_group1", "node_group2"]
    )
    client._get.assert_called_with(
        "SetRules",
        params={
            "envName": "env_name",
            "rules": "rule",
            "nodeGroup": ["node_group1", "node_group2"],
        },
        delimiter=",",
    )
    assert response == success_response
