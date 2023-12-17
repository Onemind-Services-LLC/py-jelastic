from unittest.mock import patch, Mock

import pytest

from jelastic.api import S3

success_response = {"error": "", "reason": 0, "result": 0, "source": "billing"}


@pytest.fixture
def client():
    with patch("jelastic.api.abstract.ClientAbstract._get") as mock_get:
        s3 = S3(session=Mock(), token="token")
        s3._get = mock_get
        yield s3


def test_create(client):
    client._get.return_value = success_response
    response = client.Account.Create("COLUMBUS", "test_project", 1)
    client._get.assert_called_with(
        "Create",
        params={
            "hostGroup": "COLUMBUS",
            "name": "test_project",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_delete(client):
    client._get.return_value = success_response
    response = client.Account.Delete("COLUMBUS", "proj1", 1)
    client._get.assert_called_with(
        "Delete",
        params={
            "hostGroup": "COLUMBUS",
            "name": "proj1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_generate_keys(client):
    client._get.return_value = success_response
    response = client.Account.GenerateKey("COLUMBUS", "proj1", 1)
    client._get.assert_called_with(
        "GenerateKey",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 1,
            "name": "proj1",
        },
    )
    assert response == success_response


def test_get_keys(client):
    client._get.return_value = success_response
    response = client.Account.GetKeys(1)
    client._get.assert_called_with(
        "GetKeys",
        params={
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_regenerate_keys(client):
    client._get.return_value = success_response
    response = client.Account.RegenerateKeys("COLUMBUS", "access_key", 1)
    client._get.assert_called_with(
        "RegenerateKeys",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 1,
            "accKey": "access_key",
        },
    )
    assert response == success_response


def test_revoke_key(client):
    client._get.return_value = success_response
    response = client.Account.RevokeKey("COLUMBUS", "access_key", 123)
    client._get.assert_called_with(
        "RevokeKey",
        params={
            "hostGroup": "COLUMBUS",
            "ownerUid": 123,
            "accKey": "access_key",
        },
    )
    assert response == success_response


def test_copy_object(client):
    client._get.return_value = success_response
    response = client.Bucket.CopyObject(
        "src_bucket", "src_key", "dest_bucket", "dest_key", "group1", 1
    )
    client._get.assert_called_with(
        "CopyObject",
        params={
            "srcBucketName": "src_bucket",
            "srcKey": "src_key",
            "dstBucketName": "dest_bucket",
            "dstKey": "dest_key",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_bucket_create(client):
    client._get.return_value = success_response
    response = client.Bucket.Create("bucket1", "group1", 1)
    client._get.assert_called_with(
        "Create",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_bucket_delete(client):
    client._get.return_value = success_response
    response = client.Bucket.Delete("bucket1", "group1", 1)
    client._get.assert_called_with(
        "Delete",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_delete_object(client):
    client._get.return_value = success_response
    response = client.Bucket.DeleteObject("bucket1", "key1", "group1", 1)
    client._get.assert_called_with(
        "DeleteObject",
        params={
            "bucketName": "bucket1",
            "key": "key1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_delete_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.DeletePolicy("bucket1", "group1", 1)
    client._get.assert_called_with(
        "DeletePolicy",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_get_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.GetPolicy("bucket1", "group1", 1)
    client._get.assert_called_with(
        "GetPolicy",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_get_presigned_url(client):
    client._get.return_value = success_response
    response = client.Bucket.GetPresignedURL("bucket1", "key1", "group1", 1)
    client._get.assert_called_with(
        "GetPresignedURL",
        params={
            "bucketName": "bucket1",
            "key": "key1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_list(client):
    client._get.return_value = success_response
    response = client.Bucket.List(1)
    client._get.assert_called_with(
        "List",
        params={
            "ownerUid": 1,
        },
    )
    assert response == success_response


def test_list_objects(client):
    client._get.return_value = success_response
    response = client.Bucket.ListObjects("bucket1", "group1", "prefix", "token")
    client._get.assert_called_with(
        "ListObjects",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "prefix": "prefix",
            "continuationToken": "token",
            "delimiter": ",",
            "maxKeys": 100,
            "ownerUid": None,
        },
    )
    assert response == success_response


def test_set_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.SetPolicy("bucket1", "group1", "policy1", 1)
    client._get.assert_called_with(
        "SetPolicy",
        params={
            "bucketName": "bucket1",
            "policy": "policy1",
            "hostGroup": "group1",
            "ownerUid": 1,
        },
    )
    assert response == success_response
