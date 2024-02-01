from . import *


def test_get_invoice_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetInvoiceUrl(1, "ruk")
    client._get.assert_called_with(
        "GetInvoiceUrl", params={"invoiceId": 1, "ruk": "ruk"}
    )
    assert response == success_response


def test_get_sso_url(client):
    client._get.return_value = success_response
    response = client.Integration.GetSSOUrl("path", "ruk")
    client._get.assert_called_with(
        "GetSSOUrl",
        params={"path": "path", "ruk": "ruk"},
    )
    assert response == success_response
