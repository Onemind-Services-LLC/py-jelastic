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
    response = client.Invoice.GetExternalInvoices(1, 2)
    client._get.assert_called_with(
        "ExternalInvoices",
        params={
            "limit": 1,
            "ownerUid": 2,
        },
    )
    assert response == success_response


def test_get_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.GetInvoices(
        1,
        "uname",
        "type",
        "status",
        1,
        "sub_status",
        "field",
        "direction",
        1,
        1,
        "exp_field",
    )
    client._get.assert_called_with(
        "GetInvoices",
        params={
            "id": 1,
            "uniqueName": "uname",
            "type": "type",
            "status": "status",
            "subscriptionId": 1,
            "subscriptionStatus": "sub_status",
            "orderFields": "field",
            "orderDirection": "direction",
            "startRow": 1,
            "resultCount": 1,
            "expandFields": "exp_field",
        },
    )
    assert response == success_response


def test_make_invoice(client):
    client._get.return_value = success_response
    response = client.Invoice.MakeInvoice("uid1", True)
    client._get.assert_called_with(
        "MakeInvoice", params={"uid": "uid1", "skipPay": True}
    )
    assert response == success_response


def test_mark_as_paid(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsPaid(1, "envoice")
    client._get.assert_called_with(
        "MarkAsPaid", params={"id": 1, "ebsInvoiceId": "envoice"}
    )
    assert response == success_response


def test_mark_as_void(client):
    client._get.return_value = success_response
    response = client.Invoice.MarkAsVoid(1, "envoice")
    client._get.assert_called_with(
        "MarkAsVoid", params={"id": 1, "ebsInvoiceId": "envoice"}
    )
    assert response == success_response


def test_pay(client):
    client._get.return_value = success_response
    response = client.Invoice.Pay(1, "pid", "type")
    client._get.assert_called_with(
        "Pay", params={"id": 1, "paymentMethodId": "pid", "paymentMethodType": "type"}
    )
    assert response == success_response


def test_search_invoices(client):
    client._get.return_value = success_response
    response = client.Invoice.SearchInvoices("search", "field", 1)
    client._get.assert_called_with(
        "SearchInvoices",
        params={"search": "search", "expandFields": "field", "resellerId": 1},
    )
    assert response == success_response
