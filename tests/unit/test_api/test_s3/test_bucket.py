from . import *


def test_copy_object(client):
    client._get.return_value = success_response
    response = client.Bucket.CopyObject(
        "src_bucket",
        "src_key",
        "dest_bucket",
        "dest_key",
        "group1",
        1,
        "ruk",
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_bucket_create(client):
    client._get.return_value = success_response
    response = client.Bucket.Create(
        "bucket1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Create",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_bucket_delete(client):
    client._get.return_value = success_response
    response = client.Bucket.Delete(
        "bucket1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "Delete",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_object(client):
    client._get.return_value = success_response
    response = client.Bucket.DeleteObject(
        "bucket1",
        "key1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeleteObject",
        params={
            "bucketName": "bucket1",
            "key": "key1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_delete_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.DeletePolicy(
        "bucket1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "DeletePolicy",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.GetPolicy(
        "bucket1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetPolicy",
        params={
            "bucketName": "bucket1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_get_presigned_url(client):
    client._get.return_value = success_response
    response = client.Bucket.GetPresignedURL(
        "bucket1",
        "key1",
        "group1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "GetPresignedURL",
        params={
            "bucketName": "bucket1",
            "key": "key1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_list(client):
    client._get.return_value = success_response
    response = client.Bucket.List(
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "List",
        params={
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_list_objects(client):
    client._get.return_value = success_response
    response = client.Bucket.ListObjects(
        bucket_name="bucket1",
        host_group="group1",
        prefix="prefix",
        continuation_token="token",
        ruk="ruk",
    )
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
            "ruk": "ruk",
        },
    )
    assert response == success_response


def test_set_policy(client):
    client._get.return_value = success_response
    response = client.Bucket.SetPolicy(
        "bucket1",
        "group1",
        "policy1",
        1,
        "ruk",
    )
    client._get.assert_called_with(
        "SetPolicy",
        params={
            "bucketName": "bucket1",
            "policy": "policy1",
            "hostGroup": "group1",
            "ownerUid": 1,
            "ruk": "ruk",
        },
    )
    assert response == success_response
