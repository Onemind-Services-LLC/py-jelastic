from . import *


def test_event(client):
    client._get.return_value = success_response
    response = client.Invoice.Event("id_1", "type_1")
    client._get.assert_called_with(
        "Event", params={"externId": "id_1", "eventType": "type_1"}
    )
    assert response == success_response


def test_get_external_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.GetExternalInvoices(
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    )
    client._get.assert_called_with(
        "ExternalInvoices",
        params={
            "limit": [1, 2, 3, 4],
            "ownerUid": [1, 2, 3, 4],
        },
        delimiter=",",
    )
    assert response == success_response


def test_get_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.GetInvoices(
        [1, 2, 3],
        ["uname1", "uname2", "uname3"],
        ["type1", "type2", "type3"],
        ["status1", "status2", "status3"],
        [1, 2, 3],
        ["sub_status1", "sub_status2", "sub_status3"],
        ["field1", "field2", "field3"],
        ["direction1", "direction2", "direction3"],
        [1, 2, 3],
        [1, 2, 3],
        ["exp_fields1", "exp_fields2", "exp_fields3"],
    )
    client._get.assert_called_with(
        "GetInvoices",
        params={
            "id": [1, 2, 3],
            "uniqueName": ["uname1", "uname2", "uname3"],
            "type": ["type1", "type2", "type3"],
            "status": ["status1", "status2", "status3"],
            "subscriptionId": [1, 2, 3],
            "subscriptionStatus": ["sub_status1", "sub_status2", "sub_status3"],
            "orderFields": ["field1", "field2", "field3"],
            "orderDirection": ["direction1", "direction2", "direction3"],
            "startRow": [1, 2, 3],
            "resultCount": [1, 2, 3],
            "expandFields": ["exp_fields1", "exp_fields2", "exp_fields3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_make_invoice(client):
    client._get.return_value = success_response
    response = client.Invoice.MakeInvoice(
        "uid1",
        [True, False, True],
    )
    client._get.assert_called_with(
        "MakeInvoice",
        params={
            "uid": "uid1",
            "skipPay": [True, False, True],
        },
        delimiter=",",
    )
    assert response == success_response


def test_mark_as_paid(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsPaid(
        [1, 2, 3],
        ["envoice1", "envoice2", "envoice3"],
    )
    client._get.assert_called_with(
        "MarkAsPaid",
        params={
            "id": [1, 2, 3],
            "ebsInvoiceId": ["envoice1", "envoice2", "envoice3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_mark_as_void(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsVoid(
        [1, 2, 3],
        ["envoice1", "envoice2", "envoice3"],
    )
    client._get.assert_called_with(
        "MarkAsVoid",
        params={
            "id": [1, 2, 3],
            "ebsInvoiceId": ["envoice1", "envoice2", "envoice3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_pay(client):
    client._get.return_value = success_response
    response = client.Invoice.Pay(
        1,
        ["pid1", "pid2", "pid3"],
        ["type1", "type2", "type3"],
    )
    client._get.assert_called_with(
        "Pay",
        params={
            "id": 1,
            "paymentMethodId": ["pid1", "pid2", "pid3"],
            "paymentMethodType": ["type1", "type2", "type3"],
        },
        delimiter=",",
    )
    assert response == success_response


def test_search_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.SearchInvoices(
        "search",
        ["field1", "field2", "field3"],
        [1, 2, 3],
    )
    client._get.assert_called_with(
        "SearchInvoices",
        params={
            "search": "search",
            "expandFields": ["field1", "field2", "field3"],
            "resellerId": [1, 2, 3],
        },
        delimiter=",",
    )
    assert response == success_response
