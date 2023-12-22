from datetime import datetime
from unittest.mock import patch, Mock

import pytest

from jelastic.api import Development

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}
CURRENT_DATETIME = datetime.now()


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        development = Development(session=Mock(), token="token")
        development._get = mock_get
        yield development


def test_add_app_to_pool(client):
    client._get.return_value = success_response
    response = client.Applications.AddAppToPool(
          "name","target_appid",
    )
    client._get.assert_called_with(
        "AddAppToPool",
        params={
             "name": "name",
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_allow_app_access(client):
    client._get.return_value = success_response
    response = client.Applications.AllowAppAccess(
       "target_appid","allow_appid"
    )
    client._get.assert_called_with(
        "AllowAppAccess",
        params={
             "targetAppid": "target_appid",
             "allowAppid": "allow_appid",
        }, delimiter=",",
    )
    assert response == success_response
def test_change_app_info(client):
    client._get.return_value = success_response
    response = client.Applications.ChangeAppInfo(
       "target_appid","field",["value1","value2"]
    )
    client._get.assert_called_with(
        "ChangeAppInfo",
        params={
             "targetAppid": "target_appid",
              "field": "field",
              "value": ["value1","value2"]
        }, delimiter=",",
    )
    assert response == success_response
def test_solution_app_info(client):
    client._get.return_value = success_response
    response = client.Applications.ChangeSolutionInfo(
       "target_appid","field","value"
    )
    client._get.assert_called_with(
        "ChangeSolutionInfo",
        params={
             "targetAppid": "target_appid",
              "field": "field",
              "value":"value"
        },
    )
    assert response == success_response
def test_clean_owner_cache(client):
    client._get.return_value = success_response
    response = client.Applications.CleanOwnerCache(
       1,True
    )
    client._get.assert_called_with(
        "CleanOwnerCache",
        params={
               "userId": 1,
                "cleanAllApps": True,
        },
    )
    assert response == success_response
def test_clone_app(client):
    client._get.return_value = success_response
    response = client.Applications.CloneApp(
       "target_appid",["name2","name2"]
    )
    client._get.assert_called_with(
        "CloneApp",
        params={
             "targetAppid": "target_appid",
              "name": ["name2","name2"]
        },
    )
    assert response == success_response
def test_confirm_app_transfer_request(client):
    client._get.return_value = success_response
    response = client.Applications.ConfirmAppTransferRequest(
        "key"
    )
    client._get.assert_called_with(
        "ConfirmAppTransferRequest",
        params={
              "key": "key"
        },
    )
    assert response == success_response
def test_create_apps_pool(client):
    client._get.return_value = success_response
    response = client.Applications.CreateAppsPool(
        "name"
    )
    client._get.assert_called_with(
        "CreateAppsPool",
        params={
              "name": "name"
        },
    )
    assert response == success_response
def test_create_confirm_app_transfer_key(client):
    client._get.return_value = success_response
    response = client.Applications.CreateConfirmAppTransferKey(
        "email"
    )
    client._get.assert_called_with(
        "CreateConfirmAppTransferKey",
        params={
              "email": "email"
        },
    )
    assert response == success_response
def test_create_persistence(client):
    client._get.return_value = success_response
    response = client.Applications.CreatePersistence(
       "target_appid", ["config1","config2"]
    )
    client._get.assert_called_with(
        "CreatePersistence",
        params={
             "targetAppid": "target_appid",
              "config": ["config1","config2"]
        },delimiter=",",
    )
    assert response == success_response
def test_create_solution(client):
    client._get.return_value = success_response
    response = client.Applications.CreateSolution(
       "target_appid"
    )
    client._get.assert_called_with(
        "CreateSolution",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_delete_app(client):
    client._get.return_value = success_response
    response = client.Applications.DeleteApp(
        "password", "target_appid"
    )
    client._get.assert_called_with(
        "DeleteApp",
        params={
            "password": "password",
            "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_delete_apps_pool(client):
    client._get.return_value = success_response
    response = client.Applications.DeleteAppsPool(
        "name"
    )
    client._get.assert_called_with(
        "DeleteAppsPool",
        params={
              "name": "name"
        },
    )
    assert response == success_response
def test_delete_solution(client):
    client._get.return_value = success_response
    response = client.Applications.DeleteSolution(
       "target_appid"
    )
    client._get.assert_called_with(
        "DeleteSolution",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_export_app_persistance(client):
    client._get.return_value = success_response
    response = client.Applications.ExportAppPersistance(
       "target_appid"
    )
    client._get.assert_called_with(
        "ExportAppPersistance",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_export_app_resource(client):
    client._get.return_value = success_response
    response = client.Applications.ExportAppResources(
       "target_appid"
    )
    client._get.assert_called_with(
        "ExportAppResources",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_find_solutions(client):
    client._get.return_value = success_response
    response = client.Applications.FindSolutions(
       ["keywords1","keywords2"], ["description1","description2"],[1,1],[1,1],
    )
    client._get.assert_called_with(
        "FindSolutions",
        params={
            "keywords": ["keywords1","keywords2"],
            "description": ["description1","description2"],
            "froms": [1,1],
            "count": [1,1],
        },delimiter=",",
    )
    assert response == success_response
def test_generate_app(client):
    client._get.return_value = success_response
    response = client.Applications.GenerateApp(
       "name",["description1","description2"], ["domain1","domain2"],["keywords1","keywords2"], ["config1","config2"],
    )
    client._get.assert_called_with(
        "GenerateApp",
        params={
            "name": "name",
            "description": ["description1","description2"],
            "domain": ["domain1","domain2"],
            "keywords":["keywords1","keywords2"],
            "config": ["config1","config2"],
        },delimiter=",",
    )
    assert response == success_response
def test_generate_app_with_app_id(client):
    client._get.return_value = success_response
    response = client.Applications.GenerateAppWithAppID(
       "name","idapp",["description1","description2"], ["domain1","domain2"],["keywords1","keywords2"], ["config1","config2"],
    )
    client._get.assert_called_with(
        "GenerateAppWithAppID",
        params={
            "name": "name",
            "idapp": "idapp",
            "description": ["description1","description2"],
            "domain": ["domain1","domain2"],
            "keywords":["keywords1","keywords2"],
            "config": ["config1","config2"],
        },delimiter=",",
    )
    assert response == success_response
def test_generate_shared_app(client):
    client._get.return_value = success_response
    response = client.Applications.GenerateSharedApp(
       "owner_login","name",["description1","description2"], ["domain1","domain2"],["keywords1","keywords2"], ["config1","config2"],
    )
    client._get.assert_called_with(
        "GenerateSharedApp",
        params={
            "ownerLogin": "owner_login",
            "name": "name",
            "description": ["description1","description2"],
            "domain": ["domain1","domain2"],
            "keywords":["keywords1","keywords2"],
            "config": ["config1","config2"],
        },delimiter=",",
    )
    assert response == success_response
def test_get_app(client):
    client._get.return_value = success_response
    response = client.Applications.GetApp(
       "target_appid"
    )
    client._get.assert_called_with(
        "GetApp",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_get_app_access(client):
    client._get.return_value = success_response
    response = client.Applications.GetAppAccess(
       "target_appid"
    )
    client._get.assert_called_with(
        "GetAppAccess",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_get_app_home(client):
    client._get.return_value = success_response
    response = client.Applications.GetAppHome(
    )
    client._get.assert_called_with(
        "GetAppHome",
        params={
        }
    )
    assert response == success_response
def test_get_app_permission(client):
    client._get.return_value = success_response
    response = client.Applications.GetAppPermission(
       "target_appid"
    )
    client._get.assert_called_with(
        "GetAppPermission",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_get_apps(client):
    client._get.return_value = success_response
    response = client.Applications.GetApps(
       "target_appid"
    )
    client._get.assert_called_with(
        "GetApps",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_get_apps_by_login(client):
    client._get.return_value = success_response
    response = client.Applications.GetAppsByLogin(
       "login"
    )
    client._get.assert_called_with(
        "GetAppsByLogin",
        params={
             "login": "login",
        }
    )
    assert response == success_response
def test_get_apps_pools(client):
    client._get.return_value = success_response
    response = client.Applications.GetAppsPools(
        ["name1", "name2"],
    )
    client._get.assert_called_with(
        "GetAppsPools",
        params={
             "name": ["name1","name2"],
        },delimiter=",",
    )
    assert response == success_response
def test_get_confirm_app_transfer_key(client):
    client._get.return_value = success_response
    response = client.Applications.GetConfirmAppTransferKey(

    )
    client._get.assert_called_with(
        "GetConfirmAppTransferKey",
        params={
        }
    )
    assert response == success_response
def test_get_confirm_app_transfer_keys(client):
    client._get.return_value = success_response
    response = client.Applications.GetConfirmAppTransferKeys(
        ["appid1","appid2"]
    )
    client._get.assert_called_with(
        "GetConfirmAppTransferKeys",
        params={
             "appids": ["appid1","appid2"],
        }, delimiter=",",
    )
    assert response == success_response
def test_get_shared_apps_by_login(client):
    client._get.return_value = success_response
    response = client.Applications.GetSharedAppsByLogin(
       "login"
    )
    client._get.assert_called_with(
        "GetSharedAppsByLogin",
        params={
             "login": "login",
        }
    )
    assert response == success_response
def test_get_shared_apps_by_owner_login(client):
    client._get.return_value = success_response
    response = client.Applications.GetSharedAppsByOwnerLogin(

        "owner_login", "login"
    )
    client._get.assert_called_with(
        "GetSharedAppsByOwnerLogin",
        params={
            "ownerLogin": "owner_login",
             "login": "login",
        }
    )
    assert response == success_response
def test_get_shared_apps_by_owner_logins(client):
    client._get.return_value = success_response
    response = client.Applications.GetSharedAppsByOwnerLogins(

        "owner_login", "logins"
    )
    client._get.assert_called_with(
        "GetSharedAppsByOwnerLogins",
        params={
            "ownerLogin": "owner_login",
             "logins": "logins",
        }
    )
    assert response == success_response
def test_get_solution(client):
    client._get.return_value = success_response
    response = client.Applications.GetSolution(
       "target_appid"
    )
    client._get.assert_called_with(
        "GetSolution",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_get_solutions(client):
    client._get.return_value = success_response
    response = client.Applications.GetSolutions(
       ["target_appid1","target_appid2"]
    )
    client._get.assert_called_with(
        "GetSolutions",
        params={
             "targetAppid": ["target_appid1","target_appid2"]
        }, delimiter=",",
    )
    assert response == success_response
def test_get_user_app_permission(client):
    client._get.return_value = success_response
    response = client.Applications.GetUserAppPermission(
       "target_appid",["rights1","rights2"],
    )
    client._get.assert_called_with(
        "GetUserAppPermission",
        params={
             "targetAppid": "target_appid",
             "rights": ["rights1","rights2"],
        }
    )
    assert response == success_response
def test_import_app_persistance(client):
    client._get.return_value = success_response
    response = client.Applications.ImportAppPersistance(
        "path", ["target_appid1","target_appid2"]
    )
    client._get.assert_called_with(
        "ImportAppPersistance",
        params={
            "path": "path",
             "targetAppid": ["target_appid1","target_appid2"]
        }, delimiter=",",
    )
    assert response == success_response
def test_import_app_resources(client):
    client._get.return_value = success_response
    response = client.Applications.ImportAppResources(
        "path", ["target_appid1","target_appid2"]
    )
    client._get.assert_called_with(
        "ImportAppResources",
        params={
            "path": "path",
             "targetAppid": ["target_appid1","target_appid2"]
        }, delimiter=",",
    )
    assert response == success_response
def test_is_apps_installed(client):
    client._get.return_value = success_response
    response = client.Applications.IsAppsInstalled(
    )
    client._get.assert_called_with(
        "IsAppsInstalled",
        params={
        }
    )
    assert response == success_response
def test_rebuild_app(client):
    client._get.return_value = success_response
    response = client.Applications.RebuildApp(
       "target_appid"
    )
    client._get.assert_called_with(
        "RebuildApp",
        params={
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_remove_app_access(client):
    client._get.return_value = success_response
    response = client.Applications.RemoveAppAccess(
       "target_appid", "allow_appid"
    )
    client._get.assert_called_with(
        "RemoveAppAccess",
        params={
             "targetAppid": "target_appid",
            "allowAppid": "allow_appid"
        }
    )
    assert response == success_response
def test_rebuild_app_from_pool(client):
    client._get.return_value = success_response
    response = client.Applications.RemoveAppFromPool(
       "name","target_appid"
    )
    client._get.assert_called_with(
        "RemoveAppFromPool",
        params={
            "name":"name",
             "targetAppid": "target_appid",
        }
    )
    assert response == success_response
def test_set_app_permission(client):
    client._get.return_value = success_response
    response = client.Applications.SetAppPermission(
       "target_appid","login",["rights1","rights2"],
    )
    client._get.assert_called_with(
        "SetAppPermission",
        params={
             "targetAppid": "target_appid",
            "login":"login",
             "rights": ["rights1","rights2"],
        }, delimiter=",",
    )
    assert response == success_response